"""Generate file-based Pydantic model packages."""

import os
from rdflib import Graph
from pydantic import BaseModel
from .extraction import extract_classes_and_properties
from .utils import extract_prefix_and_local, topological_sort_classes, sanitise_identifier
from .codegen import generate_docstring, generate_class_definition, generate_property_line, generate_ellipsis_line


def create_package(graph: Graph, output_dir: str, context: dict | None = None, base_cls: type[BaseModel] | None = None) -> None:
    """Generate a Python module folder structure from an RDFS graph.
    
    Args:
        graph: RDFLib Graph object containing RDFS ontology
        output_dir: Directory to write the package structure to
        context: Optional JSON-LD @context document providing aliases
        base_cls: Base class type to inherit from (default: None, uses BaseModel)
    """
    classes = extract_classes_and_properties(graph, context)
    sorted_class_uris = topological_sort_classes(classes)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Group classes by prefix
    prefix_to_classes = _group_by_prefix(sorted_class_uris, classes)
    
    # Create files for each prefix
    for prefix, class_list in prefix_to_classes.items():
        _create_prefix_package(prefix, class_list, classes, output_dir, base_cls)
    
    # Create top-level __init__.py with imports from all prefixes
    _create_toplevel_init(prefix_to_classes, classes, output_dir)


def _group_by_prefix(sorted_class_uris: list[str], classes: dict) -> dict[str, list[tuple[str, str]]]:
    """Group classes by their namespace prefix."""
    prefix_to_classes: dict[str, list[tuple[str, str]]] = {}
    for class_uri in sorted_class_uris:
        info = classes[class_uri]
        g = info["graph"]
        prefix, local = extract_prefix_and_local(info["uri"], g)
        prefix_to_classes.setdefault(prefix, []).append((local, class_uri))
    return prefix_to_classes


def _create_toplevel_init(prefix_to_classes: dict[str, list[tuple[str, str]]], classes: dict, output_dir: str) -> None:
    """Create top-level __init__.py with imports from all prefixes."""
    init_lines = []
    all_imports = []
    rebuild_calls = []
    
    # Collect all imports from each prefix package
    for prefix, class_list in sorted(prefix_to_classes.items()):
        for local, class_uri in sorted(class_list):
            class_name = classes[class_uri]['name']
            all_imports.append(class_name)
            init_lines.append(f"from .{prefix}.{local} import {class_name}")
            # Only rebuild if class has properties that reference other classes
            if classes[class_uri]['properties']:
                rebuild_calls.append(class_name)
    
    # Add __all__ to control what's exported
    if all_imports:
        init_lines.append("")
        init_lines.append(f"__all__ = {repr(sorted(all_imports))}")
    
    # Add a function to rebuild all models - users can call this after importing
    if rebuild_calls:
        init_lines.append("")
        init_lines.append("def rebuild_all_models() -> None:")
        init_lines.append('    """Rebuild all models to resolve forward references."""')
        init_lines.append('    import sys')
        init_lines.append('    # Get this module''s globals')
        init_lines.append('    this_module_globals = globals()')
        init_lines.append('    # Update module globals for all modules containing our classes')
        init_lines.append('    for mod_name in list(sys.modules.keys()):')
        init_lines.append('        if mod_name.startswith(\"linked_art.\"):')
        init_lines.append('            mod = sys.modules[mod_name]')
        init_lines.append('            mod_dict = vars(mod)')
        init_lines.append('            # Add all top-level classes to this module''s globals')
        init_lines.append('            mod_dict.update(this_module_globals)')
        init_lines.append('    ')
        for class_name in sorted(set(rebuild_calls)):
            init_lines.append(f"    {class_name}.model_rebuild()")
    
    with open(os.path.join(output_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(init_lines) + "\n" if init_lines else "")


def _create_prefix_package(prefix: str, class_list: list[tuple[str, str]], classes: dict, output_dir: str, base_cls: type[BaseModel] | None = None) -> None:
    """Create a package directory for a given prefix with all its classes."""
    folder = os.path.join(output_dir, prefix)
    os.makedirs(folder, exist_ok=True)
    
    # Write __init__.py with imports (don't call model_rebuild - forward refs are handled by Pydantic)
    init_lines = []
    for local, class_uri in sorted(class_list):
        class_name = classes[class_uri]['name']
        init_lines.append(f"from .{local} import {class_name}")
    
    with open(os.path.join(folder, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(init_lines) + "\n" if init_lines else "")
    
    # Write each class file
    for local, class_uri in class_list:
        _write_class_file(local, class_uri, prefix, class_list, classes, folder, base_cls)


def _write_class_file(local: str, class_uri: str, prefix: str, class_list: list[tuple[str, str]], classes: dict, folder: str, base_cls: type[BaseModel] | None = None) -> None:
    """Write a single class file."""
    info = classes[class_uri]
    class_name = info["name"]
    parent_uris = _dedupe_parent_uris(info["parent_uris"], classes)
    properties = info["properties"]
    label = info.get("label")
    iri = info.get("iri")
    comment = info.get("comment")
    
    # Determine parent imports and names
    parent_imports = _get_parent_imports(parent_uris, classes, prefix)
    parent_names = [classes[str(parent_uri)]["name"] for parent_uri in parent_uris if str(parent_uri) in classes]
    
    # Determine property type imports (both same-namespace and cross-namespace)
    property_imports = _get_property_imports(properties, classes, prefix, local)
    
    # Build class file lines
    lines = ["from __future__ import annotations"]
    
    # Add TYPE_CHECKING import if there are property imports (potential circular dependencies)
    if property_imports:
        lines.append("from typing import TYPE_CHECKING")
    
    # Import base model - either BaseModel or custom base class
    if base_cls is not None:
        # Import the custom base class from its module
        base_class_name = base_cls.__name__
        base_class_module = base_cls.__module__
        lines.append(f"from {base_class_module} import {base_class_name}")
    else:
        lines.append("from pydantic import BaseModel")
    
    # Parent imports at module level (needed for class inheritance)
    for imp in sorted(set(parent_imports)):
        lines.append(imp)
    
    # Property imports go under TYPE_CHECKING to avoid circular imports
    # model_rebuild() in __init__.py will resolve forward references at runtime
    if property_imports:
        lines.append("")
        lines.append("if TYPE_CHECKING:")
        for imp in sorted(set(property_imports)):
            lines.append(f"    {imp}")
    
    lines.append("")
    
    # Class definition
    class_def = generate_class_definition(class_name, parent_names if parent_names else None, "", base_cls)
    lines.append(class_def)
    
    # Docstring
    docstring = generate_docstring(label, iri, comment)
    if docstring:
        lines.append(docstring)
    
    # Properties or ellipsis
    if properties:
        for prop_name in sorted(properties):
            prop = properties[prop_name]
            lines.append(generate_property_line(prop['name'], prop['type']))
    else:
        lines.append(generate_ellipsis_line())
    lines.append("")
    
    with open(os.path.join(folder, f"{local}.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def _get_parent_imports(parent_uris: list, classes: dict, current_prefix: str) -> list[str]:
    """Get import statements for parent classes."""
    imports: list[str] = []
    for parent_uri in parent_uris:
        if str(parent_uri) in classes:
            parent_info = classes[str(parent_uri)]
            parent_n3 = parent_info["uri"].n3(namespace_manager=parent_info["graph"].namespace_manager)
            if ":" in parent_n3:
                parent_prefix, parent_local = parent_n3.split(":", 1)
            else:
                parent_prefix, parent_local = "default", parent_n3
            parent_prefix = sanitise_identifier(parent_prefix)
            parent_local = sanitise_identifier(parent_local)
            
            if parent_prefix == current_prefix:
                imports.append(f"from .{parent_local} import {parent_info['name']}")
            else:
                imports.append(f"from ..{parent_prefix}.{parent_local} import {parent_info['name']}")
    
    return imports


def _dedupe_parent_uris(parent_uris: list, classes: dict) -> list:
    """Remove parent classes that are ancestors of other listed parents.

    This prevents Python MRO conflicts when a class declares both a base and one
    of that base's descendants as parents (common in noisy ontologies).
    """
    memo: dict[str, set[str]] = {}
    parents = [(uri, str(uri)) for uri in parent_uris if str(uri) in classes]
    filtered: list = []

    for uri, uri_str in parents:
        is_redundant = any(
            uri_str in _get_ancestor_set(other_str, classes, memo)
            for _, other_str in parents
            if other_str != uri_str
        )
        if not is_redundant:
            filtered.append(uri)

    return filtered


def _get_ancestor_set(uri_str: str, classes: dict, memo: dict[str, set[str]]) -> set[str]:
    """Compute all ancestors for a given class URI (transitively)."""
    if uri_str in memo:
        return memo[uri_str]

    ancestors: set[str] = set()
    class_info = classes.get(uri_str)
    if not class_info:
        memo[uri_str] = ancestors
        return ancestors

    for parent_uri in class_info.get("parent_uris", []):
        parent_str = str(parent_uri)
        ancestors.add(parent_str)
        ancestors.update(_get_ancestor_set(parent_str, classes, memo))

    memo[uri_str] = ancestors
    return ancestors


def _get_property_imports(properties: dict, classes: dict, current_prefix: str, current_local: str) -> list[str]:
    """Get import statements for property types.
    
    Extracts class names from property range URIs and generates imports for both
    same-prefix (sibling modules) and cross-prefix references, avoiding self-imports.
    """
    imports: list[str] = []
    imported_classes: set[tuple[str, str]] = set()  # (prefix, class_name) pairs
    
    for prop_name, prop_info in properties.items():
        prop_type = prop_info.get("type", "")
        ranges = prop_info.get("ranges", [])
        
        # Extract class URIs from ranges
        for range_uri in ranges:
            if str(range_uri) in classes:
                range_info = classes[str(range_uri)]
                range_n3 = range_info["uri"].n3(namespace_manager=range_info["graph"].namespace_manager)
                
                if ":" in range_n3:
                    range_prefix, range_local = range_n3.split(":", 1)
                else:
                    range_prefix, range_local = "default", range_n3
                range_prefix = sanitise_identifier(range_prefix)
                range_local = sanitise_identifier(range_local)
                
                class_name = range_info["name"]
                
                # Skip self-import
                if range_prefix == current_prefix and range_local == current_local:
                    continue

                key = (range_prefix, class_name)
                if key in imported_classes:
                    continue

                if range_prefix == current_prefix:
                    imports.append(f"from .{range_local} import {class_name}")
                else:
                    imports.append(f"from ..{range_prefix}.{range_local} import {class_name}")
                imported_classes.add(key)
    
    return imports

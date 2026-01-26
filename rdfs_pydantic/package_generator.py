"""Generate file-based Pydantic model packages."""

import os
from rdflib import Graph
from .extraction import extract_classes_and_properties
from .utils import extract_prefix_and_local, topological_sort_classes
from .codegen import generate_docstring, generate_class_definition, generate_property_line, generate_ellipsis_line


def create_package(graphs: list[Graph], output_dir: str, contexts: list[dict] | None = None) -> None:
    """Generate a Python module folder structure from RDFS graphs.
    
    Args:
        graphs: List of RDFLib Graph objects containing RDFS ontologies
        output_dir: Directory to write the package structure to
        contexts: Optional list of JSON-LD @context documents providing aliases
    """
    classes = extract_classes_and_properties(graphs, contexts)
    sorted_class_uris = topological_sort_classes(classes)
    
    # Group classes by prefix
    prefix_to_classes = _group_by_prefix(sorted_class_uris, classes)
    
    # Create files for each prefix
    for prefix, class_list in prefix_to_classes.items():
        _create_prefix_package(prefix, class_list, classes, output_dir)


def _group_by_prefix(sorted_class_uris: list[str], classes: dict) -> dict[str, list[tuple[str, str]]]:
    """Group classes by their namespace prefix."""
    prefix_to_classes: dict[str, list[tuple[str, str]]] = {}
    for class_uri in sorted_class_uris:
        info = classes[class_uri]
        g = info["graph"]
        prefix, local = extract_prefix_and_local(info["uri"], g)
        prefix_to_classes.setdefault(prefix, []).append((local, class_uri))
    return prefix_to_classes


def _create_prefix_package(prefix: str, class_list: list[tuple[str, str]], classes: dict, output_dir: str) -> None:
    """Create a package directory for a given prefix with all its classes."""
    folder = os.path.join(output_dir, prefix)
    os.makedirs(folder, exist_ok=True)
    
    # Write __init__.py
    init_lines = []
    for local, class_uri in sorted(class_list):
        init_lines.append(f"from .{local} import {classes[class_uri]['name']}")
    with open(os.path.join(folder, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("\n".join(init_lines) + "\n")
    
    # Write each class file
    for local, class_uri in class_list:
        _write_class_file(local, class_uri, prefix, class_list, classes, folder)


def _write_class_file(local: str, class_uri: str, prefix: str, class_list: list[tuple[str, str]], classes: dict, folder: str) -> None:
    """Write a single class file."""
    info = classes[class_uri]
    class_name = info["name"]
    parent_uris = info["parent_uris"]
    properties = info["properties"]
    label = info.get("label")
    iri = info.get("iri")
    comment = info.get("comment")
    
    # Determine parent imports and names
    parent_imports = _get_parent_imports(parent_uris, classes, prefix)
    parent_names = [classes[str(parent_uri)]["name"] for parent_uri in parent_uris if str(parent_uri) in classes]
    
    # Build class file lines
    lines = ["from __future__ import annotations", "from pydantic import BaseModel"]
    for imp in sorted(set(parent_imports)):
        lines.append(imp)
    lines.append("")
    
    # Class definition
    class_def = generate_class_definition(class_name, parent_names if parent_names else None)
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
            
            if parent_prefix == current_prefix:
                imports.append(f"from .{parent_local} import {parent_info['name']}")
            else:
                imports.append(f"from ..{parent_prefix}.{parent_local} import {parent_info['name']}")
    
    return imports

"""Generate inline Pydantic model code."""

from typing import Set
from rdflib import Graph
from pydantic import BaseModel
from .extraction import extract_classes_and_properties
from .utils import extract_prefix_and_local, topological_sort_classes
from .codegen import generate_docstring, generate_class_definition, generate_property_line, generate_ellipsis_line, generate_model_config


def create_module(graph: Graph, context: dict | None = None, base_cls: type[BaseModel] | None = None) -> str:
    """Transform RDFS ontology from an RDF graph into Pydantic model code.
    
    Args:
        graph: RDFLib Graph object containing RDFS ontology
        context: Optional JSON-LD @context document providing aliases
        base_cls: Base class type to inherit from (default: None, uses BaseModel)
                 Pass a custom BaseModel subclass for specialized base models
        
    Returns:
        Python code defining Pydantic models
    """
    classes = extract_classes_and_properties(graph, context)
    
    # Import BaseModel
    import_line = "from pydantic import BaseModel"
    lines = ["from __future__ import annotations", import_line, "", ""]
    sorted_class_uris = topological_sort_classes(classes)
    
    # Group classes by their local name to detect duplicates needing namespace wrapping
    local_name_to_uris = _group_by_local_name(sorted_class_uris, classes)
    
    # Identify prefix groups for namespace wrapping
    prefix_groups = _identify_prefix_groups(local_name_to_uris)
    
    # Build class name to qualified name mapping
    class_name_map = _build_qualified_name_map(classes, prefix_groups)
    
    # Update property types to use qualified names
    _qualify_property_types(classes, class_name_map)
    
    # Process classes and generate output
    processed_classes: Set[str] = set()
    for class_uri in sorted_class_uris:
        if class_uri in processed_classes:
            continue
            
        class_info = classes[class_uri]
        g = class_info["graph"]
        prefix, local = extract_prefix_and_local(class_info["uri"], g)
        
        # Check if this class is part of a namespace group
        if prefix in prefix_groups and class_uri in prefix_groups[prefix]:
            # Find all classes in this prefix group
            classes_in_prefix = [uri for uri in prefix_groups[prefix] if uri not in processed_classes]
            
            if classes_in_prefix:
                lines.append(f"class {prefix}:")
                _emit_namespace_group(lines, classes_in_prefix, classes, prefix, processed_classes, class_name_map, base_cls)
                lines.append("")
        else:
            # Regular class without namespace wrapping
            if class_uri not in processed_classes:
                processed_classes.add(class_uri)
                _emit_single_class(lines, class_uri, classes, "", class_name_map, base_cls)
    
    return "\n".join(lines).rstrip() + "\n"


def _group_by_local_name(sorted_class_uris: list[str], classes: dict) -> dict:
    """Group classes by their local name to detect duplicates."""
    local_name_to_uris: dict = {}
    for class_uri in sorted_class_uris:
        class_info = classes[class_uri]
        g = class_info["graph"]
        prefix, local = extract_prefix_and_local(class_info["uri"], g)
        if local not in local_name_to_uris:
            local_name_to_uris[local] = []
        local_name_to_uris[local].append((prefix, class_uri))
    return local_name_to_uris


def _identify_prefix_groups(local_name_to_uris: dict) -> dict:
    """Identify which prefixes have duplicate class names."""
    prefix_groups: dict = {}
    for local_name, uri_list in local_name_to_uris.items():
        if len(uri_list) > 1:  # Multiple classes with same local name
            for prefix, class_uri in uri_list:
                if prefix not in prefix_groups:
                    prefix_groups[prefix] = []
                prefix_groups[prefix].append(class_uri)
    return prefix_groups


def _emit_namespace_group(lines: list, classes_in_prefix: list, classes: dict, prefix: str, processed_classes: Set, class_name_map: dict, base_cls: type[BaseModel] | None = None) -> None:
    """Emit a namespace group with all its nested classes."""
    for group_class_uri in sorted(classes_in_prefix):
        processed_classes.add(group_class_uri)
        group_class_info = classes[group_class_uri]
        
        # Get parent class names
        parent_names = _get_parent_names(group_class_info, classes, class_name_map)
        
        # Class definition inside wrapper
        class_def = generate_class_definition(group_class_info["name"], parent_names if parent_names else None, "    ", base_cls)
        lines.append(class_def)
        
        # Docstring
        docstring = generate_docstring(
            group_class_info.get("label"),
            group_class_info.get("iri"),
            group_class_info.get("comment"),
            "        "
        )
        if docstring:
            lines.append(docstring)
        
        # Properties or ellipsis
        if group_class_info["properties"]:
            for prop_name in sorted(group_class_info["properties"]):
                prop = group_class_info["properties"][prop_name]
                lines.append(generate_property_line(prop["name"], prop["type"], "        "))
        else:
            lines.append(generate_ellipsis_line("        "))
        lines.append("")


def _emit_single_class(lines: list, class_uri: str, classes: dict, indent: str, class_name_map: dict, base_cls: type[BaseModel] | None = None) -> None:
    """Emit a single class definition."""
    class_info = classes[class_uri]
    
    # Get parent class names
    parent_names = _get_parent_names(class_info, classes, class_name_map)
    
    # Class definition
    class_def = generate_class_definition(class_info["name"], parent_names if parent_names else None, indent, base_cls)
    lines.append(class_def)
    
    # Docstring
    docstring = generate_docstring(
        class_info.get("label"),
        class_info.get("iri"),
        class_info.get("comment"),
        indent + "    "
    )
    if docstring:
        lines.append(docstring)
    
    # Properties or ellipsis
    if class_info["properties"]:
        for prop_name in sorted(class_info["properties"]):
            prop = class_info["properties"][prop_name]
            lines.append(generate_property_line(prop["name"], prop["type"], indent + "    "))
    else:
        lines.append(generate_ellipsis_line(indent + "    "))
    lines.append("")
    lines.append("")


def _get_parent_names(class_info: dict, classes: dict, class_name_map: dict) -> list:
    """Get names of parent classes, qualified if necessary."""
    parent_names = []
    for parent_uri in class_info["parent_uris"]:
        parent_uri_str = str(parent_uri)
        if parent_uri_str in classes:
            # Use qualified name from the URI-based map
            qualified_name = class_name_map.get(parent_uri_str, classes[parent_uri_str]["name"])
            parent_names.append(qualified_name)
    return parent_names


def _build_qualified_name_map(classes: dict, prefix_groups: dict) -> dict:
    """Build a mapping from class URI to qualified name (with namespace prefix if needed).
    
    Args:
        classes: Dict of class URIs to class info
        prefix_groups: Dict of prefixes to class URIs that need namespace wrapping
        
    Returns:
        Dict mapping class_uri -> qualified_name (e.g., "uri" -> "ex1.Person")
    """
    uri_to_prefix = {}
    
    # Identify which URIs are in namespace groups
    for prefix, class_uris in prefix_groups.items():
        for class_uri in class_uris:
            uri_to_prefix[class_uri] = prefix
    
    # Build the map using URIs as keys
    name_map = {}
    for class_uri, class_info in classes.items():
        class_name = class_info["name"]
        if class_uri in uri_to_prefix:
            # This class is in a namespace group
            qualified_name = f"{uri_to_prefix[class_uri]}.{class_name}"
            name_map[class_uri] = qualified_name
        else:
            # Not in a namespace group, use simple name
            name_map[class_uri] = class_name
    
    return name_map


def _qualify_property_types(classes: dict, class_name_map: dict) -> None:
    """Update property types to use qualified names for namespace-wrapped classes.
    
    Modifies property types in-place to replace simple class names with qualified
    names when they reference namespace-wrapped classes.
    
    Args:
        classes: Dict of class URIs to class info
        class_name_map: Dict mapping class_uri -> qualified_name
    """
    # Build a reverse map: class_name -> list of (uri, qualified_name)
    name_to_uris = {}
    for class_uri, qualified_name in class_name_map.items():
        class_name = classes[class_uri]["name"]
        if class_name not in name_to_uris:
            name_to_uris[class_name] = []
        name_to_uris[class_name].append((class_uri, qualified_name))
    
    for class_info in classes.values():
        for prop_info in class_info["properties"].values():
            prop_type = prop_info["type"]
            
            # Parse and replace class names in the type annotation
            # Handle patterns like "list[ClassName]" or "list[Class1 | Class2]"
            if "list[" in prop_type:
                start = prop_type.find("[") + 1
                end = prop_type.find("]")
                if start > 0 and end > start:
                    type_content = prop_type[start:end]
                    # Split by | for union types
                    type_parts = [t.strip() for t in type_content.split("|")]
                    qualified_parts = []
                    for type_name in type_parts:
                        # Find which URI this references by checking the ranges
                        resolved_name = type_name
                        for range_uri in prop_info.get("ranges", []):
                            range_uri_str = str(range_uri)
                            if range_uri_str in classes and classes[range_uri_str]["name"] == type_name:
                                # Found the matching class, use its qualified name
                                resolved_name = class_name_map.get(range_uri_str, type_name)
                                break
                        qualified_parts.append(resolved_name)
                    
                    # Rebuild the type annotation
                    qualified_content = " | ".join(qualified_parts)
                    prop_info["type"] = f"list[{qualified_content}]"

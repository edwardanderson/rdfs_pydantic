"""Generate inline Pydantic model code."""

from typing import Set
from rdflib import Graph
from .extraction import extract_classes_and_properties
from .utils import extract_prefix_and_local, topological_sort_classes
from .codegen import generate_docstring, generate_class_definition, generate_property_line, generate_ellipsis_line


def create_module(graph: Graph, context: dict | None = None) -> str:
    """Transform RDFS ontology from an RDF graph into Pydantic model code.
    
    Args:
        graph: RDFLib Graph object containing RDFS ontology
        context: Optional JSON-LD @context document providing aliases
        
    Returns:
        Python code defining Pydantic models
    """
    classes = extract_classes_and_properties(graph, context)
    lines = ["from __future__ import annotations", "from pydantic import BaseModel", "", ""]
    sorted_class_uris = topological_sort_classes(classes)
    
    # Group classes by their local name to detect duplicates needing namespace wrapping
    local_name_to_uris = _group_by_local_name(sorted_class_uris, classes)
    
    # Identify prefix groups for namespace wrapping
    prefix_groups = _identify_prefix_groups(local_name_to_uris)
    
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
                _emit_namespace_group(lines, classes_in_prefix, classes, prefix, processed_classes)
                lines.append("")
        else:
            # Regular class without namespace wrapping
            if class_uri not in processed_classes:
                processed_classes.add(class_uri)
                _emit_single_class(lines, class_uri, classes, "")
    
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


def _emit_namespace_group(lines: list, classes_in_prefix: list, classes: dict, prefix: str, processed_classes: Set) -> None:
    """Emit a namespace group with all its nested classes."""
    for group_class_uri in sorted(classes_in_prefix):
        processed_classes.add(group_class_uri)
        group_class_info = classes[group_class_uri]
        
        # Get parent class names
        parent_names = _get_parent_names(group_class_info, classes)
        
        # Class definition inside wrapper
        class_def = generate_class_definition(group_class_info["name"], parent_names if parent_names else None, "    ")
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


def _emit_single_class(lines: list, class_uri: str, classes: dict, indent: str) -> None:
    """Emit a single class definition."""
    class_info = classes[class_uri]
    
    # Get parent class names
    parent_names = _get_parent_names(class_info, classes)
    
    # Class definition
    class_def = generate_class_definition(class_info["name"], parent_names if parent_names else None, indent)
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


def _get_parent_names(class_info: dict, classes: dict) -> list:
    """Get names of parent classes."""
    parent_names = []
    for parent_uri in class_info["parent_uris"]:
        if str(parent_uri) in classes:
            parent_names.append(classes[str(parent_uri)]["name"])
    return parent_names

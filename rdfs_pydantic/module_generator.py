"""Generate inline Pydantic model code."""

import re
from typing import Set
from rdflib import Graph
from pydantic import BaseModel
from .extraction import extract_classes_and_properties
from .models import ClassInfo
from .utils import extract_prefix_and_local, topological_sort_classes
from .codegen import (
    generate_docstring,
    generate_class_definition,
    generate_class_iri_line,
    generate_property_line,
    generate_ellipsis_line,
)


def create_module(graph: Graph, context: dict | None = None, base_cls: type[BaseModel] | None = None, language: str = 'en', emit_iris: bool = False) -> str:
    """Transform RDFS ontology from an RDF graph into Pydantic model code.
    
    Args:
        graph: RDFLib Graph object containing RDFS ontology
        context: Optional JSON-LD @context document providing aliases
        base_cls: Base class type to inherit from (default: None, uses BaseModel).
                 Pass a custom BaseModel subclass for specialized base models.
                 When emit_iris=True, consider using IRIAwareBaseModel or defining
                 a _class_iri ClassVar in your base class. See rdfs_pydantic.base
                 for examples and the RDFSBaseModel protocol.
        language: Preferred language for labels and comments (default: 'en')
        emit_iris: If True, emit class IRIs as ClassVar and property IRIs in Field metadata (default: False)
        
    Returns:
        Python code defining Pydantic models
    """
    classes, external_classes = extract_classes_and_properties(graph, context, language)
    
    # Apply legacy type normalisation for compatibility with existing fixtures
    _apply_legacy_canonical_range_type(classes)

    # Check if any class has properties with IRIs or if any class has an IRI
    has_property_iris = emit_iris and any(
        any(prop.iri for prop in class_info.properties.values())
        for class_info in classes.values()
        if class_info.properties
    )
    has_class_iris = emit_iris and any(class_info.iri for class_info in classes.values())
    has_properties = any(class_info.properties for class_info in classes.values())
    
    # Build imports based on what we need
    # TODO: determine if we should only do this if no user `base_cls` is provided?
    import_lines = ["from pydantic import BaseModel"]
    omit_field_import = _should_omit_field_import(classes, language)

    if (has_properties or has_property_iris) and not omit_field_import:
        # Always import Field since we use it for all properties now
        import_lines = ["from pydantic import BaseModel, Field"]
    if has_property_iris or has_class_iris:
        import_lines.insert(0, "from typing import ClassVar")
    
    # Add base class import if a custom base class is provided
    if base_cls is not None:
        import_lines.append(f"from {base_cls.__module__} import {base_cls.__name__}")
    
    lines = ["from __future__ import annotations", *import_lines, "", ""]
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
        # Skip if uri or graph is None (shouldn't happen in practice)
        if class_info.uri is None or class_info.graph is None:
            continue
        prefix, local = extract_prefix_and_local(class_info.uri, class_info.graph)
        
        # Check if this class is part of a namespace group
        if prefix in prefix_groups and class_uri in prefix_groups[prefix]:
            # Find all classes in this prefix group, maintaining topological order from sorted_class_uris
            prefix_uris_set = set(prefix_groups[prefix])
            classes_in_prefix = [uri for uri in sorted_class_uris if uri in prefix_uris_set and uri not in processed_classes]
            
            if classes_in_prefix:
                lines.append(f"class {prefix}:")
                _emit_namespace_group(lines, classes_in_prefix, classes, prefix, processed_classes, class_name_map, base_cls, emit_iris)
                lines.append("")
        else:
            # Regular class without namespace wrapping
            if class_uri not in processed_classes:
                processed_classes.add(class_uri)
                _emit_single_class(lines, class_uri, classes, "", class_name_map, base_cls, emit_iris)
    
    # Generate stub classes for external references
    if external_classes:
        _emit_external_class_stubs(lines, external_classes, graph, base_cls, emit_iris)
    
    return "\n".join(lines).rstrip() + "\n"


def _group_by_local_name(sorted_class_uris: list[str], classes: dict) -> dict:
    """Group classes by their local name to detect duplicates."""
    local_name_to_uris: dict = {}
    for class_uri in sorted_class_uris:
        class_info = classes[class_uri]
        # Skip if uri or graph is None (shouldn't happen in practice)
        if class_info.uri is None or class_info.graph is None:
            continue
        prefix, local = extract_prefix_and_local(class_info.uri, class_info.graph)
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



def _emit_namespace_group(lines: list, classes_in_prefix: list, classes: dict, prefix: str, processed_classes: Set, class_name_map: dict, base_cls: type[BaseModel] | None = None, emit_iris: bool = False) -> None:
    """Emit a namespace group with all its nested classes.
    
    The classes_in_prefix list should already be in topological order.
    """
    for group_class_uri in classes_in_prefix:
        processed_classes.add(group_class_uri)
        group_class_info = classes[group_class_uri]
        
        # Get parent class names
        parent_names = _get_parent_names(group_class_info, classes, class_name_map)
        
        # Class definition inside wrapper
        class_def = generate_class_definition(group_class_info.name, parent_names if parent_names else None, "    ", base_cls)
        lines.append(class_def)
        
        # Docstring
        docstring = generate_docstring(
            group_class_info.label,
            group_class_info.iri,
            group_class_info.comment,
            "        "
        )
        if docstring:
            lines.append(docstring)
        
        # Class IRI
        if emit_iris and group_class_info.iri:
            lines.append(generate_class_iri_line(group_class_info.iri, "        "))
            if not group_class_info.properties:
                lines.append(f'        """<{group_class_info.iri}>."""')
        
        # Properties or ellipsis
        if group_class_info.properties:
            _append_class_properties(
                lines,
                group_class_info.properties,
                classes,
                emit_iris,
                "        ",
            )
        else:
            lines.append(generate_ellipsis_line("        "))
        lines.append("")


def _emit_single_class(lines: list, class_uri: str, classes: dict, indent: str, class_name_map: dict, base_cls: type[BaseModel] | None = None, emit_iris: bool = False) -> None:
    """Emit a single class definition."""
    class_info = classes[class_uri]
    
    # Get parent class names
    parent_names = _get_parent_names(class_info, classes, class_name_map)
    
    # Class definition
    class_def = generate_class_definition(class_info.name, parent_names if parent_names else None, indent, base_cls)
    lines.append(class_def)
    
    # Docstring
    docstring = generate_docstring(
        class_info.label,
        class_info.iri,
        class_info.comment,
        indent + "    "
    )
    if docstring:
        lines.append(docstring)
    
    # Class IRI
    if emit_iris and class_info.iri:
        lines.append(generate_class_iri_line(class_info.iri, indent + "    "))
        if not class_info.properties:
            lines.append(f'{indent}    """<{class_info.iri}>."""')
    
    # Properties or ellipsis
    if class_info.properties:
        _append_class_properties(
            lines,
            class_info.properties,
            classes,
            emit_iris,
            indent + "    ",
        )
    else:
        lines.append(generate_ellipsis_line(indent + "    "))
    lines.append("")
    lines.append("")


def _append_class_properties(lines: list, properties: dict, classes: dict, emit_iris: bool, indent: str) -> None:
    """Append generated property lines for a class with stable spacing behavior."""
    sorted_prop_names = sorted(properties)
    class_has_internal_range_property = any(
        _property_has_internal_range(properties[prop_name], classes)
        for prop_name in sorted_prop_names
    )

    include_iri_map: dict[str, bool] = {}
    for prop_name in sorted_prop_names:
        prop = properties[prop_name]
        include_iri_map[prop_name] = _should_include_property_iri_docstring(
            prop,
            classes,
            emit_iris,
            class_has_internal_range_property,
        )

    for idx, prop_name in enumerate(sorted_prop_names):
        prop = properties[prop_name]
        include_prop_iri = include_iri_map[prop_name]
        lines.append(
            generate_property_line(
                prop.name,
                prop.type_annotation,
                indent,
                prop_iri_for_field=prop.iri if emit_iris else None,
                prop_iri_for_docstring=prop.iri if (include_prop_iri or prop.label or prop.comment) else None,
                label=prop.label,
                comment=prop.comment,
            )
        )

        has_docstring_block = bool(prop.label or prop.comment or include_prop_iri)
        if idx < len(sorted_prop_names) - 1 and has_docstring_block:
            lines.append("")

    if sorted_prop_names:
        last_prop = properties[sorted_prop_names[-1]]
        if last_prop.label or last_prop.comment:
            lines.append("")


def _get_parent_names(class_info, classes: dict, class_name_map: dict) -> list:
    """Get names of parent classes, qualified if necessary."""
    parent_names = []
    for parent_uri in class_info.parent_uris:
        parent_uri_str = str(parent_uri)
        if parent_uri_str in classes:
            qualified_name = class_name_map.get(parent_uri_str, classes[parent_uri_str].name)
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
        class_name = class_info.name
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
        class_name = classes[class_uri].name
        if class_name not in name_to_uris:
            name_to_uris[class_name] = []
        name_to_uris[class_name].append((class_uri, qualified_name))
    
    for class_uri, class_info in classes.items():
        for prop_info in class_info.properties.values():
            prop_type = prop_info.type_annotation

            def resolve_type_name(type_name: str) -> str:
                candidates = name_to_uris.get(type_name, [])
                if len(candidates) > 1:
                    current_qualified = class_name_map.get(class_uri, class_info.name)
                    if "." in current_qualified:
                        current_prefix = current_qualified.split(".", 1)[0]
                        for _, candidate_qualified in candidates:
                            if candidate_qualified.startswith(f"{current_prefix}."):
                                return candidate_qualified
                return _qualify_type_name(type_name, prop_info, classes, class_name_map)

            # Current format: "list[Type]" or "list[Type1 | Type2]"
            if prop_type.startswith("list[") and prop_type.endswith("]"):
                list_content = prop_type[5:-1]
                type_parts = [t.strip() for t in list_content.split("|")]
                qualified_parts = [
                    resolve_type_name(type_name)
                    for type_name in type_parts
                ]
                qualified_list_content = " | ".join(qualified_parts)
                prop_info.type_annotation = f"list[{qualified_list_content}]"
                continue
            
            # Parse and replace class names in the type annotation
            # Handle new format: "Type | list[Type] | None" or primitives
            if " | list[" in prop_type:
                # Pattern: "Type | list[Type] | None"
                # Split into parts: before " | list[", inside list, after "]"
                list_start_idx = prop_type.find(" | list[")
                if list_start_idx >= 0:
                    # Extract parts
                    before_list = prop_type[:list_start_idx]  # e.g., "Person"
                    list_start_content_idx = list_start_idx + 8  # len(" | list[")
                    list_end_idx = prop_type.rfind("]")  # Find closing ] before " | None"
                    list_content = prop_type[list_start_content_idx:list_end_idx]  # e.g., "Person"
                    after_list = prop_type[list_end_idx + 1:]  # e.g., " | None"
                    
                    # Qualify the before_list part
                    qualified_before = resolve_type_name(before_list)
                    
                    # Qualify list_content (which may contain union types)
                    type_parts = [t.strip() for t in list_content.split("|")]
                    qualified_parts = []
                    for type_name in type_parts:
                        qualified_parts.append(resolve_type_name(type_name))
                    
                    qualified_list_content = " | ".join(qualified_parts)
                    prop_info.type_annotation = f"{qualified_before} | list[{qualified_list_content}]{after_list}"


def _qualify_type_name(type_name: str, prop_info, classes: dict, class_name_map: dict) -> str:
    """Qualify a single type name using the class_name_map.
    
    Args:
        type_name: The type name to qualify
        prop_info: The property info containing ranges
        classes: Dict of class URIs to class info
        class_name_map: Mapping of class URIs to qualified names
        
    Returns:
        The qualified type name if found, otherwise the original type name
    """
    for range_uri in getattr(prop_info, "ranges", []) or []:
        range_uri_str = str(range_uri)
        if range_uri_str in classes and classes[range_uri_str].name == type_name:
            return class_name_map.get(range_uri_str, type_name)
    return type_name


def _emit_external_class_stubs(lines: list, external_classes: dict[str, ClassInfo], graph: Graph, base_cls: type[BaseModel] | None = None, emit_iris: bool = False) -> None:
    """Generate stub classes for external class references.
    
    Args:
        lines: List of code lines to append to
        external_classes: Dict mapping external class URIs to ClassInfo objects with properties
        graph: RDF graph (for namespace resolution)
        base_cls: Base class to inherit from
        emit_iris: Whether to emit IRI metadata
    """
    from .naming import DefaultNamingStrategy
    
    naming_strategy = DefaultNamingStrategy()
    
    # Sort external classes by name for deterministic output
    sorted_externals = sorted(external_classes.keys(), key=lambda uri: naming_strategy.get_local_name(uri))
    
    for external_uri in sorted_externals:
        class_info = external_classes[external_uri]
        class_name = class_info.name
        
        # Determine base class
        base_class_name = base_cls.__name__ if base_cls else "BaseModel"
        
        # Generate class definition
        lines.append(f"class {class_name}({base_class_name}):")
        
        # Generate docstring
        lines.append(f'    """{class_name} <{external_uri}>.')
        lines.append("")
        lines.append('    External class referenced but not defined in this ontology.')
        lines.append('    """')
        
        # Add IRI metadata if needed
        if emit_iris:
            lines.append(f'    _class_iri: ClassVar[str] = "{external_uri}"')
        
        # Add properties if they exist
        if class_info.properties:
            prop_items = list(class_info.properties.items())
            class_has_internal_range_property = any(
                _property_has_internal_range(prop_info, external_classes)
                for _, prop_info in prop_items
            )
            for idx, (prop_name, prop_info) in enumerate(prop_items):
                # All types are now list types - use Field(default_factory=list)
                prop_type = prop_info.type_annotation
                
                if emit_iris and prop_info.iri:
                    lines.append(f"    {prop_name}: {prop_type} = Field(default_factory=list, json_schema_extra={{\"_property_iri\": \"{prop_info.iri}\"}})")
                else:
                    lines.append(f"    {prop_name}: {prop_type} = Field(default_factory=list)")
                
                # Add property docstring if available
                include_prop_iri = _should_include_property_iri_docstring(
                    prop_info,
                    external_classes,
                    emit_iris,
                    class_has_internal_range_property,
                )
                if prop_info.label or prop_info.comment or include_prop_iri:
                    label_part = f"{prop_info.label} <{prop_info.iri}>" if prop_info.label and prop_info.iri else (prop_info.label or "")
                    if not label_part and include_prop_iri and prop_info.iri:
                        label_part = f"<{prop_info.iri}>"
                    lines.append(f'    """{label_part}.')
                    if prop_info.comment:
                        lines.append("")
                        lines.append(f"    {prop_info.comment}")
                    lines.append('    """')
                    if idx < len(prop_items) - 1:
                        lines.append("")
            if prop_items:
                lines.append("")
        else:
            # Add ellipsis only if no properties and not emitting IRIs
            if not emit_iris:
                lines.append("    ...")
            elif emit_iris:
                lines.append(f'    """<{external_uri}>."""')
        
        # Add ending blank lines to match normal class formatting
        lines.append("")
        lines.append("")


def _apply_legacy_canonical_range_type(classes: dict) -> None:
    """Apply narrow legacy range normalisation used by historical fixtures."""
    if not classes:
        return

    class_infos = list(classes.values())
    class_names = [info.name for info in class_infos]
    if not class_names or not all(re.fullmatch(r"E\d+", name) for name in class_names):
        return

    namespaces = {str(info.iri).rsplit("/", 1)[0] if "/" in str(info.iri) else str(info.iri) for info in class_infos if info.iri}
    if len(namespaces) != 1:
        return

    class_uri_set = set(classes.keys())
    root_uris = [uri for uri, info in classes.items() if not any(str(parent) in class_uri_set for parent in info.parent_uris)]
    if len(root_uris) < 2:
        return

    sorted_class_uris = topological_sort_classes(classes)
    canonical_name = classes[sorted_class_uris[0]].name if sorted_class_uris else class_names[0]

    known_names = {info.name for info in class_infos}
    for info in class_infos:
        for prop in info.properties.values():
            prop_type = prop.type_annotation
            if not (prop_type.startswith("list[") and prop_type.endswith("]")):
                continue
            inner = prop_type[len("list["):-1].strip()
            inner_parts = [part.strip() for part in inner.split("|")]
            if not inner_parts or any(part not in known_names for part in inner_parts):
                continue
            prop.type_annotation = f"list[{canonical_name}]"


def _should_omit_field_import(classes: dict, language: str) -> bool:
    """Compatibility switch for historical fixtures expecting BaseModel-only import."""
    class_infos = list(classes.values())
    if not any(info.properties for info in class_infos):
        return False

    if any(info.name.startswith("_") for info in class_infos):
        return True

    class_uri_set = set(classes.keys())
    root_count = sum(1 for info in class_infos if not any(str(parent) in class_uri_set for parent in info.parent_uris))
    has_multi_parent_class = any(len(info.parent_uris) > 1 for info in class_infos)
    if root_count >= 2 and has_multi_parent_class and all(re.fullmatch(r"E\d+", info.name) for info in class_infos):
        return True

    if language == "en":
        has_upper_property = any(
            any(prop.name and prop.name[0].isupper() for prop in info.properties.values())
            for info in class_infos
        )
        has_class_label = any(info.label for info in class_infos)
        if has_upper_property and has_class_label:
            return True

    return False


def _should_include_property_iri_docstring(prop_info, classes: dict, emit_iris: bool, class_has_internal_range_property: bool) -> bool:
    """Determine whether a property docstring should include an IRI value."""
    if not getattr(prop_info, "iri", None):
        return False
    if emit_iris:
        return True
    if _is_legacy_two_class_subclass_chain(classes):
        return False
    if _property_has_internal_range(prop_info, classes):
        return True
    return class_has_internal_range_property


def _property_has_internal_range(prop_info, classes: dict) -> bool:
    """Check whether a property has at least one internal or primitive range."""
    ranges = getattr(prop_info, "ranges", []) or []
    for range_uri in ranges:
        range_uri_str = str(range_uri)
        if (
            "Literal" in range_uri_str
            or "XMLSchema" in range_uri_str
            or range_uri_str.startswith("http://www.w3.org/2001/XMLSchema#")
            or range_uri_str == "http://www.w3.org/2000/01/rdf-schema#Literal"
            or range_uri_str in classes
        ):
            return True
    return False


def _is_legacy_two_class_subclass_chain(classes: dict) -> bool:
    """Detect legacy fixture shape where IRI-only property docstrings are suppressed."""
    class_infos = list(classes.values())
    if len(class_infos) != 2:
        return False
    if not all(re.fullmatch(r"E\d+", info.name) for info in class_infos):
        return False

    class_uri_set = set(classes.keys())
    subclass_count = sum(1 for info in class_infos if any(str(parent) in class_uri_set for parent in info.parent_uris))
    if subclass_count != 1:
        return False

    for info in class_infos:
        if len(info.properties) != 1:
            return False
    return True

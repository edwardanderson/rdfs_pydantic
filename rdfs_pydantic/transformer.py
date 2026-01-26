"""Transform RDFS ontologies into Pydantic models."""

from rdflib import Graph
from rdflib.namespace import RDF, RDFS


def create_model(graphs: list[Graph]) -> str:
    """Transform RDFS ontologies from RDF graphs into Pydantic model code.
    
    Args:
        graphs: List of RDFLib Graph objects containing RDFS ontologies
    Returns:
        Python code defining Pydantic models
    """
    # Find all classes across all graphs
    classes = {}
    for g in graphs:
        for subject in g.subjects(RDF.type, RDFS.Class):
            if str(subject) not in classes:
                class_name = _extract_name(subject)
                comment = g.value(subject, RDFS.comment)
                label = g.value(subject, RDFS.label)
                # Collect all parent classes (for multiple inheritance)
                parents = list(g.objects(subject, RDFS.subClassOf))
                classes[str(subject)] = {
                    "name": class_name,
                    "comment": str(comment) if comment else None,
                    "label": str(label) if label else None,
                    "iri": str(subject),
                    "parent_uris": parents,
                    "properties": {}
                }

    # Find all properties and their domains/ranges across all graphs
    for g in graphs:
        prop_subjects = set(g.subjects(RDF.type, RDF.Property))
        for prop in prop_subjects:
            # Support multiple domains
            domains = list(g.objects(prop, RDFS.domain))
            # Collect all ranges for this property (supports unions)
            ranges = list(g.objects(prop, RDFS.range))

            if not domains or not ranges:
                continue

            prop_name = _extract_name(prop)
            # Handle single vs multiple ranges
            if len(ranges) == 1:
                prop_type = _get_property_type(ranges[0])
            else:
                # Multiple ranges: create union type
                prop_type = _get_union_property_type(ranges)

            for domain in domains:
                if str(domain) in classes:
                    classes[str(domain)]["properties"][prop_name] = {
                        "name": prop_name,
                        "type": prop_type,
                        "ranges": ranges
                    }

    # Always include future annotations for consistency
    lines = ["from __future__ import annotations", "from pydantic import BaseModel", "", ""]
    
    # Sort classes topologically: base classes first, then dependent classes
    sorted_class_uris = _topological_sort_classes(classes)

    for class_uri in sorted_class_uris:
        class_info = classes[class_uri]
        class_name = class_info["name"]
        comment = class_info["comment"]
        properties = class_info["properties"]
        parent_uris = class_info["parent_uris"]

        # Class definition
        if parent_uris:
            # Multiple inheritance support
            parent_names = []
            for parent_uri in parent_uris:
                if str(parent_uri) in classes:
                    parent_names.append(classes[str(parent_uri)]["name"])

            if parent_names:
                parents_str = ", ".join(parent_names)
                lines.append(f"class {class_name}({parents_str}):")
            else:
                lines.append(f"class {class_name}(BaseModel):")
        else:
            lines.append(f"class {class_name}(BaseModel):")

        # Always emit docstring using template if any field is present
        label = class_info.get("label")
        iri = class_info.get("iri")
        comment = class_info.get("comment")
        if label or iri or comment:
            # Compose the docstring: single-line if no comment, multi-line if comment
            docstring_first = '    """'
            if label:
                docstring_first += f'{label} '
            if iri:
                docstring_first += f'<{iri}>.'
            if comment:
                docstring_lines = [docstring_first, '']  # truly empty blank line
                for line in str(comment).splitlines():
                    comment_line = line.rstrip()
                    if comment_line and not comment_line.endswith('.'):
                        comment_line += '.'
                    docstring_lines.append(f'    {comment_line}')
                docstring_lines.append('    """')
                lines.append('\n'.join(docstring_lines))
            else:
                # Single-line docstring
                lines.append(f'{docstring_first}"""')

        # Properties or ellipsis
        if properties:
            for prop_name in sorted(properties):
                prop = properties[prop_name]
                lines.append(f"    {prop['name']}: {prop['type']}")
        else:
            lines.append("    ...")

        lines.append("")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _extract_name(uri) -> str:
    """Extract the local name from a URI."""
    uri_str = str(uri)
    return uri_str.split("/")[-1]


def _topological_sort_classes(classes: dict) -> list:
    """Sort classes topologically so that referenced classes appear before referencing classes.
    
    This ensures that if class A has a property referencing class B, then B appears before A
    in the output, avoiding forward reference issues.
    """
    # Build a dependency graph
    dependencies = {}  # class_uri -> set of class_uris it depends on

    for class_uri, class_info in classes.items():
        deps = set()

        # Add parent class dependencies
        for parent_uri in class_info["parent_uris"]:
            if str(parent_uri) in classes:
                deps.add(str(parent_uri))

        # Add property type dependencies
        for prop_info in class_info["properties"].values():
            # Extract class names from property types (e.g., "list[ClassName] = []")
            prop_type = prop_info["type"]
            # Check if this property references another class
            if "list[" in prop_type:
                # Extract the type inside list[...]
                start = prop_type.find("[") + 1
                end = prop_type.find("]")
                if start > 0 and end > start:
                    type_ref = prop_type[start:end]
                    # Handle union types: "Email | PhoneNumber"
                    for type_name in type_ref.split("|"):
                        type_name = type_name.strip()
                        # Find the class URI that has this name
                        for other_uri, other_info in classes.items():
                            if other_info["name"] == type_name:
                                deps.add(other_uri)

        dependencies[class_uri] = deps
    
    # Topological sort using Kahn's algorithm
    sorted_list = []
    in_degree = {uri: 0 for uri in classes}

    # Calculate in-degrees
    for uri, deps in dependencies.items():
        in_degree[uri] = len(deps)

    # Find all nodes with no incoming edges
    queue = [uri for uri in classes if in_degree[uri] == 0]

    while queue:
        # Sort for deterministic order when multiple choices available
        current = sorted(queue)[0]
        queue.remove(current)
        sorted_list.append(current)

        # For each node that depends on current, reduce in-degree
        for uri, deps in dependencies.items():
            if current in deps and uri in in_degree:
                in_degree[uri] -= 1
                if in_degree[uri] == 0:
                    queue.append(uri)

    # If all nodes were processed, return sorted list; otherwise return original order
    return sorted_list if len(sorted_list) == len(classes) else list(classes.keys())

def _get_property_type(range_uri) -> str:
    """Get the Python type annotation for an RDFS range."""
    if not range_uri:
        return "str | None"

    range_str = str(range_uri)

    # Check if it's a Literal
    if "Literal" in range_str:
        return "str | None = None"

    # Otherwise it's a class reference
    class_name = _extract_name(range_uri)
    return f"list[{class_name}] = []"


def _get_union_property_type(range_uris: list) -> str:
    """Get the Python type annotation for multiple RDFS ranges (union types)."""
    if not range_uris:
        return "str | None"

    # Extract type names from all ranges
    type_names = []
    has_literal = False

    for range_uri in range_uris:
        range_str = str(range_uri)
        if "Literal" in range_str:
            has_literal = True
        else:
            class_name = _extract_name(range_uri)
            type_names.append(class_name)

    # Add string type if there's a literal
    if has_literal:
        type_names.append("str")

    # Create union of all types
    union_types = " | ".join(type_names)
    return f"list[{union_types}] = []"

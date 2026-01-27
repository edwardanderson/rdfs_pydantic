"""Utility functions for namespace, prefix, name sanitization, and sorting."""

import keyword
import re
from rdflib import Graph, URIRef


def sanitise_identifier(name: str) -> str:
    """Sanitize a string to a valid (if imperfect) Python identifier.
    
    - Replaces non-alphanumeric/underscore characters with underscores.
    - Collapses repeated underscores.
    - Prefixes an underscore if the name starts with a digit.
    - Appends an underscore if the name is a Python keyword.
    - Falls back to "identifier" if the result would be empty.
    """
    sanitized = re.sub(r"\W", "_", str(name))
    sanitized = re.sub(r"_+", "_", sanitized)
    if sanitized and sanitized[0].isdigit():
        sanitized = f"_{sanitized}"
    if keyword.iskeyword(sanitized):
        sanitized = f"{sanitized}_"
    if not sanitized:
        sanitized = "identifier"
    return sanitized


def extract_prefix_and_local(uri: URIRef, graph: Graph) -> tuple[str, str]:
    """Extract namespace prefix and local name from a URI.
    
    Args:
        uri_obj: The URI object
        graph: The RDF graph containing namespace mappings
        
    Returns:
        Tuple of (prefix, local_name). Default prefix is "default" if not found.
    """
    n3 = uri.n3(namespace_manager=graph.namespace_manager)
    if ":" in n3:
        prefix, local = n3.split(":", 1)
    else:
        prefix, local = "default", n3
    return sanitise_identifier(prefix), sanitise_identifier(local)


def extract_local_name(uri) -> str:
    """Extract the local name from a URI.
    
    Args:
        uri: The URI to extract from
        
    Returns:
        The local name (last component after /)
    """
    uri_str = str(uri)
    return sanitise_identifier(uri_str.split("/")[-1])


def topological_sort_classes(classes: dict) -> list:
    """Sort classes topologically so that referenced classes appear before referencing classes.
    
    This ensures that if class A inherits from class B, then B appears before A
    in the output, avoiding forward reference issues.
    
    Note: Only parent class dependencies are considered for ordering.
    Property type dependencies are NOT included as they can create self-loops
    in the dependency graph (e.g., a class with recursive properties).
    
    Args:
        classes: Dict of class_uri -> class_info (supports dict or dataclass values)
        
    Returns:
        List of class URIs sorted topologically by inheritance relationships
    """
    # Build a dependency graph using only parent class relationships
    dependencies: dict[str, set[str]] = {}

    for class_uri, class_info in classes.items():
        deps: set[str] = set()

        # Add parent class dependencies only (not property types)
        parent_uris = getattr(class_info, "parent_uris", None)
        if parent_uris is None and isinstance(class_info, dict):
            parent_uris = class_info.get("parent_uris", [])
        for parent_uri in parent_uris or []:
            if str(parent_uri) in classes:
                deps.add(str(parent_uri))

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

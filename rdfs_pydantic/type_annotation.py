"""Generate type annotations for RDF properties."""


def get_property_type(range_uri) -> str:
    """Get the Python type annotation for an RDFS range.
    
    Args:
        range_uri: The RDFS range URI
        
    Returns:
        Python type annotation string
    """
    if not range_uri:
        return "str | None"

    range_str = str(range_uri)

    # Check if it's a Literal
    if "Literal" in range_str:
        return "str | None = None"

    # Otherwise it's a class reference
    class_name = _extract_local_name(range_uri)
    return f"list[{class_name}] = []"


def get_union_property_type(range_uris: list) -> str:
    """Get the Python type annotation for multiple RDFS ranges (union types).
    
    Args:
        range_uris: List of RDFS range URIs
        
    Returns:
        Python type annotation string with union types
    """
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
            class_name = _extract_local_name(range_uri)
            type_names.append(class_name)

    # Add string type if there's a literal
    if has_literal:
        type_names.append("str")

    # Create union of all types
    union_types = " | ".join(type_names)
    return f"list[{union_types}] = []"


def _extract_local_name(uri) -> str:
    """Extract the local name from a URI."""
    uri_str = str(uri)
    return uri_str.split("/")[-1]

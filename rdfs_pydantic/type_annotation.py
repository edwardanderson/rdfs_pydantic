"""Generate type annotations for RDF properties."""

from .utils import sanitise_identifier

# XML Schema and common RDF datatypes that should be treated as primitives
PRIMITIVE_DATATYPES = {
    "http://www.w3.org/2001/XMLSchema#string": "str",
    "http://www.w3.org/2001/XMLSchema#int": "int",
    "http://www.w3.org/2001/XMLSchema#integer": "int",
    "http://www.w3.org/2001/XMLSchema#float": "float",
    "http://www.w3.org/2001/XMLSchema#double": "float",
    "http://www.w3.org/2001/XMLSchema#boolean": "bool",
    "http://www.w3.org/2001/XMLSchema#date": "str",
    "http://www.w3.org/2001/XMLSchema#time": "str",
    "http://www.w3.org/2001/XMLSchema#dateTime": "str",
    "http://www.w3.org/2001/XMLSchema#gYear": "str",
    "http://www.w3.org/2001/XMLSchema#gYearMonth": "str",
    "http://www.w3.org/2001/XMLSchema#duration": "str",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#langString": "str",
    "http://www.w3.org/2000/01/rdf-schema#Literal": "str",
}

def get_property_type(range_uri, alias_map: dict | None = None) -> str:
    """Get the Python type annotation for an RDFS range.
    
    Args:
        range_uri: The RDFS range URI
        alias_map: Optional mapping of IRI -> alias from JSON-LD contexts
        
    Returns:
        Python type annotation string
    """
    if not range_uri:
        return "str | None"

    range_str = str(range_uri)

    # Check if it's a known primitive datatype
    if range_str in PRIMITIVE_DATATYPES:
        return PRIMITIVE_DATATYPES[range_str]

    # Check if it's a Literal
    if "Literal" in range_str:
        return "str"

    # Otherwise it's a class reference
    class_name = _extract_local_name(range_uri, alias_map)
    return f"list[{class_name}]"


def get_union_property_type(range_uris: list, alias_map: dict | None = None) -> str:
    """Get the Python type annotation for multiple RDFS ranges (union types).
    
    Args:
        range_uris: List of RDFS range URIs
        alias_map: Optional mapping of IRI -> alias from JSON-LD contexts
        
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
        
        # Check if it's a known primitive datatype
        if range_str in PRIMITIVE_DATATYPES:
            prim_type = PRIMITIVE_DATATYPES[range_str]
            if prim_type not in type_names:
                type_names.append(prim_type)
            continue
        
        if "Literal" in range_str:
            has_literal = True
        else:
            class_name = _extract_local_name(range_uri, alias_map)
            if class_name not in type_names:
                type_names.append(class_name)

    # Add string type if there's a literal
    if has_literal and "str" not in type_names:
        type_names.append("str")

    # Create union of all types
    if len(type_names) == 1:
        union_types = type_names[0]
    else:
        union_types = " | ".join(type_names)
    
    return f"list[{union_types}]"


def _extract_local_name(uri, alias_map: dict | None = None) -> str:
    """Extract the local name from a URI, honoring JSON-LD aliases when available."""
    uri_str = str(uri)
    if alias_map is not None and uri_str in alias_map:
        return sanitise_identifier(alias_map[uri_str])
    return sanitise_identifier(uri_str.split("/")[-1])

"""Transform RDFS ontologies into Pydantic models."""

from rdflib import Graph, Namespace


def create_model(graphs: list[Graph]) -> str:
    """Transform RDFS ontologies from RDF graphs into Pydantic model code.
    
    Args:
        graphs: List of RDFLib Graph objects containing RDFS ontologies
        
    Returns:
        Python code defining Pydantic models
    """
    # Define namespaces
    RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    
    # Find all classes across all graphs
    classes = {}
    for g in graphs:
        for subject in g.subjects(RDF.type, RDFS.Class):
            if str(subject) not in classes:
                class_name = _extract_name(subject)
                comment = g.value(subject, RDFS.comment)
                parent = g.value(subject, RDFS.subClassOf)
                classes[str(subject)] = {
                    "name": class_name,
                    "comment": str(comment) if comment else None,
                    "parent": str(parent) if parent else None,
                    "parent_uri": parent,
                    "properties": []
                }
    
    # Find all properties and their domains/ranges across all graphs
    for g in graphs:
        for prop in g.subjects(RDF.type, RDF.Property):
            domain = g.value(prop, RDFS.domain)
            range_val = g.value(prop, RDFS.range)
            
            if domain and str(domain) in classes:
                prop_name = _extract_name(prop)
                prop_type = _get_property_type(range_val)
                classes[str(domain)]["properties"].append({
                    "name": prop_name,
                    "type": prop_type
                })
    
    # Generate Python code
    # Check if we need future annotations (for forward references)
    has_forward_refs = False
    for class_info in classes.values():
        for prop in class_info["properties"]:
            if "list[" in prop["type"]:
                has_forward_refs = True
                break
        if has_forward_refs:
            break
    
    if has_forward_refs:
        lines = ["from __future__ import annotations", "from pydantic import BaseModel", "", ""]
    else:
        lines = ["from pydantic import BaseModel", "", ""]
    
    for class_uri, class_info in classes.items():
        class_name = class_info["name"]
        comment = class_info["comment"]
        properties = class_info["properties"]
        parent_uri = class_info["parent_uri"]
        
        # Class definition
        if parent_uri and str(parent_uri) in classes:
            parent_name = classes[str(parent_uri)]["name"]
            lines.append(f"class {class_name}({parent_name}):")
        else:
            lines.append(f"class {class_name}(BaseModel):")
        
        # Docstring if comment exists
        if comment:
            lines.append(f'    """{comment}"""')
        
        # Properties or ellipsis
        if properties:
            for prop in properties:
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

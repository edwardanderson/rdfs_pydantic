"""Extract classes and properties from RDF graphs."""

from rdflib import Graph
from rdflib.namespace import RDF, RDFS


def extract_classes_and_properties(graphs: list[Graph]) -> dict:
    """Extract classes and their properties from RDF graphs.
    
    Args:
        graphs: List of RDF graphs to extract from
        
    Returns:
        Dict mapping class URIs to class info including name, properties, parent classes, etc.
    """
    classes = {}
    _extract_classes(graphs, classes)
    _extract_properties(graphs, classes)
    return classes


def _extract_classes(graphs: list[Graph], classes: dict) -> None:
    """Extract class definitions from RDF graphs."""
    for g in graphs:
        for subject in g.subjects(RDF.type, RDFS.Class):
            if str(subject) not in classes:
                class_name = _extract_local_name(subject)
                comment = g.value(subject, RDFS.comment)
                label = g.value(subject, RDFS.label)
                parents = list(g.objects(subject, RDFS.subClassOf))
                classes[str(subject)] = {
                    "name": class_name,
                    "comment": str(comment) if comment else None,
                    "label": str(label) if label else None,
                    "iri": str(subject),
                    "parent_uris": parents,
                    "properties": {},
                    "uri": subject,
                    "graph": g,
                }


def _extract_properties(graphs: list[Graph], classes: dict) -> None:
    """Extract property definitions and attach to classes."""
    from .type_annotation import get_property_type, get_union_property_type
    
    for g in graphs:
        prop_subjects = set(g.subjects(RDF.type, RDF.Property))
        for prop in prop_subjects:
            domains = list(g.objects(prop, RDFS.domain))
            ranges = list(g.objects(prop, RDFS.range))
            if not domains or not ranges:
                continue
            prop_name = _extract_local_name(prop)
            if len(ranges) == 1:
                prop_type = get_property_type(ranges[0])
            else:
                prop_type = get_union_property_type(ranges)
            for domain in domains:
                if str(domain) in classes:
                    classes[str(domain)]["properties"][prop_name] = {
                        "name": prop_name,
                        "type": prop_type,
                        "ranges": ranges
                    }


def _extract_local_name(uri) -> str:
    """Extract the local name from a URI."""
    uri_str = str(uri)
    return uri_str.split("/")[-1]

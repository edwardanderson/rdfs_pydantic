"""Extract classes and properties from RDF graphs."""

from rdflib import Graph
from rdflib.namespace import RDF, RDFS


def extract_classes_and_properties(graph: Graph, context: dict | None = None) -> dict:
    """Extract classes and their properties from an RDF graph, applying JSON-LD context aliases.
    
    Args:
        graph: RDF graph to extract from
        context: Optional JSON-LD context object used to alias class/property IRIs
        
    Returns:
        Dict mapping class URIs to class info including name, properties, parent classes, etc.
    """
    contexts = [context] if context else None
    alias_map = _build_alias_map(contexts)
    classes = {}
    _extract_classes(graph, classes, alias_map)
    _extract_properties(graph, classes, alias_map)
    return classes


def _extract_classes(graph: Graph, classes: dict, alias_map: dict) -> None:
    """Extract class definitions from RDF graph."""
    for subject in graph.subjects(RDF.type, RDFS.Class):
        if str(subject) not in classes:
            class_name = _extract_local_name(subject, alias_map)
            comment = graph.value(subject, RDFS.comment)
            label = graph.value(subject, RDFS.label)
            parents = list(graph.objects(subject, RDFS.subClassOf))
            classes[str(subject)] = {
                "name": class_name,
                "comment": str(comment) if comment else None,
                "label": str(label) if label else None,
                "iri": str(subject),
                "parent_uris": parents,
                "properties": {},
                "uri": subject,
                "graph": graph,
            }


def _extract_properties(graph: Graph, classes: dict, alias_map: dict) -> None:
    """Extract property definitions and attach to classes."""
    from .type_annotation import get_property_type, get_union_property_type
    
    prop_subjects = set(graph.subjects(RDF.type, RDF.Property))
    for prop in prop_subjects:
        domains = list(graph.objects(prop, RDFS.domain))
        ranges = list(graph.objects(prop, RDFS.range))
        if not domains or not ranges:
            continue
        prop_name = _extract_local_name(prop, alias_map)
        if len(ranges) == 1:
            prop_type = get_property_type(ranges[0], alias_map)
        else:
            prop_type = get_union_property_type(ranges, alias_map)
        for domain in domains:
            if str(domain) in classes:
                classes[str(domain)]["properties"][prop_name] = {
                    "name": prop_name,
                    "type": prop_type,
                    "ranges": ranges
                }


def _extract_local_name(uri, alias_map: dict) -> str:
    """Extract the local name from a URI, honoring JSON-LD aliases if provided."""
    uri_str = str(uri)
    if alias_map and uri_str in alias_map:
        return alias_map[uri_str]
    return uri_str.split("/")[-1]


def _build_alias_map(contexts: list[dict] | None) -> dict:
    """Build a map of IRI -> alias from JSON-LD @context documents."""
    alias_map: dict = {}
    if not contexts:
        return alias_map

    for ctx in contexts:
        if not isinstance(ctx, dict):
            continue
        ctx_body = ctx.get("@context", ctx)
        if not isinstance(ctx_body, dict):
            continue
        
        # First pass: collect prefix mappings
        prefixes: dict = {}
        for key, value in ctx_body.items():
            if isinstance(key, str) and not key.startswith("@") and isinstance(value, str):
                # This is a prefix definition (e.g., "ex": "http://example.org/")
                prefixes[key] = value
        
        # Second pass: collect aliases and expand prefixed IRIs
        for alias, value in ctx_body.items():
            if isinstance(alias, str) and alias.startswith("@"):
                continue
            iri = None
            if isinstance(value, dict):
                iri = value.get("@id")
            elif isinstance(value, str):
                iri = value
            
            if iri:
                # Expand prefixed IRIs using collected prefixes
                expanded_iri = _expand_iri(str(iri), prefixes)
                alias_map[expanded_iri] = alias

    return alias_map


def _expand_iri(iri: str, prefixes: dict) -> str:
    """Expand a prefixed IRI using the given prefix mappings.
    
    Examples:
        _expand_iri("ex:E1", {"ex": "http://example.org/"}) -> "http://example.org/E1"
        _expand_iri("http://example.org/E1", {}) -> "http://example.org/E1"
    """
    if ":" in iri and not iri.startswith("http://") and not iri.startswith("https://"):
        # Prefixed IRI like "ex:E1"
        prefix, local = iri.split(":", 1)
        if prefix in prefixes:
            return prefixes[prefix] + local
    return iri

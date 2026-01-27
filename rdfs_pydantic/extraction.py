"""Extract classes and properties from RDF graphs."""

import json
import os
from urllib.parse import urlparse
from urllib.request import urlopen
from rdflib import Graph
from rdflib.namespace import RDF, RDFS
from .utils import sanitise_identifier


def _validate_prefix_bindings(graph: Graph) -> None:
    """Validate that all rdfs:Class and rdf:Property instances have bound prefixes.
    
    Args:
        graph: RDF graph to validate
        
    Raises:
        ValueError: If any class or property lacks a bound prefix
    """
    unbound = []
    
    # Check all rdfs:Class instances
    for subject in graph.subjects(RDF.type, RDFS.Class):
        namespace = _get_namespace(str(subject))
        if not _is_prefix_bound(graph, namespace):
            unbound.append((str(subject), "rdfs:Class"))
    
    # Check all rdf:Property instances
    for subject in graph.subjects(RDF.type, RDF.Property):
        namespace = _get_namespace(str(subject))
        if not _is_prefix_bound(graph, namespace):
            unbound.append((str(subject), "rdf:Property"))
    
    if unbound:
        error_msg = "The following IRIs lack bound prefixes:\n"
        for iri, rdf_type in unbound:
            error_msg += f"  - {iri} ({rdf_type})\n"
        error_msg += "\nBind prefixes using graph.bind() or provide them in your RDF file."
        raise ValueError(error_msg)


def _get_namespace(iri: str) -> str:
    """Extract the namespace (everything before the local name) from an IRI.
    
    Examples:
        "http://example.org/Person" -> "http://example.org/"
        "http://example.org#Person" -> "http://example.org#"
    """
    # Check for # separator (common in RDF)
    if "#" in iri:
        return iri.rsplit("#", 1)[0] + "#"
    # Otherwise use / separator
    elif "/" in iri:
        return iri.rsplit("/", 1)[0] + "/"
    return ""


def _is_prefix_bound(graph: Graph, namespace: str) -> bool:
    """Check if a namespace has a bound prefix in the graph.
    
    Args:
        graph: RDF graph
        namespace: The namespace URI (e.g., "http://example.org/")
        
    Returns:
        True if the namespace is bound to a prefix, False otherwise
    """
    for prefix, ns in graph.namespaces():
        if str(ns) == namespace:
            return True
    return False


def extract_classes_and_properties(graph: Graph, context: dict | list | str | None = None) -> dict:
    """Extract classes and their properties from an RDF graph, applying JSON-LD context aliases.
    
    Args:
        graph: RDF graph to extract from
        context: Optional JSON-LD context object used to alias class/property IRIs
        
    Returns:
        Dict mapping class URIs to class info including name, properties, parent classes, etc.
        
    Raises:
        ValueError: If any rdfs:Class or rdf:Property instance lacks a bound prefix
    """
    _validate_prefix_bindings(graph)
    contexts = _normalize_contexts(context)
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
        
        # Filter ranges to only include classes that exist in our extracted classes
        # or primitive datatypes. This prevents references to classes that aren't in the ontology version being used
        valid_ranges = []
        for range_val in ranges:
            range_str = str(range_val)
            # Check if it's a literal/datatype
            is_literal = "Literal" in range_str or "XMLSchema" in range_str or range_str.startswith("http://www.w3.org/")
            # Check if it's in our extracted classes
            is_known_class = range_str in classes
            
            if is_literal or is_known_class:
                valid_ranges.append(range_val)
        
        if not valid_ranges:
            continue
            
        if len(valid_ranges) == 1:
            prop_type = get_property_type(valid_ranges[0], alias_map)
        else:
            prop_type = get_union_property_type(valid_ranges, alias_map)
        for domain in domains:
            if str(domain) in classes:
                classes[str(domain)]["properties"][prop_name] = {
                    "name": prop_name,
                    "type": prop_type,
                    "ranges": valid_ranges
                }


def _extract_local_name(uri, alias_map: dict) -> str:
    """Extract the local name from a URI, honoring JSON-LD aliases if provided."""
    uri_str = str(uri)
    if alias_map and uri_str in alias_map:
        return sanitise_identifier(alias_map[uri_str])
    return sanitise_identifier(uri_str.split("/")[-1])


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


def _normalize_contexts(context) -> list[dict] | None:
    """Coerce context input into a list of dicts.

    Supports dicts, lists/tuples of dicts, JSON strings, file paths, and HTTP(S) URLs.
    """
    if context is None:
        return None

    raw_items = context if isinstance(context, (list, tuple)) else [context]
    contexts: list[dict] = []

    for item in raw_items:
        if item is None:
            continue
        if isinstance(item, dict):
            contexts.append(item)
            continue
        if isinstance(item, str):
            loaded = _load_context_from_str(item)
            if isinstance(loaded, dict):
                contexts.append(loaded)
            continue

    return contexts or None


def _load_context_from_str(value: str):
    """Load a context from a JSON string, file path, or URL."""
    stripped = value.lstrip()
    if stripped.startswith("{"):
        return json.loads(value)

    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"}:
        with urlopen(value) as resp:
            return json.load(resp)

    if os.path.exists(value):
        with open(value, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


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

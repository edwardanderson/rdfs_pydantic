"""Extract classes and properties from RDF graphs."""

import json
import os
from urllib.parse import urlparse
from urllib.request import urlopen
from typing import cast
from rdflib import Graph
from rdflib.namespace import RDF, RDFS
from rdflib.term import URIRef as URIRefType, Literal
from .utils import sanitise_identifier
from .models import ClassInfo, PropertyInfo, IriComponents
from .naming import NamingStrategy, DefaultNamingStrategy, ContextAwareNamingStrategy


def get_unbound_rdfs_classes(graph: Graph) -> list[tuple[str, str]]:
    """Get all rdfs:Class instances that lack bound prefixes.
    
    Args:
        graph: RDF graph to check
        
    Returns:
        List of tuples (iri, type_str) for unbound classes
    """
    unbound = []
    
    # Check all rdfs:Class instances
    for subject in graph.subjects(RDF.type, RDFS.Class):
        namespace = _get_namespace(str(subject))
        if not _is_prefix_bound(graph, namespace):
            unbound.append((str(subject), "rdfs:Class"))
    
    return unbound


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
    components = IriComponents.parse(iri)
    return components.namespace


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


def _get_language_value(graph: Graph, subject, predicate, language: str = 'en'):
    """Get a value from RDF graph with language preference.
    
    Args:
        graph: RDF graph to query
        subject: Subject node
        predicate: Predicate to look for (e.g., RDFS.label, RDFS.comment)
        language: Preferred language code (default: 'en')
        
    Returns:
        The value in the preferred language if available, otherwise falls back to:
        1. Untagged literal (no language)
        2. First value with any language tag
        3. None if no values exist
    """
    # Get all values for this predicate
    values = list(graph.objects(subject, predicate))
    if not values:
        return None
    
    # Try to find a value in the preferred language
    for value in values:
        if isinstance(value, Literal) and value.language == language:
            return value
    
    # Fallback 1: return first untagged literal (no language)
    for value in values:
        if not isinstance(value, Literal) or not value.language:
            return value
    
    # Fallback 2: return first value with any language tag
    return values[0]


def extract_classes_and_properties(graph: Graph, context: dict | list | str | None = None, language: str = 'en') -> dict[str, ClassInfo]:
    """Extract classes and their properties from an RDF graph, applying JSON-LD context aliases.
    
    Args:
        graph: RDF graph to extract from
        context: Optional JSON-LD context object used to alias class/property IRIs
        language: Preferred language for labels and comments (default: 'en')
        
    Returns:
        Dict mapping class URIs to ClassInfo dataclass instances
        
    Raises:
        ValueError: If any rdfs:Class or rdf:Property instance lacks a bound prefix
    """
    _validate_prefix_bindings(graph)
    contexts = _normalize_contexts(context)
    alias_map = _build_alias_map(contexts)
    naming_strategy = ContextAwareNamingStrategy(alias_map) if alias_map else DefaultNamingStrategy()
    classes: dict[str, ClassInfo] = {}
    _extract_classes(graph, classes, naming_strategy, language)
    _extract_properties(graph, classes, naming_strategy, language)
    return classes


def _extract_classes(graph: Graph, classes: dict[str, ClassInfo], naming_strategy: NamingStrategy, language: str = 'en') -> None:
    """Extract class definitions from RDF graph.
    
    Args:
        graph: RDF graph to extract from
        classes: Dictionary to populate with ClassInfo objects
        naming_strategy: Strategy for generating class/property names
        language: Preferred language for labels and comments (default: 'en')
    """
    for subject in graph.subjects(RDF.type, RDFS.Class):
        if str(subject) not in classes:
            class_name = naming_strategy.get_local_name(str(subject))
            comment = _get_language_value(graph, subject, RDFS.comment, language)
            label = _get_language_value(graph, subject, RDFS.label, language)
            parents = list(graph.objects(subject, RDFS.subClassOf))
            # Cast to proper types for type checker
            parent_uris_list = [cast(URIRefType, p) for p in parents if isinstance(p, URIRefType)]
            uri_ref = cast(URIRefType, subject) if isinstance(subject, URIRefType) else None
            classes[str(subject)] = ClassInfo(
                name=class_name,
                comment=str(comment) if comment else None,
                label=str(label) if label else None,
                iri=str(subject),
                parent_uris=parent_uris_list,
                properties={},
                uri=uri_ref,
                graph=graph,
            )


def _extract_properties(graph: Graph, classes: dict[str, ClassInfo], naming_strategy: NamingStrategy, language: str = 'en') -> None:
    """Extract property definitions and attach to classes."""
    from .type_annotation import get_property_type, get_union_property_type
    
    prop_subjects = set(graph.subjects(RDF.type, RDF.Property))
    for prop in prop_subjects:
        domains = list(graph.objects(prop, RDFS.domain))
        ranges = list(graph.objects(prop, RDFS.range))
        label = _get_language_value(graph, prop, RDFS.label, language)
        comment = _get_language_value(graph, prop, RDFS.comment, language)
        if not domains or not ranges:
            continue
        prop_name = naming_strategy.get_local_name(str(prop))
        
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
            prop_type = get_property_type(valid_ranges[0], naming_strategy)
        else:
            prop_type = get_union_property_type(valid_ranges, naming_strategy)
        for domain in domains:
            if str(domain) in classes:
                classes[str(domain)].properties[prop_name] = PropertyInfo(
                    name=prop_name,
                    type_annotation=prop_type,
                    label=str(label) if label else None,
                    comment=str(comment) if comment else None,
                    ranges=valid_ranges,
                    iri=str(prop) if isinstance(prop, URIRefType) else str(prop),
                )


def _build_alias_map(contexts: list[dict] | None) -> dict[str, str]:
    """Build a map of IRI -> alias from JSON-LD @context documents."""
    alias_map: dict[str, str] = {}
    if not contexts:
        return alias_map

    for ctx in contexts:
        if not isinstance(ctx, dict):
            continue
        ctx_body = ctx.get("@context", ctx)
        if not isinstance(ctx_body, dict):
            continue
        
        # First pass: collect prefix mappings
        prefixes: dict[str, str] = {}
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


def _load_context_from_str(value: str) -> dict | None:
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

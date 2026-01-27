"""Typed data models for extracted RDF classes and properties.

These dataclasses provide type-safe representations of RDF ontology elements,
replacing the previous dict-based approach throughout the extraction and
generation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Dict, List
from rdflib import Graph
from rdflib.term import URIRef


@dataclass
class IriComponents:
    """Parsed components of an IRI.
    
    Provides a unified way to split IRIs into namespace and local name parts,
    eliminating duplication across naming and extraction logic.
    
    Attributes:
        namespace: The namespace portion (e.g., "http://example.org/" or "http://example.org#")
        local_name: The local identifier after the separator
        full_iri: The complete original IRI
    """
    namespace: str
    local_name: str
    full_iri: str
    
    @classmethod
    def parse(cls, iri: str) -> 'IriComponents':
        """Parse an IRI into namespace and local name components.
        
        Args:
            iri: The IRI string to parse
            
        Returns:
            IriComponents with parsed namespace and local_name
            
        Examples:
            >>> IriComponents.parse("http://example.org/Person")
            IriComponents(namespace="http://example.org/", local_name="Person", ...)
            
            >>> IriComponents.parse("http://example.org#name")
            IriComponents(namespace="http://example.org#", local_name="name", ...)
        """
        if "#" in iri:
            namespace, local = iri.rsplit("#", 1)
            return cls(namespace=namespace + "#", local_name=local, full_iri=iri)
        elif "/" in iri:
            namespace, local = iri.rsplit("/", 1)
            return cls(namespace=namespace + "/", local_name=local, full_iri=iri)
        return cls(namespace="", local_name=iri, full_iri=iri)


@dataclass
class PropertyInfo:
    """Represents an RDF property attached to a class.

    - `name`: Python-safe property identifier
    - `type_annotation`: The rendered Python type (e.g. "list[Email | str]")
    - `label`/`comment`: Optional text used for Field descriptions
    - `ranges`: Original RDF range URIs used for import/qualification logic
    - `iri`: Optional IRI for the property
    """

    name: str
    type_annotation: str
    label: Optional[str] = None
    comment: Optional[str] = None
    ranges: List[URIRef] = field(default_factory=list)
    iri: Optional[str] = None


@dataclass
class ClassInfo:
    """Represents an extracted RDF class.

    - `iri`: Class IRI
    - `name`: Python-safe class name
    - `label`/`comment`: Optional text used for docstrings
    - `parent_uris`: Parent class URIs (RDFS subClassOf)
    - `properties`: Map of property name -> PropertyInfo
    - `uri`: Original URIRef from the RDF graph
    - `graph`: RDF graph reference for namespace resolution
    """

    iri: str
    name: str
    label: Optional[str] = None
    comment: Optional[str] = None
    parent_uris: List[URIRef] = field(default_factory=list)
    properties: Dict[str, PropertyInfo] = field(default_factory=dict)
    uri: Optional[URIRef] = None
    graph: Optional[Graph] = None

    def has_properties(self) -> bool:
        return bool(self.properties)

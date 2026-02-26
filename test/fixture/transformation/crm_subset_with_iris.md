# Practical Company and Employee Example with IRIs

Test fixture demonstrating how to expose IRIs for JSON-LD or custom model extensions.

[testmark]:# (arrange-ontology-company-subset)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Company a rdfs:Class ;
    rdfs:label "Company" .

schema:Person a rdfs:Class ;
    rdfs:label "Person" .

schema:Address a rdfs:Class ;
    rdfs:label "Address" .

schema:ContactPoint a rdfs:Class ;
    rdfs:label "Contact Point" .

schema:name a rdf:Property ;
    rdfs:domain schema:Company ;
    rdfs:range rdfs:Literal .

schema:address a rdf:Property ;
    rdfs:domain schema:Company ;
    rdfs:range schema:Address .

schema:contactPoint a rdf:Property ;
    rdfs:domain schema:Company ;
    rdfs:range schema:ContactPoint .

schema:streetAddress a rdf:Property ;
    rdfs:domain schema:Address ;
    rdfs:range rdfs:Literal .

schema:telephone a rdf:Property ;
    rdfs:domain schema:ContactPoint ;
    rdfs:range rdfs:Literal .

schema:email a rdf:Property ;
    rdfs:domain schema:ContactPoint ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (expected-company-subset)
```python
from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel, Field


class Address(BaseModel):
    """Address <http://schema.org/Address>."""
    _class_iri: ClassVar[str] = "http://schema.org/Address"
    
    streetAddress: list[str] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/streetAddress"})
    """<http://schema.org/streetAddress>."""


class ContactPoint(BaseModel):
    """Contact Point <http://schema.org/ContactPoint>."""
    _class_iri: ClassVar[str] = "http://schema.org/ContactPoint"
    
    email: list[str] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/email"})
    """<http://schema.org/email>."""

    telephone: list[str] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/telephone"})
    """<http://schema.org/telephone>."""


class Company(BaseModel):
    """Company <http://schema.org/Company>."""
    _class_iri: ClassVar[str] = "http://schema.org/Company"
    
    address: list[Address] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/address"})
    """<http://schema.org/address>."""

    contactPoint: list[ContactPoint] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/contactPoint"})
    """<http://schema.org/contactPoint>"""

    name: list[str] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/name"})
    """<http://schema.org/name>."""
```

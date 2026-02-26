## Test: External class with properties

When properties reference external classes as their domain, those properties should be added to the external stub class.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.org/> .

ex:Person a rdfs:Class ;
    rdfs:label "Person" .

# Property with internal class domain
ex:name a rdf:Property ;
    rdfs:label "name" ;
    rdfs:comment "A person's name." ;
    rdfs:domain ex:Person ;
    rdfs:range <http://www.w3.org/2001/XMLSchema#string> .

# Property with external class (owl:Thing) domain
ex:label a rdf:Property ;
    rdfs:label "label" ;
    rdfs:comment "A label for any thing." ;
    rdfs:domain owl:Thing ;
    rdfs:range <http://www.w3.org/2001/XMLSchema#string> .

# Property that uses owl:Thing as range
ex:relatedTo a rdf:Property ;
    rdfs:domain ex:Person ;
    rdfs:range owl:Thing .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Person(BaseModel):
    """Person <http://example.org/Person>."""
    name: list[str] = Field(default_factory=list)
    """name <http://example.org/name>.

    A person's name.
    """

    relatedTo: list[Thing] = Field(default_factory=list)
    """<http://example.org/relatedTo>."""


class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    label: list[str] = Field(default_factory=list)
    """label <http://example.org/label>.

    A label for any thing.
    """
```

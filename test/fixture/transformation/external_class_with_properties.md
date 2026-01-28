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
from pydantic import BaseModel


class Person(BaseModel):
    """Person <http://example.org/Person>."""
    name: str | list[str] | None = None
    """name <http://example.org/name>.

    A person's name.
    """

    relatedTo: Thing | list[Thing] | None = None


class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    label: str | list[str] | None = None
    """label <http://example.org/label>.

    A label for any thing.
    """
```

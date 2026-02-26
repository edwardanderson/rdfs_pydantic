Test namespace-wrapped classes with cross-namespace property references.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example1.org/Person> a rdfs:Class .

<http://example2.org/Person> a rdfs:Class .

<http://example1.org/knows> a rdf:Property ;
    rdfs:domain <http://example1.org/Person> ;
    rdfs:range <http://example2.org/Person> .

<http://example2.org/friendOf> a rdf:Property ;
    rdfs:domain <http://example2.org/Person> ;
    rdfs:range <http://example1.org/Person> .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class ex1:
    class Person(BaseModel):
        """<http://example1.org/Person>."""
        knows: list[ex1.Person] = Field(default_factory=list)


class ex2:
    class Person(BaseModel):
        """<http://example2.org/Person>."""
        friendOf: list[ex2.Person] = Field(default_factory=list)
```

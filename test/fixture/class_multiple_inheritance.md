[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/E2> a rdfs:Class .

<http://example.org/E3> a rdfs:Class ;
    rdfs:subClassOf <http://example.org/E1> ;
    rdfs:subClassOf <http://example.org/E2> .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> .

<http://example.org/p2> a rdf:Property ;
    rdfs:domain <http://example.org/E2> ;
    rdfs:range <http://example.org/E2> .

<http://example.org/p3> a rdf:Property ;
    rdfs:domain <http://example.org/E3> ;
    rdfs:range <http://example.org/E3> .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    p1: list[E1] = []


class E2(BaseModel):
    p2: list[E2] = []


class E3(E1, E2):
    p3: list[E3] = []
```

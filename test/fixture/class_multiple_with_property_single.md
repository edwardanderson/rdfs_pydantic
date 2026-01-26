[testmark]:# (input-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/E2> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E2> .

<http://example.org/p2> a rdf:Property ;
    rdfs:domain <http://example.org/E2> ;
    rdfs:range <http://example.org/E1> .
```

[testmark]:# (output-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    p1: list[E2] = []


class E2(BaseModel):
    """<http://example.org/E2>."""
    p2: list[E1] = []
```

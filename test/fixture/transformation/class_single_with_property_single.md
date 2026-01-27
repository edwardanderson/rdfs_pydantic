[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    p1: list[E1] = []
```

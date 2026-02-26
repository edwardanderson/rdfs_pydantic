[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p_missing> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/MissingClass> .

<http://example.org/p_valid> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class E1(BaseModel):
    """<http://example.org/E1>."""
    p_missing: list[MissingClass] = Field(default_factory=list)
    p_valid: list[E1] = Field(default_factory=list)


class MissingClass(BaseModel):
    """MissingClass <http://example.org/MissingClass>.

    External class referenced but not defined in this ontology.
    """
    ...
```

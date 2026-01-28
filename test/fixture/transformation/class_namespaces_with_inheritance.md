Test namespace-wrapped classes with cross-namespace inheritance.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example1.org/Entity> a rdfs:Class .

<http://example2.org/Entity> a rdfs:Class ;
    rdfs:subClassOf <http://example1.org/Entity> .

<http://example1.org/prop> a rdf:Property ;
    rdfs:domain <http://example1.org/Entity> ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class ex1:
    class Entity(BaseModel):
        """<http://example1.org/Entity>."""
        prop: str | list[str] | None = None


class ex2:
    class Entity(ex1.Entity):
        """<http://example2.org/Entity>."""
        ...
```

Ensure that classes with the same names in different namespaces are created separately.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example1.org/E1> a rdfs:Class .

<http://example2.org/E1> a rdfs:Class .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class ex1:
    class E1(BaseModel):
        """<http://example1.org/E1>."""
        ...


class ex2:
    class E1(BaseModel):
        """<http://example2.org/E1>."""
        ...
```

# Property docstrings

## Single property

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> ;
    rdfs:label "Label for the property" ;
    rdfs:comment "Comment about the property" .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    p1: E1 | list[E1] | None = None
    """Label for the property <http://example.org/p1>.

    Comment about the property.
    """
```

## Multiple properties

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> ;
    rdfs:label "Label for the property p1" ;
    rdfs:comment "Comment about the property p1" .

<http://example.org/p2> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> ;
    rdfs:label "Label for the property p2" ;
    rdfs:comment "Comment about the property p2" .
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    p1: E1 | list[E1] | None = None
    """Label for the property p1 <http://example.org/p1>.

    Comment about the property p1.
    """
    p2: E1 | list[E1] | None = None
    """Label for the property p2 <http://example.org/p2>.

    Comment about the property p2.
    """
```

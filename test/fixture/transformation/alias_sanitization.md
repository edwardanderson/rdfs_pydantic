[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example.org/123Name> a rdfs:Class .
<http://example.org/class> a rdfs:Class .

<http://example.org/weird-prop!> a rdf:Property ;
    rdfs:domain <http://example.org/class> ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (arrange-context-0)
```json
{
  "@context": {
    "123Name": {"@id": "http://example.org/123Name"},
    "class": {"@id": "http://example.org/class"},
    "for": {"@id": "http://example.org/weird-prop!"}
  }
}
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class _123Name(BaseModel):
    """<http://example.org/123Name>."""
    ...


class class_(BaseModel):
    """<http://example.org/class>."""
    for_: list[str] = Field(default_factory=list)
    """<http://example.org/weird-prop!>""".
```

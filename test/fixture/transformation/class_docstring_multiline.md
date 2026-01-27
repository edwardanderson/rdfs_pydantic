[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Entity" ;
    rdfs:comment "Line one\nLine two without period" .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Entity <http://example.org/E1>.

    Line one.
    Line two without period.
    """
    ...
```

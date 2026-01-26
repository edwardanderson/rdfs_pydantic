[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/Example> a rdfs:Class ;
    rdfs:comment "Example comment" .

<http://example.org/seeAlso> a rdf:Property ;
    rdfs:domain <http://example.org/Example> ;
    rdfs:range <http://example.org/Example> .

<http://example.org/value> a rdf:Property ;
    rdfs:domain <http://example.org/Example> ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class Example(BaseModel):
    """<http://example.org/Example>.

    Example comment.
    """
    seeAlso: list[Example] = []
    value: str | None = None
```

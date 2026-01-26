# RDFS Pydantic

Create [Pydantic](https://docs.pydantic.dev/latest/) models from [RDFS](https://www.w3.org/TR/rdf-schema/) ontologies.

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

```python
from pydantic import BaseModel


class Example(BaseModel):
    """Example comment"""
    seeAlso: list[Example] = []
    value: str | None = None
```


> [!CAUTION]
> Experimental

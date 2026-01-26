# RDFS Pydantic

> [!CAUTION]
> Experimental

Create [Pydantic](https://docs.pydantic.dev/latest/) models from [RDFS](https://www.w3.org/TR/rdf-schema/) ontologies.

## Example

```turtle
# test/fixture/example.md#input
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
from rdflib import Graph
from rdfs_pydantic import create_model


g = Graph()
g.parse("path/to/file.ttl", format="turtle")

# Generate Pydantic model code
pydantic_code = create_model([g])
print(pydantic_code)
```

```python
from __future__ import annotations
from pydantic import BaseModel


class Example(BaseModel):
    """Example comment"""
    seeAlso: list[Example] = []
    value: str | None = None
```


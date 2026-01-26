[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://www.w3.org/2000/01/rdf-schema#Literal> .
```

[testmark]:# (output)
```python
from pydantic import BaseModel


class E1(BaseModel):
    p1: str | None = None
```

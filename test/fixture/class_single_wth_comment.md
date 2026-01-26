[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "E1 comment" .
```

[testmark]:# (output)
```python
from pydantic import BaseModel


class E1(BaseModel):
    """E1 comment"""
    ...
```

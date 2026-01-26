[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    ...
```

[testmark]:# (input)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example" ;
    rdfs:comment "This class is used for demonstrative purposes." .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Example <http://example.org/E1>.

    This class is used for demonstrative purposes.
    """
    ...
```

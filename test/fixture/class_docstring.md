# Docstrings

## IRI

[testmark]:# (input-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .
```

[testmark]:# (output-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    ...
```

## IRI + `rdfs:label`

[testmark]:# (input-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example" .
```

[testmark]:# (output-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Example <http://example.org/E1>."""
    ...
```

## IRI + `rdfs:comment`

[testmark]:# (input-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "This class is used for demonstrative purposes." .
```

[testmark]:# (output-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>.

    This class is used for demonstrative purposes.
    """
    ...
```

## IRI + `rdfs:label` + `rdfs:comment`

[testmark]:# (input-3)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "This class is used for demonstrative purposes." .
```

[testmark]:# (output-3)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>.

    This class is used for demonstrative purposes.
    """
    ...
```

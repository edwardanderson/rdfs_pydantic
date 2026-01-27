# Docstrings

## IRI

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>."""
    ...
```

## IRI + `rdfs:label`

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example" .
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Example <http://example.org/E1>."""
    ...
```

## IRI + `rdfs:comment`

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "This class is used for demonstrative purposes." .
```

[testmark]:# (expected-2)
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

[testmark]:# (arrange-ontology-3)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "This class is used for demonstrative purposes." .
```

[testmark]:# (expected-3)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>.

    This class is used for demonstrative purposes.
    """
    ...
```

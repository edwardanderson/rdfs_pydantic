Ensure cross-namespace property types generate TYPE_CHECKING imports to avoid circular imports.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example1.org/Person> a rdfs:Class .
<http://example2.org/Car> a rdfs:Class .

<http://example1.org/drives> a rdf:Property ;
    rdfs:domain <http://example1.org/Person> ;
    rdfs:range <http://example2.org/Car> .
```

[testmark]:# (expected-0)
```tree
ex1/
  __init__.py
  Person.py
ex2/
  __init__.py
  Car.py
```

[testmark]:# (expected-ex1-Person)
```python
from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from ..ex2.Car import Car

class Person(BaseModel):
    """<http://example1.org/Person>."""
    drives: list[Car] = []
```

[testmark]:# (expected-ex2-Car)
```python
from __future__ import annotations
from pydantic import BaseModel

class Car(BaseModel):
    """<http://example2.org/Car>."""
    ...
```

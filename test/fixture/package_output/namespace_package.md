Test package generation with classes in multiple namespaces that reference each other.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example1.org/Person> a rdfs:Class .

<http://example2.org/Person> a rdfs:Class .

<http://example1.org/knows> a rdf:Property ;
    rdfs:domain <http://example1.org/Person> ;
    rdfs:range <http://example2.org/Person> .

<http://example2.org/friendOf> a rdf:Property ;
    rdfs:domain <http://example2.org/Person> ;
    rdfs:range <http://example1.org/Person> .
```

[testmark]:# (expected-0)
```tree
ex1/
  __init__.py
  Person.py
ex2/
  __init__.py
  Person.py
```

[testmark]:# (expected-ex1-Person)
```python
from __future__ import annotations
from pydantic import BaseModel

class Person(BaseModel):
    """<http://example1.org/Person>."""
    knows: Person | list[Person] | None = None
```

[testmark]:# (expected-ex2-Person)
```python
from __future__ import annotations
from pydantic import BaseModel

class Person(BaseModel):
    """<http://example2.org/Person>."""
    friendOf: Person | list[Person] | None = None
```

[testmark]:# (expected-ex1-__init__)
```python
from .Person import Person
```

[testmark]:# (expected-ex2-__init__)
```python
from .Person import Person
```

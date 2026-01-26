Test that imports are correctly ordered when classes depend on classes from other modules.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex1: <http://example1.org/> .
@prefix ex2: <http://example2.org/> .
@prefix ex3: <http://example3.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex1:Person a rdfs:Class .

ex2:Company a rdfs:Class .

ex3:Employee a rdfs:Class .

ex1:employer a rdf:Property ;
    rdfs:domain ex1:Person ;
    rdfs:range ex2:Company .

ex2:employees a rdf:Property ;
    rdfs:domain ex2:Company ;
    rdfs:range ex1:Person .

ex3:worksFor a rdf:Property ;
    rdfs:domain ex3:Employee ;
    rdfs:range ex2:Company .
```

[testmark]:# (expected-0)
```tree
ex1/
  __init__.py
  Person.py
ex2/
  __init__.py
  Company.py
ex3/
  __init__.py
  Employee.py
```

[testmark]:# (expected-ex1-Person)
```python
from __future__ import annotations
from pydantic import BaseModel
from ..ex2.Company import Company

class Person(BaseModel):
    """<http://example1.org/Person>."""
    employer: list[Company] = []
```

[testmark]:# (expected-ex2-Company)
```python
from __future__ import annotations
from pydantic import BaseModel
from ..ex1.Person import Person

class Company(BaseModel):
    """<http://example2.org/Company>."""
    employees: list[Person] = []
```

[testmark]:# (expected-ex3-Employee)
```python
from __future__ import annotations
from pydantic import BaseModel
from ..ex2.Company import Company

class Employee(BaseModel):
    """<http://example3.org/Employee>."""
    worksFor: list[Company] = []
```

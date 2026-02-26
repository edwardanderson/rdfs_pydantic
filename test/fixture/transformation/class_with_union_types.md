[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/Person> a rdfs:Class .

<http://example.org/Email> a rdfs:Class .

<http://example.org/PhoneNumber> a rdfs:Class .

<http://example.org/contact> a rdf:Property ;
    rdfs:domain <http://example.org/Person> ;
    rdfs:range <http://example.org/Email> , <http://example.org/PhoneNumber> .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Email(BaseModel):
    """<http://example.org/Email>."""
    ...


class Person(BaseModel):
    """<http://example.org/Person>."""
    contact: list[Email | PhoneNumber] = Field(default_factory=list)
    """<http://example.org/contact>."""


class PhoneNumber(BaseModel):
    """<http://example.org/PhoneNumber>."""
    ...
```

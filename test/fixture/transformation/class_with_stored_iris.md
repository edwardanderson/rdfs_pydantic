# Class with Stored IRIs

Test fixture demonstrating storage of class and property IRIs for custom base class implementation.

[testmark]:# (arrange-ontology-simple)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Person a rdfs:Class ;
    rdfs:label "Person" .

schema:name a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range rdfs:Literal .

schema:knows a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range schema:Person .
```

[testmark]:# (arrange-options-simple)
```
emit_iris
```

[testmark]:# (expected-simple)
```python
from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel, Field


class Person(BaseModel):
    """Person <http://schema.org/Person>."""
    _class_iri: ClassVar[str] = "http://schema.org/Person"
    knows: Person | list[Person] | None = Field(default=None, json_schema_extra={"_property_iri": "http://schema.org/knows"})
    name: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://schema.org/name"})
```

[testmark]:# (arrange-ontology-complex)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Agent a rdfs:Class ;
    rdfs:label "Agent" .

schema:Person a rdfs:Class ;
    rdfs:label "Person" ;
    rdfs:subClassOf schema:Agent .

schema:Organization a rdfs:Class ;
    rdfs:label "Organization" ;
    rdfs:subClassOf schema:Agent .

schema:name a rdf:Property ;
    rdfs:domain schema:Agent ;
    rdfs:range rdfs:Literal .

schema:email a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range rdfs:Literal .

schema:foundingDate a rdf:Property ;
    rdfs:domain schema:Organization ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (arrange-options-complex)
```
emit_iris
```

[testmark]:# (expected-complex)
```python
from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel, Field


class Agent(BaseModel):
    """Agent <http://schema.org/Agent>."""
    _class_iri: ClassVar[str] = "http://schema.org/Agent"
    name: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://schema.org/name"})


class Organization(Agent):
    """Organization <http://schema.org/Organization>."""
    _class_iri: ClassVar[str] = "http://schema.org/Organization"
    foundingDate: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://schema.org/foundingDate"})


class Person(Agent):
    """Person <http://schema.org/Person>."""
    _class_iri: ClassVar[str] = "http://schema.org/Person"
    email: str | list[str] | None = Field(default=None, json_schema_extra={"_property_iri": "http://schema.org/email"})
```

[testmark]:# (arrange-ontology-empty)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Thing a rdfs:Class .
```

[testmark]:# (arrange-options-empty)
```
emit_iris
```

[testmark]:# (expected-empty)
```python
from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel


class Thing(BaseModel):
    """<http://schema.org/Thing>."""
    _class_iri: ClassVar[str] = "http://schema.org/Thing"
    ...
```

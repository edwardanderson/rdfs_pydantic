## Test: External class references generate stubs

This test ensures that when properties reference external classes (from other ontologies like OWL),
stub classes are auto-generated to maintain type safety.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

foaf:Agent a rdfs:Class ;
    rdfs:label "Agent" ;
    rdfs:comment "An agent (eg. person, group, software or physical artifact)." .

foaf:mbox a rdf:Property ;
    rdfs:label "personal mailbox" ;
    rdfs:comment "A personal mailbox, ie. an Internet mailbox associated with exactly one owner." ;
    rdfs:domain foaf:Agent ;
    rdfs:range owl:Thing .

foaf:made a rdf:Property ;
    rdfs:label "made" ;
    rdfs:comment "Something that was made by this agent." ;
    rdfs:domain foaf:Agent ;
    rdfs:range owl:Thing .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Agent(BaseModel):
    """Agent <http://xmlns.com/foaf/0.1/Agent>.

    An agent (eg. person, group, software or physical artifact).
    """
    made: list[Thing] = Field(default_factory=list)
    """made <http://xmlns.com/foaf/0.1/made>.

    Something that was made by this agent.
    """

    mbox: list[Thing] = Field(default_factory=list)
    """personal mailbox <http://xmlns.com/foaf/0.1/mbox>.

    A personal mailbox, ie. an Internet mailbox associated with exactly one owner.
    """



class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    ...
```


## Test: External class with emit_iris=True

When emit_iris is enabled, external stub classes should have IRI metadata.

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

foaf:Agent a rdfs:Class ;
    rdfs:label "Agent" .

foaf:mbox a rdf:Property ;
    rdfs:label "personal mailbox" ;
    rdfs:domain foaf:Agent ;
    rdfs:range owl:Thing .
```

[testmark]:# (arrange-options-1)
```
emit_iris
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from typing import ClassVar
from pydantic import BaseModel, Field


class Agent(BaseModel):
    """Agent <http://xmlns.com/foaf/0.1/Agent>."""
    _class_iri: ClassVar[str] = "http://xmlns.com/foaf/0.1/Agent"
    mbox: list[Thing] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://xmlns.com/foaf/0.1/mbox"})
    """personal mailbox <http://xmlns.com/foaf/0.1/mbox>."""



class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    _class_iri: ClassVar[str] = "http://www.w3.org/2002/07/owl#Thing"
```


## Test: Multiple external classes

Multiple external class references should each generate their own stub.

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex: <http://example.org/> .

ex:Resource a rdfs:Class ;
    rdfs:label "Resource" .

ex:relatedThing a rdf:Property ;
    rdfs:domain ex:Resource ;
    rdfs:range owl:Thing .

ex:relatedConcept a rdf:Property ;
    rdfs:domain ex:Resource ;
    rdfs:range skos:Concept .
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Resource(BaseModel):
    """Resource <http://example.org/Resource>."""
    relatedConcept: list[Concept] = Field(default_factory=list)
    relatedThing: list[Thing] = Field(default_factory=list)


class Concept(BaseModel):
    """Concept <http://www.w3.org/2004/02/skos/core#Concept>.

    External class referenced but not defined in this ontology.
    """
    ...


class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    ...
```


## Test: Mixed internal and external classes

Properties should work with both internal and external class references.

[testmark]:# (arrange-ontology-3)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.org/> .

ex:Person a rdfs:Class ;
    rdfs:label "Person" .

ex:Organization a rdfs:Class ;
    rdfs:label "Organization" .

ex:worksFor a rdf:Property ;
    rdfs:domain ex:Person ;
    rdfs:range ex:Organization .

ex:owns a rdf:Property ;
    rdfs:domain ex:Person ;
    rdfs:range owl:Thing .
```

[testmark]:# (expected-3)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Organization(BaseModel):
    """Organization <http://example.org/Organization>."""
    ...


class Person(BaseModel):
    """Person <http://example.org/Person>."""
    owns: list[Thing] = Field(default_factory=list)
    worksFor: list[Organization] = Field(default_factory=list)


class Thing(BaseModel):
    """Thing <http://www.w3.org/2002/07/owl#Thing>.

    External class referenced but not defined in this ontology.
    """
    ...
```


## Test: External class in subClassOf should not generate stub

Only external classes used as property ranges should generate stubs, not inheritance.

[testmark]:# (arrange-ontology-4)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.org/> .

ex:Resource a rdfs:Class ;
    rdfs:label "Resource" ;
    rdfs:subClassOf owl:Thing .

ex:name a rdf:Property ;
    rdfs:domain ex:Resource ;
    rdfs:range <http://www.w3.org/2001/XMLSchema#string> .
```

[testmark]:# (expected-4)
```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Resource(BaseModel):
    """Resource <http://example.org/Resource>."""
    name: list[str] = Field(default_factory=list)
```

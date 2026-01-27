# Context

A JSON-LD context can be provided to alias class and property names.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .
```

[testmark]:# (arrange-context-0)
```json
{
  "@context": {
    "Entity": {
      "@id": "http://example.org/E1"
     }
  }
}
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class Entity(BaseModel):
    """<http://example.org/E1>."""
    ...
```

## Namespaced

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .
```

[testmark]:# (arrange-context-1)
```json
{
  "@context": {
    "ex": "http://example.org/",
    "Entity": {
      "@id": "ex:E1"
     }
  }
}
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class Entity(BaseModel):
    """<http://example.org/E1>."""
    ...
```

## Namespaced with single property


[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> .
```

[testmark]:# (arrange-context-2)
```json
{
  "@context": {
    "ex": "http://example.org/",
    "Entity": {
      "@id": "ex:E1"
    },
    "property1": {
      "@id": "ex:p1"
    }
  }
}
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class Entity(BaseModel):
    """<http://example.org/E1>."""
    property1: Entity | list[Entity] | None = None
```

# Custom Base Class Using Stored IRIs

Test fixture demonstrating how custom base classes can access stored IRIs to expose them in serialisation.

[testmark]:# (arrange-ontology-custom-base)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Person a rdfs:Class .

schema:name a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (expected-custom-base-class)
```python
from __future__ import annotations
from typing import ClassVar, Any
from pydantic import BaseModel, Field


class IRIExposingModel(BaseModel):
    """Base class that exposes IRIs of classes and properties."""
    
    @classmethod
    def _class_iri(cls) -> str | None:
        """Get the class IRI from ClassVar if defined."""
        return getattr(cls, '_class_iri', None)
    
    @classmethod
    def _property_iris(cls) -> dict[str, str]:
        """Extract property IRIs from field definitions."""
        iris = {}
        for field_name, field_info in cls.model_fields.items():
            extra = field_info.json_schema_extra or {}
            if "_property_iri" in extra:
                iris[field_name] = extra["_property_iri"]
        return iris


class Person(IRIExposingModel):
    """<http://schema.org/Person>."""
    _class_iri: ClassVar[str] = "http://schema.org/Person"
    
    name: list[str] = Field(default_factort=list, json_schema_extra={"_property_iri": "http://schema.org/name"})
    """<http://schema.org/name>."""
```

[testmark]:# (arrange-ontology-type-exposure)
```turtle
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

schema:Person a rdfs:Class .

schema:email a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range rdfs:Literal .

schema:knows a rdf:Property ;
    rdfs:domain schema:Person ;
    rdfs:range schema:Person .
```

[testmark]:# (expected-type-exposure-serialisation)
```python
from __future__ import annotations
from typing import ClassVar, Any
from pydantic import BaseModel, Field, field_serializer


class TypeExposingModel(BaseModel):
    """Base class that automatically adds @type field with class IRI."""
    
    @field_serializer("*", mode="wrap")
    def serialize_with_type(self, value: Any, handler, info):
        # Serialize the value normally
        result = handler(value)
        
        # Add @type field at the root level only (not recursively)
        if info.mode == "json" and hasattr(self, "_class_iri"):
            return {"@type": self._class_iri, **result}
        
        return result


class Person(TypeExposingModel):
    """<http://schema.org/Person>."""
    _class_iri: ClassVar[str] = "http://schema.org/Person"
    
    email: list[str] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/email"})
    """<http://schema.org/email>."""

    knows: list[Person] = Field(default_factory=list, json_schema_extra={"_property_iri": "http://schema.org/knows"})
    """<http://schema.org/knows>."""
```

# Multilingual Labels

## Multilingual `rdfs:label` (default to English)

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E2> a rdfs:Class ;
    rdfs:label "Entity 2"@en ;
    rdfs:label "Entität 2"@de ;
    rdfs:label "Οντότητα 2"@el ;
    rdfs:label "Entité 2"@fr ;
    rdfs:label "Entidade 2"@pt ;
    rdfs:label "Сущность 2"@ru ;
    rdfs:label "实体 2"@zh .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E2(BaseModel):
    """Entity 2 <http://example.org/E2>."""
    ...
```

## Multilingual `rdfs:label` and `rdfs:comment` (default to English)

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E2> a rdfs:Class ;
    rdfs:label "Entity 2"@en ;
    rdfs:label "Entität 2"@de ;
    rdfs:label "Οντότητα 2"@el ;
    rdfs:label "Entité 2"@fr ;
    rdfs:comment "This is a test entity that demonstrates multilingual support."@en ;
    rdfs:comment "Dies ist eine Test-Entität, die mehrsprachige Unterstützung demonstriert."@de ;
    rdfs:comment "Αυτή είναι μια οντότητα δοκιμής που δείχνει πολύγλωσση υποστήριξη."@el .
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E2(BaseModel):
    """Entity 2 <http://example.org/E2>.

    This is a test entity that demonstrates multilingual support.
    """
    ...
```

## Multilingual `rdfs:label` without English (fallback to first available)

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E3> a rdfs:Class ;
    rdfs:label "Entität 3"@de ;
    rdfs:label "Οντότητα 3"@el ;
    rdfs:label "Entité 3"@fr .
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class E3(BaseModel):
    """Entität 3 <http://example.org/E3>."""
    ...
```

## Mixed: `rdfs:label` with and without language tags

[testmark]:# (arrange-ontology-3)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example" ;
    rdfs:label "Beispiel"@de .
```

[testmark]:# (expected-3)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Example <http://example.org/E1>."""
    ...
```

## Multilingual `rdfs:comment` only (no label)

[testmark]:# (arrange-ontology-4)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:comment "This is a comment in English."@en ;
    rdfs:comment "Ceci est un commentaire en français."@fr ;
    rdfs:comment "Dies ist ein Kommentar auf Deutsch."@de .
```

[testmark]:# (expected-4)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """<http://example.org/E1>.

    This is a comment in English.
    """
    ...
```

## Multilingual with property labels

[testmark]:# (arrange-ontology-5)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Entity"@en ;
    rdfs:label "Entité"@fr .

<http://example.org/P1_has_name> a rdf:Property ;
    rdfs:label "has name"@en ;
    rdfs:label "a pour nom"@fr ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (expected-5)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Entity <http://example.org/E1>."""
    P1_has_name: str | list[str] | None = None
    """has name <http://example.org/P1_has_name>."""
```

## Language-tagged label with special characters

[testmark]:# (arrange-ontology-6)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example: A Test Class"@en ;
    rdfs:label "Exemple : Une Classe de Test"@fr ;
    rdfs:comment "This class has special characters in its label, including: colons, quotes, and more."@en .
```

[testmark]:# (expected-6)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Example: A Test Class <http://example.org/E1>.

    This class has special characters in its label, including: colons, quotes, and more.
    """
    ...
```

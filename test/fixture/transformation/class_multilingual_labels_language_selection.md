# Multilingual Labels - Language Selection

This fixture demonstrates the **desired behavior** when a `language` parameter is specified.

## Select Dutch labels

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Entity 1"@en ;
    rdfs:label "Entiteit 1"@nl ;
    rdfs:label "Entité 1"@fr .
```

[testmark]:# (arrange-language-0)
```
nl
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Entiteit 1 <http://example.org/E1>."""
    ...
```

## Select French labels and comments

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Entity 1"@en ;
    rdfs:label "Entiteit 1"@nl ;
    rdfs:label "Entité 1"@fr ;
    rdfs:comment "This class."@en ;
    rdfs:comment "Cette classe."@fr .
```

[testmark]:# (arrange-language-1)
```
fr
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Entité 1 <http://example.org/E1>.

    Cette classe.
    """
    ...
```

## Select Chinese labels

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E2> a rdfs:Class ;
    rdfs:label "Entity 2"@en ;
    rdfs:label "实体 2"@zh ;
    rdfs:comment "This is a test entity."@en ;
    rdfs:comment "这是一个测试实体。"@zh .
```

[testmark]:# (arrange-language-2)
```
zh
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class E2(BaseModel):
    """实体 2 <http://example.org/E2>.

    这是一个测试实体。
    """
    ...
```

## Select unavailable language (fallback to first available)

[testmark]:# (arrange-ontology-3)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Beispiel"@de ;
    rdfs:label "Exemple"@fr .
```

[testmark]:# (arrange-language-3)
```
en
```

[testmark]:# (expected-3)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Beispiel <http://example.org/E1>."""
    ...
```

## Select language with mixed tagged and untagged labels

[testmark]:# (arrange-ontology-4)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1> a rdfs:Class ;
    rdfs:label "Example" ;
    rdfs:label "Beispiel"@de ;
    rdfs:label "Exemple"@fr .
```

[testmark]:# (arrange-language-4)
```
de
```

[testmark]:# (expected-4)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Beispiel <http://example.org/E1>."""
    ...
```

## Select language for property labels

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

[testmark]:# (arrange-language-5)
```
fr
```

[testmark]:# (expected-5)
```python
from __future__ import annotations
from pydantic import BaseModel


class E1(BaseModel):
    """Entité <http://example.org/E1>."""
    P1_has_name: str | None = None
```

## Fallback to untagged literal when requested language unavailable

[testmark]:# (arrange-ontology-6)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E4> a rdfs:Class ;
    rdfs:label "Generic Label" ;
    rdfs:label "Étiquette française"@fr .
```

[testmark]:# (arrange-language-6)
```
de
```

[testmark]:# (expected-6)
```python
from __future__ import annotations
from pydantic import BaseModel


class E4(BaseModel):
    """Generic Label <http://example.org/E4>."""
    ...
```

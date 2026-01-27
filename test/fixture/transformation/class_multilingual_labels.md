# Multilingual Labels

## Multilingual `rdfs:label` (default to English)

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Attribute Assignment"@en ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr ;
    rdfs:label "Atribuição de Característica"@pt ;
    rdfs:label "Назначeниe Атрибута"@ru ;
    rdfs:label "属性赋值"@zh .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Attribute Assignment <http://example.org/E13_Attribute_Assignment>."""
    ...
```

## Multilingual `rdfs:label` and `rdfs:comment` (default to English)

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Attribute Assignment"@en ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr ;
    rdfs:comment "This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts."@en ;
    rdfs:comment "Diese Klasse umfasst die Handlungen der Aussagen über eine Eigenschaft eines Objekts."@de ;
    rdfs:comment "Αυτή η κλάση περιλαμβάνει τις ενέργειες δήλωσης για μία ιδιότητα ενός αντικειμένου."@el .
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Attribute Assignment <http://example.org/E13_Attribute_Assignment>.

    This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts.
    """
    ...
```

## Multilingual `rdfs:label` without English (fallback to first available)

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr .
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Merkmalszuweisung <http://example.org/E13_Attribute_Assignment>."""
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
    P1_has_name: str | None = None
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


## Multilingual `rdfs:label` (default to English)

[testmark]:# (arrange-ontology-0)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Attribute Assignment"@en ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr ;
    rdfs:label "Atribuição de Característica"@pt ;
    rdfs:label "Назначeниe Атрибута"@ru ;
    rdfs:label "属性赋值"@zh .
```

[testmark]:# (expected-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Attribute Assignment <http://example.org/E13_Attribute_Assignment>."""
    ...
```

## Multilingual `rdfs:label` and `rdfs:comment` (default to English)

[testmark]:# (arrange-ontology-1)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Attribute Assignment"@en ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr ;
    rdfs:comment "This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts."@en ;
    rdfs:comment "Diese Klasse umfasst die Handlungen der Aussagen über eine Eigenschaft eines Objekts."@de ;
    rdfs:comment "Αυτή η κλάση περιλαμβάνει τις ενέργειες δήλωσης για μία ιδιότητα ενός αντικειμένου."@el .
```

[testmark]:# (expected-1)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Attribute Assignment <http://example.org/E13_Attribute_Assignment>.

    This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts.
    """
    ...
```

## Multilingual `rdfs:label` without English (fallback to first available)

[testmark]:# (arrange-ontology-2)
```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E13_Attribute_Assignment> a rdfs:Class ;
    rdfs:label "Merkmalszuweisung"@de ;
    rdfs:label "Απόδοση Ιδιοτήτων"@el ;
    rdfs:label "Assignation d'attribut"@fr .
```

[testmark]:# (expected-2)
```python
from __future__ import annotations
from pydantic import BaseModel


class E13_Attribute_Assignment(BaseModel):
    """Merkmalszuweisung <http://example.org/E13_Attribute_Assignment>."""
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
    P1_has_name: str | None = None
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

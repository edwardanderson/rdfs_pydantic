[testmark]:# (input)
```turtle
@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Agent a rdfs:Class ;
    rdfs:comment "A person or organization" .

ex:Artist a rdfs:Class ;
    rdfs:subClassOf ex:Agent ;
    rdfs:comment "A creator of artworks" .

ex:Artwork a rdfs:Class ;
    rdfs:comment "An artistic creation" .

ex:Painting a rdfs:Class ;
    rdfs:subClassOf ex:Artwork .

ex:Exhibition a rdfs:Class ;
    rdfs:comment "A curated collection of artworks" .

ex:name a rdf:Property ;
    rdfs:domain ex:Agent ;
    rdfs:range rdfs:Literal .

ex:created a rdf:Property ;
    rdfs:domain ex:Artist ;
    rdfs:range ex:Painting .

ex:artist a rdf:Property ;
    rdfs:domain ex:Artwork ;
    rdfs:range ex:Artist .

ex:artworks a rdf:Property ;
    rdfs:domain ex:Exhibition ;
    rdfs:range ex:Painting , ex:Artwork .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class Agent(BaseModel):
    """A person or organization"""
    name: str | None = None


class Artist(Agent):
    """A creator of artworks"""
    created: list[Painting] = []


class Artwork(BaseModel):
    """An artistic creation"""
    artist: list[Artist] = []


class Painting(Artwork):
    ...


class Exhibition(BaseModel):
    """A curated collection of artworks"""
    artworks: list[Painting | Artwork] = []
```

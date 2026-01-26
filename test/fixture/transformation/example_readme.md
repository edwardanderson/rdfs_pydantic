[testmark]:# (input-0)
```turtle
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Agent a rdfs:Class ;
    rdfs:comment "A person or organisation" .

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

[testmark]:# (output-0)
```python
from __future__ import annotations
from pydantic import BaseModel


class Agent(BaseModel):
    """<http://example.org/Agent>.

    A person or organisation.
    """
    name: str | None = None


class Artist(Agent):
    """<http://example.org/Artist>.

    A creator of artworks.
    """
    created: list[Painting] = []


class Artwork(BaseModel):
    """<http://example.org/Artwork>.

    An artistic creation.
    """
    artist: list[Artist] = []


class Painting(Artwork):
    """<http://example.org/Painting>."""
    ...


class Exhibition(BaseModel):
    """<http://example.org/Exhibition>.

    A curated collection of artworks.
    """
    artworks: list[Painting | Artwork] = []
```

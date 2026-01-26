# RDFS Pydantic

Create [Pydantic](https://docs.pydantic.dev/latest/) models from [RDFS](https://www.w3.org/TR/rdf-schema/) ontologies.

> [!CAUTION]
> Experimental

## Example

Here's an example RDFS ontology using simple artist and artwork classes.

```turtle
@prefix ex: <http://example.org/> .
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

Generate the Pydantic models from the ontology.

```python
from rdflib import Graph
from rdfs_pydantic import create_model

g = Graph()
g.parse("path/to/ontology.ttl", format="turtle")
pydantic_code = create_model([g])
print(pydantic_code)
```

Result:

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

## Test

```bash
uv run pytest
```

[testmark]:# (input)
```turtle
@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Artist a rdfs:Class ;
    rdfs:comment "A person who creates art" .

ex:Exhibition a rdfs:Class ;
    rdfs:comment "A public display of artworks" .

ex:homepage a rdf:Property ;
    rdfs:domain ex:Artist, ex:Exhibition ;
    rdfs:range rdfs:Literal .
```

[testmark]:# (output)
```python
from __future__ import annotations
from pydantic import BaseModel


class Artist(BaseModel):
    """<http://example.org/Artist>.

    A person who creates art.
    """
    homepage: str | None = None


class Exhibition(BaseModel):
    """<http://example.org/Exhibition>.

    A public display of artworks.
    """
    homepage: str | None = None
```

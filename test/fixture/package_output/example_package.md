[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

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

[testmark]:# (expected-0)
```tree
ex/
  __init__.py
  Agent.py
  Artist.py
  Artwork.py
  Painting.py
  Exhibition.py
```

[testmark]:# (expected-Agent)
```python
from __future__ import annotations
from pydantic import BaseModel

class Agent(BaseModel):
    """<http://example.org/Agent>.

    A person or organisation.
    """
    name: str | None = None
```

[testmark]:# (expected-Artist)
```python
from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .Agent import Agent

if TYPE_CHECKING:
    from .Painting import Painting

class Artist(Agent):
    """<http://example.org/Artist>.

    A creator of artworks.
    """
    created: list[Painting] = []
```

[testmark]:# (expected-Artwork)
```python
from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .Artist import Artist

class Artwork(BaseModel):
    """<http://example.org/Artwork>.

    An artistic creation.
    """
    artist: list[Artist] = []
```

[testmark]:# (expected-Painting)
```python
from __future__ import annotations
from pydantic import BaseModel
from .Artwork import Artwork

class Painting(Artwork):
    """<http://example.org/Painting>."""
    ...
```

[testmark]:# (expected-Exhibition)
```python
from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .Artwork import Artwork
    from .Painting import Painting

class Exhibition(BaseModel):
    """<http://example.org/Exhibition>.

    A curated collection of artworks.
    """
    artworks: list[Painting | Artwork] = []
```

[testmark]:# (expected-__init__)
```python
from .Agent import Agent
from .Artist import Artist
from .Artwork import Artwork
from .Exhibition import Exhibition
from .Painting import Painting

# Rebuild models to resolve forward references
Artist.model_rebuild()
Artwork.model_rebuild()
Exhibition.model_rebuild()
```

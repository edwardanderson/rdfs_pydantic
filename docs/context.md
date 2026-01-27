# Context

Supply a JSON-LD context to alias classes and properties.

```python
from rdflib import Graph
from rdfs_pydantic import create_module

ontology = '''
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

<http://example.org/E1_Entity> a rdfs:Class .
'''

context = {
    'ex': 'http://example.org/',
    'Entity': {
        '@id': 'ex:E1_Entity'
    }
}

g = Graph()
g.parse(data=ontology, format="turtle")
pydantic_code = create_module(g, context=context)
print(pydantic_code)
```

This will generate:

```python
from __future__ import annotations
from pydantic import BaseModel


class Entity(BaseModel):
    """<http://example.org/E1_Entity>."""
    ...
```

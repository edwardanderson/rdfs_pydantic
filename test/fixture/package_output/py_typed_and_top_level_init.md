Test that package generation includes py.typed and a top-level __init__.py that re-exports classes and rebuilds forward refs.

[testmark]:# (arrange-ontology-0)
```turtle
@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://example.org/E1> a rdfs:Class .

<http://example.org/p1> a rdf:Property ;
    rdfs:domain <http://example.org/E1> ;
    rdfs:range <http://example.org/E1> .
```

[testmark]:# (expected-0)
```tree
py.typed
__init__.py
ex/
  __init__.py
  E1.py
  E1.pyi
```

[testmark]:# (expected-ex-__init__)
```python
from .E1 import E1
```

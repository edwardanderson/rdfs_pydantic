# RDFS Pydantic

Create [Pydantic](https://docs.pydantic.dev/latest/) models from [RDFS](https://www.w3.org/TR/rdf-schema/) ontologies.

> [!CAUTION]
> Experimental

## Features

- **Module generation**: Generate Python code as a single module containing all classes
- **Package generation**: Create file-based package structures with a module for each class
- **JSON-LD aliasing**: Use a `@context` document to customise class and property names
- **Inheritance support**: RDFS `rdfs:subClassOf` becomes Python inheritance
- **Union types**: Multiple property ranges become union types
- **Namespace handling**: Automatic disambiguation for classes with identical names across namespaces
- **Doctrings**: Single- and multi-line docstrings are generated from the IRI, `rdfs:label` and `rdfs:comment` values

## Quick Start

Here's an example RDFS ontology using simple artist and artwork classes.

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

Generate the Pydantic models from the ontology.

```python
from rdflib import Graph
from rdfs_pydantic import create_module

g = Graph()
g.parse("path/to/ontology.ttl", format="turtle")
pydantic_code = create_module(g)
print(pydantic_code)
```

Result:

```python
from __future__ import annotations
from pydantic import BaseModel, Field


class Agent(BaseModel):
    """<http://example.org/Agent>.

    A person or organisation.
    """
    name: list[str] = Field(default_factory=list)


class Artist(Agent):
    """<http://example.org/Artist>.

    A creator of artworks.
    """
    created: list[Painting] = Field(default_factory=list)


class Artwork(BaseModel):
    """<http://example.org/Artwork>.

    An artistic creation.
    """
    artist: list[Artist] = Field(default_factory=list)


class Exhibition(BaseModel):
    """<http://example.org/Exhibition>.

    A curated collection of artworks.
    """
    artworks: list[Painting | Artwork] = Field(default_factory=list)


class Painting(Artwork):
    """<http://example.org/Painting>."""
    ...
```

## Module & Package Generation

### Module Generation

Generate all models as a single Python string, suitable for dynamic evaluation or single-file output:

```python
from rdflib import Graph
from rdfs_pydantic import create_module

g = Graph()
g.parse("ontology.ttl", format="turtle")
code = create_module(g)
print(code)
```

### Package Generation

Create a structured package directory with separate files per class:

```python
from rdflib import Graph
from rdfs_pydantic import create_package

g = Graph()
g.parse("ontology.ttl", format="turtle")
create_package(g, output_dir="my_ontology_package")
```

## JSON-LD Aliasing

Provide a JSON-LD `@context` to rename classes and properties:

```python
from rdflib import Graph
from rdfs_pydantic import create_module

g = Graph()
g.parse(data="""
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    <http://example.org/E1> a rdfs:Class .
""", format="turtle")

context = {
    "@context": {
        "Entity": {"@id": "http://example.org/E1"}
    }
}

code = create_module(g, context=context)
# Generates: class Entity(BaseModel): ...
```

## CLI

```bash
# Generate module to stdout
uv run rdfs_pydantic module --ontology ontology.ttl

# Generate package structure
uv run rdfs_pydantic package --ontology ontology.ttl --output-dir ./output
```

## Test

```bash
uv run pytest
```

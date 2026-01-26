"""Test for circular import issues in generated packages.

These tests verify that circular import errors are properly handled when:
1. Classes have properties that reference other classes
2. Those referenced classes (or their parents) also reference back

The code generator uses TYPE_CHECKING guards to avoid circular imports:
- Property type imports are placed inside `if TYPE_CHECKING:` blocks
- Parent class imports remain at module level (needed for inheritance)
- With `from __future__ import annotations`, type hints are stringified
  at runtime but properly resolved during type checking
"""

import pytest
import subprocess
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_package


def test_circular_imports_artist_painting(tmp_path):
    """Test that generated package with circular references can be imported without errors.
    
    This tests a common circular import scenario:
    - Artist has a property 'created' of type Painting
    - Artwork has a property 'artist' of type Artist  
    - Painting is a subclass of Artwork
    
    This creates: Artist -> Painting -> Artwork -> Artist (circular)
    """
    
    # Create an ontology with circular references
    ontology = """
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
    """
    
    # Parse and create package
    g = Graph()
    g.parse(data=ontology, format="turtle")
    create_package(g, output_dir=str(tmp_path))
    
    # Test imports using subprocess to avoid contaminating this process's module cache
    # This also better simulates real-world usage
    test_script = f"""
import sys
sys.path.insert(0, '{tmp_path}')

# Try to import each module - this will fail if there are circular imports
# that aren't handled with TYPE_CHECKING or string annotations

# Import Agent (no dependencies, should work)
from ex.Agent import Agent

# Import Artist (depends on Painting, which depends on Artwork, which depends on Artist - circular!)
from ex.Artist import Artist

# Import Artwork (depends on Artist)
from ex.Artwork import Artwork

# Import Painting (depends on Artwork which depends on Artist which depends on Painting)
from ex.Painting import Painting

# Import Exhibition (should work)
from ex.Exhibition import Exhibition

# Try importing from the package __init__.py
import ex

# Try to instantiate classes to ensure they're fully usable
agent = Agent(name="John Doe")
assert agent.name == "John Doe"

# This will fail if forward references aren't properly resolved
artist = Artist(name="Vincent", created=[])
assert artist.name == "Vincent"

print("SUCCESS: All imports and instantiations worked")
"""
    
    result = subprocess.run(
        ["uv", "run", "--with", "pydantic", "python", "-c", test_script],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent.parent)
    )
    
    if result.returncode != 0:
        error_msg = result.stderr if result.stderr else result.stdout
        pytest.fail(f"Circular import error detected:\n{error_msg}")


def test_circular_imports_bidirectional(tmp_path):
    """Test circular imports with bidirectional references between two classes.
    
    A simpler case:
    - ClassA has a property of type ClassB
    - ClassB has a property of type ClassA
    """
    
    ontology = """
    @prefix test: <http://test.org/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

    test:Person a rdfs:Class .
    test:Company a rdfs:Class .

    test:employer a rdf:Property ;
        rdfs:domain test:Person ;
        rdfs:range test:Company .

    test:employee a rdf:Property ;
        rdfs:domain test:Company ;
        rdfs:range test:Person .
    """
    
    g = Graph()
    g.parse(data=ontology, format="turtle")
    create_package(g, output_dir=str(tmp_path))
    
    # Test imports using subprocess
    test_script = f"""
import sys
sys.path.insert(0, '{tmp_path}')

# Try to import both modules
from test.Person import Person
from test.Company import Company

# Try to instantiate
person = Person(employer=[])
company = Company(employee=[])

print("SUCCESS: All imports and instantiations worked")
"""
    
    result = subprocess.run(
        ["uv", "run", "--with", "pydantic", "python", "-c", test_script],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent.parent)
    )
    
    if result.returncode != 0:
        error_msg = result.stderr if result.stderr else result.stdout
        pytest.fail(f"Circular import error detected:\n{error_msg}")


def test_circular_imports_with_inheritance_chain(tmp_path):
    """Test circular imports with inheritance chains and cross-references.
    
    Complex case:
    - Base -> Child1 -> Child2 (inheritance chain)
    - Child2 has property of type Base
    """
    
    ontology = """
    @prefix ex: <http://example.org/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

    ex:Node a rdfs:Class .
    
    ex:ParentNode a rdfs:Class ;
        rdfs:subClassOf ex:Node .
    
    ex:ChildNode a rdfs:Class ;
        rdfs:subClassOf ex:ParentNode .

    ex:parent a rdf:Property ;
        rdfs:domain ex:ChildNode ;
        rdfs:range ex:Node .

    ex:children a rdf:Property ;
        rdfs:domain ex:Node ;
        rdfs:range ex:ChildNode .
    """
    
    g = Graph()
    g.parse(data=ontology, format="turtle")
    create_package(g, output_dir=str(tmp_path))
    
    # Test imports using subprocess
    test_script = f"""
import sys
sys.path.insert(0, '{tmp_path}')

# Import all classes
from ex.Node import Node
from ex.ParentNode import ParentNode
from ex.ChildNode import ChildNode

# Test instantiation
node = Node(children=[])
parent = ParentNode(children=[])
child = ChildNode(parent=[], children=[])

print("SUCCESS: All imports and instantiations worked")
"""
    
    result = subprocess.run(
        ["uv", "run", "--with", "pydantic", "python", "-c", test_script],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent.parent)
    )
    
    if result.returncode != 0:
        error_msg = result.stderr if result.stderr else result.stdout
        pytest.fail(f"Circular import error detected:\n{error_msg}")

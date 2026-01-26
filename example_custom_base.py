"""Example demonstrating the refactored API with custom base models."""

from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdfs_pydantic import create_module
from pydantic import BaseModel, ConfigDict


# Define a custom base model
class MyCustomBaseModel(BaseModel):
    """Custom base model with specific configuration."""
    model_config = ConfigDict(
        ser_json_schema=False,
        exclude_none=True,
    )


# Create a simple ontology
g = Graph()
ex = Namespace("http://example.org/")
g.bind("ex", ex)

g.add((ex.Person, RDF.type, RDFS.Class))
g.add((ex.Person, RDFS.label, Literal("Person")))
g.add((ex.name, RDF.type, RDF.Property))
g.add((ex.name, RDFS.domain, ex.Person))
g.add((ex.name, RDFS.range, RDFS.Literal))

# Generate code with default BaseModel
print("=== With default BaseModel ===")
code_default = create_module(g)
print(code_default)

print("\n=== With custom MyCustomBaseModel ===")
# Generate code with custom base model
code_custom = create_module(g, base_cls=MyCustomBaseModel)
print(code_custom)

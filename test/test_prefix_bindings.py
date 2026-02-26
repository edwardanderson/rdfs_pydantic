import pytest
from rdflib import Graph

from rdfs_pydantic import create_module


def test_unbound_prefixes_raise_actionable_error_message():
    ontology = """
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    <http://example.org/E1> a rdfs:Class .
    """

    g = Graph()
    g.parse(data=ontology, format="turtle")

    with pytest.raises(ValueError) as exc_info:
        create_module(g)

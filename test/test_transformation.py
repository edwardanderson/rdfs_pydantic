import pytest
import testmark
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_model
import re

def get_suffixes(fixtures):
    """Return sorted list of suffixes for input/output pairs in the fixture."""
    input_keys = set()
    output_keys = set()
    for key in fixtures.keys():
        m = re.match(r"input-(\w+)", key)
        if m:
            input_keys.add(m.group(1))
        m = re.match(r"output-(\w+)", key)
        if m:
            output_keys.add(m.group(1))
    return sorted(input_keys & output_keys)

@pytest.fixture(
    params=list(Path("test/fixture").glob("*.md")),
    ids=[f.name for f in Path("test/fixture").glob("*.md")]
)
def fixture_file(request):
    """Parameterised fixture that yields each .md file in the fixture directory."""
    return request.param

def test_rdfs_to_pydantic(fixture_file):
    """Test that RDFS code is transformed into expected Pydantic model for all input/output pairs."""
    fixtures = testmark.parse(str(fixture_file))
    suffixes = get_suffixes(fixtures)
    if not suffixes:
        pytest.skip(f"No input/output pairs found in {fixture_file.name}")
    for suffix in suffixes:
        arrange = fixtures.get(f"input-{suffix}", "")
        expected = fixtures.get(f"output-{suffix}", "")
        if not arrange or not expected:
            continue
        # Add rdf prefix if missing
        if "@prefix rdf:" not in arrange:
            arrange = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" + arrange
        g = Graph()
        g.parse(data=arrange, format="turtle")
        result = create_model([g])
        assert result.strip() == expected.strip(), (
            f"[{fixture_file.name} | suffix={suffix}]\nExpected model:\n{expected}\n\nGot:\n{result}"
        )

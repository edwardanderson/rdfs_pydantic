import pytest
import testmark
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_model


@pytest.fixture(
    params=list(Path("test/fixture").glob("*.md")),
    ids=[f.name for f in Path("test/fixture").glob("*.md")]
)
def fixture_file(request):
    """Parameterised fixture that yields each .md file in the fixture directory."""
    return request.param


def test_rdfs_to_pydantic(fixture_file):
    """Test that RDFS code is transformed into expected Pydantic model."""
    # Extract fixtures from markdown file
    fixtures = testmark.parse(str(fixture_file))

    # Get arrange and assert sections
    arrange = fixtures.get("input", "")
    expected = fixtures.get("output", "")

    if not arrange or not expected:
        pytest.skip(f"Missing arrange or assert section in {fixture_file.name}")

    # Act: Parse Turtle and create the model from RDFS graphs
    # Add rdf prefix if missing
    if "@prefix rdf:" not in arrange:
        arrange = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" + arrange
    
    g = Graph()
    g.parse(data=arrange, format="turtle")
    result = create_model([g])

    # Assert: Verify the result matches expected output
    assert result.strip() == expected.strip(), (
        f"Expected model:\n{expected}\n\nGot:\n{result}"
    )

import pytest
import testmark
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_model
import re


def collect_test_cases():
    """Yield (fixture_file, suffix) for each input/output pair in all fixture files."""
    cases = []
    for fixture_path in Path("test/fixture").glob("*.md"):
        fixtures = testmark.parse(str(fixture_path))
        input_keys = set()
        output_keys = set()
        for key in fixtures.keys():
            m = re.match(r"input-(\w+)", key)
            if m:
                input_keys.add(m.group(1))
            m = re.match(r"output-(\w+)", key)
            if m:
                output_keys.add(m.group(1))
        for suffix in sorted(input_keys & output_keys):
            cases.append((str(fixture_path), suffix))
    return cases


@pytest.mark.parametrize(
    "fixture_path,suffix",
    collect_test_cases(),
    ids=lambda val: val[0].split("/")[-1] + ":" + val[1] if isinstance(val, tuple) else str(val)
)
def test_rdfs_to_pydantic(fixture_path, suffix):
    """Test that RDFS code is transformed into expected Pydantic model for each input/output pair."""
    fixtures = testmark.parse(fixture_path)
    arrange = fixtures.get(f"input-{suffix}", "")
    expected = fixtures.get(f"output-{suffix}", "")
    if not arrange or not expected:
        pytest.skip(f"Missing arrange or assert section in {fixture_path} (suffix={suffix})")
    # Add rdf prefix if missing
    if "@prefix rdf:" not in arrange:
        arrange = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" + arrange
    g = Graph()
    g.parse(data=arrange, format="turtle")
    result = create_model([g])
    assert result.strip() == expected.strip(), (
        f"[{fixture_path} | suffix={suffix}]\nExpected model:\n{expected}\n\nGot:\n{result}"
    )

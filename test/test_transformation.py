import json
import re
from pathlib import Path

import pytest
import testmark
from rdflib import Graph
from rdfs_pydantic import create_module


def collect_test_cases():
    """Yield (fixture_file, suffix) for each arrange/expected pair in all fixture files."""
    cases = []
    arrange_pattern = re.compile(r"arrange-(?P<type>[\w-]+)-(?P<suffix>\w+)$")
    expected_pattern = re.compile(r"expected-(?P<suffix>\w+)$")

    for fixture_path in Path("test/fixture/transformation/").glob("*.md"):
        fixtures = testmark.parse(str(fixture_path))
        arrange_suffixes = set()
        expected_suffixes = set()

        for key in fixtures.keys():
            arrange_match = arrange_pattern.match(key)
            if arrange_match:
                arrange_suffixes.add(arrange_match.group("suffix"))

            expected_match = expected_pattern.match(key)
            if expected_match:
                expected_suffixes.add(expected_match.group("suffix"))

        for suffix in sorted(arrange_suffixes & expected_suffixes):
            cases.append((str(fixture_path), suffix))

    return cases


@pytest.mark.parametrize(
    "fixture_path,suffix",
    collect_test_cases(),
    ids=lambda val: val[0].split("/")[-1] + ":" + val[1] if isinstance(val, tuple) else str(val)
)
def test_rdfs_to_pydantic(fixture_path, suffix):
    """Test that RDFS code is transformed into expected Pydantic model for each arrange/expected pair."""
    fixtures = testmark.parse(fixture_path)
    arrange_pattern = re.compile(rf"arrange-(?P<type>[\w-]+)-{re.escape(str(suffix))}$")

    arrange_sections = {
        m.group("type"): fixtures[key]
        for key in fixtures.keys()
        if (m := arrange_pattern.match(key))
    }

    ontology = arrange_sections.get("ontology", "")
    context_json = arrange_sections.get("context", "")
    expected = fixtures.get(f"expected-{suffix}", "")

    if not ontology or not expected:
        pytest.skip(f"Missing arrange or expected section in {fixture_path} (suffix={suffix})")

    # Add rdf prefix if missing
    if "@prefix rdf:" not in ontology:
        ontology = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" + ontology

    context = None
    if context_json:
        context = json.loads(context_json)

    g = Graph()
    g.parse(data=ontology, format="turtle")

    result = create_module(g, context=context)

    assert result.strip() == expected.strip(), (
        f"[{fixture_path} | suffix={suffix}]\nExpected model:\n{expected}\n\nGot:\n{result}"
    )

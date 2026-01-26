import pytest
import testmark
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_package


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Parse the testmark fixture once
_fixture_path = Path("test/fixture/package_output/example_package.md")
_cases = testmark.parse(str(_fixture_path))

@pytest.mark.parametrize("case_name, case_content", _cases.items())
def test_create_package_from_rdfs(case_name, case_content, tmp_path):
    """Test that RDFS code is transformed into a package folder structure with correct files."""
    # Only run for the main input/output case (arrange-ontology-0, output-0, output-*)
    if not str(case_name).startswith("input-0"):
        return
    arrange = case_content
    # Find all outputs for this input
    outputs = {k: v for k, v in _cases.items() if str(k).startswith("output-")}
    expected_tree = outputs.get("output-0", "")
    expected_files = {
        str(k).replace("output-", ""): v for k, v in outputs.items() if k != "output-0"
    }
    if not arrange or not expected_tree:
        pytest.skip(f"Missing arrange or output-0 section in {case_name}")

    g = Graph()
    g.parse(data=arrange, format="turtle")
    # This function should create the package structure in tmp_path
    create_package([g], output_dir=str(tmp_path))

    # Check folder structure (tree)
    def walk_tree(root):
        lines = []
        for path in sorted(Path(root).rglob("*")):
            rel = path.relative_to(root)
            if path.is_dir():
                lines.append(str(rel) + "/")
            else:
                lines.append(str(rel))
        return lines
    actual_tree = "\n".join(walk_tree(tmp_path))
    # The expected tree is a code block with 'tree' as language
    expected_tree_lines = [l.strip() for l in expected_tree.split("\n") if l.strip() and not l.startswith('```')]
    assert all(any(e in a for a in actual_tree.splitlines()) for e in expected_tree_lines), f"Expected tree structure not found.\nExpected:\n{expected_tree}\nActual:\n{actual_tree}"

    # Check file contents
    for fname, expected_content in expected_files.items():
        # The expected content is a code block with python as language
        expected_lines = [l.rstrip() for l in expected_content.split("\n") if l.strip() and not l.startswith('```')]
        # Ensure .py extension for model files
        if not fname.endswith(".py") and fname != "__init__.py":
            fname = fname + ".py"
        # Find the file in the output dir
        fpath = tmp_path / "ex" / fname
        assert fpath.exists(), f"File {fpath} does not exist"
        actual = read_file(fpath)
        for eline in expected_lines:
            assert eline in actual, f"Expected line not found in {fpath}: {eline}"

import pytest
import testmark
from pathlib import Path
import tempfile
import shutil
from rdflib import Graph
from rdfs_pydantic import create_package

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

@pytest.mark.parametrize(
    "fixture_path",
    [Path("test/fixture/package_output/example_package.md")],
    ids=["example_module"]
)
def test_create_module_from_rdfs(fixture_path, tmp_path):
    """Test that RDFS code is transformed into a module folder structure with correct files."""
    fixtures = testmark.parse(str(fixture_path))
    arrange = fixtures.get("input-0", "")
    expected_tree = fixtures.get("output-0", "")
    expected_files = {
        k.replace("output-", ""): v for k, v in fixtures.items() if k.startswith("output-") and k not in ("output-0",)
    }
    if not arrange or not expected_tree:
        pytest.skip(f"Missing arrange or output-0 section in {fixture_path}")

    g = Graph()
    g.parse(data=arrange, format="turtle")
    # This function should create the module structure in tmp_path
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
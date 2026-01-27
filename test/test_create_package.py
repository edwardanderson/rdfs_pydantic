import json
import pytest
import testmark
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS
from rdfs_pydantic import create_package
from pydantic import BaseModel
import re


# Custom base model for testing
class CustomBaseModel(BaseModel):
    """Custom base model for testing."""
    pass


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def collect_package_test_cases():
    """Collect all package test cases from fixture files."""
    cases = []
    for fixture_path in Path("test/fixture/package_output/").glob("*.md"):
        fixtures = testmark.parse(str(fixture_path))
        
        # Find all arrange-ontology blocks
        arrange_pattern = re.compile(r"arrange-ontology-(\d+)")
        suffixes = set()
        for key in fixtures.keys():
            m = arrange_pattern.match(key)
            if m:
                suffixes.add(m.group(1))
        
        for suffix in sorted(suffixes):
            cases.append((str(fixture_path), suffix))
    
    return cases


@pytest.mark.parametrize(
    "fixture_path,suffix",
    collect_package_test_cases(),
    ids=lambda val: val[0].split("/")[-1].replace(".md", "") + ":" + val[1] if isinstance(val, tuple) else str(val)
)
def test_create_package_from_rdfs(fixture_path, suffix, tmp_path):
    """Test that RDFS code is transformed into a package folder structure with correct files."""
    fixtures = testmark.parse(fixture_path)
    
    arrange = fixtures.get(f"arrange-ontology-{suffix}", "")
    expected_tree = fixtures.get(f"expected-{suffix}", "")
    
    if not arrange or not expected_tree:
        pytest.skip(f"Missing arrange or expected section in {fixture_path} (suffix={suffix})")
    
    # Parse and create package
    g = Graph()
    
    # Add standard prefixes if missing
    if "@prefix rdf:" not in arrange:
        arrange = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" + arrange
    if "@prefix ex" not in arrange:
        arrange = "@prefix ex: <http://example.org/> .\n" + arrange
    
    g.parse(data=arrange, format="turtle")
    create_package(g, output_dir=str(tmp_path))

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
    expected_tree_lines = [l.strip() for l in expected_tree.split("\n") if l.strip()]
    
    for expected_line in expected_tree_lines:
        assert any(expected_line in actual_line for actual_line in actual_tree.splitlines()), \
            f"Expected tree item not found: {expected_line}\nActual tree:\n{actual_tree}"
    
    # Check individual file contents
    # Pattern: expected-{prefix}-{filename} or expected-{filename}
    file_pattern = re.compile(rf"expected-(?!{suffix}$)(.+)")
    for key in fixtures.keys():
        if key == f"expected-{suffix}":
            continue  # Skip the tree structure
        m = file_pattern.match(key)
        if m:
            # This is a file content expectation
            file_spec = m.group(1)
            expected_content = fixtures[key]
            
            # Parse file_spec: could be "ex1-Person", "ex1-__init__", "Agent", "__init__", etc.
            if "-" in file_spec:
                # Multi-part: prefix-filename
                parts = file_spec.split("-", 1)
                prefix = parts[0]
                fname = parts[1]
            else:
                # Single part: filename only, infer prefix from tree
                # Look for which prefixes exist in the tree
                prefix_dirs = [p.rstrip("/") for p in expected_tree_lines if "/" in p and not p.count("/") > 1]
                if prefix_dirs:
                    prefix = prefix_dirs[0].rstrip("/")
                else:
                    prefix = "ex"  # Default fallback
                fname = file_spec
            
            if not fname.endswith(".py"):
                fname = fname + ".py"
            
            fpath = tmp_path / prefix / fname
            if not fpath.exists():
                continue  # Skip if file doesn't exist for this test case
            
            actual = read_file(fpath)
            expected_lines = [l.rstrip() for l in expected_content.split("\n") if l.strip()]
            
            for eline in expected_lines:
                assert eline in actual, f"Expected line not found in {fpath}:\n{eline}\n\nActual content:\n{actual}"


def test_optimized_base_multiple_inheritance(tmp_path, monkeypatch):
    """Ensure custom base class works with multiple inheritance."""
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    for cls in ("Base", "A", "B", "C"):
        g.add((ex[cls], RDF.type, RDFS.Class))

    g.add((ex.A, RDFS.subClassOf, ex.Base))
    g.add((ex.B, RDFS.subClassOf, ex.Base))
    g.add((ex.C, RDFS.subClassOf, ex.A))
    g.add((ex.C, RDFS.subClassOf, ex.B))

    pkg_dir = tmp_path / "pkg"
    pkg_dir.mkdir()

    create_package(g, output_dir=str(pkg_dir), base_cls=CustomBaseModel)

    monkeypatch.syspath_prepend(str(tmp_path))

    pkg = __import__("pkg")
    from pkg.ex import A, B, C, Base

    assert issubclass(C, CustomBaseModel)
    assert issubclass(C, BaseModel)
    assert issubclass(C, A)
    assert issubclass(C, B)
    assert C().model_dump() == {}


def test_dedupes_redundant_parent_classes(tmp_path):
    """Redundant parents (ancestor + descendant) should be collapsed to avoid MRO errors."""
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    for cls in ("Base", "Mid", "Sub", "Target"):
        g.add((ex[cls], RDF.type, RDFS.Class))

    g.add((ex.Mid, RDFS.subClassOf, ex.Base))
    g.add((ex.Sub, RDFS.subClassOf, ex.Mid))
    g.add((ex.Target, RDFS.subClassOf, ex.Mid))
    g.add((ex.Target, RDFS.subClassOf, ex.Sub))

    out_dir = tmp_path / "pkg"
    create_package(g, output_dir=str(out_dir))

    target_file = out_dir / "ex" / "Target.py"
    content = target_file.read_text(encoding="utf-8")

    assert "class Target(Sub):" in content
    assert "class Target(Mid, Sub)" not in content
    assert "class Target(Sub, Mid)" not in content
    assert "from .Sub import Sub" in content
    assert "from .Mid import Mid" not in content


def test_creates_missing_output_dir(tmp_path):
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)

    g.add((ex.Foo, RDF.type, RDFS.Class))

    out_dir = tmp_path / "nested" / "pkg"
    assert not out_dir.exists()

    create_package(g, output_dir=str(out_dir))

    assert out_dir.exists()
    assert (out_dir / "__init__.py").exists()


def test_context_path_alias(tmp_path):
    g = Graph()
    ex = Namespace("http://example.org/")
    g.bind("ex", ex)
    g.add((ex.Person, RDF.type, RDFS.Class))

    ctx = {"@context": {"Person": {"@id": str(ex.Person)}}}
    ctx_path = tmp_path / "ctx.json"
    ctx_path.write_text(json.dumps(ctx), encoding="utf-8")

    out_dir = tmp_path / "pkg"
    create_package(g, output_dir=str(out_dir), context=str(ctx_path))

    person_file = out_dir / "ex" / "Person.py"
    assert person_file.exists()
    assert "class Person(" in person_file.read_text(encoding="utf-8")

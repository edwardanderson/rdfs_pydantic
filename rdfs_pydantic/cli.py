import typer
import json
import requests
from pathlib import Path
from rdflib import Graph
from rdfs_pydantic import create_module, create_package
from rdfs_pydantic.extraction import get_unbound_rdfs_classes

app = typer.Typer()


def infer_rdf_format(file_path: str) -> str:
    """Infer RDF format from file extension.
    
    Args:
        file_path: Path to RDF file
        
    Returns:
        RDF format string (turtle, xml, json-ld, n3, etc.)
        
    Raises:
        typer.BadParameter: If format cannot be determined
    """
    path = Path(file_path)
    suffix = path.suffix.lower()
    
    format_map = {
        '.ttl': 'turtle',
        '.rdf': 'xml',
        '.xml': 'xml',
        '.jsonld': 'json-ld',
        '.json-ld': 'json-ld',
        '.n3': 'n3',
        '.nt': 'nt',
        '.nq': 'nquads',
    }
    
    if suffix in format_map:
        return format_map[suffix]
    else:
        raise typer.BadParameter(
            f"Cannot determine RDF format from file extension '{suffix}'. "
            f"Supported formats: {', '.join(format_map.keys())}"
        )


def load_context(context_path: str) -> dict:
    """Load JSON-LD context from local file or remote URL.
    
    Args:
        context_path: Path to local file or URL
        
    Returns:
        Parsed JSON-LD context object
    """
    if Path(context_path).exists():
        # Local file
        with open(context_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Try to fetch from URL
        try:
            response = requests.get(context_path)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise typer.BadParameter(f"Failed to load context from '{context_path}': {e}")


def parse_and_apply_bindings(graph: Graph, bindings: list[tuple[str, str]] | None) -> None:
    """Parse prefix bindings and apply them to the graph.
    
    Args:
        graph: RDF graph to bind prefixes to
        bindings: List of tuples (prefix, namespace)
                 (e.g., [('ex', 'http://example.org/'), ('foaf', 'http://xmlns.com/foaf/0.1/')])
    """
    if not bindings:
        return
    
    for prefix, namespace in bindings:
        if not prefix or not namespace:
            raise typer.BadParameter("Prefix and namespace cannot be empty")
        graph.bind(prefix, namespace)

@app.command()
def module(
        ontology: list[str] = typer.Option(
            ...,
            "--ontology",
            help="Path(s) to RDFS ontology file(s) (can be specified multiple times; format is inferred from file extension)"
        ),
        context: str = typer.Option(
            None,
            "--context",
            help="Path to a JSON-LD @context file (optional)"
        ),
        bind: list[str] = typer.Option(
            None,
            "--bind",
            help="Bind prefixes to namespaces (format: 'prefix http://namespace', can be specified multiple times)"
        ),
        language: str = typer.Option(
            'en',
            "--language",
            help="Preferred language for labels and comments (default: 'en')"
        )
    ):
    """Generate Pydantic models from RDFS ontology/ontologies and print to stdout."""
    g = Graph()
    for ontology_path in ontology:
        try:
            fmt = infer_rdf_format(ontology_path)
            g.parse(ontology_path, format=fmt)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    # Parse bindings from "prefix namespace" format
    bindings = None
    if bind:
        bindings = []
        for binding_str in bind:
            parts = binding_str.split(None, 1)
            if len(parts) != 2:
                typer.echo(
                    f"Invalid binding format '{binding_str}'. Expected 'prefix http://namespace'",
                    err=True
                )
                raise typer.Exit(1)
            bindings.append((parts[0], parts[1]))
    
    try:
        parse_and_apply_bindings(g, bindings)
    except typer.BadParameter as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)
    
    # Check for unbound RDFS classes
    unbound = get_unbound_rdfs_classes(g)
    if unbound:
        typer.echo("Warning: The following RDFS classes have no bound prefixes:", err=True)
        for iri, _ in unbound:
            typer.echo(f"  - {iri}", err=True)
    
    ctx = None
    if context:
        try:
            ctx = load_context(context)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    code = create_module(g, context=ctx, language=language)
    print(code)

@app.command()
def package(
    ontology: list[str] = typer.Option(
        ...,
        "--ontology",
        help="Path(s) to RDFS ontology file(s) (can be specified multiple times; format is inferred from file extension)"
    ),
    output_dir: str = typer.Option(
        ...,
        "--output-dir",
        help="Directory to write the generated package"
    ),
    context: str = typer.Option(
        None,
        "--context",
        help="Path to a JSON-LD @context file (optional)"
    ),
    bind: list[str] = typer.Option(
        None,
        "--bind",
        help="Bind prefixes to namespaces (format: 'prefix http://namespace', can be specified multiple times)"
    ),
    language: str = typer.Option(
        'en',
        "--language",
        help="Preferred language for labels and comments (default: 'en')"
    )
):
    """Generate a Python package of Pydantic models from RDFS ontology/ontologies."""
    g = Graph()
    for ontology_path in ontology:
        try:
            fmt = infer_rdf_format(ontology_path)
            g.parse(ontology_path, format=fmt)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    # Parse bindings from "prefix namespace" format
    bindings = None
    if bind:
        bindings = []
        for binding_str in bind:
            parts = binding_str.split(None, 1)
            if len(parts) != 2:
                typer.echo(
                    f"Invalid binding format '{binding_str}'. Expected 'prefix http://namespace'",
                    err=True
                )
                raise typer.Exit(1)
            bindings.append((parts[0], parts[1]))
    
    try:
        parse_and_apply_bindings(g, bindings)
    except typer.BadParameter as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)
    
    # Check for unbound RDFS classes
    unbound = get_unbound_rdfs_classes(g)
    if unbound:
        typer.echo("Warning: The following RDFS classes have no bound prefixes:", err=True)
        for iri, _ in unbound:
            typer.echo(f"  - {iri}", err=True)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    ctx = None
    if context:
        try:
            ctx = load_context(context)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    create_package(g, output_dir=output_dir, context=ctx, language=language)
    typer.echo(f"Package written to {output_dir}")

if __name__ == "__main__":
    app()

import typer
import json
import requests
from rdflib import Graph
from rdfs_pydantic import create_module, create_package
from pathlib import Path

app = typer.Typer()


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


def parse_and_apply_bindings(graph: Graph, bindings: list[str] | None) -> None:
    """Parse prefix bindings and apply them to the graph.
    
    Args:
        graph: RDF graph to bind prefixes to
        bindings: List of bindings in format 'prefix:namespace' 
                 (e.g., ['ex:http://example.org/', 'foaf:http://xmlns.com/foaf/0.1/'])
                 
    Raises:
        typer.BadParameter: If binding format is invalid
    """
    if not bindings:
        return
    
    for binding in bindings:
        if ':' not in binding:
            raise typer.BadParameter(
                f"Invalid binding format '{binding}'. Expected 'prefix:namespace' "
                f"(e.g., 'ex:http://example.org/')"
            )
        
        try:
            prefix, namespace = binding.split(':', 1)
            if not prefix or not namespace:
                raise ValueError("Prefix and namespace cannot be empty")
            graph.bind(prefix, namespace)
        except ValueError as e:
            raise typer.BadParameter(f"Failed to parse binding '{binding}': {e}")

@app.command()
def module(
        ontology: list[str] = typer.Option(
            ...,
            "--ontology",
            help="Path(s) to RDFS ontology file(s) (Turtle format, can be specified multiple times)"
        ),
        context: str = typer.Option(
            None,
            "--context",
            help="Path to a JSON-LD @context file (optional)"
        ),
        format: str = typer.Option(
            "turtle",
            "--format",
            help="RDF format of ontology file(s) (turtle, xml, json-ld, etc.)"
        ),
        bind: list[str] = typer.Option(
            None,
            "--bind",
            help="Bind prefixes to namespaces (format: 'prefix:namespace', can be specified multiple times)"
        )
    ):
    """Generate Pydantic models from RDFS ontology/ontologies and print to stdout."""
    g = Graph()
    for ontology_path in ontology:
        g.parse(ontology_path, format=format)
    
    try:
        parse_and_apply_bindings(g, bind)
    except typer.BadParameter as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)
    
    ctx = None
    if context:
        try:
            ctx = load_context(context)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    code = create_module(g, context=ctx)
    print(code)

@app.command()
def package(
    ontology: list[str] = typer.Option(
        ...,
        "--ontology",
        help="Path(s) to RDFS ontology file(s) (Turtle format, can be specified multiple times)"
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
    format: str = typer.Option(
        "turtle",
        "--format",
        help="RDF format of ontology file(s) (turtle, xml, json-ld, etc.)"
    ),
    bind: list[str] = typer.Option(
        None,
        "--bind",
        help="Bind prefixes to namespaces (format: 'prefix:namespace', can be specified multiple times)"
    )
):
    """Generate a Python package of Pydantic models from RDFS ontology/ontologies."""
    g = Graph()
    for ontology_path in ontology:
        g.parse(ontology_path, format=format)
    
    try:
        parse_and_apply_bindings(g, bind)
    except typer.BadParameter as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    ctx = None
    if context:
        try:
            ctx = load_context(context)
        except typer.BadParameter as e:
            typer.echo(str(e), err=True)
            raise typer.Exit(1)
    
    create_package(g, output_dir=output_dir, context=ctx)
    typer.echo(f"Package written to {output_dir}")

if __name__ == "__main__":
    app()

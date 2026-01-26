import typer
from rdflib import Graph
from rdfs_pydantic import create_module, create_package
from pathlib import Path

app = typer.Typer()

@app.command()
def module(
        ontology: str = typer.Option(
            ...,
            "--ontology",
            help="Path to the RDFS ontology file (Turtle format)"
        )
    ):
    """Generate Pydantic models from an RDFS ontology and print to stdout."""
    g = Graph()
    g.parse(ontology, format="turtle")
    code = create_module([g])
    print(code)

@app.command()
def package(
    ontology: str = typer.Option(
        ...,
        "--ontology",
        help="Path to the RDFS ontology file (Turtle format)"
    ),
    output_dir: str = typer.Option(
        ...,
        "--output-dir",
        help="Directory to write the generated package"
    )
):
    """Generate a Python package of Pydantic models from an RDFS ontology."""
    g = Graph()
    g.parse(ontology, format="turtle")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    create_package([g], output_dir=output_dir)
    typer.echo(f"Package written to {output_dir}")

if __name__ == "__main__":
    app()

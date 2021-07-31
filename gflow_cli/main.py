import typer

from gflow_cli import __version__, long_license

app = typer.Typer(name="gflow_cli")


@app.command()
def version():
    typer.echo(f"Hi there 👋! You're using GradsFlow CLI version={__version__} ✨")


@app.command()
def license():
    typer.echo(long_license)

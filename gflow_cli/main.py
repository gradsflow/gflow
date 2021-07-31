import typer

from gflow_cli import __version__

app = typer.Typer(name='gflow_cli')


@app.command()
def version():
    typer.echo(f"Hi there 👋! You're using GradsFlow CLI version={__version__} ✨")

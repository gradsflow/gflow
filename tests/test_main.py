import typer
from typer.testing import CliRunner

from gflow_cli import __version__, long_license
from gflow_cli.main import license, version

runner = CliRunner()


def test_version():
    app = typer.Typer()
    app.command()(version)
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_version():
    app = typer.Typer()
    app.command()(license)
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert long_license in result.stdout

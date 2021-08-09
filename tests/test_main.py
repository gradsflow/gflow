#  Copyright (c) 2021 GradsFlow Team.
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import typer
from typer.testing import CliRunner

from gflow_cli import __version__, long_license
from gflow_cli.info import license_info, version

runner = CliRunner()


def test_version():
    app = typer.Typer()
    app.command()(version)
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_version():
    app = typer.Typer()
    app.command()(license_info)
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert long_license in result.stdout

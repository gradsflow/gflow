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

from unittest.mock import MagicMock, patch

import typer
from typer.testing import CliRunner

from gflow_cli.projects import add_project
from gflow_cli.utility import init_config

runner = CliRunner()

init_config("fake", "fake")


@patch("gflow_cli.projects.requests")
@patch("gflow_cli.projects.read_config")
def test_add_project(mock_conf: MagicMock, mock_req: MagicMock):
    mock_conf.return_value = True
    mock_post = mock_req.post = MagicMock()
    mock_post.json = ""
    mock_post.text = ""
    mock_post.return_value = True

    app = typer.Typer()
    app.command()(add_project)
    result = runner.invoke(app, args=["--timeout", 5], input="title\ndesc\n")

    mock_conf.assert_called_with()
    assert "Enter" in result.stdout

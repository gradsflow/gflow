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


@patch("gflow_cli.projects.requests.post")
@patch("gflow_cli.projects.read_config")
def test_add_project(mock_read_config: MagicMock, mock_post: MagicMock):
    mock_response = mock_post.return_value = MagicMock()
    mock_response.return_value = False
    mock_response.text = ""

    app = typer.Typer()
    app.command()(add_project)
    result = runner.invoke(app, input="title\ndesc\n")

    mock_read_config.assert_called_with()
    assert result.exit_code == 0

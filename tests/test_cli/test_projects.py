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

from gflow.cli.main import projects
from gflow.client import Client
from gflow.utility import cli_test_runner, init_config

init_config("fake", "fake")


@patch("gflow.cli.projects.Client")
@patch("gflow.cli.projects.read_config")
def test_add_project(mock_read_config: MagicMock, mock_client):
    runner = cli_test_runner(projects.add_project)
    task = Client.get_task_types()[0]
    result = runner(args=["--timeout", "5"], input=f"title\ndesc\n{task}")

    mock_read_config.assert_called_with()
    assert result.exit_code == 0

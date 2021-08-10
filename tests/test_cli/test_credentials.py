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

from gflow.cli.credentials import login
from gflow.utility import cli_test_runner


@patch("gflow.cli.credentials.keyring.set_password")
@patch("gflow.cli.credentials.Client.login")
def test_login(mock_login, mock_save_pwd):
    mock_client, mock_response = mock_login.return_value = MagicMock(), MagicMock()
    mock_client.token = "dummy"
    mock_response.return_value.text = ""

    result = cli_test_runner(login)(input="hello@abc.com\n12345\n")

    assert "Authentication successful" in result.stdout

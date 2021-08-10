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

from gflow.client.main import Client


@patch("gflow.client.main.requests.post")
def test_create_project(mock_post: MagicMock):
    client = Client(token="fake")

    mock_response = mock_post.return_value = MagicMock()
    mock_response.return_value = False
    mock_response.text = ""

    task_types = Client.get_task_types()
    visibility = Client.get_visibility()[0]

    response = client.create_project(
        name="hello",
        description="",
        task_type=task_types[0],
        visibility=visibility,
        team_id=1,
        timeout=10,
    )
    assert response

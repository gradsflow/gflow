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
import requests
from gflow_cli.constants import USER_URL
from typer import Option

from gflow.constants import PROJECTS_URL
from gflow.schema import ProjectModel

TASK_TYPE = dict(image_classification=1, text_clf=2)


class Client:
    def __init__(self, config: Option[dict] = None, token: Option[str] = None):
        if config is None and token is None:
            raise UserWarning("Both config and token can't be None")

        if config:
            token = config.get("token")
        else:
            config = {}
        self.token = token
        self.config = config

    def login(self, email: str, password: str):
        response = requests.post(USER_URL, data={"email": email, "password": password})
        return response

    def create_project(
        self,
        name: str,
        description: str,
        task_type: str,
        visibility_type: str,
        team_id: int,
        timeout: int = 60,
    ):
        task_id = TASK_TYPE.get(task_type)
        visibility_id = TASK_TYPE.get(visibility_type)

        data = ProjectModel(
            tittle=name,
            description=description,
            task_id=task_id,
            visibility_id=visibility_id,
            team_id=team_id,
        )
        headers = {"x-auth-token": self.token}

        response = requests.post(
            PROJECTS_URL + "/create",
            data=data.dict(by_alias=True),
            headers=headers,
            timeout=timeout,
        )
        return response

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
from typer import Option


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

    def create_project(
        self,
        name: str,
        task_type: str,
    ):
        pass

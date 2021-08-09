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
from pydantic import BaseModel


def to_camel(string: str) -> str:
    split_string = string.split("_")
    return split_string[0] + "".join(word.capitalize() for word in split_string[1:])


class BaseBackendModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class ProjectModel(BaseBackendModel):
    title: str
    description: str
    task_id: int
    type_id: int
    visibility_id: int
    team_id: int

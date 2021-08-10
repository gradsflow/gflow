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
import typer
from loguru import logger

from gflow_cli.constants import PROJECTS_URL
from gflow_cli.utility import read_config

app = typer.Typer(help="Manage your Projects with gflow-cli project command.")

from gflow_cli.schema import ProjectModel


@app.command(name="create")
def add_project(
    title: str = typer.Option(..., prompt=True),
    description: str = typer.Option(..., prompt=True),
    timeout: int = 60,
) -> None:
    config: dict = read_config()
    if not config:
        typer.echo("Login first")
        return
    task_id = 1
    type_id = 1
    visibility = 1
    team_id = 4

    data = ProjectModel(
        tittle=title,
        description=description,
        task_id=task_id,
        type_id=type_id,
        visibility_id=visibility,
        team_id=team_id,
    )
    typer.echo("project url is " + PROJECTS_URL)
    headers = {"x-auth-token": config["token"]}
    typer.echo(data.dict(by_alias=True))
    response = requests.post(
        PROJECTS_URL + "/create",
        data=data.dict(by_alias=True),
        headers=headers,
        timeout=timeout,
    )
    if response:
        typer.secho("✅ Project Created", color=typer.colors.GREEN)
        logger.debug(response.json())
    else:
        typer.secho("🛑 Error While creating Project\n", color=typer.colors.RED)
        typer.echo(response.text)

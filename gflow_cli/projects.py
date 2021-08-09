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

from dataclasses import asdict

import requests
import typer

from gflow_cli.constants import PROJECTS_URL
from gflow_cli.utility import read_config

app = typer.Typer(help="Manage your Projects with `gflow-cli project` command.")

from gflow_cli.schema import ProjectModel


@app.command(name="add")
def add_project() -> None:
    config = read_config()
    if not config:
        typer.echo("Login first")
        return
    title = typer.prompt("Enter Project Name", type=str)
    desc = typer.prompt("Enter Description")
    task_id = 1
    type_id = 1
    visibility = 1
    team_id = 4

    data = ProjectModel(
        title=title,
        description=desc,
        task_id=task_id,
        type_id=type_id,
        visibility_id=visibility,
        team_id=team_id,
    )
    typer.echo("project url is " + PROJECTS_URL)
    headers = {"x-auth-token": config["token"]}
    typer.echo(data.json())
    response = requests.post(PROJECTS_URL + "/create", data.json(), headers=headers)
    if response:
        typer.echo("✅ Project Created")
    else:
        typer.secho("🛑 Error While creating Project\n", fg=typer.colors.RED)
        typer.echo(response.text)

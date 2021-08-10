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
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import typer
from loguru import logger

from gflow.client import Client
from gflow.utility import read_config

app = typer.Typer(help="Manage your Projects with gflow-cli project command.")

PROJECT_TYPES = dict(image_classification=1, text_classification=2)


@app.command(name="create")
def add_project(
    title: str = typer.Option(..., prompt=True),
    description: str = typer.Option(..., prompt=True),
    project_type: str = typer.Option(
        ..., prompt=True, help=f"One of the value from {PROJECT_TYPES}"
    ),
    timeout: int = 60,
) -> None:
    config: dict = read_config()
    if not config:
        typer.echo("Login first")
        return

    client = Client(config)

    visibility = "public"
    team_id = 4

    response = client.create_project(
        name=title,
        description=description,
        task_type=project_type,
        visibility=visibility,
        team_id=team_id,
        timeout=timeout,
    )

    if response:
        typer.secho("✅ Project Created", color=typer.colors.GREEN)
        logger.debug(response.json())
    else:
        typer.secho("🛑 Error While creating Project\n", color=typer.colors.RED)
        typer.echo(response.text)

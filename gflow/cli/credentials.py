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

import keyring
import typer

from gflow.client import Client
from gflow.constants import KEYRING_NAME
from gflow.utility import init_config

app = typer.Typer()


@app.command()
def login(
    email: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True, hide_input=True),
):
    client, response = Client.login(email=email, password=password)
    if response:
        keyring.set_password(KEYRING_NAME, email, password)
        token = client.token
        init_config(email, token)
        typer.secho(f"Authentication successful {email} 🔐", fg=typer.colors.GREEN)
    else:
        typer.secho(response.text, fg=typer.colors.RED)

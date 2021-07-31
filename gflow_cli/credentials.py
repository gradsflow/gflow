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

from gflow_cli.constants import KEYRING_NAME

app = typer.Typer()


@app.command(help="enter username followed by password")
def login(username: str, password: str):
    # TODO add validation here
    keyring.set_password(KEYRING_NAME, username, password)
    typer.echo(f"Password saver for user {username} 🔐")

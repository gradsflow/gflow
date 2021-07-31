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

import typer

from gflow_cli import credentials, info, short_license
from gflow_cli.codeless_ai import datasets

app = typer.Typer(name="gflow_cli", help=short_license)
app.add_typer(credentials.app, name="user")
app.add_typer(info.app, name="info")
app.add_typer(datasets.app, name="dataset")

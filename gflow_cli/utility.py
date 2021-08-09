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
import json
import os
from typing import Optional

import typer

from gflow_cli.constants import CONFIG_DIR, CONFIG_PATH


def save_text(text: str, filepath: str, mode: str = "w"):
    with open(filepath, mode) as fw:
        fw.write(text)


def read_text_file(filepath: str, mode: str = "r"):
    with open(filepath, mode) as fr:
        data = fr.read()

    return data


def init_config(email: str, token: str):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    data = json.dumps(dict(email=email, token=token))
    save_text(data, CONFIG_PATH)
    typer.echo(f"login token saved at {CONFIG_PATH}")


def read_config() -> Optional[dict]:
    if not os.path.exists(CONFIG_PATH):
        return None
    data = json.loads(read_text_file(CONFIG_PATH))
    return data

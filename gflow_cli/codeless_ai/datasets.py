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

from dataclasses import asdict, dataclass
from typing import Tuple

import requests
import typer

from gflow_cli.constants import DATASETS_URL

app = typer.Typer(help="Manage your datasets with `gflow-cli datasets` command.")

AVAILABLE_STORAGE = ("LOCAL", "REMOTE")
AVAILABLE_TASKS = ("IMAGE-CLASSIFICATION",)
AVAILABLE_DATASET_TYPES = ("FROM-FOLDER", "FROM-CSV")


@dataclass
class DatasetRequest:
    path: str
    task: str
    dataset_type: str
    storage: str


@app.command(name="available-tasks")
def get_available_tasks() -> Tuple[str]:
    return AVAILABLE_TASKS


@app.command()
def add_dataset(path: str, task: str, dataset_type: str, storage: str) -> None:
    """
    Add Training Dataset
    Args:
        path: Path of dataset on your local filesystem
        task: Type of Task/Model you want to train with this dataset.
        See available tasks `gflow-cli datasets available-tasks`
        dataset_type: `from-folder` or `from-csv`
        storage: Either `local` or `remote`

    Returns:

    """
    data = DatasetRequest(
        path=path, task=task, dataset_type=dataset_type, storage=storage
    )
    response = requests.post(DATASETS_URL, asdict(data))
    if response:
        typer.echo("✅ Dataset Created")
    else:
        typer.echo("🛑 Error While creating Dataset\n")
        typer.echo(f"status code = {response.status_code}")

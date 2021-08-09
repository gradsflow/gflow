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

import os
from pathlib import Path

KEYRING_NAME = "GRADSFLOW_CLI"
DEFAULT_ADDR = os.environ.get("DEFAULT_ADDR")
BASE_URL = f"http://{DEFAULT_ADDR}/api"

DATASETS_URL = f"{BASE_URL}/dataset"
PROJECTS_URL = f"{BASE_URL}/project"
USER_URL = f"{BASE_URL}/auth"

CONFIG_DIR = Path.home() / ".gradsflow"
CONFIG_PATH = CONFIG_DIR / "config.json"

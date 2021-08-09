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

from gflow_cli.constants import CONFIG_PATH
from gflow_cli.utility import init_config, read_config, read_text_file, save_text


def test_save_text():
    save_text("hi", "./temp.txt")
    assert os.path.exists("temp.txt")
    assert read_text_file("temp.txt")


def test_init_config():
    init_config("hello@gflow.com", "1234")
    assert read_config()

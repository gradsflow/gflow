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

from gflow import __version__, long_license
from gflow.cli.info import license_info, version
from gflow.utility import cli_test_runner


def test_version():
    result = cli_test_runner(version)()
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_license_info():
    result = cli_test_runner(license_info)()
    assert result.exit_code == 0
    assert long_license in result.stdout

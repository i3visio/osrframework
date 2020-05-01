################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

__author__ = "Felix Brezo, Yaiza Rubio  <contacto@i3visio.com>"
__version__ = "3.0"


from osrframework.utils.platforms import Platform


class Taringa(Platform):
    """<Platform> class"""
    def __init__(self):
        """Constructor with parameters

        This method permits the developer to instantiate dinamically Platform
        objects."""
        self.platformName = "taringa"
        self.tags = ["social"]
        self.modes = {
            "usufy": {
                "debug": True,
                "extra_fields": {
                    "com.i3visio.Name": '<h2>([^<]+)</h2>',
                    "com.i3visio.Name": '"firstname":"([^"]+)"',
                    "com.i3visio.Surname": '"lastname":"([^"]+)"',
                    "com.i3visio.BirthDate": '"birthday":"([^"]+)"',
                    "com.i3visio.Gender": '"gender":"([^"]+)"',
                    "com.i3visio.Country": '"country":"([^"]+)"'
                },
                "needs_credentials": False,
                "not_found_text": '"firstname":"Taringa!"',
                "query_validator": "[a-z0-9A-Z_]+",
                "url": "https://www.taringa.net/{placeholder}",
            }
        }

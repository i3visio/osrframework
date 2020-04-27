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

__author__ = "Felix Brezo, Yaiza Rubio <contacto@i3visio.com>"
__version__ = "3.0"


from osrframework.utils.platforms import Platform


class Jamiiforums(Platform):
    """<Platform> class"""
    def __init__(self):
        """Constructor with parameters

        This method permits the developer to instantiate dinamically Platform
        objects."""
        self.platformName = "Jamiiforums"
        self.tags = ["opinions"]
        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.Name": '>([^<]+)</span></h1>',
                },
                "needs_credentials": False,
                "not_found_text": "The specified member cannot be found. Please enter a member's entire name.",
                "query_validator": "[a-z0-9A-Z_]+",
                "url": "https://www.jamiiforums.com/members/?username={placeholder}",
            }
        }

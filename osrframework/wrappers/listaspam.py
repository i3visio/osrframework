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


class Listaspam(Platform):
    """A <Platform> object for Listaspam"""
    def __init__(self):
        self.platformName = "Listaspam"
        self.tags = ["phone"]

        self.modes = {
            "phonefy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.Location": "<div>📍([^<]+)</div>",
                    "com.i3visio.Labels": 'Nube de tags: (.+)</div>'
                },
                "needs_credentials": False,
                "not_found_text": "No te quedes sin saber quién te llama por teléfono.",                   # Text that indicates a missing profile
                "query_validator": "[0-9+\-\.]{6-16}",                            # Regular expression that the alias SHOULD match
                "url": "http://www.listaspam.com/busca.php?Telefono={placeholder}",       # Target URL where {placeholder} would be modified by the alias
            }
        }

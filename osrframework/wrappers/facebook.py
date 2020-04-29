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
__version__ = "2.0"


from osrframework.utils.platforms import Platform


class Facebook(Platform):
    """A <Platform> object for Facebook"""
    def __init__(self):
        self.platformName = "Facebook"
        self.tags = ["social", "contact"]

        # Base URL
        self.baseURL = "https://facebook.com/"

        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.FullName": '<title id="pageTitle">(.+) \| Facebook</title>',    # Regular expresion to extract the alias
                },
                "needs_credentials": False,
                "not_found_text": "https://static.xx.fbcdn.net/rsrc.php/v3/yp/r/U4B06nLMGQt.png",                   # Text that indicates a missing profile
                "query_validator": "[a-zA-Z\.0-9_\-]+",                            # Regular expression that the alias SHOULD match
                "url": "https://www.facebook.com/{placeholder}",       # Target URL where {placeholder} would be modified by the alias
            },
            "searchfy": {
                "debug": False,
                "extra_fields": {},
                "needs_credentials": False,
                "not_found_text": "We couldn&#039;t find anything for",
                "query_validator": ".+",
                "url": "https://www.facebook.com/public?query={placeholder}",
                # Needed function to extract aliases from the website
                "alias_regexp": '<a title="[^\"]+" class="_32mo" href="https://www.facebook.com/([^\"]+)"><span>'
            },
            # Reimplementation needed of check_mailfy
            "mailfy": {},
        }

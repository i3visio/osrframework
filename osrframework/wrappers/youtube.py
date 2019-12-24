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


class Youtube(Platform):
    """<Platform> class"""
    def __init__(self):
        """Constructor with parameters

        This method permits the developer to instantiate dinamically Platform
        objects."""
        self.platformName = "Youtube"
        self.tags = ["social", "video"]
        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.Date.Create": '{"start": "<li class=\"about-stat joined-date\">", "end": "</li>"}',    # Regular expresion to extract the alias
                },
                "needs_credentials": False,
                "not_found_text": "channel-empty-message banner-message",                   # Text that indicates a missing profile
                "query_validator": "[^@, ]+",                            # Regular expression that the alias SHOULD match
                "url": "https://www.youtube.com/user/{placeholder}/about",       # Target URL where {placeholder} would be modified by the alias
            },
            "searchfy": {
                "debug": False,
                "extra_fields": {},
                "needs_credentials": False,
                "not_found_text": "style-scope ytd-background-promo-renderer",
                "query_validator": ".+",
                "url": "https://www.youtube.com/results?filters=channel&lclk=channel&search_query={placeholder}&sp=EgIQAg%253D%253D",
                # Needed function to extract aliases from the website
                "alias_regexp": 'url":"/user/([^"]+)","webPageType":"WEB_PAGE_TYPE_BROWSE'
            },
            # Reimplementation needed of check_mailfy
            "mailfy": {},
        }

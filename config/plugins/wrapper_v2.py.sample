# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2018 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

__author__ = "i3visio <contacto@i3visio.com>"
__version__ = "2.0"

from osrframework.utils.platforms import Platform
import urllib2

class Demo(Platform):
    """
        A <Platform> object for Demo.
    """
    def __init__(self):
        """
            Constructor...
        """
        self.platformName = "Demo"
        self.tags = ["demo"]
        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "i3visio.alias": "My alias: ([^<]+)",
                },
                "needs_credentials": False,
                "not_found_text": "<h1>404</h1>",
                "query_validator": ".+",
                "url": "http://demo.demo/user/{placeholder}",
            },
            "searchfy": {
                "debug": False,
                "extra_fields": {
                    "i3visio.alias": "My alias: ([^<]+)",
                },
                "needs_credentials": False,
                "not_found_text": "<h1>404</h1>",
                "query_validator": ".+",
                "url": "http://demo.demo/user/{placeholder}",
                # Needed function to extract aliases from the website
                "alias_regexp": "demo.demo/(.+)"
            },
            # Reimplementation needed of check_mailfy
            "mailfy": {},
        }

    def check_mailfy(self, query):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
        -----
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Return:
        -------
            Returns the collected data if exists or None if not.
        """
        return query if query urllib2.open("https://demo.demo/{}".format(query)) else None

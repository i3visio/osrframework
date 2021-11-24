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
__version__ = "2.1"


import requests
from osrframework.utils.platforms import Platform
from osrframework.api.twitter_api import TwitterAPIWrapper as TwitterAPIWrapper


class Twitter(Platform):
    """A <Platform> object for Twitter"""
    def __init__(self):
        self.platformName = "Twitter"
        self.tags = ["contact", "microblogging", "social"]

        # Base URL
        self.baseURL = "https://twitter.com/"

        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.FullName": ' \((.+)\)</title>',    # Regular expresion to extract the alias
                },
                "needs_credentials": False,
                "not_found_text": "Sorry, that page does not exist. ",                   # Text that indicates a missing profile
                "query_validator": "[a-zA-Z0-9_]{3,15}",                            # Regular expression that the alias SHOULD match
                "url": "https://tweettunnel.com/{placeholder}",       # Target URL where {placeholder} would be modified by the alias
            },
            # Reimplementation needed of check_mailfy
            "mailfy": {
                "debug": False,
                "extra_fields": {},
                "needs_credentials": False,
                "not_found_text": '"valid":true',
                "query_validator": ".+",
                "url": "https://api.twitter.com/i/users/email_available.json?email=",
            },
        }

    def do_usufy(self, query, **kwargs):
        """Verifying a usufy query in this platform using the API

        If no credentials are provided, the standard verifier will be raised.

        Args:
            query: The element to be searched.

        Return:
            A list of elements to be appended.
        """
        # Trying to interact with the API Wrapper
        try:
            self.wrapperAPI = TwitterAPIWrapper()

            results = self.wrapperAPI.get_user(query)

            for r in results:
                # Manually appending the URL
                aux = {}
                aux["type"]="i3visio.uri"
                alias=r["value"].split(' - ')[1]
                aux["value"]= self.createURL(word=alias, mode="usufy")
                aux["attributes"]= []
                r["attributes"].append(aux)

        # Standard execution
        except Exception as e:
            return super(Twitter, self).do_usufy(query, **kwargs)

    def do_searchfy(self, query, **kwargs):
        """Verifying a searchfy query in this platform using the API

        If no credentials are provided, the standard verifier will be raised.

        Args:
            query (str): The element to be searched.

        Return:
            A list of elements to be appended.
        """
        # Trying to interact with the API Wrapper
        try:
            results = self.wrapperAPI.search_users(query)
            # Manually appending the URL
            for r in results:
                aux = {}
                aux["type"]="i3visio.uri"
                alias=r["value"].split(' - ')[1]
                qURL = self.createURL(word=alias, mode="usufy")
                aux["value"]= qURL
                aux["attributes"]= []
                r["attributes"].append(aux)

        # Standard execution
        except Exception as e:
            return super(Twitter, self).do_searchfy(query, **kwargs)


    def check_mailfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Returns:
            Returns the collected data if exists or None if not.
        """
        try:
            response = requests.get(f"https://api.twitter.com/i/users/email_available.json?email={query}")
            # It is occupied, so it exists
            if '"valid":false' in response.text:
                return query
            # It is not occupied, so it is not registered
            else:
                return False
        except Exception as _:
            return False

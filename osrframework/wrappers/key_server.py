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
__version__ = "2.0"


import re

import osrframework.utils.general as general
from osrframework.utils.platforms import Platform


class KeyServerIO(Platform):
    """A <Platform> object for the MIT PGP public keys repository"""
    def __init__(self):
        self.platformName = "KeyServerIO"
        self.tags = ["mails", "cryptography"]

        # Base URL
        self.baseURL = "https://pgp.key-server.io/pks/lookup?search="
        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["mailfy"] = True
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = False
        self.isValidMode["searchfy"] = True

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        #self.url["usufy"] = "https://github.com/" + "<usufy>"
        self.url["searchfy"] = "https://pgp.key-server.io/pks/lookup?search=<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        #self.needsCredentials["phonefy"] = False
        #self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        #self.validQuery["usufy"] = ".*"
        self.validQuery["searchfy"] = ".+"
        self.validQuery["mailfy"] = ".+"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = [
            "This is not the web page you are looking for"
        ]
        self.notFoundText["searchfy"] = []

        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}

        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""

        # Definition of regular expressions to be searched in usufy mode
        #self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        #self.searchfyAliasRegexp = '&lt;([^\&]+)&gt;'
        self.searchfyEmailRegexp = ' &lt;([^\&]+)&gt;'

        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

    def check_mailfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
            query (str): The element to be searched.

        Returns:
            String. Returns the collected data if exists or None if not.
        """
        import re
        import requests

        s = requests.Session()

        # Getting the first response to grab the csrf_token
        resp = s.get(f"https://pgp.key-server.io/pks/lookup?search={query}")

        if resp.status_code == 200 or resp.status_code == 404:
            if '         0 keys found..' in resp.text:
                return None
            else:
                return resp.text
        else:
            print(general.warning(f"Something happened. keyserver.io returned status '{resp.status_code}' for '{query}'."))
            return None

    def do_mailfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return an equivalent array.

        Args:
            query: The element to be searched.

        Returns:
            A list of elements to be appended. A sample output format is as follows:
            [
              {
                "attributes": [
                  {
                    "attributes": [],
                    "type": "com.i3visio.Email",
                    "value": "contacto@i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Alias",
                    "value": "contacto"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Domain",
                    "value": "i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Platform",
                    "value": "Twitter"
                  }
                ],
                "type": "com.i3visio.Profile",
                "value": "Twitter - contacto@i3visio.com"
              }
            ]
        """
        info = self.check_mailfy(query, **kwargs)

        results = []
        if info:
            emails = set(re.findall(' &lt;([^\&]+)&gt;', info))

            for i, email in enumerate(emails):
                try:
                    expandedEntities = general.expand_entities_from_email(email)
                    r = {
                        "type": "com.i3visio.Profile",
                        "value": self.platformName + " - " + email,
                        "attributes": expandedEntities + [
                            {
                                "type": "com.i3visio.Platform",
                                "value": self.platformName,
                                "attributes": []
                            }
                        ]
                    }
                    results.append(r)
                except IndexError:
                    # A result does not contain a @.
                    pass

        return results

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


from osrframework.utils.platforms import Platform


class Instagram(Platform):
    """A <Platform> object for Instagram"""
    def __init__(self):
        self.platformName = "Instagram"
        self.tags = ["social"]

        # Base URL
        self.baseURL = "http://instagram.com/"

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["mailfy"] = True
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = True

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        self.url["usufy"] = "http://www.instagram.com/" + "<usufy>"
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["searchfy"] = "http://picbear.online/search/" + "<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["mailfy"] = False
        self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        self.validQuery["mailfy"] = ".+"
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["searchfy"] = ".*"
        self.validQuery["usufy"] = ".+"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["p-error dialog-404"]
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
        self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        #"<img alt=\"@([^\"]+)\""
        self.searchfyAliasRegexp = "\" alt=\"@([^\"]+)\"> <\/div> <div class="
        # Example of fields:"<img alt=\"@([^\"]+)\""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

    def check_mailfy(self, query, kwargs={}):
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
        r1 = s.get("https://www.instagram.com")
        csrf_token = re.findall("csrf_token", r1.text)[0]

        # Launching the query to Instagram
        r2 = s.post(
            'https://www.instagram.com/accounts/web_create_ajax/attempt/',
            data={"email": query},
            headers={"X-CSRFToken": csrf_token}
        )

        if '{"email": [{"message": "Another account is using' in r2.text:
            return r2.text
        else:
            return None

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
from osrframework.api.twitter_api import TwitterAPIWrapper as TwitterAPIWrapper


class Twitter(Platform):
    """A <Platform> object for Twitter"""
    def __init__(self):
        self.platformName = "Twitter"
        self.tags = ["contact", "microblogging", "social"]

        # Base URL
        self.baseURL = "http://twitter.com/"

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["mailfy"] = True
        self.isValidMode["phonefy"] = False
        self.isValidMode["searchfy"] = True
        self.isValidMode["usufy"] = True

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        self.url["mailfy"] = "https://api.twitter.com/i/users/email_available.json?email=<mailfy>"
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["searchfy"] = "https://twitter.com/search?f=users&vertical=default&q=\"" + "<searchfy>" + "\""
        self.url["usufy"] = "http://twitter.com/" + "<usufy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        self.needsCredentials["mailfy"] = False
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = "[a-zA-Z0-9_]+"
        self.validQuery["searchfy"] = ".+"
        self.validQuery["mailfy"] = ".+"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        self.notFoundText["mailfy"] = ['"valid":true']
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["<form class=\"search-404\""]
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
        # Examples (do NOT forget to escape the quoting marks inside any string: \"):
        self.fieldsRegExp["usufy"]["@protected"] = {"start": "data-protected=\"", "end": "\">\n      <span class=\"UserActions"}
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "class=\"ProfileHeaderCard-nameLink u-textInheritColor js-nav\n\">", "end": "</a>\n  </h1>"}
        #self.fieldsRegExp["usufy"]["ProfileHeaderCard-bio"] = {"start": "<p class=\"ProfileHeaderCard-bio u-dir\"\n    \n    dir=\"ltr\">", "end": "</p>"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "<span class=\"ProfileHeaderCard-locationText u-dir\" dir=\"ltr\">\n            ", "end": "\n        </span>\n      </div>\n\n    <div class=\"ProfileHeaderCard-url"}
        self.fieldsRegExp["usufy"]["@created_at"] = {"start": "<span class=\"ProfileHeaderCard-joinDateText js-tooltip u-dir\" dir=\"ltr\" title=\"", "end": "\">Se uni"}
        self.fieldsRegExp["usufy"]["i3visio.uri.homepage"] = {"start": "<span class=\"ProfileHeaderCard-urlText u-dir\" dir=\"ltr\"><a class=\"u-textUserColor\" target=\"_blank\" rel=\"me nofollow\" href=\"[^\"]*\" title=\"", "end": "\">"}
        #self.fieldsRegExp["usufy"]["PhotoRail-headingText"] = {"start": "class=\"js-nav\">\n                \n                ", "end": "             </a>"}

        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        self.searchfyAliasRegexp = "data-screen-name=\"([^\"]+)\""
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}


    def do_usufy(self, query, **kwargs):
        """
        Verifying a usufy query in this platform.

        This might be redefined in any class inheriting from Platform.

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
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
        """Verifying a usufy query in this platform

        This might be redefined in any class inheriting from Platform.

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

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


class Photobucket(Platform):
    """A <Platform> object for Photobucket"""
    def __init__(self):
        self.platformName = "Photobucket"
        self.tags = ["imagery"]

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "http://photobucket.com/user/<usufy>/library/?sort=3&page=1"
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = ".+"
        #self.validQuery["searchfy"] = ".*"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = [
            "<h2>Sorry, the requested page does not exist.</h2>"
        ]
        #self.notFoundText["searchfy"] = []

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
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

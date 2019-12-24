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


class Xtelefono(Platform):
    """A <Platform> object for Xtelefono."""
    def __init__(self):
        self.platformName = "Xtelefonos"
        self.tags = ["phone"]

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["phonefy"] = True
        self.isValidMode["usufy"] = False
        self.isValidMode["searchfy"] = False

        ######################################
        # Search URL for the different modes #
        ######################################
        self.url = {}
        self.url["phonefy"] = "http://www.xtelefono.es/search/?q=" + "<phonefy>"
        #self.url["usufy"] = "http://anyurl.com/user/" + "<phonefy>"
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<phonefy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False

        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        self.validQuery["phonefy"] = ".+"
        self.validQuery["usufy"] = ".+"
        self.validQuery["searchfy"] = ".+"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the phone number is not appearing
        self.notFoundText = {}
        self.notFoundText["phonefy"] = ["</strong> Número desconocido</h1>"]
        #self.notFoundText["usufy"] = []
        #self.notFoundText["searchfy"] = []

        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}
        # Definition of regular expressions to be searched in phonefy mode
        self.fieldsRegExp["phonefy"] = {}
        #self.fieldsRegExp["phonefy"]["i3visio.location.province"] = "<strong class='located_label'>(.*),"
        #self.fieldsRegExp["phonefy"]["i3visio.location.country"] = "class='country_located' alt='([a-zA-Zñ]*)'"
        self.fieldsRegExp["phonefy"]["i3visio.text"] = '<h4 class="media-heading">(.*)</p>'

        # Definition of regular expressions to be searched in usufy mode
        #self.fieldsRegExp["usufy"] = {}
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

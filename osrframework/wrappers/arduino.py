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
__version__ = "1.1"


from osrframework.utils.platforms import Platform


class Arduino(Platform):
    """A <Platform> object for Arduino"""
    def __init__(self):
        self.platformName = "Arduino"
        self.tags = ["development", "hardware"]

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
        self.url["usufy"] = "https://forum.arduino.cc/u/" + "<usufy>"
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
        self.notFoundText["usufy"] = ["page-not-found"]
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
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "<td><b>Name: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@total_posts"] = {"start": "<td><b>Posts: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@position"] = {"start": "<td><b>Posts: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@karma"] = {"start": "<b>Karma: </b>\n\t\t\t\t\t</td><td>\n\t\t\t\t\t\t", "end": "\n\t\t\t\t\t</td>"}
        self.fieldsRegExp["usufy"]["i3visio.date"] = {"start": "<td><b>Date Registered: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@last_active"] = {"start": "<td><b>Last Active: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@ICQ"] = {"start": "<td><b>ICQ:</b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@AIM"] = {"start": "<td><b>AIM: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@MSN"] = {"start": "<td><b>MSN: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@YIM"] = {"start": "<td><b>YIM: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["i3visio.email"] = {"start": "<td><b>Email: </b></td>\n\t\t\t\t\t<td><i>", "end": "</i>"}
        self.fieldsRegExp["usufy"]["i3visio.uri.homepage"] = {"start": "<td><b>Website: </b></td>\n\t\t\t\t\t<td><a href=\"", "end": "\""}
        self.fieldsRegExp["usufy"]["@current_status"] = {"start": "<td><b>Current Status: </b></td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<i><img src=\"http://forum.arduino.cc/Themes/arduinoWide/images/useroff.gif\" alt=\"Offline\" align=\"middle\" /><span class=\"smalltext\">", "end": "</span></i>"}
        self.fieldsRegExp["usufy"]["@gender"] = {"start": "<td><b>Gender: </b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@age"] = {"start": "<td><b>Age:</b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "<td><b>Location:</b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@local_time"] = {"start": "<td><b>Local Time:</b></td>\n\t\t\t\t\t<td>", "end": "</td>"}
        self.fieldsRegExp["usufy"]["@language"] = {"start": "<td><b>Language:</b></td>\n\t\t\t\t\t<td>", "end": "</td>"}

        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

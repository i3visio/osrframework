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


class Infojobs(Platform):
    """A <Platform> object for Infojobs"""
    def __init__(self):
        self.platformName = "Infojobs"
        self.tags = ["jobs"]

        # Valid modes
        self.isValidMode = {
            "mailfy": True,
            "phonefy": False,
            "searchfy": False,
            "usufy": False,
        }

        self.url = {}

        self.needsCredentials = {
            "mailfy": False
        }

        self.validQuery = {
            "mailfy": ".+"
        }


        self.fieldsRegExp = {}

        # Definition of regular expressions to be searched in usufy mode
        self.fieldsRegExp["mailfy"] = {}

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
            String. The collected data if exists or None if not.
        """
        import requests

        s = requests.Session()

        # Getting the first response to grab the csrf_token
        r1 = s.get('https://www.infojobs.net')

        # Launching the query to Instagram
        r2 = s.post(
            'https://www.infojobs.net/candidate/profile/check-email-registered'
            '.xhtml',
            data={"email": query},
        )

        if '{"email_is_secure":true,"email":true}' in r2.text:
            return r2.text
        return None

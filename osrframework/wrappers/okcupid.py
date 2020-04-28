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
__version__ = "3.0"


from osrframework.utils.platforms import Platform


class OkCupid(Platform):
    """<Platform> class"""
    def __init__(self):
        """Constructor with parameters

        This method permits the developer to instantiate dinamically Platform
        objects."""
        self.platformName = "OkCupid"
        self.tags = ["contact"]
        self.modes = {
            "mailfy": {
                "debug": False,
            }
        }

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
        r1 = s.get('https://www.okcupid.com')

        # Launching the query to Instagram
        r2 = s.post(
            'https://www.okcupid.com/1/apitun/signup/check_email',
            json={"email": query},
        )

        if self.modes["mailfy"]["debug"]:
            print(f"Response: {[r2.text]}")

        if '"is_valid" : false' in r2.text:
            return r2.text
        return None

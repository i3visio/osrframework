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

import os

import osrframework.utils.config_credentials as c_creds
import osrframework.utils.general as general


class Credential():
    """Class to match the credentials needed by a platform
    """
    def __init__(self, user, password):
        """Creation of the credentials

        Args:
            user (str): Login name.
            password (str): Password.
        """
        self.user = user
        self.password = password


def get_credentials():
    """Recovering the credentials from a file with the following structure

    Returns:
        A dictionary with the following struture:
            { "platform1": [C1<Credential>, C2<Credential>], "platform2": [C3<Credential>]}
    """
    creds = {}

    creds_tuples = c_creds.get_list_of_credentials()

    for cTuple in creds_tuples:
        plat, user, password = cTuple

        c = Credential(user, password)

        if plat not in creds.keys():
            creds[plat] = [c]
        else:
            creds[plat] = creds[plat].append(c)
    print(f"{general.info(str(len(creds_tuples)))} credentials have been loaded.")
    return creds

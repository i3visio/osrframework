# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


import json
import sys
import urllib2

from osrframework.transforms.lib.maltego import *
import osrframework.thirdparties.md5db_net.checkIfHashIsCracked as md5crack

def hashToMD5dbDotNet(hash=None):
    """
        Method that checks if the given hash is stored in the md5db.net.

        :param argv:    hash to verify.

    """

    resolvedHash = md5crack.checkIfHashIsCracked(hash)
    me = MaltegoTransform()

    if resolvedHash.split():

        newEntities = []

        new = {}
        new["value"] = resolvedHash
        new["type"] = "i3visio.text"
        new["attributes"] = []

        newEntities.append(new)

        # Adding the new entities
        me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()


if __name__ == "__main__":
    hashToMD5dbDotNet(hash=sys.argv[1])



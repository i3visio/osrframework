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
import osrframework.thirdparties.md5crack_com.checkIfHashIsCracked as md5crack

def hashToMD5crackDotCom(argv=None):
    ''' 
        Method that checks if the given hash is stored in the md5crack.com.

        :param argv:    hash to verify.

    '''
    me = MaltegoTransform(argv)
    
    # Recovering the phone value
    try:
        query = me.getVar("@value")
    except:
        query = me.getValue()       

    newEntities = md5crack.checkIfHashIsCracked(hash=query)

    # This returns a dictionary like:
    """ 
        [
          {
            "attributes": [
              {
                "attributes": [], 
                "type": "i3visio.text", 
                "value": "DE"
              }
            ], 
            "type": "i3visio.location.country", 
            "value": "Germany"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.text", 
            "value": "1&1 Internet AG"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.ipv4", 
            "value": "217.160.129.99"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.location.geo", 
            "value": "51, 9"
          }
        ]
    """

    # Adding the new entities
    me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()


if __name__ == "__main__":
    hashToMD5crackDotCom(argv=sys.argv)



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

import osrframework.thirdparties.infobel_com.checkPhoneDetails as infobel_com
from osrframework.transforms.lib.maltego import *


def phoneToPerson(argv ):
    ''' 
        Method that obtains all the entities in a given profile.

        :param argv:    the serialized entity. First parameter is always the platform and the second parameter is always the phone.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform(argv)

    # Recovering the phone value
    try:
        phone = me.getVar("@value")
    except:
        phone = me.getValue()
        
    # Trying to recover all the possible i3visio entities    
    newEntities = infobel_com.checkPhoneDetails(phone)
    # This returns a dictionary like the following:
    """
    [
      {
        "attributes": [
          {
            "attributes": [], 
            "type": "i3visio.fullname", 
            "value": "-----"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.location.postalcode", 
            "value": "-----"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.location.city", 
            "value": "-----"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.location.address", 
            "value": "-----"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.uri", 
            "value": "-----"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.platform", 
            "value": "Infobel"
          }
        ], 
        "type": "i3visio.person", 
        "value": "-----"
      }
    ]
    """
    # Adding the new entities
    me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()


if __name__ == "__main__":
    phoneToPerson(sys.argv)



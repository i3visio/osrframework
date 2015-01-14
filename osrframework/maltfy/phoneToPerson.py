# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
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
#import osframework.maltfy.lib.constants as constants
from osrframework.maltfy.lib.maltego import *


def phoneToPerson(argv ):
    ''' 
        Method that obtains all the entities in a given profile.

        :param argv:    the serialized entity. First parameter is always the platform and the second parameter is always the phone.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform()
    #me.parseArguments(argv);
    phone = sys.argv[1]

    # Trying to recover all the possible i3visio entities    
    results = infobel_com.checkPhoneDetails(phone)
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

    # Getting the first and unique object retrieved
    if len(results) > 0:
        # Creating the entity
        newEnt = me.addEntity("i3visio.person",results[0]["value"])    
        
        # Writing down the extra information
        newEnt.setDisplayInformation("<h3>" + results[0]["value"] +"</h3><p>" + json.dumps(results[0], sort_keys=True, indent=2) + "!</p>");                
        
        # Selecting the attributes
        entities = results[0]["attributes"]
        for elem in entities:
            # This will create new entities linked to the telephone
            newEnt.addAdditionalFields(elem["type"],elem["type"],True,elem["value"])

        # Returning the output text...
    me.returnOutput()


if __name__ == "__main__":
    phoneToPerson(sys.argv)



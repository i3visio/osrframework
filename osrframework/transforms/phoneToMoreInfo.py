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

import osrframework.utils.platform_selection as platform_selection
import osrframework.phonefy as phonefy
#import osframework.transforms.lib.constants as constants
from osrframework.transforms.lib.maltego import *


def phoneToMoreInfo(argv ):
    ''' 
        Method that obtains all the entities in a given profile.

        :param argv:    the serialized entity. First parameter is always the platform and the second parameter is always the phone.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform(argv)
    #me.parseArguments(argv);
    platform = argv[1]
    platforms = platform_selection.getPlatformsByName([platform])

    phone = argv[2]
    numbers = [phone]        

    # Trying to recover all the possible i3visio entities    
    results = phonefy.processPhoneList(platforms=platforms, numbers=numbers)

    newEntities = []

    # Getting the first and unique object retrieved
    if len(results) >0:
        entities = results[0]["attributes"]
        # This returns a dictionary like the following:
        """
        [
          {
            "attributes": [],
            "type": "i3visio.location.country",
            "value": "Espa\u00f1a"
          },
          {
            "attributes": [],
            "type": "i3visio.location.province",
            "value": "Sevilla"
          },
          {
            "attributes": [],
            "type": "i3visio.text",
            "value": "Por <span>An\u00f3nimo</span>&nbsp;hace 2 meses </h4><p class=\"co
        mment_text\">Gentuza. se vayan mirando esto http://ccaa.elpais.com/ccaa/2013/11/
        20/madrid/<a target='_blank' href='busca.php?Telefono=1384983847'>1384983847</a>
        _<a target='_blank' href='busca.php?Telefono=570086'>570086</a>.html"
          },
          {
            "attributes": [],
            "type": "i3visio.text",
            "value": "Por <span>An\u00f3nimo</span>&nbsp;hace 5 meses </h4><p class=\"co
        mment_text\">Los mejores clientes de todas las telefonicas son los centros de ll
        amadas,hay mucho dinero en juego."
        }
        ]
        """

        #print json.dumps(entities, indent=2)
        for elem in entities:
            newEntities.append(elem)
        
            """       
            newEnt = me.addEntity(elem["type"],elem["value"])
            
            otherIssues = []
            
            for att in elem["attributes"]:
                # This will create new entities linked to the telephone
                if att["type"] == "i3visio.location.country" or att["type"] == "i3visio.location.province":
                    me.addEntity(att["type"],att["value"])
                if att:
                    otherIssues.append(att) 
            
		    newEnt.setDisplayInformation("<h3>" + elem["value"] +"</h3><p>" + json.dumps(elem["attributes"], sort_keys=True, indent=2) + "!</p>"); """

    # Adding the new entities
    me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()



if __name__ == "__main__":
    phoneToMoreInfo(sys.argv)



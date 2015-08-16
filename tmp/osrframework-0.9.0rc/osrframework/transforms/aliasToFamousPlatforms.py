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


import sys
import json
from osrframework.transforms.lib.maltego import *
import osrframework.thirdparties.skype.checkInSkype as skype

def aliasToSkypeAccounts(query=None):
    ''' 
        Method that checks if a given alias appears in Skype.

        :param query:    query to verify.

    '''
    me = MaltegoTransform()

    jsonData = skype.checkInSkype(query=query)

    # This returns a dictionary like:
    # [{}]

    #print json.dumps(entities, indent=2)
    for user in jsonData:
        newEnt = me.addEntity("i3visio.profile","Skype - " +str(user["i3visio.alias"]))
        aliasEnt = me.addEntity("i3visio.alias",user["i3visio.alias"])

        newEnt.setDisplayInformation("<h3>" + user["i3visio.alias"] +"</h3><p>");# + json.dumps(user, sort_keys=True, indent=2) + "!</p>");
        newEnt.addAdditionalFields("i3visio.platform","i3visio.platform",True,"Skype")
        for field in user.keys():
            #if field != "i3visio.alias":
            # [TO-DO] Appending all the information from the json:
            #if field == "i3visio.aliases":
            #    listAliases = [user["i3visio.alias"]]
            #    listAliases += user[field]
            #    # in this case, this is a list
            #    for alias in user[field]:
            #        aliasEnt = me.addEntity("i3visio.alias",alias.encode('utf-8'))
            #elif user[field] != None:
            if user[field] != None:
                try:
                    newEnt.addAdditionalFields(field,field,True,str(user[field]).encode('utf-8'))
                except:
                    # Something passed...
                    pass

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    aliasToSkypeAccounts(query=sys.argv[1])



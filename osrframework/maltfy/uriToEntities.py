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

import osrframework.entify.processing as processing
import osrframework.maltfy.lib.constants as constants
import osrframework.utils.browser as browser
from osrframework.maltfy.lib.maltego import *
import osrframework.entify.config_entify as config

def uriToI3visioEntities(uri, platform='all'):
    ''' 
        Method that obtains all the entities in a given profile.

        :param uri:    the uri to be received.
        :param platform:    a platform string representing the regular expression to be used.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform()
    me.parseArguments(argv)

    ent = json.loads(me.getVar("_serialized"))

    # Trying to recover all the possible i3visio entities
    found_fields = {}

    # Using i3visio browser to avoid certain issues...
    i3Browser = browser.Browser()
    # Accessing the resources
    data = i3Browser.recoverURL(uri)

    # Getting the list of <RegExp> objects from entify
    lRegexp = config.getRegexpsByName([platform])

    new_entities = processing.getEntitiesByRegexp(data=data, listRegexp = lRegexp)    
    # This returns a dictionary like the following:
    """
        [{
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'a9b8c5d848205db514d4097d2b78f4528d01a79f39601e0f9c5c40ed689471'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'b28b896e6eeb8d651cacd5f4a4d1490fbe9d05dbc92221609350b0ce7a68e9'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'd727fed4d969b14b28165c75ad12d7dddd56c0198fa70cedc3fdad7ac395b2'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': '3e9a2204fcfc6f7dde250e61ca35353411880024102cba14a0bd45f05f1e74'
        }]
    """

    #print json.dumps(entities, indent=2)
    for elem in entities:
        newEnt = me.addEntity(elem["type"],elem["value"])
        newEnt.setDisplayInformation("<h3>" + elem["value"] +"</h3><p>"+str(elem["attributes"])+"</p>")        
        for extraAtt in elem["attributes"]:
            newEnt.addAdditionalFields(str(extraAtt['type']), str(extraAtt['type']), True, str(extraAtt['value']))    

    # Returning the output text...
    me.returnOutput()


if __name__ == "__main__":
    uriToI3visioEntities(sys.argv[2], platform = sys.argv[1])



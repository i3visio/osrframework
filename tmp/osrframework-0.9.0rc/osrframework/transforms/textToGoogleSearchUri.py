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

from osrframework.transforms.lib.maltego import *
import osrframework.searchengines.google as google

def textToGoogleSearchUri(argv):
    ''' 
        List of URI entities corresponding to the results of a Google Search.

        :param argv:    the text to be searched.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform(argv)

    # Recovering the text value
    try:
        text = me.getVar("@value")
    except:
        text = me.getValue()

    newEntities = google.processSearch(text)
    # This returns a dictionary like the following:
    """ 
        [{
        'attributes': [],
        'type': 'i3visio.uri',
        'value': 'http://foo.com'
        }, {
        'attributes': [],
        'type': 'i3visio.uri',
        'value': 'http://bar.com'
        }, 
        ...
        ]
    """
    # Adding the new entities
    me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    textToGoogleSearchUri(sys.argv)



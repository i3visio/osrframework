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
import re

from osrframework.transforms.lib.maltego import *

def uriToGoogleCacheUri(argv=None):
    ''' 
        Method that recovers the domain from a URI.

        :param argv:    the serialized entity.

    '''
    me = MaltegoTransform(argv)

    # Recovering the Uri value
    try:
        uri = me.getVar("@value")
    except:
        uri = me.getValue()

    # We add a trailing '/' to the uri if there is not a trailing one
    if uri.count('/') == 2:
        uri+='/'
    
    newEntities = []
    
    # Google Cache Base URI
    baseCacheURI = "http://webcache.googleusercontent.com/search?q=cache:"
    
    aux = {}
    aux["type"] = "i3visio.uri"
    aux["value"] = baseCacheURI + uri
    aux["attributes"] = []
    newEntities.append(aux)
    
    me.addListOfEntities(newEntities)
        
    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    uriToGoogleCacheUri(sys.argv)



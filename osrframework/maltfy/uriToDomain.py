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
import re

from osrframework.maltfy.lib.maltego import *

def uriToDomain(uri=None):
    ''' 
        Method that recovers the domain from a URI.

        :param uri:    uri to verify.

    '''
    me = MaltegoTransform()

    newEnt = me.addEntity("i3visio.domain",domain.split('.')[-1])

    domainRegExp = "(?:https?|s?ftp)://([a-zA-Z0-9\_\.\-]+)(?:\:|/)"
    found = re.findall(domainRegExp, uri)
    if len(found) > 0:        
        newEnt = me.addEntity("i3visio.domain",found[0])
        
    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    uriToDomain(uri=sys.argv[1])



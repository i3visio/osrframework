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

def domainToTld(argv=None):
    ''' 
        Method that extract the TLD from a domain.

        :param argv:    the serialized entity.

    '''
    me = MaltegoTransform(argv)

    # Recovering the domain value
    try:
        domain = me.getVar("@value")
    except:
        domain = me.getValue()

    tld = domain.split('.')[-1]
    
    newEntities = []
    
    # Creation of a temp entity
    aux = {}
    aux["type"] = "i3visio.tld"
    aux["value"] = tld
    aux["attributes"] = []
    newEntities.append(aux)
    
    me.addListOfEntities(newEntities)
    
    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    domainToTld(argv=sys.argv)



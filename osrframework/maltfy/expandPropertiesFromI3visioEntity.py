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

from osrframework.maltfy.lib.maltego import *
import sys
import json
import osrframework.maltfy.lib.constants as constants

def expandPropertiesFromI3visioEntity(argv):
    ''' 
        Method that expands the properties from a given i3visio entity. It is useful to create new Entities based on the contents of the properties.
        :param argv:    the serialized entity.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform(argv)

    try:
        # Trying to recover pending entities if they exist...
        if me.getVar("_number_pending") != "0":
            entitiesToShow = me.getVar("_pending")
            newEntities = json.loads(entitiesToShow)        
            me.addListOfEntities(newEntities)            
    except:
        pass

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    expandPropertiesFromI3visioEntity(sys.argv)



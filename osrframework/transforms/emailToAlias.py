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


from osrframework.transforms.lib.maltego import *

def emailToAlias(email=None):
    ''' 
        Method that recovers the alias of the given email.

        :param email:    email to extract the alias from.

    '''
    me = MaltegoTransform()

    aux = {}
    aux["type"] = "i3visio.alias"
    aux["value"] = email.split('@')[0]
    aux["attributes"] = []
        
    me.addListOfEntities([aux])

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    emailToAlias(email=sys.argv[1])



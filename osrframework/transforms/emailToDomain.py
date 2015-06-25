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
import urllib2

from osrframework.transforms.lib.maltego import *

def emailToDomain(email=None):
    ''' 
        Method that recovers the entity of the domain of the given mail.

        :param email:    email to verify.

    '''
    me = MaltegoTransform()

    aux = {}
    aux["type"] = "i3visio.domain"
    aux["value"] = email.split('@')[1]
    aux["attributes"] = []
        
    me.addListOfEntities([aux])

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    emailToDomain(email=sys.argv[1])



# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
from osrframework import domainfy

def aliasToKnownEmails(query=None, parType="global"):
    '''
        Method that checks if there exist domains for a given a alias.

        :param query:    alias to verify.

    '''
    me = MaltegoTransform()


    # Processing the options returned to remove the "all" option
    tlds = []
    for typeTld in domainfy.TLD.keys():
        if typeTld == parType:
            for tld in domainfy.TLD[typeTld]:
                tlds.append({ "tld" : tld, "type" : typeTld })

    domains = domainfy.createDomains(tlds, nicks = [query])

    jsonData = domainfy.performSearch(domains)
    #print json.dumps(jsonData, indent=2)
    me.addListOfEntities(jsonData)

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    # We avoi using additional parameters
    aliasToKnownEmails(parType=sys.argv[1], query=sys.argv[2])

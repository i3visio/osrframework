# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This file is part of entify.
#
#    entify is free software: you can redistribute it and/or modify
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

import os
import copy
import logging
# Importing Classes of <RegexpObject> objects that will be used in the script. The files are stored in the regexp folder.
# For demo only
#from regexp.demo import Demo
from entify.lib.patterns.bitcoinaddress import BitcoinAddress
from entify.lib.patterns.dni import DNI
from entify.lib.patterns.dogecoinaddress import DogecoinAddress
from entify.lib.patterns.email import Email
from entify.lib.patterns.ipv4 import IPv4
from entify.lib.patterns.litecoinaddress import LitecoinAddress
from entify.lib.patterns.md5 import MD5
from entify.lib.patterns.namecoinaddress import NamecoinAddress
from entify.lib.patterns.peercoinaddress import PeercoinAddress
from entify.lib.patterns.sha1 import SHA1
from entify.lib.patterns.sha256 import SHA256
from entify.lib.patterns.url import URL
# Add any additional import here
#from regexp.anynewregexp import AnyNewRegexp
# <ADD_NEW_REGEXP_IMPORT_BELOW>
# Please, notify the authors if you have written a new regexp.

def getAllRegexp():
    ''' 
        Method that recovers ALL the list of <RegexpObject> classes to be processed....

        :return:    Returns a list [] of <RegexpObject> classes.
    '''
    logger = logging.getLogger("entify")

    logger.debug("Recovering all the available <RegexpObject> classes.")
    listAll = []
    # For demo only
    #listAll.append(Demo())
    listAll.append(BitcoinAddress())
    listAll.append(DNI())
    listAll.append(DogecoinAddress())         
    listAll.append(Email())
    listAll.append(IPv4())
    listAll.append(LitecoinAddress())
    listAll.append(MD5())
    listAll.append(NamecoinAddress())
    listAll.append(PeercoinAddress())
    listAll.append(SHA1())
    listAll.append(SHA256())
    listAll.append(URL())
    # Add any additional import here
    #listAll.append(AnyNewRegexp)
    # <ADD_NEW_REGEXP_TO_THE_LIST>
    # Please, notify the authors if you have written a new regexp.

    logger.debug("Returning a list of " + str(len(listAll)) + " <RegexpObject> classes.")
    return listAll

def getAllRegexpNames(regexpList = None):
    ''' 
        Method that recovers the names of the <RegexpObject> in a given list.

        :param regexpList:    list of <RegexpObject>. If None, all the available <RegexpObject> will be recovered.

        :return:    Array of strings containing the available regexps.
    '''
    if regexpList == None:
        regexpList = getAllRegexp()
    listNames = ['all']
    # going through the regexpList 
    for r in regexpList:
        listNames.append(r.name)
    return listNames

def getRegexpsByName(regexpNames = ['all']):
    ''' 
        Method that recovers the names of the <RegexpObject> in a given list.

        :param regexpNames:    list of strings containing the possible regexp.

        :return:    Array of <RegexpObject> classes.
    '''

    allRegexpList = getAllRegexp()
    if 'all' in regexpNames:
        return allRegexpList

    regexpList = []
    # going through the regexpList 
    for name in regexpNames:
        for r in allRegexpList:
            if name == r.name:
                regexpList.append(r)
    return regexpList


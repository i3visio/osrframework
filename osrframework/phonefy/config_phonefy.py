# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of OSRFramework.
#
#	OSRFramework is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import os
import copy
import logging
# Importing Classes of <RegexpObject> objects that will be used in the script. The files are stored in the regexp folder.
# For demo only
#from regexp.demo import Demo
from osrframework.phonefy.listspam import Listspam
# Add any additional import here
#from regexp.anynewregexp import AnyNewRegexp
# <ADD_NEW_REGEXP_IMPORT_BELOW>
# Please, notify the authors if you have written a new regexp.

def getAllPlatforms():
    ''' 
        Method that recovers ALL the list of <Platform> classes to be processed....

        :return:    Returns a list [] of <Platform> objects.
    '''
    logger = logging.getLogger("osrframework.phonefy")

    logger.debug("Recovering all the available <Platform> classes.")
    listAll = []
    # For demo only
    #listAll.append(Demo())
    listAll.append(Listspam())
    # Add any additional import here
    #listAll.append(AnyNewRegexp)
    # <ADD_NEW_PLATFORM_TO_THE_LIST>
    # Please, notify the authors if you have written a new regexp.

    logger.debug("Returning a list of " + str(len(listAll)) + " <Platform> classes.")
    return listAll

def getPlatformNames(platList = None):
    ''' 
        Method that recovers the names of the <Platform> in a given list.

        :param platList:    list of <Platform> objects. If None, all the available <Platform> will be recovered.

        :return:    Array of strings containing the available regexps.
    '''
    if platList == None:
        platList = getAllPlatforms()
    listNames = ['all']
    # going through the platList 
    for r in platList:
        listNames.append(str.lower(r.platformName))
    return listNames

def getPlatformsByName(platformNames = ['all']):
    ''' 
        Method that recovers the names of the <Platforms> in a given list.

        :param platformNames:    list of strings containing the possible platforms.

        :return:    Array of <Platforms> classes.
    '''

    allPlatformsList = getAllPlatforms()
    if 'all' in platformNames:
        return allPlatformsList

    platformList = []
    # going through the regexpList 
    for name in platformNames:
        for plat in allPlatformsList:
            if name == plat.platformName:
                platformList.append(plat)
    return platformList


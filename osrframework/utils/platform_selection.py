# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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

import osrframework.utils.credentials as credentials

##################################################
##################################################
from osrframework.wrappers.listspam import Listspam
from osrframework.wrappers.twitter import Twitter
##################################################
##################################################


def getAllPlatformNames(mode):
    ''' 
        Method that defines the whole list of available parameters.
        
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

        Return values:
            Returns a list [] of strings for the platform objects.
    '''
    # Recovering all the possible platforms installed
    allPlatforms = getAllPlatformObjects(mode=mode)
    # Defining the platOptions
    platOptions = []
    for p in allPlatforms:
        try:
            # E. g.: to use wikipedia instead of wikipedia_ca and so on
            parameter = p.parameterName
        except:
            parameter = p.platformName.lower()
        
        if parameter not in platOptions:
            platOptions.append(parameter)
    platOptions =  sorted(set(platOptions))
    platOptions.insert(0, 'all')
    return platOptions


def getPlatformsByName(platformNames = ['all'], mode = None, tags = []):
    ''' 
        Method that recovers the names of the <Platforms> in a given list.
        
        :param platformNames:    list of strings containing the possible platforms.
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        :param tags:    Just in case the method to select the candidates is a series of tags.
        :return:    Array of <Platforms> classes.
    '''

    allPlatformsList = getAllPlatformObjects(mode)
    
    if 'all' in platformNames:
        return allPlatformsList

    platformList = []
    # going through the regexpList 
    for name in platformNames:
        for plat in allPlatformsList:
            added = False
            # Verifying if the parameter was provided
            if name == str(plat.platformName).lower():
                platformList.append(plat)
                added = True
                break	
            # Verifying if any of the platform tags match the original tag
            if not added:
                for t in plat.tags:
                    if t in tags:
                        platformList.append(plat)
                        break	                
    return platformList      


def getAllPlatformObjects(mode = None):
    ''' 
        Method that recovers ALL the list of <Platform> classes to be processed....

        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        
        :return:    Returns a list [] of <Platform> objects.
    '''
    listAll = []
    ##################################################
    ##################################################
    listAll.append(Listspam())
    listAll.append(Twitter())
    ##################################################
    ##################################################

    creds = credentials.getCredentials()

    for p in listAll:
        # Verify if there are credentials to be loaded
        if p.platformName.lower() in creds.keys():
            p.setCredentials(creds[p.platformName.lower()])    
    
    if mode == None:
        return listAll
    else:
        # We are returning only those platforms which are required by the mode.
        selected = []
        for p in listAll:
            if p.isValidMode[mode]:
                selected.append(p)
        return selected
        
  
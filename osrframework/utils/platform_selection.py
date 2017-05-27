# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2014-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import os
import sys

import pkgutil
import importlib
import inspect
import osrframework.wrappers

import osrframework.utils.credentials as credentials
import osrframework.utils.configuration as configuration
import osrframework


def getAllPlatformNames(mode):
    """Method that defines the whole list of available parameters.

        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

        Return values:
            Returns a list [] of strings for the platform objects.
    """
    # Recovering all the possible platforms installed
    platOptions = []
    if mode in ["phonefy", "usufy", "searchfy"]:
        allPlatforms = getAllPlatformObjects(mode=mode)
        # Defining the platOptions
        for p in allPlatforms:
            try:
                # E. g.: to use wikipedia instead of wikipedia_ca and so on
                parameter = p.parameterName
            except:
                parameter = p.platformName.lower()

            if parameter not in platOptions:
                platOptions.append(parameter)
    elif mode == "domainfy":
        platOptions = osrframework.domainfy.TLD.keys()
    elif mode == "mailfy":
        platOptions = osrframework.mailfy.EMAIL_DOMAINS

    platOptions =  sorted(set(platOptions))
    platOptions.insert(0, 'all')
    return platOptions


def getPlatformsByName(platformNames=['all'], mode=None, tags=[], excludePlatformNames=[]):
    """Method that recovers the names of the <Platforms> in a given list.

        :param platformNames:    List of strings containing the possible platforms.
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        :param tags:    Just in case the method to select the candidates is a series of tags.
        :param excludePlatformNames:    List of strings to be excluded from the search.
        :return:    Array of <Platforms> classes.
    """

    allPlatformsList = getAllPlatformObjects(mode)

    platformList = []

    # Tags has priority over platform
    if "all" in platformNames and len(tags) == 0:
        # Last condition: checking if "all" has been provided
        for plat in allPlatformsList:
            if str(plat.platformName).lower() not in excludePlatformNames:
                platformList.append(plat)
        return platformList
    else:
        # going through the regexpList
        for name in platformNames:
            if name not in excludePlatformNames:
                for plat in allPlatformsList:
                    # Verifying if the parameter was provided
                    if name == str(plat.platformName).lower():
                        platformList.append(plat)
                        break

                    # We need to perform additional checks to verify the Wikipedia platforms, which are called with a single parameter
                    try:
                        if name == str(plat.parameterName).lower():
                            platformList.append(plat)
                            break
                    except:
                        pass

                    # Verifying if any of the platform tags match the original tag
                    for t in plat.tags:
                        if t in tags:
                            platformList.append(plat)
                            break
    # If the platformList is empty, we will return all
    if platformList == []:
        return allPlatformsList
    else:
        return platformList

def getAllPlatformNamesByTag (mode = None):
    """Returns the platforms in the framework grouped by tags.
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
    """
    tags = {}

    allPlatformsList = getAllPlatformObjects(mode)

    # Iterating the list of platforms to collect the tags
    for plat in allPlatformsList:
        # Grabbing the tags and providing them
        for t in plat.tags:
            if t not in tags.keys():
                tags[t] = [str(plat)]
            else:
                tags[t].append(str(plat))

    return tags


def getAllPlatformObjects(mode = None):
    """Method that recovers ALL the list of <Platform> classes to be processed....

        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

        :return:    Returns a list [] of <Platform> objects.
    """

    listAll = []

    ############################################################################
    ############################################################################

    # --------------------------------------------------------------------------
    # Dinamically collecting all the "official" modules
    # --------------------------------------------------------------------------

    # A list that will contain all of the module names
    all_modules = []

    # Grabbing all the module names
    for _, name, _ in pkgutil.iter_modules(osrframework.wrappers.__path__):
        all_modules.append("osrframework.wrappers." + name)

    # Iterating through all the module names to grab them
    for moduleName in all_modules:
        # Importing the module
        my_module = importlib.import_module(moduleName)

        # Getting all the classNames.
        classNames = [m[0] for m in inspect.getmembers(my_module, inspect.isclass) if m[1].__module__ == moduleName]

        # Dinamically grabbing the first class of the module. IT SHOULD BE ALONE!
        MyClass = getattr(my_module, classNames[0])

        # Instantiating the object
        newInstance = MyClass()

        # Adding to the list!
        listAll.append(newInstance)

    # --------------------------------------------------------------------------
    # Loading user-defined wrappers under [OSRFrameworkHOME]/plugins/wrappers/
    # --------------------------------------------------------------------------

    # Creating the application paths
    paths = configuration.getConfigPath()

    newPath = os.path.abspath(paths["appPathWrappers"])

    # Inserting in the System Path
    if not newPath in sys.path:
        sys.path.append(newPath)

    userImportedModules = {}

    for module in os.listdir(newPath):
        if module[-3:] == '.py':
            current = module.replace('.py', '')
            userImportedModules[current] = __import__(current)

    del newPath

    userClasses = []

    # Iterating through all the files
    for userModule in userImportedModules.keys():

        my_module = userImportedModules[userModule]
        # Getting all the classNames.
        classNames = [m[0] for m in inspect.getmembers(my_module, inspect.isclass) if m[1].__module__ == userModule]

        # Dinamically grabbing the first class of the module. IT SHOULD BE ALONE!
        MyClass = getattr(my_module, classNames[0])

        # Instantiating the object
        newInstance = MyClass()

        # Adding to the list!
        userClasses.append(newInstance)

    # --------------------------------------------------------------------------
    # Overwriting original modules with the user plugins
    # --------------------------------------------------------------------------
    listToAdd = []
    for userClass in userClasses:
        overwritten = False
        for i, officialClass in enumerate(listAll):
            # Checking if the name is the same
            if str(userClass) == str(officialClass):
                # Replacing the official module if a user module exists for it
                listAll[i] = userClass
                # We stop iterating this loop
                overwritten = True
                break
        if not overwritten:
            # Appending the new class
            listToAdd.append(userClass)

    # Merging listAll and listToAdd
    listAll = listAll + listToAdd
    ############################################################################
    ############################################################################

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

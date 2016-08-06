# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import os
import sys

import pkgutil
import importlib
import inspect

import copy

import osrframework.patterns
import osrframework.utils.configuration as configuration

def getAllRegexp():
    '''
        Method that recovers ALL the list of <RegexpObject> classes to be processed....

        :return:    Returns a list [] of <RegexpObject> classes.
    '''

    listAll = []

    ############################################################################
    ############################################################################

    # --------------------------------------------------------------------------
    # Dinamically collecting all the "official" modules
    # --------------------------------------------------------------------------

    # A list that will contain all of the module names
    all_modules = []

    # Grabbing all the module names
    for _, name, _ in pkgutil.iter_modules(osrframework.patterns.__path__):
        all_modules.append("osrframework.patterns." + name)

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
    # Loading user-defined wrappers under [OSRFrameworkHOME]/plugins/patterns/
    # --------------------------------------------------------------------------

    # Creating the application paths
    paths = configuration.getConfigPath()

    newPath = os.path.abspath(paths["appPathPatterns"])

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
        for i, officialClass in enumerate(listAll):
            # Checking if the name is the same
            if str(userClass) == str(officialClass):
                # Replacing the official module if a user module exists for it
                listAll[i] = userClass
            else:
                if userClass not in listToAdd:
                    # Appending the new class
                    listToAdd.append(userClass)

    # Merging listAll and listToAdd
    listAll = listAll + listToAdd
    ############################################################################
    ############################################################################

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

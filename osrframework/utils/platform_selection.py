################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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


def get_all_platform_names(mode):
    """Method that defines the whole list of available parameters

    Args:
        mode (str): The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

    Returns:
        list. Returns a list [] of strings for the platform objects.
    """
    # Recovering all the possible platforms installed
    plat_options = []
    if mode in ["phonefy", "usufy", "searchfy", "mailfy"]:
        all_platforms = get_all_platform_objects(mode=mode)
        # Defining the plat_options
        for p in all_platforms:
            try:
                # E. g.: to use wikipedia instead of wikipedia_ca and so on
                parameter = p.parameter_name
            except:
                parameter = p.platformName.lower()

            if parameter not in plat_options:
                plat_options.append(parameter)
    elif mode == "domainfy":
        plat_options = osrframework.domainfy.TLD.keys()

    plat_options = sorted(set(plat_options))
    plat_options.insert(0, 'all')
    return plat_options


def get_platforms_by_name(platform_names=['all'], mode=None, tags=[], exclude_platform_names=[]):
    """Method that recovers the names of the <Platforms> in a given list

    Args:
        platform_names (list): List of strings containing the possible platforms.
        mode (str): The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        tags (list): Just in case the method to select the candidates is a series of tags.
        exclude_platform_names (list): List of strings to be excluded from the search.

    Returns:
        list. Array of <Platforms> classes.
    """
    all_platforms_list = get_all_platform_objects(mode)

    platform_list = []

    # Tags has priority over platform
    if "all" in platform_names and len(tags) == 0:
        # Last condition: checking if "all" has been provided
        for plat in all_platforms_list:
            if str(plat.platformName).lower() not in exclude_platform_names:
                platform_list.append(plat)
        return platform_list
    else:
        # going through the regexpList
        for name in platform_names:
            if name not in exclude_platform_names:
                for plat in all_platforms_list:
                    # Verifying if the parameter was provided
                    if name == str(plat.platformName).lower():
                        platform_list.append(plat)
                        break

                    # We need to perform additional checks to verify the Wikipedia platforms, which are called with a single parameter
                    try:
                        if name == str(plat.parameter_name).lower():
                            platform_list.append(plat)
                            break
                    except:
                        pass

                    # Verifying if any of the platform tags match the original tag
                    for t in plat.tags:
                        if t in tags:
                            platform_list.append(plat)
                            break
    # If the platform_list is empty, we will return all
    if platform_list == []:
        return all_platforms_list
    else:
        return platform_list


def get_all_platform_names_by_tag (mode = None):
    """Returns the platforms in the framework grouped by tags

    Args:
        mode (str): The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

    Returns:
        list.
    """
    tags = {}

    all_platforms_list = get_all_platform_objects(mode)

    # Iterating the list of platforms to collect the tags
    for plat in all_platforms_list:
        # Grabbing the tags and providing them
        for t in plat.tags:
            if t not in tags.keys():
                tags[t] = [str(plat)]
            else:
                tags[t].append(str(plat))

    return tags


def get_all_platform_objects(mode=None):
    """Method that recovers ALL the list of <Platform> classes to be processed

    The method dinamically loads all the wrappers stored under [OSRFrameworkHOME]/plugins/wrappers/.

    Args:
        mode (str):The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

    Returns:
        Returns a list [] of <Platform> objects.
    """
    list_all = []

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
    for module_name in all_modules:
        # Importing the module
        my_module = importlib.import_module(module_name)

        # Getting all the classNames.
        classNames = [m[0] for m in inspect.getmembers(my_module, inspect.isclass) if m[1].__module__ == module_name]

        # Dinamically grabbing the first class of the module. IT SHOULD BE ALONE!
        MyClass = getattr(my_module, classNames[0])

        # Instantiating the object
        new_instance = MyClass()

        # Adding to the list!
        list_all.append(new_instance)

    # --------------------------------------------------------------------------
    # Loading user-defined wrappers under [OSRFrameworkHOME]/plugins/wrappers/
    # --------------------------------------------------------------------------

    # Creating the application paths
    paths = configuration.get_config_path()

    new_path = os.path.abspath(paths["appPathWrappers"])

    # Inserting in the System Path
    if not new_path in sys.path:
        sys.path.append(new_path)

    user_imported_modules = {}

    for module in os.listdir(new_path):
        if module[-3:] == '.py':
            current = module.replace('.py', '')
            user_imported_modules[current] = __import__(current)

    del new_path

    user_classes = []

    # Iterating through all the files
    for userModule in user_imported_modules.keys():

        my_module = user_imported_modules[userModule]
        # Getting all the classNames.
        classNames = [m[0] for m in inspect.getmembers(my_module, inspect.isclass) if m[1].__module__ == userModule]

        # Dinamically grabbing the first class of the module. IT SHOULD BE ALONE!
        MyClass = getattr(my_module, classNames[0])

        # Instantiating the object
        new_instance = MyClass()

        # Adding to the list!
        user_classes.append(new_instance)

    # --------------------------------------------------------------------------
    # Overwriting original modules with the user plugins
    # --------------------------------------------------------------------------
    list_to_add = []

    for user_class in user_classes:
        overwritten = False
        for i, official_class in enumerate(list_all):
            # Checking if the name is the same
            if str(user_class) == str(official_class):
                # Replacing the official module if a user module exists for it
                list_all[i] = user_class
                # We stop iterating this loop
                overwritten = True
                break
        if not overwritten:
            # Appending the new class
            list_to_add.append(user_class)

    # Merging list_all and list_to_add
    list_all = list_all + list_to_add
    ############################################################################
    ############################################################################

    creds = credentials.get_credentials()

    for p in list_all:
        # Verify if there are credentials to be loaded
        if p.platformName.lower() in creds.keys():
            p.setCredentials(creds[p.platformName.lower()])

    if mode is None:
        return list_all
    else:
        # We are returning only those platforms which are required by the mode.
        selected = []
        for p in list_all:
            if p._mode_is_valid(mode):
                selected.append(p)
        return selected

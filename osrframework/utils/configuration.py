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

from configparser import ConfigParser

import osrframework.utils.errors as errors


def change_permissions_recursively(path, uid, gid):
    """Function to recursively change the user id and group id

    It sets 700 permissions in the different files.
    """
    os.chown(path, uid, gid)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception as e:
                # If this crashes it may be because we are running the
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 600)
        elif os.path.isdir(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception as e:
                # If this crashes it may be because we are running the
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 6600)
            # Recursive function to iterate the files
            change_permissions_recursively(itempath, uid, gid)


def get_config_path(config_file_name=None):
    """Auxiliar function to get the configuration paths depending on the system

    Args:
        config_file_name (str): Filepath to the configuration file.

    Returns:
        A dictionary with the following keys: appPath, appPathDefaults,
            appPathTransforms, appPathPlugins, appPathPatterns, appPathPatterns.
    """
    paths = {}
    application_path = "./"

    # Returning the path of the configuration folder
    if sys.platform == 'win32':
        application_path = os.path.expanduser(os.path.join('~\\', 'OSRFramework'))
    else:
        application_path = os.path.expanduser(os.path.join('~/', '.config', 'OSRFramework'))

    # Defining additional folders
    paths = {
        "appPath": application_path,
        "appPathData": os.path.join(application_path, "data"),
        "appPathDefaults": os.path.join(application_path, "default"),
        "appPathPlugins": os.path.join(application_path, "plugins"),
        "appPathWrappers": os.path.join(application_path, "plugins", "wrappers"),
    }

    # Creating them if they don't exist
    for path in paths.keys():
        if not os.path.exists(paths[path]):
            os.makedirs(paths[path])

    return paths


def get_configuration_values_for(util):
    """Method that recovers the configuration information about each program

    Args:
        util: Any of the utils that are contained in the framework: checkfy,
            domainfy, entify, mailfy, phonefy, searchfy, usufy.

    Returns:
        A dictionary containing the default configuration.
    """

    VALUES = {}

    # If a api_keys.cfg has not been found, creating it by copying from default
    configPath = os.path.join(get_config_path()["appPath"], "general.cfg")

    # Checking if the configuration file exists
    if not os.path.exists(configPath):
        # Copy the data from the default folder
        defaultConfigPath = os.path.join(get_config_path()["appPathDefaults"], "general.cfg")

        try:
            # Recovering default file
            with open(defaultConfigPath) as iF:
                cont = iF.read()
                # Moving its contents as the default values
                with open(configPath, "w") as oF:
                    oF.write(cont)
        except Exception as e:
            raise errors.DefaultConfigurationFileNotFoundError(configPath, defaultConfigPath);

    # Reading the configuration file
    config = ConfigParser()
    config.read(configPath)

    LISTS = ["tlds", "domains", "platforms", "extension", "exclude_platforms", "exclude_domains"]

    # Iterating through all the sections, which contain the platforms
    for section in config.sections():
        incomplete = False
        if section.lower() == util.lower():
            # Iterating through parameters
            for (param, value) in config.items(section):
                if value == '':
                    # Manually setting an empty value
                    if param in LISTS:
                        value = []
                    else:
                        value = ""
                # Splitting the parameters to create the arrays when needed
                elif param in LISTS:
                    value = value.split(' ')
                # Converting threads to int
                elif param == "threads":
                    try:
                        value = int(value)
                    except Exception as err:
                        raise errors.ConfigurationParameterNotValidError(configPath, section, param, value)
                elif param == "debug":
                    try:
                        if int(value) == 0:
                            value = False
                        else:
                            value = True
                    except Exception as err:
                        print("Something happened when processing this debug option. Resetting to default.")
                        # Copy the data from the default folder
                        defaultConfigPath = os.path.join(get_config_path()["appPathDefaults"], "general.cfg")

                        try:
                            # Recovering default file
                            with open(defaultConfigPath) as iF:
                                cont = iF.read()
                                # Moving its contents as the default values
                                with open(configPath, "w") as oF:
                                    oF.write(cont)
                        except Exception as e:
                            raise errors.DefaultConfigurationFileNotFoundError(configPath, defaultConfigPath);

                        #raise errors.ConfigurationParameterNotValidError(configPath, section, param, value)
                VALUES[param] = value
            break

    return VALUES

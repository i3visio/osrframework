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

from configparser import ConfigParser
import os

import osrframework.utils.configuration as configuration
import osrframework.utils.errors as errors


def get_list_of_api_keys():
    """Return list of API keys

    Return:
        A dictionary containing the API Keys stored in a dictionary depending
            on the information required by each platform.
    """

    dict_api_keys = {}

    # If a api_keys.cfg has not been found, creating it by copying from default
    config_path = os.path.join(configuration.get_config_path()["appPath"], "api_keys.cfg")

    # Checking if the configuration file exists
    if not os.path.exists(config_path):
        # Copy the data from the default folder
        default_config_path = os.path.join(configuration.get_config_path()["appPathDefaults"], "api_keys.cfg")

        try:
            with open(default_config_path) as file:
                cont = file.read()
                with open(config_path, "w") as output_file:
                    output_file.write(cont)
        except Exception as e:
            raise errors.ConfigurationFileNotFoundError(config_path, default_config_path);
            return dict_api_keys

    # Reading the configuration file
    config = ConfigParser()
    config.read(config_path)

    # Iterating through all the sections, which contain the platforms
    for platform in config.sections():
        # Initializing values
        platform_api = {}

        incomplete = False

        # Iterating through parametgers
        for (param, value) in config.items(platform):
            if value == '':
                incomplete = True
                break
            platform_api[param] = value

        # Loading the info in the dict
        if not incomplete:
            dictAPIeys[platform] = platform_api

    return dict_api_keys

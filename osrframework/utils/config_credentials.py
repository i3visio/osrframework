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


def get_list_of_credentials():
    """Return list of credentials taken from configuration files

    Returns:
        list. A list of tuples containing in the first the name of the platform,
            as read from the accounts.cfg file in the application folder. E. g.:

            list_creds.append(("<platform>", "<username>", "<password>"))
    """
    list_creds = []
    # If a accounts.cfg has not been found, creating it by copying from default
    config_path = os.path.join(configuration.get_config_path()["appPath"], "accounts.cfg")

    # Checking if the configuration file exists
    if not os.path.exists(config_path):
        # Copy the data from the default folder
        default_config_path = os.path.join(configuration.get_config_path()["appPathDefaults"], "accounts.cfg")

        try:
            with open(default_config_path) as file:
                cont = file.read()
                with open(config_path, "w") as output_file:
                    output_file.write(cont)
        except Exception as e:
            raise errors.ConfigurationFileNotFoundError(config_path, default_config_path);
            return list_creds

    # Reading the configuration file
    config = ConfigParser()
    config.read(config_path)

    # Iterating through all the sections, which contain the platforms
    for platform in config.sections():
        # Initializing values
        creds = {}

        incomplete = False

        # Iterating through parametgers
        for (param, value) in config.items(platform):
            if value == '':
                incomplete = True
                break
            creds[param] = value

        # Appending credentials if possible
        try:
            if not incomplete:
                list_creds.append((platform, creds["login"], creds["password"]))
        except Exception:
            pass

    return list_creds

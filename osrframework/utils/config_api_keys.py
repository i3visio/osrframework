# !/usr/bin/python
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

import ConfigParser
import os

import osrframework.utils.configuration as configuration
import osrframework.utils.errors as errors

def returnListOfAPIKeys():
    '''
        :return: A dictionary containing the API Keys stored in a dictionary depending on the information required by each platform
    '''

    dictAPIKeys = {}

    # If a api_keys.cfg has not been found, creating it by copying from default
    configPath = os.path.join(configuration.getConfigPath()["appPath"], "api_keys.cfg")

    # Checking if the configuration file exists
    if not os.path.exists(configPath):
        # Copy the data from the default folder
        defaultConfigPath = os.path.join(configuration.getConfigPath()["appPathDefaults"], "api_keys.cfg")
        
        try:
            with open(defaultConfigPath) as iF:
                cont = iF.read()
                with open(configPath, "w") as oF:
                    oF.write(cont)
        except Exception, e:
            raise errors.ConfigurationFileNotFoundError(configPath, defaultConfigPath);
            return dictAPIKeys

    # Reading the configuration file
    config = ConfigParser.ConfigParser()
    config.read(configPath)

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
            dictAPIKeys[platform] = platform_api

    return dictAPIKeys

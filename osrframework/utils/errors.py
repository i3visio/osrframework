# !/usr/bin/python
# -*- coding: utf-8 -*-
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

class Error(Exception):
    """Base class for exceptions in this module.

    Attributes:
        reason -- Defines what has just happened
        steps -- Defines what the user can do to solve this
        post -- Additional information on how to report the bug
    """

    def __init__(self, reason="OSRFramework Generic Error.", steps = "No more information here. Just have a look at the code :(."):
        self.reason = reason
        self.steps = steps
        self.post = "If you need more information on how to solve this, copy this information and ask us by placing an issue at <https://github.com/i3visio/osrframework/issues>."

    def __str__(self):
        return "\n\t- Oh! What's happening? > " + self.reason + "\n\t- How can I solve this? > " + self.steps + "\n\t- This is not enough... > " + self.post

class DefaultConfigurationFileNotFoundError(Error):
    """Exception raised when a given configuration file is not found.

    Attributes:
        fileName -- input expression in which the error occurred
        defaultPath  -- the path where the default files should be found
    """
    def __init__(self, fileName, defaultPath):
        reason = "The configuration file " +  fileName +  " could not be found. The system tried to get the files provided by default with OSRFramework but they were not found either."
        steps = "Check if the configuration path exists or if it is accesible by the current user. You should be able to find the default configuration files at '" + defaultPath + "'. If they are not there, try to solve this by reinstalling OSRFramework again for this user."
        Error.__init__(self, reason, steps)

class ConfigurationParameterNotValidError(Error):
    """Exception raised when a given parameter is not valid for this option.

    Attributes:
        configurationFilePath -- path to the configuration file
        application -- the application that had the problem
        parameter -- the parameter that was not properly configured
        value --  the value to be changed
    """
    def __init__(self, configurationFilePath, application, parameter, value):
        reason = "The following parameter in " +  application +  " was misconfigured: " + parameter + " = " + str(value)
        steps = "You can go to the configuration file stored at '" + configurationFilePath + "' and update it accordingly by using the examples provided in the commented lines. In any case, you can always use the backup configuration files provided with the framework."
        Error.__init__(self, reason, steps)

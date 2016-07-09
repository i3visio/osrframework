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

import os
import sys

def changePermissionsRecursively(path, uid, gid):
    """
        Function to recursively change the user id and group id. It sets 700 
        permissions.
    """
    os.chown(path, uid, gid)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception, e:
                # If this crashes it may be because we are running the 
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 0600) 
        elif os.path.isdir(itempath):
            # Setting owner
            try:
                os.chown(itempath, uid, gid)
            except Exception, e:
                # If this crashes it may be because we are running the 
                # application in Windows systems, where os.chown does NOT work.
                pass
            # Setting permissions
            os.chmod(itempath, 6600)             
            # Recursive function to iterate the files
            changePermissionsRecursively(itempath, uid, gid)

def getConfigPath(configFileName = None):
    """
        Auxiliar function to get the configuration paths depending on the system.
        
        Returns a dictionary with the following keys: appPath, appPathDefaults, appPathTransforms, appPathPlugins, appPathPatterns, appPathPatterns.
    """
    paths = {}
    applicationPath = "./"
    

    # Returning the path of the configuration folder
    if sys.platform == 'win32':
        applicationPath = os.path.expanduser(os.path.join('~\\', 'OSRFramework'))
    else:
        applicationPath = os.path.expanduser(os.path.join('~/', '.config', 'OSRFramework'))

    # Defining additional folders
    paths = {
        "appPath": applicationPath,
        "appPathDefaults": os.path.join(applicationPath, "default"),
        "appPathTransforms": os.path.join(applicationPath, "transforms"),
        "appPathPlugins": os.path.join(applicationPath, "plugins"),
        "appPathWrappers": os.path.join(applicationPath, "plugins", "wrappers"),
        "appPathPatterns": os.path.join(applicationPath, "plugins", "patterns"),
    }
    
    # Creating them if they don't exist 
    for path in paths.keys():
        if not os.path.exists(paths[path]):
            os.makedirs(paths[path]) 

    return paths

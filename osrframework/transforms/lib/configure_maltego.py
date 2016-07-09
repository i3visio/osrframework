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
import zipfile
import argparse
import shutil, errno

import osrframework
import osrframework.utils.configuration as configuration

VERSION = "v0.10"

def copyAnything(src="./osrframework-maltego-settings", dst=os.path.join("./", "tmp", "osrframework-maltego-settings") ):
    '''
        :param src: Source folder.
        :param dst: Destination folder.
    '''
    # first of all trying to delete the folder
    try:
        shutil.rmtree(dst)    
    except:
        pass
    
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def setNewPath(iPath=None, dst=None):
    '''
        :param iPath:   The new installation path where the transforms will be searched. Concretely, the configuration folder.
        :param dst:     Path where the files have been copied.
    '''
    pathFolder = dst + "/TransformRepositories/Local"
    for file in os.listdir( pathFolder):
        if file.endswith("transformsettings") or file.endswith("transform"):
            cont = ""
            # reading the contents of such file
            with open(os.path.join(pathFolder, file), "r") as iF:
                cont = iF.read()
            # replacing the working directory
            cont = cont.replace("<CUSTOM_WORKING_DIRECTORY>", iPath)
            # Writing the output
            with open(os.path.join(pathFolder, file), "w") as oF:
                oF.write(cont)

def setDebugMode(dst=None, debug="false"):
    '''
        :param dst:     Path where the files have been copied.
        :param debug:     Whether the transforms will be launched in debug mode.
    '''
    pathFolder = dst + "/TransformRepositories/Local"
    for file in os.listdir( pathFolder):
        if file.endswith("transformsettings") or file.endswith("transform"):
            cont = ""
            # reading the contents of such file
            with open(os.path.join(pathFolder, file), "r") as iF:
                cont = iF.read()
            # replacing the working directory
            cont = cont.replace('<Property name="transform.local.debug" type="boolean" popup="false"><DEBUG_MODE></Property>','<Property name="transform.local.debug" type="boolean" popup="false">'+ debug + '</Property>')
            # Writing the output
            with open(os.path.join(pathFolder, file), "w") as oF:
                oF.write(cont)

def zip(pathFolder=None):
    '''
        Zipping a file onto a mtz file.
        
        :param pathFolder: Source folder or files.
    '''
    filePath =  "%s.mtz" % (pathFolder)
    
    zf = zipfile.ZipFile(filePath, "w", zipfile.ZIP_DEFLATED)

    abs_src = os.path.abspath(pathFolder)
    for dirname, subdirs, files in os.walk(pathFolder):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            #print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
            zf.write(absname, arcname)
    zf.close()
    
    # After everything, deleting the previously created folder
    try:
        shutil.rmtree(pathFolder)    
    except:
        pass

    return filePath

def configureMaltego(transformsConfigFolder = None, base=None, wFolder=None, debug=False, mainPath = os.path.expanduser('~/'), backupPath = None):
    '''
    '''
    # Defining the name of the output file
    settingsFile = "osrframework-maltego-settings"  + "_" + VERSION 

    # Defining the full path to the folder in which the configuration files will be created
    dst=os.path.join("./", "tmp", settingsFile)    

    # copying anything in the config folder
    copyAnything(src=base, dst=dst)

    print "Configuring OSRFramework working directory for Maltego..."
    # Setting the new path for 
    setNewPath(iPath = transformsConfigFolder, dst=dst)
    
    # Setting the new path for 
    setDebugMode(dst=dst, debug=str(debug).lower())    
    
    print "Building the .mtz file."
    # Zipping the new configuration
    filePath = zip(pathFolder=dst)

    folder, fileName = os.path.split(filePath)

    # Make copies of the file
    if mainPath != None:
        print "Moving the .mtz file to the following folder: " + os.path.join(mainPath, fileName)
        shutil.copy2(filePath, mainPath)
       
    if backupPath != None:
        print "Moving the .mtz file to the backup folder:    " + os.path.join(backupPath, fileName)
        shutil.copy2(filePath, backupPath)        
       
    # Remove tmp files.
    #shutil.rmtree(os.path.join("./", "tmp"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='configure_maltego.py - A function to automatically generate Maltego configuration files.', prog='configure_maltego.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-b', '--base', metavar='<path>', action='store', help="name of the base folder.", required=False, default="./osrframework-maltego-settings[Base]")                        
    parser.add_argument('-d', '--debug', action='store_true', help="storing the value of whether the transforms will be displaying a debug window when launched.", default=False, required=False)
    parser.add_argument('-o', '--output', action='store_true', help="Path where the files will be copied.", default=False, required=False)    

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version=VERSION, help='shows the version of the program and exists.')
    
    args = parser.parse_args()        

    # Creating the application paths
    paths = configuration.getConfigPath()
    
    configureMaltego(transformsConfigFolder = paths["appPathTransforms"], base=args.base, debug = args.debug, backupPath = paths["applicationPathDefaults"])

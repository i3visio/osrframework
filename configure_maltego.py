# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

#!/usr/bin/env python2.7

import os
import zipfile
import argparse
import shutil, errno

def copyAnything(src="./i3visio-[Base]", dst="./i3visio-[Personal]"):
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
        :param iPath:   The new installation path where the transforms will be searched.
        :param dst:     Path where the files have being copied.
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
        :param dst:     Path where the files have being copied.
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
    zf = zipfile.ZipFile("%s.mtz" % (pathFolder), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(pathFolder)
    for dirname, subdirs, files in os.walk(pathFolder):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()
    
    # After everything, deleting the previously created folder
    try:
        shutil.rmtree(pathFolder)    
    except:
        pass

def configureMaltego(base=None, iPath=None, personal=None, wFolder=None, debug=False):
    '''
    '''
    # copying anything in the config folder
    copyAnything(src=os.path.join(wFolder,base), dst=os.path.join(wFolder,personal))
    
    # Setting the new path for 
    setNewPath(iPath = iPath, dst=os.path.join(wFolder,personal))

    # Setting the new path for 
    setDebugMode(dst=os.path.join(wFolder,personal), debug=str(debug).lower())    
    
    # Zipping the new configuration
    zip(pathFolder=wFolder+personal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='configure_maltego.py - A function to automatically generate Maltego configuration files.', prog='configure_maltego.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-b', '--base', metavar='<path>', action='store', help="name of the base folder.", required=False, default="i3visio-[Base]")            
    parser.add_argument('-i', '--installation_folder', metavar='<path>', action='store', help="path to wherever this framework is installed. By default, this folder.", required=False, default = os.getcwd())
    parser.add_argument('-p', '--personal', metavar='<name>', action='store', help="name of the destiny's name for the configuration file.", default="i3visio-[Personal]", required=False)                
    parser.add_argument('-d', '--debug', action='store_true', help="storing the value of whether the transforms will be displaying a debug window when launched.", default=False, required=False)        
    parser.add_argument('-w', '--working_folder', metavar='<path>', action='store', help="path to the working folder.", default="./osrframework/transforms/lib/", required=False)                    
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.1', help='shows the version of the program and exists.')
    
    args = parser.parse_args()        
    
    configureMaltego(base=args.base, iPath = args.installation_folder, personal = args.personal, wFolder = args.working_folder, debug = args.debug)

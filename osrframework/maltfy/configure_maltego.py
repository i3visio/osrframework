# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

#!/usr/bin/env python2.7

import os
import zipfile
import argparse
import shutil, errno

def copyanything(src="./i3visio-v0.7.0a[Base]", dst="./i3visio-v0.7.0a[Personal]"):
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

def setNewPath(newPath, dst):
    '''
        :param newPath: New path is the folder of the transforms.
    '''
    pathFolder = "./" + dst + "/TransformRepositories/Local"
    for file in os.listdir("./" + dst + "/TransformRepositories/Local"):
        if file.endswith("settings"):
            cont = ""
            # reading the contents of such file
            with open(os.path.join(pathFolder, file), "r") as iF:
                cont = iF.read()
            # replacing the working directory
            cont = cont.replace("<CUSTOM_WORKING_DIRECTORY>", newPath)
            # Writing the output
            with open(os.path.join(pathFolder, file), "w") as oF:
                oF.write(cont)

def zip(folder):
    '''
        Zipping a file onto a mtz file.
        
        :param folder: Source folder or files.
    '''
    zf = zipfile.ZipFile("%s.mtz" % (folder), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(folder)
    for dirname, subdirs, files in os.walk(folder):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()
    
    # After everything, deleting the previously created folder
    try:
        shutil.rmtree(folder)    
    except:
        pass

def configureMaltego(defaultConfig, dstName, baseFolder):
    '''
    '''
    # copying anything in the config folder
    copyanything(src=defaultConfig, dst="./"+dstName)
    
    # Setting the new path for 
    setNewPath(baseFolder, dstName)
    
    # Zipping the new configuration
    zip(folder="./"+dstName)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='configure_maltego.py - A function to automatically generate Maltego configuration files.', prog='configure_maltego.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-c', '--current', metavar='<path>', action='store', help="of the Maltego configuration files.", required=True)
    parser.add_argument('-s', '--src', metavar='<path>', action='store', help="path to the base folder.", required=False, default="./i3visio-v0.7.0a[Base]")        
    parser.add_argument('-d', '--dst', metavar='<name>', action='store', help="name of the destiny's name for the configuration file.", default="i3visio-v0.7.0a[Personal]", required=False)                
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')
    
    args = parser.parse_args()        
    
    configureMaltego(args.src, args.dst, args.current)

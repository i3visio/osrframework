# -*- coding: cp1252 -*-
#
##################################################################################
#
#    OSRFramework is free software: you can redistribute it and/or modify
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


import hashlib
import json
import datetime
from osrframework.maltfy.lib.maltego import MaltegoEntity, MaltegoTransform

import logging

def dictToJson(d):
    '''
        Workaround to convert any dictionary to json text.
        
        :param d:    Dictionary to convert to json.

        :return:    jsonText (string).
    '''
    # creating json
    jsonText =  json.dumps(d, indent=2, sort_keys=True)
    return jsonText

def listToMaltego(profiles):
    """ 
        Method to generate the text to be appended to a Maltego file.

        :param profiles:    a list of dictionaries with the information of the profiles: {"a_nick": [<list_of_results>]}
                    [
                        {
                          "attributes": [
                            {
                              "attributes": [], 
                              "type": "i3visio.uri", 
                              "value": "http://twitter.com/i3visio"
                            }, 
                            {
                              "attributes": [], 
                              "type": "i3visio.alias", 
                              "value": "i3visio"
                            }, 
                            {
                              "attributes": [], 
                              "type": "i3visio.platform", 
                              "value": "Twitter"
                            }
                          ], 
                          "type": "i3visio.profile", 
                          "value": "Twitter - i3visio"
                        }
                        ,
                        ...
                    ]                    
        
        :return:    maltegoText as the string to be written for a Maltego file.                
    """
    logger = logging.getLogger("osrframework.utils")
    logger.info( "Generating Maltego File...")

    maltegoText = ""
    logger.debug("Going through all the keys in the dictionary...")
    me = MaltegoTransform()
    # A dictionary with the structure:

    newEntities = []
    for profile in profiles:
	    # Defining the main entity
        """aux ={}
        aux["type"] = "i3visio.profile"
        aux["value"] =  "Skype - " + str(user["i3visio.alias"])
        aux["attributes"] = []    
                
        # Creation of a temp entity
        aux = {}
        aux["type"] = profile["value"]
        aux["value"] = profile["type"]
        aux["attributes"] = []"""
        newEntities.append(profile)
        
    me.addListOfEntities(newEntities)        
        
    # Getting the output text
    me.addUIMessage("Process completed!")    
    # Returning the output text...
    me.returnOutput()
    return me.getOutput()

def fileToMD5(filename, block_size=256*128, binary=False):
    '''
        :param filename:    Path to the file.
        :param block_size:    Chunks of suitable size. Block size directly depends on the block size of your filesystem to avoid performances issues. Blocks of 4096 octets (Default NTFS).
        :return:    md5 hash.
    '''
    md5 = hashlib.md5()
    with open(filename,'rb') as f: 
        for chunk in iter(lambda: f.read(block_size), b''): 
             md5.update(chunk)
    if not binary:
        return md5.hexdigest()
    return md5.digest()


def getCurrentStrDatetime():
    '''
        Generating the current Datetime with a given format.

        :return:    strTime
    '''
    # Generating current time
    i = datetime.datetime.now()
    strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
    return strTime
    
def getFilesFromAFolder(path):
    '''
        Getting all the files in a folder.
        
        :param path:    path in which looking for files.
        
        :return:    list of filenames.
    '''
    from os import listdir
    from os.path import isfile, join
    #onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    onlyFiles = []
    for f in listdir(path):
        if isfile(join(path, f)):
            onlyFiles.append(f)
    return onlyFiles
    


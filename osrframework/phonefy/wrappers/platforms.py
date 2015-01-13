# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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

import argparse
import json
import re
import sys
import urllib2

import osrframework.utils.browser as browser

class Platform():
    def __init__(self):
        '''
        '''
        self.platformName = "Platform"
        
        # Strings with the URL for each and every mode
        self.url = {}        
        self.url["phonefy"] = "http://anyurl.com/" + "<phonefy>"
        
        # Strings that will imply that the phone number is not appearing
        self.notFoundText = {}
        # List of strings that appear when the phone IS NOT found
        self.notFoundText["phonefy"] = []
        # List of strings that appear when the user IS NOT found
        #self.notFoundText["usufy"] = []        
        
        # Strings to be searched
        self.fieldsRegExp = {}
        # Definition of regualr expressions to be searched in phonefy mode
        self.fieldsRegExp["phonefy"] = {}
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""
        # Definition of regualr expressions to be searched in usufy mode
        #self.fieldsRegExp["phonefy"] = {}
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""
        
    def createURL(self, word, mode="phonefy"):
        ''' 
            Method to create the URL replacing the word in the appropriate URL.
            
            :param word:   Word to be searched.
            :param mode:    Mode to be executed.
            
            :return:    The URL to be queried.
        '''
        try:
            return self.url[mode].replace("<"+mode+">", word)
        except:
            pass
            # TO-DO: BaseURLNotFoundExceptionThrow base URL not found for the mode.
        
    def getInfo(self, query=None, process = False, mode="phonefy"):
        ''' 
            Method that checks the presence of a given telephone in listspam.com and recovers the first list of complains.

            :param query: Phone number to verify.
            :param proces:  Calling the processing function.
            :param mode:    Mode to be executed.            

            :return:    Python structure for the html processed.
        '''
        # Defining variables for this process
        results = {}
        data = ""
        
        if not self.modeIsValid(mode=mode):
            # TO-DO: InvalidModeException
            #print "InvalidModeException"
            return results
            
        try:
            i3Browser = browser.Browser()
            qURL = createURL(word=query, mode=mode)

            # Accessing the resources
            data = i3Browser.recoverURL(qURL)
        except:
            # No information was found, then we return a null entity
            # TO-DO: i3BrowserException            
            #print "i3BrowserException"
            return results            
            
        # Verifying if the platform exists
        if self.somethingFound(data, mode=mode):
            if mode == "phonefy":
                results["type"] = "i3visio.phone"
                results["value"] = self.platformName + " - " + query
            #else:
            #    results["type"] = "i3visio.phone"
            #    results["value"] = self.platformName + " - " + query
            results["attributes"] = []
            
            # Appending platform name
            aux = {}
            aux["type"] = "i3visio.platform"
            aux["value"] = self.platformName
            aux["attributes"] = []
            results["attributes"].append(aux)
            
            # Appending platform name
            aux = {}
            aux["type"] = "i3visio.uri"
            aux["value"] = qURL
            # Iterating if requested to extract more entities from the URI
            if not process:                
                aux["attributes"] = []
            else:
                aux["attributes"] = self.processURI(data=data, mode=mode)
            results["attributes"].append(aux)                
                
        return results

    def modeIsValid(self, mode):
        ''' 
            Verification of whether the mode is a correct option to be used.
            
            :param mode:    Mode to be executed.            
            
            :return:    True if the mode exists in the three main folders.
        '''
        if mode in self.url.keys():
            if mode in self.notFoundText.keys():
                #if mode in self.fieldsRegexp.keys():
                return True
        return False
        
    def processURI(self, uri=None, data = None, mode=None):
        ''' 
            Method to process and extract the entities of a URL of this type.
           
            :param uri: The URI of this platform to be processed.
            :param data: The information from which the info will be extracted. This way, info will not be downloaded twice.
            :param mode:    Mode to be executed.            
                        
            :return:    A list of the entities found.
        '''
        if data == None:
            # Accessing the resource
            data = i3Browser.recoverURL(uri)        

        info = []
        
        # Iterating through all the type of fields
        for field in self.fieldsRegExp[mode].keys():
            # Recovering all the matching expressions
            values = re.findall(fieldsRegExp[mode][field], data)
            
            for val in values:
                aux = {}
                aux["type"] = field
                aux["value"] = val
                aux["attributes"] = []                
                if aux not in info:
                    info.append(aux)        
        return info
    
    def somethingFound(self,data,mode="phonefy"):
        ''' 
            Verifying if something was found.
            
            :param data:    Data where the self.notFoundText will be searched.
            :param mode:    Mode to be executed.            
            
            :return: Returns True if exists.
        '''
        try:
            for text in self.notFoundText[mode]:
                if text in data:
                    return False
            return True
        except:
            pass
            # TO-DO: Throw notFoundText not found for thid mode.        
            

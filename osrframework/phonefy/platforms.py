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
        
        self.basePhoneURL = "http://anyurl.com/" + "<PHONE_NUMBER>"
        
        # Strings that will imply that the phone number is not appearing
        self.notFoundText = [""]
        
        self.fieldsRegExp = {}
        
    def createPhoneURL(self, phone):
        '''
            Method to create the URL replacing the 
            
            :param phone:   Phone to be searched.
            
            :return:    The URL to be queried.
        '''
        return self.basePhoneURL.replace("<PHONE_NUMBER>", phone)

    def doesPhoneExist(self,data):
        '''
            Verifying if the platform exists.
            
            :param data:    Data where the self.notFoundText will be searched.
            
            :return: Returns True if exists.
        '''
        for text in self.notFoundText:
            if text in data:
                return False
        return True
        
    def getPhoneComplains(self, query=None, process = False):
        ''' 
            Method that checks the presence of a given telephone in listspam.com and recovers the first list of complains.

            :param query: Phone number to verify.
            :param proces:  Calling the processing function.

            :return:    Python structure for the html processed.
        '''
        results = {}
        try:
            i3Browser = browser.Browser()
            qURL = createPhoneURL(phone=query)

            # Accessing the resources
            data = i3Browser.recoverURL(qURL)
            
            # Verifying if the platform exists
            if doesPhoneExist(data):
                results["type"] = "i3visio.phone"
                results["value"] = self.platformName + " - " + query
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
                    aux["attributes"] = self.processingURI(data=data)
                results["attributes"].append(aux)                
                
        except:
            # No information was found, then we return a null entity
            pass
        return results
        
    def processingURI(self, uri=None, data = None):
        '''
            Method to process and extract the entities of a URL of this type.
           
            :param uri: The URI of this platform to be processed.
            :param data: The information from which the info will be extracted. This way, info will not be downloaded twice.
            
            :return:    
        '''            
        if data == None:
            # Accessing the resource
            data = i3Browser.recoverURL(uri)        

        info = []
        
        # Iterating thorugh all the type of fields
        for field in self.fieldsRegExp.keys():
            # Recovering all the matching expressions
            values = re.findall(fieldsRegExp[field], data)
            
            for v in values:
                aux = {}
                aux["type"] = field
                aux["value"] = v
                aux["attributes"] = []                
                if aux not in info:
                    info.append(aux)        
        return info

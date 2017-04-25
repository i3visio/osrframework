# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
import logging
import re
import sys
import urllib2

import osrframework.utils.browser as browser
import osrframework.thirdparties.skype.checkInSkype as skype
from osrframework.utils.platforms import Platform

import Skype4Py

class Skype(Platform):
    """ 
        A <Platform> object for Skype.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Skype"
        self.tags = ["conversation"]

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = True      
        
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = ""
        self.url["searchfy"] = ""

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False 
        
        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = ".+"
        self.validQuery["searchfy"] = ".+"
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = [] # N/A in Skype
        self.notFoundText["searchfy"] = [] # N/A in Skype
        
        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}
        
        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""
        
        # Definition of regular expressions to be searched in usufy mode
        self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
    

    def processData(self, uri=None, data=None, mode=None):
        '''
            Method that process the data in a Skype User.
            
            :return:    A i3visio-like object.
        '''
        info = []
        
        # splitting info
        pairs = data.split('; ')
        
        for p in pairs:
            parts = p.split(':')
            
            aux = {}
            aux["type"] = parts[0]
            aux["value"] = parts[1]        
            aux["attributes"] = {}
            
            info.append(aux)
        return json.dumps(info)

    def getInfo(self, query=None, process = False, mode="usufy"):
        ''' 
            Method that checks the presence of a given query and recovers the first list of complains.

            :param query: Phone number to verify.
            :param proces:  Calling the processing function.
            :param mode:    Mode to be executed.            

            :return:    Python structure for the html processed.
        '''
        # Defining variables for this process
        results = []
        data = ""
        if not self.modeIsValid(mode=mode):
            # TO-DO: InvalidModeException
            #print "InvalidModeException"
            return json.dumps(results)
               
        try:
            logger = logging.getLogger("osrframework.wrappers")
            # Verifying if the nick is a correct nick
            if self._isValidQuery(query, mode):
                logger.debug("Starting Skype client...")

                logger.warning("A Skype client must be set up... Note that the program will need a valid session of Skype having been started. If you were performing too many searches, the server may block or ban your account depending on the ToS. Please run this program under your own responsibility.")
                # Instantiate Skype object, all further actions are done
                # using this object.

                # Dealing with UTF8
                import codecs
                import sys

                UTF8Writer = codecs.getwriter('utf8')
                sys.stdout = UTF8Writer(sys.stdout)
   
                # Search for users and display their Skype name, full name
                # and country.
                #print "In skype.py, before sending the query: '" + query + "'"
                data = skype.checkInSkype(query)
                #print "In skype.py, printing the 'data' variable:\n" + json.dumps(data, indent=2)
        except Exception as e:
            print "[!] In skype.py, exception caught when checking information in Skype!"
            # No information was found, then we return a null entity
            return json.dumps(results)            
                
        # Verifying if the platform exists
        if mode == "usufy":
            for user in data:
                if user["value"] == "Skype - " + query.lower():            
                    results.append(user)
        elif mode == "searchfy":
            results = data

    	#print "In skype.py, printing the 'results' variable:\n" + json.dumps(results, indent=2)              
        return json.dumps(results)


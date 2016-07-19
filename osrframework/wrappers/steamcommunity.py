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
import re
import sys
import urllib2

import osrframework.utils.browser as browser
from osrframework.utils.platforms import Platform

class Steamcommunity(Platform):
    """ 
        A <Platform> object for Steamcommunity.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Steamcommunity"
        self.tags = ["social", "news"]

        # Base URL
        self.baseURL = "https://steamcommunity.com"
        
        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False
        
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "http://steamcommunity.com/id/" + "<usufy>"       
        #self.url["searchfy"] = "http://steamcommunity.com/search/?text=" + "<searchfy>" + "&x=0&y=0#filter=users&text=" + "<searchfy>"       

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False 
        
        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any query.
        #self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = ".+"
        #self.validQuery["searchfy"] = ".*"
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] =  [":: Error</title>"]
        #self.notFoundText["searchfy"] = []        
        
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
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "<bci>", "end": "</bci>"}#\n\t\t\t\t\t\t\t\t\t\t\t"}#\t<span class=\"namehistory"}#{"start": "<span class=\"actual_persona_name\">", "end": "r</span>"}#\n\t\t\t\t\t\t\t\t\t\t\t"}#\t<span class=\"namehistory"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "<img class=\"profile_flag\" src=\"http://steamcommunity-a.akamaihd.net/public/images/countryflags/be.gif\">\t\t\t\t\t\t\t\t\t\t\t\t\t", "end": "\t\t\t\t\t</div>\t\t\t\t\t\t\t\t\t\t</div>"}        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        #self.searchfyAliasRegexp = '<a class="searchPersonaName" href="([^\"]+)\"'
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
            

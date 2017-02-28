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

class Anarchy101(Platform):
    """ 
        A <Platform> object for Anarchy101.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Anarchy101"
        # Add the tags for the platform
        self.tags = ["activism"]

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
        self.url["usufy"] = "http://www.anarchy101.org/user/" + "<usufy>"
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"       

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
        self.notFoundText["usufy"] = ["User not found", "Could not establish database connection. Please check the username", "Page not found"]   
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
        # User
        self.fieldsRegExp["usufy"]["i3visio.profile.anarchy101"] = {"start": "var qa_request='user/", "end": "';"}
        # Member for
        self.fieldsRegExp["usufy"]["@member_for"] = {"start": "Member for:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@type"] = {"start": "Type:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "Full name:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "Location:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["i3visio.uri.home"] = {"start": "Website:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        # About
        self.fieldsRegExp["usufy"]["i3visio.text"] = {"start": "About:\n\t\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@score"] = {"start": "Score:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-points\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@questions"] = {"start": "Questions:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-q-posts\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@answers"] = {"start": "Answers:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-a-posts\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@¢omments"] = {"start": "Comments:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-c-posts\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@voted_on"] = {"start": "Voted on:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-q-posts\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@gave_out"] = {"start": "Gave out:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-upvotes\">", "end": "</SPAN>"}
        self.fieldsRegExp["usufy"]["@received"] = {"start": "Received:\n\t\t\t\t\t\t</TD>\n\t\t\t\t\t\t<TD CLASS=\"qa-form-wide-data\">\n\t\t\t\t\t\t\t<SPAN CLASS=\"qa-form-wide-static\"><SPAN CLASS=\"qa-uf-user-upvoteds\">", "end": "</SPAN>"}        
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}


        


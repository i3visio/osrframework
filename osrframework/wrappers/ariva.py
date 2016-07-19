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

class Ariva(Platform):
    """ 
        A <Platform> object for Ariva.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Ariva"

        self.tags = ["opinions", "professional"]
        
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
        self.url["usufy"] = "http://www.ariva.de/profil/" + "<usufy>"       
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
        self.notFoundText["usufy"] = ["<b>Fehler (404)"]   
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
        self.fieldsRegExp["usufy"]["@profil"] = {"start": "</profil/", "end": ">"}
        self.fieldsRegExp["usufy"]["@image"] = {"start": "solid #FFFFFF\" src=\"", "end": "\""}
        self.fieldsRegExp["usufy"]["@clearfloat"] = {"start": "<div class=\"clearfloat\"></div> <div style=\"padding:5px 5px 0px 0px; line-height:16px;\">", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@mitgl. seit, Sterne"] = {"start": "Mitgl. seit, Sterne</td> <td class=\"middle\">\n\n\t\t\t\t\t", "end": "<span"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "<a href=\"/forum/find.m?attr=land&val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@beruf"] = {"start": "<a href=\"/forum/find.m?attr=Beruf&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@firma"] = {"start": "<a href=\"/forum/find.m?attr=Firma&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@postings"] = {"start": "Postings</td> <td class=\"middle\">\n\n\t\t\t\t\t", "end": "\n"}
        self.fieldsRegExp["usufy"]["@alter"] = {"start": "<a href=\"/forum/find.m?attr=Geburtstag&amp;val=", "end": "&amp"}
        self.fieldsRegExp["usufy"]["@geschlecht"] = {"start": "<a href=\"/forum/find.m?attr=Geschlecht&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@ort"] = {"start": "<a href=\"/forum/find.m?attr=Ort&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@interest_1"] = {"start": "<a href=\"/forum/find.m?attr=Interesse1&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@interest_2"] = {"start": "<a href=\"/forum/find.m?attr=Interesse2&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["@interest_3"] = {"start": "<a href=\"/forum/find.m?attr=Interesse3&amp;val=", "end": "\""}
        self.fieldsRegExp["usufy"]["i3visio.uri.homepage"] = {"start": "Homepage</td> <td class=\"middle\"> <a href=\"", "end": "\""}
        self.fieldsRegExp["usufy"]["@broker"] = {"start": "<a href=\"/forum/find.m?attr=broker&amp;val=", "end": "\""}        
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
        


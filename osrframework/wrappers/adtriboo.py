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

class Adtriboo(Platform):
    """ 
        A <Platform> object for Adtriboo.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Adtriboo"
        self.tags = ["contact", "professional"]

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
        self.url["usufy"] = "http://www.adtriboo.com/en/users/" + "<usufy>"       
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
        # The regular expression '.*' will match any query.
        #self.validQuery["phonefy"] = re.compile(".*")
        self.validQuery["usufy"] = re.compile(".*")   
        #self.validQuery["searchfy"] = re.compile(".*")
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["OOps! Página no encontrada"]   
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
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": "<li class='active'>", "end": "</li>"}
        #self.fieldsRegExp["usufy"]["active"] = {"start": "<span class=\"ProfileHeaderCard-locationText u-dir\" dir=\"ltr\">", "end": "</span>"}
        self.fieldsRegExp["usufy"]["i3visio.date"] = {"start": "Member since\n<span class='highlighted'>", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@last_active"] = {"start": "Last activity\n<span class='highlighted'>", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@imeline"] = {"start": "<time datetime='", "end": "'>"}
        #self.fieldsRegExp["usufy"]["username"] = {"start": "<h1 class='username'>", "end": "</h1>"}
        self.fieldsRegExp["usufy"]["@flag_16"] = {"start": "<span class='flag_16 ..'>", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@received_mentions"] = {"start": "<li class='span4 mentions hit'>", "end": "</span>\nReceived mentions"}
        self.fieldsRegExp["usufy"]["@contests_won"] = {"start": "<li class='span4 won-contests hit'>", "end": "</span>\ncontests won"}
        self.fieldsRegExp["usufy"]["@freelance_contract"] = {"start": "<li class='span4 freelance-contracts hit'>", "end": "</span>\nFreelance contract"}
        self.fieldsRegExp["usufy"]["@average_valuation"] = {"start": "<h1>Average Valuation</h1>", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@specialties_and_skills"] = {"start": "<h1>Specialties and skills</h1>", "end": "</span>"}
        self.fieldsRegExp["usufy"]["@Ultimate_jobs_uploaded"] = {"start": "<h1>Ultimate jobs uploaded</h1>", "end": "</span>"}
        # CV
        self.fieldsRegExp["usufy"]["i3visio.text"] = {"start": "<h1>CV</h1>", "end": "</span>"}
        # Friends
        self.fieldsRegExp["usufy"]["i3visio.profile.adtriboo"] = {"start": "To the user\n<a href=\"/en/users/", "end": "\" class="}        
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}


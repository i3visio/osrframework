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

class Xtube(Platform):
    ''' 
        A <Platform> object for Xtube.
    '''
    def __init__(self):
        ''' 
            Constructor... 
        '''
        self.platformName = "Xtube"
        # Add the tags for the platform
        self.tags = ["video", "adult", "contact"]
        self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
        # Add the URL below
        self.url = "http://www.xtube.com/community/profile.php?user=" + self.NICK_WILDCARD
        # Add the strings to look for when an error appears
        #self.notFoundText = ["<title>about.me | your personal homepage</title><style>"]
        self.notFoundText = ["<div class=\"profile-not-found-pic\"></div>"]
        self.forbiddenList = ['.']

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
        self.url["usufy"] = "http://www.apsense.com/user/" + "<usufy>"       
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
        self.notFoundText["usufy"] = ["<h2>404 Page</h2>"]   
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
        gap = "\n                                              <hr color=\"#cccccc\">\n                                              "        
        self.fieldsRegExp["usufy"]["@horoscope"] = {"start": "<h3>Horoscope</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@tobacco_consumption"] = {"start": "<h3>Tobacco Consumption</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@alcohol_consumption"] = {"start": "<h3>Alcohol Consumption</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@ideal_partner"] = {"start": "<h3>Ideal partner</h3>" + gap +"<p>", "end": "</p>\n                                            <div"}
        self.fieldsRegExp["usufy"]["@looking_for"] = {"start": "<h3>Looking for</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@age of partner from"] = {"start": "<h3>Age of partner from</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@age of partner to"] = {"start": "<h3>Age of partner to</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@appearance"] = {"start": "<h3>Appearance</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@body_type"] = {"start": "<h3>Body Type</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@height"] = {"start": "<h3>Height</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@eyecolor"] = {"start": "<h3>Eyecolor</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@hair_color"] = {"start": "<h3>Hair Color</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@hair_length"] = {"start": "<h3>Hair Length</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@facial_hair"] = {"start": "<h3>Facial Hair</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@body_hair"] = {"start": "<h3>Body Hair</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@body_decorations"] = {"start": "<h3>Body Decorations</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@glasses_or_Contacts"] = {"start": "<h3>Glasses or Contacts</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@allergies"] = {"start": "<h3>Allergies</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@career/Job"] = {"start": "<h3>Career/Job</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@work"] = {"start": "<h3>Work</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@living_arrangement"] = {"start": "<h3>Living Arrangement</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@Sexual_orientation"] = {"start": "<h3>Sexual Orientation</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@sex_how_often"] = {"start": "<h3>Sex, How often?</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@practice_safe_sex"] = {"start": "<h3>Practice Safe Sex</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@making_home_videos/pics"] = {"start": "<h3>Making home videos/pics</h3>" + gap +"<p>", "end": "</p>"}
        self.fieldsRegExp["usufy"]["@porn_movies_how_often?"] = {"start": "<h3>Porn Movies, How often?</h3>" + gap +"<p>", "end": "</p>"}
        
        self.fieldsRegExp["usufy"]["@sexual_orientation"] = {"start": "Sexual orientation:", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@member_for"] = {"start": "<div class=\"font11 first\">Member for ", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@comments"] = {"start": "<div id=\"commentBar\">", "end": "Comments</div>"}
        self.fieldsRegExp["usufy"]["@number_of_friends"] = {"start": "<strong>john's Friends ", "end": "</strong>"}
        self.fieldsRegExp["usufy"]["@subscribers"] = {"start": "Subscribers:</div><div class=\"color_blue\" style=\"float: left; width: 30px;\">", "end": "</div>"}    
        self.fieldsRegExp["usufy"]["@viewed_videos"] = {"start": "Viewed Videos:</div><div class=\"color_blue\" style=\"float: left; width: 45px;\">", "end": "</div>"}
        
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "<div class=\"small_infos\">.*<div class=\"font11 first\">", "end": "</div>"}
        self.fieldsRegExp["usufy"]["@ratings"] = {"start": "Ratings:</div><div class=\"color_blue\" style=\"float: left; width: 30px;\">", "end": "</div>"}
        
        self.fieldsRegExp["usufy"]["@viewed_photos"] = {"start": "Viewed Photos:</div><div class=\"color_blue\" style=\"float: left; width: 50px;\">", "end": "</div>"}        
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
        
        

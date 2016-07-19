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

class Youtube(Platform):
    ''' 
        A <Platform> object for Youtube.
    '''
    def __init__(self):
        ''' 
            Constructor... 
        '''
        self.platformName = "Youtube"
        self.tags = ["social", "video"]

        # Base URL
        self.baseURL = "http://youtube.com/"

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
        self.url["usufy"] = "https://www.youtube.com/user/" + "<usufy>" + "/about" 
        self.url["searchfy"] = "https://www.youtube.com/results?filters=channel&lclk=channel&search_query=" + "<searchfy>"       

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
        self.validQuery["usufy"] = "[^@, ]+"
        self.validQuery["searchfy"] = ".+"
        
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["Este canal no existe.", "channel-empty-message banner-message"] 
        self.notFoundText["searchfy"] = []        
        
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
        self.fieldsRegExp["usufy"]["subscribers"] = {"start": "<span class=\"yt-subscription-button-subscriber-count-branded-horizontal subscribed\" title=\"", "end": "\">"}
        self.fieldsRegExp["usufy"]["@total_views"] = {"start": "</li>.*<li class=\"about-stat \">.*<b>", "end": "</b>"}
        self.fieldsRegExp["usufy"]["i3visio.date"] = {"start": "<li class=\"about-stat joined-date\">", "end": "</li>"}
        self.fieldsRegExp["usufy"]["i3visio.profile.facebook"] = {"start": "alt=\"https://www.facebook.com/", "end": "\""}
        self.fieldsRegExp["usufy"]["i3visio.profile.twitter"] = {"start": "alt=\"http://www.twitter.com/#!/", "end": "\""}
        self.fieldsRegExp["usufy"]["i3visio.profile.instagram"] = {"start": "alt=\"http://instagram.com/", "end": "\""}
        self.fieldsRegExp["usufy"]["i3visio.alias"] = '<meta itemprop="name" content="([^\"]+)\"'
        
        # Description
        self.fieldsRegExp["usufy"]["i3visio.text"] = {"start": "<div class=\"about-description branded-page-box-padding\" >", "end": "</div>"}
                
        
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        self.searchfyAliasRegexp = '<div class="yt-lockup-byline"><a href="([^\"]+)" class="yt-uix-sessionlink g-hovercard      spf-link "'
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}

    def createURL(self, word, mode="phonefy"):
        ''' 
            Method to create the URL replacing the word in the appropriate URL.
            
            :param word:   Word to be searched.
            :param mode:    Mode to be executed.
            
            :return:    The URL to be queried.
        '''
        # Youtube has two different types of profiles: channels and users
        if "/user/" in word:
            alias = word[6:]
        else:
            alias = word        
        try:
            if mode == "base":
                if word[0] == "/":
                    return self.baseURL+word[1:], alias
                else:
                    return self.baseURL+word, alias
            else:
                try:
                    return self.url[mode].replace("<"+mode+">", word.replace(' ', '+')), alias
                except:
                    pass   
        except:
            pass
            # TO-DO: BaseURLNotFoundExceptionThrow base URL not found for the mode.        
         


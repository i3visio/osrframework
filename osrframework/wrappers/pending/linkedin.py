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

class Linkedin(Platform):
    """
        A <Platform> object for Linkedin.
    """
    def __init__(self):
        """
            Constructor...
        """
        self.platformName = "Linkedin"
        self.tags = ["professional", "contact"]
        self.creds =[]

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
        self.url["usufy"] = "https://www.linkedin.com/in/" + "<usufy>"
        self.url["searchfy"] = "https://us.linkedin.com/pub/dir/" + "<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = True
        self.needsCredentials["searchfy"] = True

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
        self.notFoundText["usufy"] = ["Perfil no encontrado"]
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
        # Definition of regular expressions to be searched in searchfy mode
        self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""
        self.searchfyAliasRegexp = "<h3><a href=\"https://us.linkedin.com/in/([^\"]+)\">"
        #self.searchfyAliasRegexp = "\" width=\"100\" height=\"100\"></a><div class=\"content\"><h3><a href=\"https://us.linkedin.com/in/([^\"]+)\
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}



    def do_mailfy(self, query):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return an equivalent array.

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
            A list of elements to be appended. A sample output format is as follows:
            [
              {
                "attributes": [
                  {
                    "attributes": [],
                    "type": "i3visio.email",
                    "value": "contacto@i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.alias",
                    "value": "contacto"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.domain",
                    "value": "i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.platform",
                    "value": "Twitter"
                  }
                ],
                "type": "i3visio.profile",
                "value": "Twitter - contacto@i3visio.com"
              }
            ]
        """
        from bs4 import BeautifulSoup
        #LINKEDIN-------------------------------------------------
        r = br.open('https://www.linkedin.com/')
        br.select_form(nr=0)
        br.form["session_key"] = query
        br.form["session_password"] = "123456"
        br.submit()
        respuestaURL = br.response().geturl()
        if "captcha" in respuestaURL:
        	print "|--[INFO][LinkedIn][Captcha][>] Captcha detect!"
        else:
        	pass
        html = br.response().read()
        #print "|--[INFO][LinkedIn][URL][>] " + respuestaLI
        soup = BeautifulSoup(html, "html.parser")
        for span in soup.findAll("span", {"class", "error"}):
        	data = remove_tags(str(span))
        	if "password" in data:
        		print "|--[INFO][LinkedIn][CHECK][>] The account exist..."
        		if state == 1:
        			print colores.blue + "|--[INFO][LinkedIn][CHECK][>] it's possible to hack it !!!" + colores.normal
        	if "recognize" in data:
                print "|--[INFO][LinkedIn][CHECK][>] The account doesn't exist..."

        data = self.launchQueryForMode(query=query, mode="mailfy")

        expandedEntities = general.expandEntitiesFromEmail(query)

        if self.somethingFound(data, mode="mailfy"):
            r = {
                "type": "i3visio.profile",
                "value": self.platformName + " - " + query,
                "attributes": expandedEntities + [
                    {
                        "type": "i3visio.platform",
                        "value": self.platformName,
                        "attributes": []
                    }
                ]
            }
            return [r]
        return []

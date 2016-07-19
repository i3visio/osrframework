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

class Aporrealos(Platform):
    """ 
        A <Platform> object for Aporrealos.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Aporrealos"
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
        self.url["usufy"] = "http://www.aporrealos.com/forum/profile.php?mode=viewprofile&u=" + "<usufy>"       
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
        self.notFoundText["usufy"] = ["Lo sentimos, pero ese usuario no existe.", "<b>Critical Error</b>"]   
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
        self.fieldsRegExp["usufy"]["i3visio.profile.aporrealos"] = {"start": "Viendo perfil :: ", "end": "</th>"}
        self.fieldsRegExp["usufy"]["@registered"] = {"start": "Registrado:&nbsp;</span></td>\n\n\t\t  <td width=\"100%\"><b><span class=\"gen\">", "end": "</span></b></td>"}
        self.fieldsRegExp["usufy"]["@total_posts"] = {"start": "<td valign=\"top\"><b><span class=\"gen\">", "end": "</span>"}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": "Ubicaci.n:&nbsp;</span></td>\n\n\t\t  <td><b><span class=\"gen\">", "end": "</span></b></td>"}
        self.fieldsRegExp["usufy"]["i3visio.uri.home"] = {"start": "Sitio Web:&nbsp;</span></td>\n\n\t\t  <td><span class=\"gen\">", "end": "</span></td>"}
        self.fieldsRegExp["usufy"]["@occupation"] = {"start": "Ocupaci.n:&nbsp;</span></td>\n\n\t\t  <td><b><span class=\"gen\">", "end": "</span></b></td>"}
        self.fieldsRegExp["usufy"]["@interests"] = {"start": "Intereses:</span></td>\n\n\t\t  <td> <b><span class=\"gen\">", "end": "</span></b></td>"}
        
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
        
        


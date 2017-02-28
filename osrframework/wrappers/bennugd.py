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

class Bennugd(Platform):
    """ 
        A <Platform> object for Bennugd.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Bennugd"
        self.tags = ["gaming", "development"]
        
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
        self.url["usufy"] = "http://forum.bennugd.org/index.php?action=profile;user=" + "<usufy>"       
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
        self.notFoundText["usufy"] = ["El usuario cuyo perfil estás intentando editar no existe."]
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
        self.fieldsRegExp["usufy"]["i3visio.fullname"] = {"start": '<div class="username"><h4>', "end": '<span'}
        self.fieldsRegExp["usufy"]["@sex"] = {"start": '<dt>Sexo: </dt>\n\t\t\t\t\t<dd>', "end": '</dd>'}
        self.fieldsRegExp["usufy"]["@age"] = {"start": '<dt>Edad:</dt>\n\t\t\t\t\t<dd>', "end": '</dd>'}
        self.fieldsRegExp["usufy"]["i3visio.location"] = {"start": '<dt>Ubicación:</dt>\n\t\t\t\t\t<dd>', "end": '</dd>'} 
        self.fieldsRegExp["usufy"]["@last_active"] = {"start": '<dt>\xe9ltima vez activo: </dt>\n\t\t\t\t\t<dd>', "end": '</dd>'} 
        self.fieldsRegExp["usufy"]["@created_at"] = {"start": '<dt>Fecha de registro: </dt>\n\t\t\t\t\t<dd>', "end": '</dd>'} 
        self.fieldsRegExp["usufy"]["@language"] = {"start": '<dt>Idioma:</dt>\n\t\t\t\t\t<dd>', "end": '</dd>'}
        
        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""        
        
        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}
        

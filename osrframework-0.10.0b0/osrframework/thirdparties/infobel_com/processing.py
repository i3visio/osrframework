# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
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

import osrframework.utils.browser as browser

def extractFieldsFromResult(data):
    '''
        Method that parses Infobel textual information to return a series of attributes.
        
        :return:    a list of i3visio-like objects.
    ''' 
    
    entities = []
    
    # Defining the objects to extract
    fieldsRegExp = {}
    fieldsRegExp["i3visio.fullname"] = "<span class=\"fn\">([^<]*)</span>"
    fieldsRegExp["i3visio.name"] = "    por <strong>[^ ]* ([^<]*)</strong>"        
    fieldsRegExp["i3visio.surname"] = "    por <strong>([^ ]*) "     
    fieldsRegExp["i3visio.location.address"] = "itemprop=\"streetAddress\">([^<]*)</span>"
    fieldsRegExp["i3visio.location.city"] = "addressLocality\">([^<]*)</span>"
    fieldsRegExp["i3visio.location.postalcode"] = "postalCode\">([^<]*)</span>"    
    fieldsRegExp["i3visio.phone"] = "document.write\('([0-9]+)'"        

    for field in fieldsRegExp.keys():
        listRecovered = re.findall(fieldsRegExp[field], data)
        if len(listRecovered) >0:
            aux = {}
            aux["type"]= field
            aux["value"] = listRecovered[0].replace('\xa0', ' ')
            aux["attributes"] = []
            entities.append(aux)
            
    return entities
    
def getResults(uri):
    '''
        Method that recovers the text for each result in infobel.com
        
        :param uri: Infobel uri
        
        :return:    A list of textual information to be processed
    '''
    # Using i3visio browser to avoid certain issues...
    i3Browser = browser.Browser()

    data = i3Browser.recoverURL(uri)        

    # Strings to be searched
    regExp = "<!-- Results -->(.*)<!-- /Results -->"
    # re.DOTALL is needed to match any character INCLUDING \n
    results = re.findall(regExp, data, re.DOTALL)
    
    return results

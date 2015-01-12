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
import urllib2

import osrframework.utils.browser as browser
from osrframework.phonefy.platforms import Platform

class Listspam(Platform):
    '''
    '''
    def __init__(self):
        '''
        '''
        self.platformName = "Listspam"        
        
        self.basePhoneURL = "http://www.listaspam.com/busca.php?Telefono=" + "<PHONE_NUMBER>"
        
        # Strings that will imply that the phone number is not appearing
        self.notFoundText = ["No te quedes sin saber quien te llama por teléfono."]
        
        self.fieldsRegExp = {}
        self.fieldsRegExp["i3visio.location.province"] = "<strong class='located_label'>(.*),"
        self.fieldsRegExp["i3visio.location.country"] = "class='country_located' alt='([a-zA-Zñ]*)'"
        self.fieldsRegExp["i3visio.text"] = '<h4 class="media-heading">(.*)</p>'




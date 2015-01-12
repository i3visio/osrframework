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
        self.notFoundText = [""]
        
        self.fieldsRegExp = {}
        self.fieldsRegExp["i3visio.location.province"] = "<strong class='located_label'>(.*),"
        self.fieldsRegExp["i3visio.location.country"] = "class='country_located' alt='([a-zA-Zñ]*)'"
        self.fieldsRegExp["i3visio.text"] = '<h4 class="media-heading">(.*)</p>'


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='A library to check if there exist any kind of issues related to a telephone number in listspam.com.', prog='getPhoneComplains.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to blockchain.info.', required=True)        
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        
    
    print json.dumps(getPhoneComplains(query=args.query), indent=2)

    

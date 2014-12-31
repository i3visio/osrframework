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
import sys
import urllib2

def getBitcoinAddressDetails(address=None):
    ''' 
        Method that checks the presence of a Bitcoin Address in blockchain.info:
{
  "total_sent": 41301084, 
  "total_received": 52195147, 
  "final_balance": 10894063, 
  "address": "1APKyS2TEdFMjXjJfMCgavFtoWuv2QNXTw", 
  "hash160": "66f21efc754af07e87913db46bf24df2eb0d5075", 
...
}

        :param address: Bitcoin address to verify.

        :return:        Python structure for the json received. If nothing was found, it will return an empty dictionary.
    '''
    try:
        apiURL = "https://blockchain.info/rawaddr/" + str(address)

        # Accessing the HIBP API
        data = urllib2.urlopen(apiURL).read()

        # Reading the text data onto python structures
        jsonData = json.loads(data)
        return jsonData
    except:
        # No information was found, then we return a null entity
        return {}    

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='A library that wraps the search about a Bitcoin address in blockchain.info.', prog='getBitcoinAddressDetails.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to blockchain.info.', required=True)        
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        
    
    print json.dumps(getBitcoinAddressDetails(address=args.query), indent=2)

    

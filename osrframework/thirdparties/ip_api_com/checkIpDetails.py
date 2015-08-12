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

def checkIpDetails(query=None):
    ''' 
        Method that checks if the given hash is stored in the md5crack.com website. An example of the json received:
        {
            "as": "AS8560 1\u00261 Internet AG",
            "city": "",
            "country": "Germany",
            "countryCode": "DE",
            "isp": "1\u00261 Internet AG",
            "lat": 51,
            "lon": 9,
            "org": "1\u00261 Internet AG",
            "query": "217.160.251.126",
            "region": "",
            "regionName": "",
            "status": "success",
            "timezone": "",
            "zip": ""
        }

        :param query:    Query to verify. It can be either a domain or an IPv4 address.

        :return:    Python structure for the json received. If nothing was found, it will return an empty dictionary.
        [
          {
            "attributes": [
              {
                "attributes": [], 
                "type": "i3visio.text", 
                "value": "DE"
              }
            ], 
            "type": "i3visio.location.country", 
            "value": "Germany"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.text", 
            "value": "1&1 Internet AG"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.ipv4", 
            "value": "217.160.129.99"
          }, 
          {
            "attributes": [], 
            "type": "i3visio.location.geo", 
            "value": "51, 9"
          }
        ]        
    '''
    try:    
        apiURL = "http://ip-api.com/json/" + query


        # Accessing the ip-api.com RESTful API
        data = urllib2.urlopen(apiURL).read()

        # Reading the text data onto python structures
        apiData = json.loads(data)
        
        # i3visio structure to be returned
        jsonData = []
       
        if apiData["status"] == "success":
            for key in apiData:
                value = apiData[key]
                if value != "":
                    aux = {}
                    if key == "city":
                        aux["type"] = "i3visio.location." + key
                        aux["value"] = value
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)
                    elif key == "country":
                        aux["type"] = "i3visio.location." + key
                        aux["value"] = value
                        # Adding a new attribute
                        att ={}
                        att["type"] = "i3visio.text"
                        att["value"] = apiData["countryCode"]
                        att["attributes"] = []
                        aux["attributes"] = [att]
                        # Appending to the list of results
                        jsonData.append(aux)
                    elif key == "isp":
                        aux["type"] = "i3visio.text"
                        aux["value"] = value
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)                        
                    elif key == "lat":
                        aux["type"] = "i3visio.location.geo"
                        aux["value"] = str(apiData["lat"]) + ", " + str(apiData["lon"])
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)
                    elif key == "region":
                        aux["type"] = "i3visio.location.province"
                        aux["value"] = value
                        # Adding a new attribute
                        att ={}
                        att["type"] = "i3visio.text"
                        att["value"] = apiData["regionName"]
                        att["attributes"] = []                        
                        aux["attributes"] = [att]
                        # Appending to the list of results                        
                        jsonData.append(aux)
                    elif key == "timezone":
                        aux["type"] = "i3visio.text"
                        aux["value"] = value
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)                        
                    elif key == "zip":
                        aux["type"] = "i3visio.location.postalcode"
                        aux["value"] = value
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)                        
                    elif key == "query":
                        aux["type"] = "i3visio.ipv4"
                        aux["value"] = value
                        aux["attributes"] = []
                        # Appending to the list of results                        
                        jsonData.append(aux)                        
            
        #print json.dumps(jsonData, indent = 2)
        return jsonData
    except:
        # No information was found, then we return a null entity
        return {}   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps a search onto ip-api.com.', prog='checkIPDetails.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    general.add_argument('-q', '--query', metavar='<ip_or_domain>', action='store', help='query to be resolved by ip-api.com.')        
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.2.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        
    
    print json.dumps(checkIpDetails(query=args.query), indent=2)



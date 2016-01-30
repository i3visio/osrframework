# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import argparse
import json
import osrframework.utils.config_api_keys as config_api_keys
import sys
import urllib2

def checkIfHashIsCracked(hash=None, api_key=None):
	''' 
		Method that checks if the given hash is stored in the md5crack.com website. 

		:param hash:	hash to verify.
		:param api_key:	api_key to be used in md5crack.com. If not provided, the API key will be searched in the config_api_keys.py file.

		:return:	Python structure for the Json received. It has the following structure:
	        {
              "phrase": "4d186321c1a7f0f354b297e8914ab240",
              "code": 6,
              "parsed": "hola",
              "response": "The MD5 hash was cracked."
            }
	'''
	# This is for i3visio
	if api_key==None:
		#api_key = raw_input("Insert the API KEY here:\t")
		allKeys = config_api_keys.returnListOfAPIKeys()
		try: 
			api_key_data = allKeys["md5crack_com"]
			api_key = api_key_data["api_key"]
		except:
			# API_Key not found
			return {}			

	apiURL = "http://api.md5crack.com/crack/"+ api_key +"/" + hash

	# Accessing the HIBP API
	data = urllib2.urlopen(apiURL).read()
	if "\"parsed\":null" in data:
		data = data.replace("\"parsed\":null", "\"parsed\":\"\"")
	
	# Reading the text data onto python structures
	jsonData = json.loads(data)
	#print json.dumps(jsonData, indent = 2)
	return jsonData

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='A library that wraps a search onto md5crack.com.', prog='checkIfHashIsCracked.py', epilog="NOTE: if not provided, the API key will be searched in the config_api_keys.py file.", add_help=False)
	# Adding the main options
	# Defining the mutually exclusive group for the main options
	parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to md5crack.com.', required=True)		
	parser.add_argument('-a', '--api_key', action='store', help='API key in md5crack.com to be used.', required=False, default=None)
	
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

	args = parser.parse_args()		
	
	print json.dumps(checkIfHashIsCracked(hash=args.query, api_key=args.api_key), indent=2)



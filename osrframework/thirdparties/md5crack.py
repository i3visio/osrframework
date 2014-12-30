# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of apify. You can redistribute it and/or modify
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

import sys
import json
import urllib2
import i3visiotools.config_api_keys as config_api_keys

def checkIfCrackedInMD5crack(hash=None, api_key=None):
	''' 
		Method that checks if the given hash is stored in the md5crack.com website. An example of the json received:

		:param hash:	hash to verify.

		:return:	Python structure for the Json received.
	'''
	#with open("./_config.txt", "r") as iF:
	#	cont = iF.read().splitlines()
	# This is for i3visio
	if api_key==None:
		#api_key = raw_input("Insert the API KEY here:\t")
		allKeys = config_api_keys.returnListOfAPIKeys()
		try: 
			api_key = allKeys["md5crack"]
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
	checkIfCrackedInMD5crack(hash=sys.argv[1])



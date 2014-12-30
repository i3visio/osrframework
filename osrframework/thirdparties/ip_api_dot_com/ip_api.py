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

def checkIPDetails(query=None):
	''' 
		Method that checks if the given hash is stored in the md5crack.com website. An example of the json received:

		:param query:	Query to verify. It can be either a domain or an IPv4 address.

		:return:	Python structure for the Json received. The format is as follows:
		
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
	'''
	#with open("./_config.txt", "r") as iF:
	#	cont = iF.read().splitlines()
	# This is for i3visio
	apiURL = "http://ip-api.com/json/" + query


	# Accessing the ip-api.com RESTful API
	data = urllib2.urlopen(apiURL).read()

	
	# Reading the text data onto python structures
	jsonData = json.loads(data)
	#print json.dumps(jsonData, indent = 2)
	return jsonData

if __name__ == "__main__":
	checkIPDetails(query=sys.argv[1])



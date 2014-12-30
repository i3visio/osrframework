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

		:param address:	Bitcoin address to verify.

		:return:	Python structure for the Json received.
	'''

	apiURL = "https://blockchain.info/rawaddr/" + str(address)

	# Accessing the HIBP API
	data = urllib2.urlopen(apiURL).read()

	# Reading the text data onto python structures
	jsonData = json.loads(data)
	#print json.dumps(jsonData, indent = 2)
	return jsonData

if __name__ == "__main__":
	getBitcoinAddressDetails(address=sys.argv[1])



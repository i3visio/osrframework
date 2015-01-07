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

from osrframework.maltfy.maltego import *
import sys
import json
import urllib2
import i3OSRFramework.thirdparties.md5crack_com.checkIfHashIsCracked as md5crack

def hashToMD5crackDotCom(hash=None):
	''' 
		Method that checks if the given email is stored in the md5crack.com.

		:param email:	email to verify.

	'''
	me = MaltegoTransform()

	jsonData = md5crack.checkIfCrackedInMD5crack(hash=hash)

	# This returns a dictionary like:
	""" 
	{
      "phrase": "4d186321c1a7f0f354b297e8914ab240",
      "code": 6,
      "parsed": "hola",
      "response": "The MD5 hash was cracked."
    }
    """

	#print json.dumps(entities, indent=2)
	if not jsonData["parsed"] == "":
		newEnt = me.addEntity("i3visio.text",jsonData["parsed"])
		newEnt.setDisplayInformation("<h3>" + jsonData["parsed"] +"</h3><p>" + json.dumps(jsonData, sort_keys=True, indent=2) + "</p>");
		for field in jsonData.keys():
			if field != "parsed":
				pass
				# [TO-DO] Appending all the information from the json:
				#newEnt.addAdditionalFields(field,field,True,breach[field])

	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	hashToMD5crackDotCom(hash=sys.argv[1])



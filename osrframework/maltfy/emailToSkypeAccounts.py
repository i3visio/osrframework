# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of osrframework. You can redistribute it and/or modify
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

from MaltegoTransform import *
import sys
import json
import osrframework.thirdparties.skype.checkInSkype as skype

def emailToSkypeAccount(query=None):
	''' 
		Method that checks if the given email is appears in Skype.

		:param query:	query to verify.

	'''
	me = MaltegoTransform()

	jsonData = skype.checkInSkype(query=query)

	# This returns a dictionary like:
	# [{}]

	#print json.dumps(entities, indent=2)
	for user in jsonData:
		newEnt = me.addEntity("i3visio.profile","skype://" + str(user["i3visio.alias"]))
		# From v0.3.1 and ongoing versions, the i3visio.alias is not created directly but appended to the profile.
		#aliasEnt = me.addEntity("i3visio.alias",user["i3visio.alias"])

		newEnt.setDisplayInformation("<h3>" + user["i3visio.alias"] +"</h3><p>");# + json.dumps(user, sort_keys=True, indent=2) + "!</p>");
		for field in user.keys():
			# [TO-DO] Appending all the information from the json:
			if user[field] != None:
				try:
					newEnt.addAdditionalFields(field,field,True,str(user[field]).encode('utf-8'))
				except:
					# Something passed...
					pass

	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	emailToSkypeAccount(query=sys.argv[1])



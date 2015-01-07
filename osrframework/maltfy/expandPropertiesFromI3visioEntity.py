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
import constants

def expandPropertiesFromI3visioEntity(argv):
	''' 
		Method that expands the properties from a given i3visio entity. It is useful to create new Entities based on the contents of the properties.
		:param argv:	the serialized entity.

		:return:	Nothing is returned but the code of the entities is created.
	'''
	me = MaltegoTransform()
	me.parseArguments(argv);

	# Trying to recover all the possible i3visio entities
	found_fields = {}
	
	for entity in constants.I3VISIO_ENTITIES:
		found_fields[entity]  = me.getVar(entity)
	# All the possible fields must be written down here...

	# iterating through the possible i3visio entities
	for field in found_fields.keys():
		if found_fields[field] != None:
			newEnt = me.addEntity(field,str(found_fields[field]))
		#newEnt.setDisplayInformation("<h3>" + prof +"</h3><p>" + str(prof) + "\t" + str(plat) + "\t" + profiles[prof][plat]  + "</p>");
		#newEnt.addAdditionalFields("i3visio.platform","Platform name",True,plat)

	try:
		# Adding new entities observing the attributes tab:
		attributes = me.getVar("attributes")
		#print attributes
		attJson = json.loads(attributes)
		#print attJson
		for att in attJson:
			#print att
			newEnt = me.addEntity(str(att["type"]),str(att["value"]))
			#newEnt.setDisplayInformation("<h3>" + prof +"</h3><p>" + str(prof) + "\t" + str(plat) + "\t" + profiles[prof][plat]  + "</p>");
			newEnt.addAdditionalFields("attributes","attributes",True,str(att["attributes"]))
	except:
		pass
	# Getting the output text
	#maltegoText = me.getOutput()	
	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	expandPropertiesFromI3visioEntity(sys.argv)



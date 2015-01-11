# -*- coding: cp1252 -*-
#
##################################################################################
#
#	OSRFramework is free software: you can redistribute it and/or modify
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


import hashlib
import json
import datetime
from osrframework.maltfy.lib.maltego import MaltegoEntity, MaltegoTransform

import logging

def dictToJson(d):
	'''
		Workaround to convert any dictionary to json text.
		
		:param d:	Dictionary to convert to json.

		:return:	jsonText (string).
	'''
	# creating json
	jsonText =  json.dumps(d, indent=2)
	return jsonText

def listToMaltego(profiles):
	""" 
		Method to generate the text to be appended to a Maltego file.

		:param profiles:	a list of dictionaries with the information of the profiles: {"a_nick": [<list_of_results>]}
		
		:return:	maltegoText as the string to be written for a Maltego file.				
	"""
	logger = logging.getLogger("osrframework.utils")
	logger.info( "Generating Maltego File...")

	maltegoText = ""
	logger.debug("Going through all the keys in the dictionary...")
	me = MaltegoTransform()
	# A dictionary with the structure:

	for profile in profiles:
		# recovering the nick
		valueEnt = profile["value"]
		typeEnt = profile["type"]
		attributesEnt  = profile["attributes"]
		newEnt = me.addEntity(str(typeEnt),str(valueEnt))
		#newEnt = me.addEntity("i3visio.alias", "value")
		newEnt.addAdditionalFields("attributes","attributes",True,dictToJson(attributesEnt))
		newEnt.setDisplayInformation("<h3>" + valueEnt +"</h3><pre>" + dictToJson(attributesEnt)+ "</pre>")

		# Adding platform entity:
		for att in attributesEnt:
			if att["type"] == "i3visio.platform":
				newEnt.addAdditionalFields(str(att["type"]),str(att["type"]),True,str(att["value"]))		
		"""newEnt = me.addEntity("i3visio.url",str(url))
		#newEnt.setDisplayInformation("<h3>" + prof +"</h3><p>" + str(prof) + "\t" + str(plat) + "\t" + profiles[prof][plat]  + "</p>");
		for attribute in profiles[alias][url].keys():
			newEnt.addAdditionalFields(attribute,attribute,True,profiles[alias][url][attribute])"""
	# Getting the output text
	me.addUIMessage("completed!")	
	# Returning the output text...
	me.returnOutput()
	return me.getOutput()

def fileToMD5(filename, block_size=256*128, binary=False):
	'''
		:param filename:	Path to the file.
		:param block_size:	Chunks of suitable size. Block size directly depends on the block size of your filesystem to avoid performances issues. Blocks of 4096 octets (Default NTFS).
		:return:	md5 hash.
	'''
	md5 = hashlib.md5()
	with open(filename,'rb') as f: 
		for chunk in iter(lambda: f.read(block_size), b''): 
			 md5.update(chunk)
	if not binary:
		return md5.hexdigest()
	return md5.digest()


def getCurrentStrDatetime():
	'''
		Generating the current Datetime with a given format.

		:return:	strTime
	'''
	# Generating current time
	i = datetime.datetime.now()
	strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
	return strTime
	
def getFilesFromAFolder(path):
	'''
		Getting all the files in a folder.
		
		:param path:	path in which looking for files.
		
		:return:	list of filenames.
	'''
	from os import listdir
	from os.path import isfile, join
	#onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
	onlyFiles = []
	for f in listdir(path):
		if isfile(join(path, f)):
			onlyFiles.append(f)
	return onlyFiles
	


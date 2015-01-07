# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of OSRFramework.
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

import logging

#from bs4 import BeautifulSoup
import requests
import os
from os import listdir
from os.path import isfile, join, isdir


import osrframework.utils.logger
import osrframework.utils.general as general
import osrframework.utils.entify.config_entify as config

def getEntitiesByRegexp(data = None, listRegexp = None, verbosity=1, logFolder="./logs"):
	''' 
		Method to obtain entities by Regexp.

		:param data:	text where the entities will be looked for.
		:param listRegexp:	list of selected regular expressions to be looked for. If None was provided, all the available will be chosen instead.
		:param verbosity:	Verbosity level.
		:param logFolder:	Folder to store the logs.
		
		:return:	a list of the available objects containing the expressions found in the provided data.
		[
		  {
			"attributes": [],
			"type": "i3visio.email",
			"value": "foo@bar.com"
		  },
		  {
			"attributes": [],
			"type": "i3visio.email",
			"value": "bar@foo.com"
		]
	'''
	osrframework.utils.logger.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)	
	logger = logging.getLogger("osrframework.entify")
	if listRegexp == None:
		listRegexp = config.getAllRegexp()

	foundExpr = []

	for r in listRegexp:
		foundExpr += r.findExp(data)

	# print foundExpr

	return foundExpr


def scanFolderForRegexp(folder = None, listRegexp = None, recursive = False, verbosity=1, logFolder= "./logs"):
	''' 
		[Optionally] recursive method to scan the files in a given folder.

		:param folder:	the folder to be scanned.
		:param listRegexp:	listRegexp is an array of <RegexpObject>.
		:param recursive:	when True, it performs a recursive search on the subfolders.
	
		:return:	a list of the available objects containing the expressions found in the provided data.
		[
		  {
			"attributes": [],
			"type": "i3visio.email",
			"value": "foo@bar.com"
		  },
		  {
			"attributes": [],
			"type": "i3visio.email",
			"value": "bar@foo.com"
		  }
		]
	'''
	osrframework.utils.logger.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)
	logger = logging.getLogger("osrframework.entify")

	logger.info("Scanning the folder: " + folder)	
	results = {}

	#onlyfiles = []
	#for f in listdir(args.input_folder):
	#	if isfile(join(args.input_folder, f)):
	#		onlyfiles.append(f)	
	onlyfiles = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
	
	for f in onlyfiles:
		filePath = join(folder,f)
		logger.debug("Looking for regular expressions in: " + filePath)	

		with open(filePath, "r") as tempF:
			# reading data
			foundExpr = getEntitiesByRegexp(data = tempF.read(), listRegexp = listRegexp)
			logger.debug("Updating the " + str(len(foundExpr)) + " results found on: " + filePath)	
			results[filePath] = foundExpr

	if recursive:
		onlyfolders = [ f for f in listdir(folder) if isdir(join(folder,f)) ]
		for f in onlyfolders:
			folderPath = join(folder, f)
			logger.debug("Looking for additional in the folder: "+ folderPath)
			results.update(scanFolderForRegexp(folder = folderPath,listRegexp = listRegexp, recursive = recursive))
	return results

	
def scanResource(uri = None, listRegexp = None, verbosity=1, logFolder= "./logs"):
	''' 
		[Optionally] recursive method to scan the files in a given folder.

		:param uri:	the URI to be scanned.
		:param listRegexp:	listRegexp is an array of <RegexpObject>.

		:return:	a dictionary where the key is the name of the file.
	'''
	osrframework.utils.logger.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)
	logger = logging.getLogger("osrframework.entify")

	results = {}

	logger.debug("Looking for regular expressions in: " + uri)	
	
	import urllib2
	
	foundExpr = getEntitiesByRegexp(data = urllib2.urlopen(uri).read(), listRegexp = listRegexp)
	logger.debug("Updating the " + str(len(foundExpr)) + " results found on: " + uri)	
	results[uri] = foundExpr

	return results
	
def entify_main(args):
	''' 
		Main function. This function is created in this way so as to let other applications make use of the full configuration capabilities of the application.	
	'''
	# Recovering the logger
	# Calling the logger when being imported
	osrframework.utils.logger.setupLogger(loggerName="osrframework.entify", verbosity=args.verbose, logFolder=args.logfolder)	
	# From now on, the logger can be recovered like this:
	logger = logging.getLogger("osrframework.entify")

	logger.info("""osrframework.entify-launcher.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
\tpython entify-launcher.py --license""")

	logger.info("Selecting the regular expressions to be analysed...")

	listRegexp = []
	if args.regexp:
		listRegexp = config.getRegexpsByName(args.regexp)

	elif args.new_regexp:
		for i, r in enumerate(args.new_regexp):
			list.Regexp.append(RegexpObject(name = "NewRegexp"+str(i), reg_exp = args.new_regexp))

	if not args.web:
		results = scanFolderForRegexp(folder = args.input_folder, listRegexp= listRegexp, recursive = args.recursive, verbosity=args.verbose, logFolder= args.logfolder)
	else:
		results = scanResource(uri = args.web, listRegexp= listRegexp, verbosity=args.verbose, logFolder= args.logfolder)
	logger.info("Printing the results:\n" + general.dictToJson(results))

	if args.output_folder:
		logger.info("Preparing the output folder...")
		if not os.path.exists(args.output_folder):
			logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
			os.makedirs(args.output_folder)
		logger.info("Storing the results...")
		"""if "csv" in args.extension:
			with open(os.path.join(args.output_folder, "results.csv"), "w") as oF:
				oF.write(resultsToCSV(results))"""
		if "json" in args.extension:
			with open(os.path.join(args.output_folder, "results.json"), "w") as oF:
				oF.write(general.dictToJson(results))

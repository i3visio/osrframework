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


import os
import logging

import osrframework.wrappers.platforms as platforms
import osrframework.utils.credentials as credentials

def getPlatforms(sites=["all"], tags=[], fileCreds="./creds.txt"):
	''' 
		Method that defines the list of <Platform> objects to be processed... Note that <Facebook> or <Twitter> objects inherit from <Platform>.

		Parameters:
			:param sites:	A list of platforms: 'all', 'twitter', facebook', ...
			:param tags:	A list of the tags of the looked platforms: 'news', 'social', ...
			:param fileCreds: the path to the credentials file.
		
		Return values:
			Returns a list [] of <Platform> objects.
	'''
	logger = logging.getLogger("usufy")
	
	logger.debug("Recovering all usufy platforms...")
	# Mode will let the i3visiotools module know which kind of platforms we want
	listAllUsufy = platforms.getAllPlatformsByMode(mode="usufy")
	
	logger.info("Recovering all the credentials stored in the i3visiotools.config_credentials.py file.")	
	#creds = credentials.getCredentials(fileCreds)
	creds = credentials.getCredentials()

	for p in listAllUsufy:
		# Verify if there are credentials to be loaded
		if p.platformName.lower() in creds.keys():
			p.setCredentials(creds[p.platformName.lower()])

	listSelected = []	
	
	logger.debug("Selecting the platforms to be queried according to the input parameters...")
	if "all" in sites:
		return listAllUsufy
	else:
		for plat in listAllUsufy:
			added = False
			# Verifying if the parameter was provided
			for s in sites:
				if s in str(plat).lower():
					listSelected.append(plat)
					added = True
					break						
			# Verifying if the tag was provided
			if not added:
				for t in plat.tags:
					if t in tags:
						listSelected.append(plat)
						added = True
						break						
		return listSelected



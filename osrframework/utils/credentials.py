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
import osrframework.utils.config_credentials as c_creds

def getCredentials():
	''' 
		Recovering the credentials from a file with the following structure:
		
		:return: A dictionary with the following struture:
			{ "platform1": [C1<Credential>, C2<Credential>], "platform2": [C3<Credential>]}
	'''
	logger = logging.getLogger("osrframework.utils")
	# Dictionary of lists:
	# 	{'Twitter': {cred1, cred2, ...}}
	creds = {} 
	try:
		contenido = c_creds.returnListOfCreds()
		#contenido = ["demo	champ2001	hacker"]
		for l in contenido:
			plat, user, password = l
			c = Credential(user, password)

			if plat not in creds.keys():
				creds[plat] = [c]
			else:
				creds[plat] = creds[plat].append(c)
		logger.info(str(len(contenido)) + " credentials have been loaded.")	
		return creds
	except:
		logger.error("The user credentials file could not be opened. Check if you have installed it in python.")
	logger.debug("No credentials were loaded.")	
	return {}

class Credential():
	""" 
		Class to match the credentials needed by a platform.
	"""
	def __init__(self, user, password):
		""" 
			Creation of the credentials.
			
			:param user:	Login name.
			:param password:	Password.
		"""
		self.user = user
		self.password = password


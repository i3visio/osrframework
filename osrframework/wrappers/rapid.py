# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of usufy.py.
#
#	Usufy is free software: you can redistribute it and/or modify
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

from platforms import Platform
import random

import logging

# CHANGE: the name of the object
class Rapid(Platform):
	""" 
		A <Platform> object for Demo using Rapid.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		# CHANGE: The name displayed
		self.platformName = "Rapid"
		# CHANGE: Add the tags for the platform
		self.tags = ["social", "trips"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		# CHANGE: Add the URL below
		self.url = "http://rapid-i.com/rapidforum/index.php?action=profile;user=" + self.NICK_WILDCARD
		# CHANGE: Add the strings to look for when an error appears
		self.notFoundText = ["The user whose profile you are trying to view does not exist."]

		# CHANGE: Add a series of forbidden characters that should NEVER appear in the nicknames to be processed
		self.forbiddenList = [" ", "?"]

		# CHANGE: Whenever credentials are needed this value needs to be True.
		# Any credential (or set of credentials) must be included in the utils/creds.txt file in the following format:
		#	platform	login	password
		# (The gaps in between are tabs).
		# More than one credental can be stored in that file. Usufy.py will choose one randomly.
		self._needsCredentials = True

		# The empty list of credentials... This list will be loaded when running the program...
		self.creds = []

	def _getAuthenticated(self, uBrowser):
		""" 
                       Getting authenticated to a given browser <UsufyBrowser> type.
		"""
		logger = logging.getLogger("usufy")

		# Checking if we have credentials loaded for this platform. 
		if len(self.creds) > 0:
			# Choosing a random credential from self.creds
			c = random.choice(self.creds)
			
			# CHANGE: This is the URL where the system will try to perform the login
			urlLogin = "http://rapid-i.com/rapidforum/"

			r = uBrowser.br.open(urlLogin)

			# CHANGE: Developing options...
			#	True	the forms of the urlLogin page will be shown after executing python usufy.py -n randomnick -p thisplatform. This is used to get more information about how Python understands the login form.
			#	False	the system will try to get connected to the urlLogin form.
			DEVELOPING = False

			if DEVELOPING:
				###########################################################################
				## THE LINES WHICH FOLLOW ARE USED TO CHECK THE FORMS IN THE SITE        ##
				## 	By doing this this way, we can get the NAMES of the input fields ##
				###########################################################################
				print ("Printing forms")
				for i, form in enumerate(uBrowser.br.forms()):
					print ("----------------------")
					print ("This form is form number:\t" + str(i))
					print (str(form))
					print ("----------------------")
				return False
			else:
				######################################################################
				## THE LINES WHICH FOLLOW ARE THE ONES USED IN PRODUCTION           ##
				## 	Here will be performed the action of getting authenticating ##
				######################################################################
				# CHANGE: this number MUST fit the number of the form previously seen
				formNumber = 1 # Change this number with the appropriate number

				# choosing the appropriate form... Nothing to be done
				uBrowser.br.select_form(nr=formNumber)

				# CHANGE: These fields are the name of the LOGIN fields in the form. E. g.: email, username, user, etc.
				loginField = "user" 
				# CHANGE: These fields are the name of the PASSWORD field in the form. E. g.: pass, password, etc.
				passwordField = "passwrd"

				# Assigning the users in the creds.txt file to the form...
				uBrowser.br.form[loginField] = c.user
				uBrowser.br.form[passwordField] = c.password

				# Submitting the authentication request
				uBrowser.br.submit()

			return True
		else:
			logger.debug("No credentials have been added and this platform needs them.")
			return False


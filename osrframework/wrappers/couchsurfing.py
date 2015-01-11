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

##############################################################
# Not working. Need a fix.                                   #
##############################################################

from platforms import Platform

class Couchsurfing(Platform):
	""" 
		A <Platform> object for Coachsurfing.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "Couchsurfing"
		self.tags = ["e-commerce"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		self.url = "https://www.couchsurfing.org/people/" + self.NICK_WILDCARD
		self.notFoundText = ["<title>Couchsurfing - Error 404: PAGE AIN'T HERE</title>"]
		self.forbiddenList = []


    # While the issue cannot be solved on this platform
	def _doesTheUserExist(self, html):
		''' 
		    Method that performs the verification of the existence or not of a given profile. This is a reimplementation of the method found in all the <Platform> objects.	In this case, this will return ALWAYS None because the platform is no longer available.
			
			:param html:    The html text in which the self.notFoundText
			:return :   None if the user was not found in the html text and the html text if the user DOES exist.
		'''
		return None

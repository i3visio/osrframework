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

class Kongregate(Platform):
	""" 
		A <Platform> object for Kongregate.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "Kongregate"
		self.tags = ["e-commerce", "gaming"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		self.url = "http://www.kongregate.com/accounts/" + self.NICK_WILDCARD
		self.notFoundText = ["<h2>Sorry, no account with that name was found.</h2>"]
		self.forbiddenList = []
	

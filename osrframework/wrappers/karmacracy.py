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

class Karmacracy(Platform):
	""" 
		A <Platform> object for Karmacracy.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "Karmacracy"
		self.tags = ["social", "tools"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		self.url = "http://karmacracy.com/" + self.NICK_WILDCARD
		self.notFoundText = ["page not found", "404 error"]
		self.forbiddenList = []
		self.score= 10.0

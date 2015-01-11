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

class Spotify(Platform):
	""" 
		A <Platform> object for Spotify.
	"""
	def __init__(self):
		'''  
			Constructor... 
		'''
		self.platformName = "Spotify"
		self.tags = ["social", "music"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		self.url = "http://open.spotify.com/user/" + self.NICK_WILDCARD
		#self.notFoundText = ["<h3>Top Tracks</h3>"]
		self.forbiddenList = [" "]	

        def _doesTheUserExist(self, html):
                ''' 
                        Method that performs the verification of the existence or not of a given profile. This method has been rewritten as the standard notFoundText approach is not possible and we have to look for text that appears on VALID profiles.
                '''
                # this platform requires a special treatment, as we have been able to identify only characterized text that appears when a user exists
                userExistsText = ["<h3>Top Tracks</h3>"]
                # the traditional function is rewritten...
                for t in userExistsText:
                        if t in html:
                                return html
                return None


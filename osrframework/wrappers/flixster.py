# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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

from platforms import Platform

class Flixster(Platform):
    """ 
        A <Platform> object for Flixster.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Flixster"
        self.tags = ["opinions"]
        self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
        self.url = "http://community.flixster.com/user/" + self.NICK_WILDCARD
        self.notFoundText = ["<title>Oops!</title>"]
        self.forbiddenList = []
        # CHANGE: Whenever credentials are needed this value needs to be True.
        # Any credential (or set of credentials) must be included in the utils/creds.txt file
        self._needsCredentials = True        


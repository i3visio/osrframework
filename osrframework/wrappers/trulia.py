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

class Trulia(Platform):
    """ 
        A <Platform> object for Trulia.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Trulia"
        self.tags = ["contact", "professional", "social"]
        self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
        self.url = "http://activerain.trulia.com/profile/" + self.NICK_WILDCARD
        self.notFoundText = ["Welcome to the ActiveRain Real Estate Community!"]
        self.forbiddenList = []


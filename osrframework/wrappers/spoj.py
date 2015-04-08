# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This file is part of usufy.py.
#
#    Usufy is free software: you can redistribute it and/or modify
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

class Spoj(Platform):
    """ 
        A <Platform> object for Spoj.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Spoj"
        # Add the tags for the platform
        self.tags = ["social", "news"]
        self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
        # Add the URL below
        self.url = "http://www.spoj.com/users/" + self.NICK_WILDCARD
        # Add the strings to look for when an error appears
        self.notFoundText = []
        # NOTE: IN THIS CASE THE TEXT IS THE TEXT THAT EXISTS
        self.foundText = [">History of submissions</a>"]
        self.forbiddenList = []

    def _doesTheUserExist(self, html):
        ''' 
            Method that performs the verification of the existence or not of a given profile. This method may be rewrritten.
            
            :param html:    The html text in which the self.notFoundText
            :return :   None if the user was not found in the html text and the html text if the user DOES exist.            
        '''
        for t in self.foundText:
            if t in html:
                return html
        return None
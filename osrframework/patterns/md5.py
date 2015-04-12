# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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


from osrframework.utils.regexp import RegexpObject

class MD5(RegexpObject):
    ''' 
        <MD5> class.
    '''
    def __init__(self):
        ''' 
            Constructor without parameters.
            Most of the times, this will be the ONLY method needed to be overwritten.

            :param name:    string containing the name of the regular expression.
            :param reg_exp:    string containing the regular expresion.
        '''
        # This is the tag of the regexp
        self.name = "i3visio.md5"
        # This is the string containing the reg_exp to be seeked
        self.reg_exp = ["[^a-zA-Z0-9]" + "([a-z0-9]{32}|[A-Z0-9]{32})" + "[^a-zA-Z0-9]"]
        

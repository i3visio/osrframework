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

class DNI(RegexpObject):
    ''' 
        <DNI> class.
    '''
    def __init__(self):
        ''' 
            Constructor without parameters.
            Most of the times, this will be the ONLY method needed to be overwritten.

            :param name:    string containing the name of the regular expression.
            :param reg_exp:    string containing the regular expresion.
        '''
        # This is the tag of the regexp
        self.name = "i3visio.dni"
        # This is the string containing the reg_exp to be seeked
        self.reg_exp = ["[^a-zA-Z1-9]" + "[0-9]{7,8}[\-\ ]?[a-zA-Z]" +"[^a-zA-Z1-9]"]
        
    def isValidExp(self, exp):
        '''     
            Method to verify if a given expression is correct just in case the used regular expression needs additional processing to verify this fact.$
            This method will be overwritten when necessary.

            :param exp:     Expression to verify.

            :return:        True | False
        '''
        # order of the letters depending on which is the mod of the number
        #         0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23
        order = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

        #print exp
        l = exp[len(exp)-1]

        try:
            # verifying if it is an 8-length number
            number = int(exp[0:7])
            if l == order[number%23]:
                return True                            
        except:
            try:
                # verifying if it is a 7-length number
                number = int(exp[0:6])
                if l == order[number%23]:
                    return True                
            except:
                # not a  valid number
                return False
        return False
            


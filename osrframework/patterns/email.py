# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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


from osrframework.utils.regexp import RegexpObject

class Email(RegexpObject):
    ''' 
        <Email> class. It identifies emails that include:
            foo@bar.com
            foo[at]bar[dot]com
            foo[arroba]bar[punto]com
            foo [at] bar [dot] com
    '''
    def __init__(self):
        ''' 
            Constructor without parameters.
            Most of the times, this will be the ONLY method needed to be overwritten.

            :param name:    string containing the name of the regular expression.
            :param reg_exp:    string containing the regular expresion.
        '''
        # This is the tag of the regexp
        self.name = "i3visio.email"
        # This is the string containing the reg_exp to be seeked
        self.reg_exp = ["([a-zA-Z0-9\.\-_]+(?:@| ?\[(?:arroba|at)\] ?)[a-zA-Z0-9\.\-]+(?:\.| ?\[(?:punto|dot)\] ?)[a-zA-Z]+)"]

        # This will be the expression to be processed. This variable only exists in this class:
        self.substitutionValues= {}
        self.substitutionValues["@"]= [' at ',' arroba ', '[at]', '[arroba]', ' [at] ', ' [arroba] ']
        self.substitutionValues["."]= [' dot ', ' punto ', '[dot]', '[punto]', ' [dot] ', ' [punto] ']

    def getAttributes(self, found = None):
        '''
            Method to extract additional attributes from a given expression (i. e.: domains and ports from URL and so on). This method may be overwritten in certain child classes.
            :param found:   expression to be processed.
            :return:    The output format will be like:
                [{"type" : "i3visio.email", "value": "foo@bar.com", "attributes": [] }, {"type" : "i3visio.domain", "value": "foo.com", "attributes": [] }]
        '''
        # List of attributes
        results = []
        
        if not '@' in found:    
            # character may be '@' or '.'
            for character in self.substitutionValues.keys():
                for value in self.substitutionValues[character]:
                    # replacing '[at]' for '@'...
                    found=found.replace(value, character)
                
            # Building the auxiliar  email
            aux = {}
            aux["type"] = "i3visio.email"
            aux["value"] = found
            aux["attributes"] = []
            results.append(aux)   
        else:
            # Getting the information of the alias:
            aux = {}
            aux["type"] = "i3visio.alias"
            aux["value"] = found.split('@')[0]
            aux["attributes"] = []
            results.append(aux)           

            # Getting the information of the domain:
            aux = {}
            aux["type"] = "i3visio.domain"
            aux["value"] = found.split('@')[1]
            aux["attributes"] = []
            results.append(aux)         
        
        return results

    def getEntityType(self, found = None):
        '''
            Method to recover the value of the entity in case it may vary. 
            :param found:   The expression to be analysed.
            :return:    The entity type returned will be an s'i3visio.email' for foo@bar.com and an 'i3visio.text' for foo[at]bar[dot]com.
        '''
        # character may be '@' or '.'
        for character in self.substitutionValues.keys():
            for value in self.substitutionValues[character]:
                if value in found:
                    return "i3visio.text"
        # If none of the values were found... Returning as usual the 'i3visio.email' string.
        return self.name



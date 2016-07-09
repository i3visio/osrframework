# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of OSRFramework.
#
#	OSRFramework is free software: you can redistribute it and/or modify
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


import os
import re
import copy
# logging imports
import logging

class RegexpObject():
    ''' 
        <RegexpObject> class.
    '''
    def __init__(self):
        ''' 
            Constructor without parameters...
            Most of the times, this will be the ONLY method needed to be overwritten.
        '''
        # This is the tag of the regexp
        self.name = "<empty>"
        # This is the string containing the regexp to be seeked
        self.reg_exp = []


    def __init__(self, name, reg_exp):
        ''' 
            Constructor with parameters. This method permits the developer to instantiate dinamically <RegexpObject> objects.

            :param name:    string containing the name of the regular expression.
            :param reg_exp:    list of strings containing the regular expresion.
        '''
        # This is the tag of the regexp
        self.name = name
        # This is the string containing the reg_exp to be seeked
        self.reg_exp = [reg_exp]

        
    def __str__(self):
        ''' 
            Function to obtain the text that represents this object.
            
            :return:    str(self.getJson())
        '''
        return str(self.getResults())

    def getAttributes(self, found = None):
        '''
            Method to extract additional attributes from a given expression (i. e.: domains and ports from URL and so on). This method may be overwritten in certain child classes.
            :param found:   expression to be processed.
            :return:    The output format will be like:
                [{"type" : "i3visio.email", "value": "foo@bar.com", "attributes": [] }, {"type" : "i3visio.email", "value": "bar@foo.com", "attributes": [] }]
        '''
        return []

    def getEntityType(self, found = None):
        '''
            Method to recover the value of the entity in case it may vary. By default this method does nothing but returning the entity type. However, some plugins may have to choose the entity type. This method may be overwritten in certain child classes.
            :param found:   The expression to be analysed.
            :return:    The entity type to be provided.
        '''
        return self.name

    def getValue(self, found = None):
        '''
            Method to recover the value of the entity in case it needs any kind of processing. By default this method does nothing but returning the value. However, some plugins may need transformations such as the foo[at]bar[dot]com to be foo@bar.com. This method may be overwritten in certain child classes.
            :param found:   The expression to be analysed.
            :return:    Any kind of transformed value.
        '''
        return found
        
    def getResults(self, parFound = None):
        ''' 
            Function to obtain the Dictionarythat represents this object.
            
            :param parFound:    values to return.

            :return:    The output format will be like:
                [{"type" : "i3visio.email", "value": "foo@bar.com", "attributes": [] }, {"type" : "i3visio.email", "value": "bar@foo.com", "attributes": [] }]
        '''
        # Defining a dictionary
        results = []
        # Defining a dictionary inside with a couple of fields: reg_exp for the regular expression and found_exp for the expressions found.
        #results[self.name] = {"reg_exp" : self.reg_exp, "found_exp" : parFound}
        #results[self.name] = parFound
        if len(parFound ) >0:
            for found in parFound:
                aux = {}
                aux["type"] = self.getEntityType(found)
                aux["value"] = self.getValue(found)
                aux["attributes"] = self.getAttributes(found)
                results.append(aux)
        return results

    def isValidExp(self, exp):
        '''    
            Method to verify if a given expression is correct just in case the used regular expression needs additional processing to verify it.
            This method will be overwritten when necessary.

            :param exp:    Expression to verify.

            :return:    True | False
        '''
        return True        


    def findExp(self, data):
        ''' 
            Method to look for the current regular expression in the provided string.

            :param data:    string containing the text where the expressions will be looked for.

            :return:    a list of verified regular expressions.
        '''
        temp = []
        for r in self.reg_exp:
            try:
                temp += re.findall(r,  data)        
            except:
                print self.name
                print r
                print "CABOOOOM!"
    
        verifiedExp = []
        # verification
        for t in temp:
            # Remember: the regexps include two extra charactes (before and later) that should be removed now.
            if self.isValidExp(t):
                if t not in verifiedExp:
                    verifiedExp.append(t)

        return self.getResults(verifiedExp)
        
        
    def __str__(self):
        ''' 
            Function to represent the text when printing the object
            
            :return:    self.platformName
        '''
        try:
            return self.name        
        except:
            return "UNKNOWN_NAME"    

    def __eq__(self, obj):
        ''' 
            Function to check if two wrappers are the same based on the convention.

            :return:    True or False
        '''
        return self.name == obj.name

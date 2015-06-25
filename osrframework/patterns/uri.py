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

import re
from osrframework.utils.regexp import RegexpObject

class URI(RegexpObject):
    ''' 
        <URI> class.
    '''
    def __init__(self):
        ''' 
            Constructor without parameters.
            Most of the times, this will be the ONLY method needed to be overwritten.

            :param name:    string containing the name of the regular expression.
            :param reg_exp:    string containing the regular expresion.
        '''
        # This is the tag of the regexp
        self.name = "i3visio.uri"
        # This is the string containing the reg_exp to be seeked. The former and latter characters are not needed.
        #self.reg_exp = ["((?:https?|s?ftp|file)://[a-zA-Z0-9\_\.\-]+(?:\:[0-9]{1,5})(?:/[a-zA-Z0-9\_\.\-/=\?&]+))"]
        self.reg_exp = ["((?:https?|s?ftp|file)://[a-zA-Z0-9\_\.\-]+(?:\:[0-9]{1,5}|)(?:/[a-zA-Z0-9\_\.\-/=\?&]+|))"]
        #self.reg_exp = ["((?:https?|s?ftp|file)://[a-zA-Z0-9\_\.\-]+(?:/[a-zA-Z0-9\_\.\-/=\?&%]+))"]

    def getAttributes(self, foundExp):
        '''
            Method to extract additional attributes from a given expression (i. e.: domains and ports from URL and so on). This method may be overwritten in certain child classes.
            :param found_exp:   expression to be processed.
            :return:    The output format will be like:
                [{"type" : "i3visio.domain", "value": "twitter.com", "attributes": [] }, {"type" : "i3visio.protocol", "value": "http", "attributes": [] }]
        '''
        # Defining a dictionary
        attributes = []
        
        protocolRegExp = "((?:https?|s?ftp|file))://"
        foundProtocol = re.findall(protocolRegExp, foundExp)
        if len(foundProtocol) > 0:        
            # Defining a protocol element
            aux = {}
            aux["type"] = "i3visio.protocol"
            # Defining the regular expression to extract the protocol from a URL
            aux["value"] = foundProtocol[0]
            # Each attributes will be swept
            aux["attributes"] = []
            attributes.append(aux)

        domainRegExp = "(?:https?|s?ftp)://([a-zA-Z0-9\_\.\-]+)(?:\:|/)"
        foundDomain = re.findall(domainRegExp, foundExp)
        if len(foundDomain) > 0:
            # Defining a domain element
            aux = {}
            aux["type"] = "i3visio.domain"
            # Inserting the found domain
            aux["value"] = foundDomain[0]
            # Each attributes will be swept
            aux["attributes"] = []
            attributes.append(aux)

        portRegExp = "(?:https?|s?ftp)://[a-zA-Z0-9\_\.\-]+:([0-9]{1,5})/"
        foundPort = re.findall(portRegExp, foundExp)
        if len(foundPort) > 0:
            # Defining a domain element
            aux = {}
            aux["type"] = "i3visio.port"
            # Inserting the found domain
            aux["value"] = foundPort[0]
            # Each attributes will be swept
            aux["attributes"] = []
            attributes.append(aux)

        return attributes

        

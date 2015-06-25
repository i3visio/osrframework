# !/usr/bin/python
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

import json
import sys
import urllib2

from osrframework.transforms.lib.maltego import *
import osrframework.thirdparties.haveibeenpwned_com.checkIfEmailWasHacked as HIBP

def emailToBreachedAccounts(email=None):
    ''' 
        Method that checks if the given email is stored in the HIBP website.

        :param email:    email to verify.

    '''
    me = MaltegoTransform()

    jsonData = HIBP.checkIfEmailWasHacked(email=email)

    # This returns a dictionary like:
    # [{"Title":"Adobe","Name":"Adobe","Domain":"adobe.com","BreachDate":"2013-10-4","AddedDate":"2013-12-04T00:12Z","PwnCount":152445165,"Description":"The big one. In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and <a href=\"http://stricture-group.com/files/adobe-top100.txt\" target=\"_blank\">many were quickly resolved back to plain text</a>. The unencrypted hints also <a href=\"http://www.troyhunt.com/2013/11/adobe-credentials-and-serious.html\" target=\"_blank\">disclosed much about the passwords</a> adding further to the risk that hundreds of millions of Adobe customers already faced.","DataClasses":["Email addresses","Password hints","Passwords","Usernames"]}]
    
    newEntities = []

    for breach in jsonData:
        # Defining the main entity
        aux ={}
        aux["type"] = "i3visio.breach"
        aux["value"] =  str(breach["Title"])
        aux["attributes"] = []

        # Defining the attributes recovered
        att ={}
        att["type"] = "i3visio.domain"
        att["value"] =  str(breach["Domain"])
        att["attributes"] = []
        aux["attributes"].append(att)

        att ={}
        att["type"] = "@added_date"
        att["value"] =  str(breach["AddedDate"])
        att["attributes"] = []
        aux["attributes"].append(att)

        att ={}
        att["type"] = "@breach_date"
        att["value"] =  str(breach["BreachDate"])
        att["attributes"] = []
        aux["attributes"].append(att)

        att ={}
        att["type"] = "@total_pwned"
        att["value"] =  str(breach["PwnCount"])
        att["attributes"] = []
        aux["attributes"].append(att)
   
        att ={}
        att["type"] = "@description"
        att["value"] =  str(breach["Description"])
        att["attributes"] = []
        aux["attributes"].append(att)
   
        # Appending the entity
        newEntities.append(aux)

    me.addListOfEntities(newEntities)

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    emailToBreachedAccounts(email=sys.argv[1])



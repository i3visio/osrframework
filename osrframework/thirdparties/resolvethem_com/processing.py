# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
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

import argparse
import re
import requests
import urllib

def checkIPFromAlias(alias=None):
    ''' 
		Method that checks if the given alias is currently connected to Skype and returns its IP address. 

		:param alias:	Alias to be searched.

		:return:	Python structure for the Json received. It has the following structure:
	        {
              "type": "i3visio.ip",
              "value": "1.1.1.1",
              "attributes" : []
            }
	'''
    headers = {
    "Content-type": "text/html",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": " gzip, deflate",
    "Accept-Language": " es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "www.resolvethem.com",
    "Referer": "http://www.resolvethem.com/index.php",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Content-Length": "26",
    "Content-Type": "application/x-www-form-urlencoded",
    }    
    
    req = requests.post("http://www.resolvethem.com/index.php",headers=headers,data={'skypeUsername': alias,'submit':''})
    # Data returned
    data = req.content
    # Compilation of the regular expression
    p = re.compile("class='alert alert-success'>([0-9\.]*)<")
    allMatches = p.findall(data)
    if len(allMatches)> 0:
        jsonData = {}
        jsonData["type"]="i3visio.ip"
        jsonData["value"]=allMatches[0]
        jsonData["attributes"]=[]     
        return jsonData
    return {}




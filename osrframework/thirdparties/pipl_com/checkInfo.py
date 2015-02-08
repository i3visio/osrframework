# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
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

import argparse
import json
import osrframework.utils.config_api_keys as config_api_keys
import sys
import urllib2

from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest, SearchAPIError
from osrframework.thirdparties.pipl_com.lib import Person, Name, Address, Job

def checkInfo(email=None, username=None, api_key=None):
    ''' 
        Method that checks if the given hash is stored in the pipl.com website. 

        :param email: queries to be launched.
        :param api_key: api_key to be used in pipl.com. If not provided, the API key will be searched in the config_api_keys.py file.

        :return:    Python structure for the Json received. It has the following structure:
    '''
    # This is for i3visio
    if api_key==None:
        #api_key = raw_input("Insert the API KEY here:\t")
        allKeys = config_api_keys.returnListOfAPIKeys()
        try: 
            api_key = allKeys["pipl_com"]
        except:
            # API_Key not found. The samplekey will be used but it has a limit of 10 queries/day.
            api_key = "samplekey"            

    results = {}
    results["person"] = []
    results["records"] = []    

    if username != None:
        request = SearchAPIRequest( username=username, api_key=api_key)
        person, records = launchRequest(request)
        # Appending the results 
        results["person"].append(person)
        results["records"].append(records)        
    if email != None:
        request = SearchAPIRequest( email=email, api_key=api_key)
        person, records = launchRequest(request)
        # Appending the results 
        results["person"].append(person)
        results["records"].append(records)        
    return results
    

def launchRequest(request):
    '''
        Method to launch a given request.
        
        :param request: The request object.
        
        :return:    A dictionary containinf the results of the person and a list of dicts containing the references for the record.
    '''
    person = {}
    records = []
   
    try:
        response = request.send()
        # Trying to recover a person object. This is a dict:
        try:
            person = (response.person).to_dict()
        except:
            pass                
        # Trying to recover a list of record objects. This is a list dicts
        try:
            aux = response.records 
            records = [r.to_dict() for r in aux]
        except:
            pass
    except SearchAPIError as e:
        print e.http_status_code, e    
        
    return  person, records
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps a search onto pipl.com API.', prog='checkInfo.py', epilog="NOTE: if not provided, the API key will be searched in the config_api_keys.py file.", add_help=False)
    # Adding the main options

    parser.add_argument('-a', '--api_key', action='store', help='API key in pipl.com to be used.', required=False)

    # Defining the mutually exclusive group for the main options
    groupQueries = parser.add_mutually_exclusive_group(required=True) 
    groupQueries.add_argument('-e', '--email', metavar='<email>', action='store', help='query to be performed to pipl.com.')        
    groupQueries.add_argument('-u', '--username', metavar='<email>', action='store', help='query to be performed to pipl.com.')        
        
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        

    print json.dumps(checkInfo(email=args.email, username=args.username, api_key=args.api_key), indent=2)



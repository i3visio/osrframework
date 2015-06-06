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

import argparse
import json

import osrframework.thirdparties.skype.checkInSkype as skype

def checkInSkype(args):
    '''
    '''
    if args.query != None:
        return skype.checkInSkype(args.query)
    elif args.file != None:
        results = []
        with open(args.file, "r") as iF:
            queries = iF.read().splitlines()
            
            for q in queries:
                print "Performing query:\t"+q
                results += skype.checkInSkype(args.query)
        return results
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps a search onto Skype4Py.', prog='checkInSkype.py', epilog="NOTE: you must be logged in into Skype to use this program.", add_help=False)

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    general.add_argument('-q', '--query', metavar='<text_to_search>', action='store', help='query to be launched.')        
    general.add_argument('-f', '--file', metavar='<path_to_search_file>', action='store', help='path to the search file.')            
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        
    
    print json.dumps(checkInSkype(args), indent = 2)

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

''' 
searchfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2015
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
    python searchfy.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2015, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v0.1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import json

import osrframework.utils.platform_selection as platform_selection


def performSearch(platformNames=[], queries=[]):
    ''' 
        Method to perform the phone list.
        
        :param platforms: List of <Platform> objects.
        :param queries: List of queries to be performed.
        
        :return:
    '''
    # Grabbing the <Platform> objects
    platforms = platform_selection.getPlatformsByName(platformNames, mode="searchfy")    
    
    results = []
    for q in queries:
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.getInfo(query=q, process = True, mode="searchfy")
            if entities != {}:
                results.append(json.loads(entities))
    return results

def searchfy_main(args):
    ''' 
        Main program.
        
        :param args: Arguments received in the command line.
    '''

    
    results = performSearch(platformNames=args.platforms, queries=args.queries)

    # Printing the results
    if not args.quiet:
        print json.dumps(results, indent=2) 

    # Writing the results onto a file
    if args.output_file != None:
        with open(output_file, "w") as oF:
            oF.write(json.dumps(results, indent=2) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='searchfy.py - Piece of software that performs a query on the platforms in OSRFramework.', prog='searchfy.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    general.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')    
    general.add_argument('-q', '--queries', metavar='<searches>', nargs='+', action='store', help = 'the list of queries to be performed).')

    listAll = platform_selection.getAllPlatformNames("searchfy")

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which searchfy will process the identified profiles.')
    #groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')        
    groupProcessing.add_argument('-o', '--output_file',  metavar='<path_to_output_file>',  action='store', help='path to the output file where the results will be stored in json format.', required=False)
    groupProcessing.add_argument('-p', '--platforms', metavar='<platform>', choices=listAll, nargs='+', required=False, default =['all'] ,action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(listAll) + '. More than one option can be selected.')    
    groupProcessing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')        

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    #groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +__version__, help='shows the version of the program and exists.')

    args = parser.parse_args()    

    # Calling the main function
    searchfy_main(args)

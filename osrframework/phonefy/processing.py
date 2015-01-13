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

import json

import osrframework.phonefy.config_phonefy as config

def processPhoneList(platforms=[], numbers=[]):
    ''' 
        Method to perform the phone list.
        
        :param platforms: List of <Platform> objects.
        :param numbers: List of numbers to be queried.
        
        :return:
    '''
    results = {}
    for num in numbers:
        for pla in platforms:
            results.update(pla.getInfo(query=num, process = True, mode="phonefy"))
    return results

def phonefy_main(args):
    ''' 
        Main program.
        
        :param args: Arguments received by parameter
    '''
    platforms = config.getPlatformsByName(args.platforms)
    numbers = args.numbers
    
    results = processPhoneList(platforms=platforms, numbers=numbers)

    if not args.quiet:
        print json.dumps(results, indent=2)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
enumeration.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
import argparse
import os
import os.path
import osrframework.utils.banner as banner
import osrframework.utils.browser as browser
import re

__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2016, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v1.0.2"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"

def enumerateURL(urlDict, outputFolder, startIndex= 0, maxErrors = 100):

    for i, url in enumerate(urlDict.keys()):
        # Grabbing domain name:
        domain = re.findall("://(.*)/", url)[0]

        # Defining the starting index
        index = startIndex

        # The app will stop when this value reaches maxErrors
        consecutiveErrors = 0

        i3Browser = browser.Browser()

        # Main loop
        while consecutiveErrors <= maxErrors:
            # creating the new URL to download
            newQuery = url.replace("<INDEX>", str(index))
            print newQuery
            # Downloading the file
            try:

                data = i3Browser.recoverURL(newQuery)
                print "Data recovered..."
                filename = domain + "_" + "-profile_" + str(index).rjust(10, "0") +".html"
                if urlDict[url] != None:
                    if urlDict[url] in data:
                        print "Storing resource as:\t" + filename + "..."
                        # The profile was found  so we will store it:
                        with open( outputFolder + "/" + filename, "w") as oF:
                            oF.write(data)
                else:
                    # The profile was found  so we will store it:
                    print "Storing resource as:\t" + filename + "..."
                    with open( outputFolder + "/" + filename, "w") as oF:
                        oF.write(data)
            except:
                pass
                #logger.error("The resource could not be downloaded.")

            index+=1
def enumeration_main(args):
    '''
        Main loop.
    '''
    sayingHello = """enumeration.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit <http://www.gnu.org/licenses/gpl-3.0.txt>."""
    #logger.info(sayingHello)
    print banner.text


    print sayingHello
    print
    # Loading URL
    urlDict = {}
    if args.url !=None:
        urlDict[str(args.url)] = None
    elif args.platforms != None:
        for p in args.platforms:
            with open(args.config, "r") as iF:
                lines = iF.read().splitlines()
                for l in lines:
                    platform = l.split('\t')[0]
                    url = l.split('\t')[1]
                    notFound = l.split('\t')[2]
                    if p == platform:
                        urlDict[url] = notFound
    else:
        return
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Making the call
    enumerateURL(urlDict, args.output_folder, startIndex = args.start_index, maxErrors = args.max_errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='enumeration.py - Checking the existence of a possible enumeration.', prog='enumeration.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    general.add_argument('-u', '--url', metavar='<URL>', action='store', help = 'the URL address to test. The place where the index will be updated should be indicated as <INDEX> in the URL. For example: http://example.com/user/<INDEX> would match "http://example.com/user/1", "http://example.com/user/2", etc. Only those platforms receiving a valid response will be loaded, so NO filter by not-found-tags is permitted in this mode.')
    general.add_argument('-p', '--platforms', metavar='<platform>', nargs='+', action='store', help = 'Selection of a domain found in the configuration file.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    groupProcessing.add_argument('-o', '--output_folder',  metavar='<path_to_output_folder>',  action='store', help='path to the output folder where the results will be stored in raw. The name of the files will be their index.', required=False, default = "./results")
    groupProcessing.add_argument('--config', metavar='<url>',  action='store', default="./utils/enumeration_config.txt", help = 'the file with the list of URL to test. The format should be: "platform_name\\thttp://example.com/user/<INDEX>\\tNOT_FOUND_TEXT".')
    groupProcessing.add_argument('--max_errors',  metavar='<max_errors>',  action='store', help='maximum number of consecutive errors tolerated until finishing the crawling process.', required=False, default = 100, type = int)
    groupProcessing.add_argument('--start_index',  metavar='<start_index>',  action='store', help='starting user index for the crawling process.', required=False, default = 0, type = int)

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s'+" " + __version__ , help='shows the version of the program and exists.')

    args = parser.parse_args()

    # Calling the main function
    enumeration_main(args)

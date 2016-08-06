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
entify.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.  For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2016, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v2.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"

import argparse
# logging imports
import logging
import json
import requests
import os
from os import listdir
from os.path import isfile, join, isdir

# Imports
import osrframework.utils.banner as banner
from osrframework.utils.regexp import RegexpObject
import osrframework.utils.general as general
import osrframework.utils.logger as logSet
import osrframework.utils.regexp_selection as regexp_selection


def getEntitiesByRegexp(data = None, listRegexp = None, verbosity=1, logFolder="./logs"):
    '''
        Method to obtain entities by Regexp.

        :param data:    text where the entities will be looked for.
        :param listRegexp:    list of selected regular expressions to be looked for. If None was provided, all the available will be chosen instead.
        :param verbosity:    Verbosity level.
        :param logFolder:    Folder to store the logs.

        :return:    a list of the available objects containing the expressions found in the provided data.
        [
          {
            "attributes": [],
            "type": "i3visio.email",
            "value": "foo@bar.com"
          },
          {
            "attributes": [],
            "type": "i3visio.email",
            "value": "bar@foo.com"
        ]
    '''
    logSet.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)
    logInstance = logging.getLogger("osrframework.entify")
    if listRegexp == None:
        listRegexp = regexp_selection.getAllRegexp()

    foundExpr = []

    for r in listRegexp:
        foundExpr += r.findExp(data)

    return foundExpr


def scanFolderForRegexp(folder = None, listRegexp = None, recursive = False, verbosity=1, logFolder= "./logs", quiet=False):
    '''
        [Optionally] recursive method to scan the files in a given folder.

        :param folder:    the folder to be scanned.
        :param listRegexp:    listRegexp is an array of <RegexpObject>.
        :param recursive:    when True, it performs a recursive search on the subfolders.

        :return:    a list of the available objects containing the expressions found in the provided data.
        [
          {
            "attributes": [],
            "type": "i3visio.email",
            "value": "foo@bar.com"
          },
          {
            "attributes": [],
            "type": "i3visio.email",
            "value": "bar@foo.com"
          }
        ]
    '''
    logSet.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)
    logger = logging.getLogger("osrframework.entify")

    logger.info("Scanning the folder: " + folder)
    results = []

    #onlyfiles = []
    #for f in listdir(args.input_folder):
    #    if isfile(join(args.input_folder, f)):
    #        onlyfiles.append(f)
    onlyfiles = [ f for f in listdir(folder) if isfile(join(folder,f)) ]

    for i, f in enumerate(onlyfiles):
        filePath = join(folder,f)
        logger.debug("Looking for regular expressions in: " + filePath)
        if not quiet:
            print str(i) + "/" + str(len(onlyfiles)) + "\tLooking for regular expressions in: " + filePath
        with open(filePath, "r") as tempF:
            # reading data
            foundExpr = getEntitiesByRegexp(data = tempF.read(), listRegexp = listRegexp)
            logger.debug("Updating the " + str(len(foundExpr)) + " results found on: " + filePath)
            aux = {}
            aux["type"] = "i3visio.uri"
            aux["value"] = filePath
            aux["attributes"] = foundExpr
            results.append(aux)

    if recursive:
        onlyfolders = [ f for f in listdir(folder) if isdir(join(folder,f)) ]
        for f in onlyfolders:
            folderPath = join(folder, f)
            logger.debug("Looking for additional in the folder: "+ folderPath)
            results.update(scanFolderForRegexp(folder = folderPath,listRegexp = listRegexp, recursive = recursive))

    # Printing the information if not in quiet mode
    if not quiet:
        print json.dumps(results, indent=2)
    #with open("./entify_out.txt", "w") as oF:
    #    oF.write(json.dumps(results, indent=2))
    return results


def scanResource(uri = None, listRegexp = None, verbosity=1, logFolder= "./logs"):
    '''
        [Optionally] recursive method to scan the files in a given folder.

        :param uri:    the URI to be scanned.
        :param listRegexp:    listRegexp is an array of <RegexpObject>.

        :return:    a dictionary where the key is the name of the file.
    '''
    logSet.setupLogger(loggerName="osrframework.entify", verbosity=verbosity, logFolder=logFolder)
    logger = logging.getLogger("osrframework.entify")

    results = []
    logger.debug("Looking for regular expressions in: " + uri)

    import urllib2
    data = urllib2.urlopen(uri).read()
    foundExpr = getEntitiesByRegexp(data = data, listRegexp = listRegexp)

    logger.debug("Updating the " + str(len(foundExpr)) + " results found on: " + uri)

    # Creating the output structure
    for f in foundExpr:
        aux = {}

        aux={}
        aux["type"] = "i3visio.search"
        aux["value"] = "URI - " +f["value"]
        aux["attributes"] = []
        for a in f["attributes"]:
            aux["attributes"].append(a)

        #Appending the entity itself
        entity={}
        entity["type"] = f["type"]
        entity["value"] = f["value"]
        entity["attributes"] = []
        aux["attributes"].append(entity)

        #Appending the uri
        entity={}
        entity["type"] = "i3visio.uri"
        entity["value"] = uri
        entity["attributes"] = []
        aux["attributes"].append(entity)

        results.append(aux)

    return results

def main(args):
    '''
        Main function. This function is created in this way so as to let other applications make use of the full configuration capabilities of the application.
    '''
    # Recovering the logger
    # Calling the logger when being imported
    logSet.setupLogger(loggerName="osrframework.entify", verbosity=args.verbose, logFolder=args.logfolder)
    # From now on, the logger can be recovered like this:
    logger = logging.getLogger("osrframework.entify")

    logger.info("""entify.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.""")

    logger.info("Selecting the regular expressions to be analysed...")

    sayingHello = """entify.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit <http://www.gnu.org/licenses/gpl-3.0.txt>."""
    if not args.quiet:
        print banner.text

        print sayingHello
        print
        logger.info("Starting entify.py")

    listRegexp = []
    if args.regexp:
        listRegexp = regexp_selection.getRegexpsByName(args.regexp)
    elif args.new_regexp:
        for i, r in enumerate(args.new_regexp):
            listRegexp.append(RegexpObject(name = "NewRegexp"+str(i), reg_exp = args.new_regexp))

    if not args.web:
        results = scanFolderForRegexp(folder = args.input_folder, listRegexp= listRegexp, recursive = args.recursive, verbosity=args.verbose, logFolder= args.logfolder, quiet=args.quiet)
    else:
        results = scanResource(uri = args.web, listRegexp= listRegexp, verbosity=args.verbose, logFolder= args.logfolder)
    logger.info("Logging the results:\n" + json.dumps(results, indent=2, sort_keys=True))

    # Trying to store the information recovered
    if args.output_folder != None:
        # Verifying an output folder was selected
        logger.debug("Preparing the output folder...")
        if not os.path.exists(args.output_folder):
            logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
            os.makedirs(args.output_folder)

        # Grabbing the results
        fileHeader = os.path.join(args.output_folder, args.file_header)
        for ext in args.extension:
            # Generating output files
            general.exportUsufy(results, ext, fileHeader)

    # Showing the information gathered if requested
    if not args.quiet:
        print "A summary of the results obtained are shown in the following table:"
        print unicode(general.usufyToTextExport(results))
        print

        print "You can find all the information collected in the following files:"
        for ext in args.extension:
            # Showing the output files
            print "\t-" + fileHeader + "." + ext

    # Urging users to place an issue on Github...
    if not args.quiet:
        print
        print "Did something go wrong? Is a platform reporting false positives? Do you need to integrate a new one?"
        print "Then, place an issue in the Github project: <https://github.com/i3visio/osrframework/issues>."
        print "Note that otherwise, we won't know about it!"
        print

    return results


def getParser():
    import osrframework.utils.configuration as configuration
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("entify")

    parser = argparse.ArgumentParser(description='entify.py - entify.py is a program designed to extract using regular expressions all the entities from the files on a given folder. This software also provides an interface to look for these entities in any given text.', prog='entify.py', epilog="Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.", add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    listAll = regexp_selection.getAllRegexpNames()
    groupMainOptions.add_argument('-r', '--regexp', metavar='<name>', choices=listAll, action='store', nargs='+', help='select the regular expressions to be looked for amongst the following: ' + str(listAll))
    groupMainOptions.add_argument('-R', '--new_regexp', metavar='<regular_expression>', action='store', help='add a new regular expression, for example, for testing purposes.')

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    groupInput = parser.add_mutually_exclusive_group(required=True)
    groupInput.add_argument('-i', '--input_folder',  metavar='<path_to_input_folder>', default=None, action='store',  help='path to the folder to analyse.')
    groupInput.add_argument('-w', '--web',  metavar='<url>',  action='store', default=None, help='URI to be recovered and analysed.')

    # adding the option
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the processing parameters.')
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'mtz', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default = DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default = DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    # Getting a sample header for the output files
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default = DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('-q', '--quiet', required=False, action='store_true', default=False, help='Asking the program not to show any output.')
    groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    groupProcessing.add_argument('--recursive', action='store_true', default=False, required=False, help='Variable to tell the system to perform a recursive search on the folder tree.')

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s '+" " +__version__, help='shows the version of the program and exists.')

    return parser

if __name__ == "__main__":
    # Grabbing the parser
    parser = getParser()

    args = parser.parse_args()

    # Recovering the logger
    # Calling the logger when being imported
    logSet.setupLogger(loggerName="osrframework", verbosity=args.verbose, logFolder=args.logfolder)
    # From now on, the logger can be recovered like this:
    logger = logging.getLogger("osrframework")

    main(args)

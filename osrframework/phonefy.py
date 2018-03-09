#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2015-2018 Félix Brezo and Yaiza Rubio
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


import argparse
import datetime as dt
import json
import os
import sys

import osrframework
import osrframework.utils.banner as banner
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general


def processPhoneList(platformNames=[], numbers=[], excludePlatformNames=[]):
    """
        Method to perform the phone list.

        :param platformNames: List of names fr the platforms.
        :param numbers: List of numbers to be queried.

        :return:
    """
    # Grabbing the <Platform> objects
    platforms = platform_selection.getPlatformsByName(platformNames, mode="phonefy", excludePlatformNames=excludePlatformNames)

    results = []
    for num in numbers:
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.getInfo(query=num, process = True, mode="phonefy")
            if entities != {}:
                results+=json.loads(entities)
    return results


def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("phonefy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        excludeList = []

    parser = argparse.ArgumentParser(description='phonefy - Piece of software that checks the existence of a given series of phones in a bunch of phone number lists associated to malicious activities.', prog='phonefy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-n', '--numbers', metavar='<phones>', nargs='+', action='store', help = 'the list of phones to process (at least one is required).')

    listAll = platform_selection.getAllPlatformNames("phonefy")

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
    #groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-p', '--platforms', metavar='<platform>', choices=listAll, nargs='+', required=False, default=DEFAULT_VALUES["platforms"] ,action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(listAll) + '. More than one option can be selected.')
    # Getting a sample header for the output files
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')
    groupProcessing.add_argument('-w', '--web_browser', required=False, action='store_true', help='opening the URIs returned in the default web browser.')
    groupProcessing.add_argument('-x', '--exclude', metavar='<platform>', choices=listAll, nargs='+', required=False, default=excludeList, action='store', help='select the platforms that you want to exclude from the processing.')


    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """
    Main function to launch phonefy.

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `getParser()`.

    Args:
    -----
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point.

    Returns:
    --------
        A list of i3visio entities.
    """
    # Grabbing the parser
    parser = getParser()

    if params != None:
        args = parser.parse_args(params)
    else:
        args = parser.parse_args()

    results = []

    if not args.quiet:
        print(general.title(banner.text))

        sayingHello = """
Phonefy | Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2018

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit """ + general.LICENSE_URL + "\n"
        print(general.title(sayingHello))

    if args.license:
        general.showLicense()
    else:
        # Showing the execution time...
        startTime= dt.datetime.now()
        #TODO: Get the number searchable platforms in this context
        print(str(startTime) + "\tStarting search in different platform(s)... Relax!\n")
        print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))
        try:
            results = processPhoneList(platformNames=args.platforms, numbers=args.numbers, excludePlatformNames=args.exclude)
        except KeyboardInterrupt:
            print(general.error("\n[!] Process manually stopped by the user. Workers terminated without providing any result.\n"))

        # Trying to store the information recovered
        if args.output_folder != None:
            # Verifying an output folder was selected
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)
            # Grabbing the results
            fileHeader = os.path.join(args.output_folder, args.file_header)
            for ext in args.extension:
                # Generating output files
                general.exportUsufy(results, ext, fileHeader)

        # Showing the information gathered if requested
        if not args.quiet:
            now = dt.datetime.now()
            print(str(now) + "\tA summary of the results obtained is shown in the following table:\n")
            print(general.success(general.usufyToTextExport(results)))

            if args.web_browser:
                general.openResultsInBrowser(results)

            now = dt.datetime.now()
            print("\n" + str(now) + "\tYou can find all the information collected in the following files:")
            for ext in args.extension:
                # Showing the output files
                print("\t" + general.emphasis(fileHeader + "." + ext))

            # Showing the execution time...
            endTime= dt.datetime.now()
            print("\n" + str(endTime) +"\tFinishing execution...\n")
            print("Total time consumed:\t" + general.emphasis(str(endTime-startTime)) + "\n")
            #TODO: Get the number searchable platforms in this context
            #print("Average seconds/query:\t" + general.emphasis(str((endTime-startTime).total_seconds()/len(listPlatforms))) +" seconds\n")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

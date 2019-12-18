################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
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


def perform_search(platformNames=[], queries=[], exclude_platform_names=[]):
    """Method to perform the search itself on the different platforms

    Args:
        platformNames: List of names of the platforms.
        queries: List of queries to be performed.
        exclude_platform_names: A list of platforms not to be searched.

    Returns:
        list: A list with the entities collected.
    """
    # Grabbing the <Platform> objects
    platforms = platform_selection.get_platforms_by_name(platformNames, mode="searchfy", exclude_platform_names=exclude_platform_names)
    results = []
    for q in queries:
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.get_info(query=q, mode="searchfy")
            if entities != "[]":
                results += json.loads(entities)
    return results

def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    DEFAULT_VALUES = configuration.get_configuration_values_for("searchfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        exclude_list = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        exclude_list = []

    parser = argparse.ArgumentParser(description='searchfy - Piece of software that performs a query on the platforms in OSRFramework.', prog='searchfy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    group_main = parser.add_mutually_exclusive_group(required=True)
    group_main.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    group_main.add_argument('-q', '--queries', metavar='<searches>', nargs='+', action='store', help = 'the list of queries to be performed).')

    listAll = platform_selection.get_all_platform_names("searchfy")

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'Configuring the way in which searchfy will process the identified profiles.')
    group_processing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    group_processing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>' )
    group_processing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    group_processing.add_argument('-p', '--platforms', metavar='<platform>', choices=listAll, nargs='+', required=False, default=DEFAULT_VALUES["platforms"] ,action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(listAll) + '. More than one option can be selected.')
    group_processing.add_argument('-w', '--web_browser', required=False, action='store_true', help='opening the URIs returned in the default web browser.')
    group_processing.add_argument('-x', '--exclude', metavar='<platform>', choices=listAll, nargs='+', required=False, default=exclude_list, action='store', help='select the platforms that you want to exclude from the processing.')

    # About options
    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """Main function to launch searchfy

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `get_parser()`.

    Args:
        params (list): A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point. If it is called by osrf
            the data is already parsed.

    Returns:
        list. A list of i3visio entities.
    """
    if params is None:
        parser = get_parser()
        args = parser.parse_args(params)
    else:
        args = params

    results = []

    print(general.title(banner.text))

    saying_hello = f"""
     Searchfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{general.LICENSE_URL}>.
"""
    print(general.info(saying_hello))

    if args.license:
        general.showLicense()
    else:
        # Showing the execution time...
        start_time = dt.datetime.now()
        print(f"{start_time}\tStarting search in different platform(s)... Relax!\n")
        print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))
        # Performing the search
        try:
            results = perform_search(platformNames=args.platforms, queries=args.queries, exclude_platform_names=args.exclude)
        except KeyboardInterrupt:
            print(general.error("\n[!] Process manually stopped by the user. Workers terminated without providing any result.\n"))
            results = []

        # Generating summary files for each ...
        if args.extension:
            # Verifying if the outputPath exists
            if not os.path.exists (args.output_folder):
                os.makedirs(args.output_folder)

            # Grabbing the results
            fileHeader = os.path.join(args.output_folder, args.file_header)

            # Iterating through the given extensions to print its values
            for ext in args.extension:
                # Generating output files
                general.export_usufy(results, ext, fileHeader)

        # Printing the results if requested
        now = dt.datetime.now()
        print(f"\n{now}\tResults obtained:\n")
        print(general.success(general.osrf_to_text_export(results)))

        if args.web_browser:
            general.open_results_in_browser(results)

        now = dt.datetime.now()
        print("\n{date}\tYou can find all the information collected in the following files:".format(date=str(now)))
        for ext in args.extension:
            # Showing the output files
            print("\t" + general.emphasis(fileHeader + "." + ext))

        # Showing the execution time...
        end_time = dt.datetime.now()
        print(f"\n{end_time}\tFinishing execution...\n")
        print("Total time used:\t" + general.emphasis(str(end_time-start_time)))
        print("Average seconds/query:\t" + general.emphasis(str((end_time-start_time).total_seconds()/len(args.platforms))) +" seconds\n")

        # Urging users to place an issue on Github...
        print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

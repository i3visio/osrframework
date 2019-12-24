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


def process_phone_list(platformNames=[], numbers=[], exclude_platform_names=[]):
    """Method to perform searchs on a series of numbers

    Args:
        platformNames: List of names of the platforms.
        numbers: List of numbers to be queried.
        exclude_platform_names: A list of platforms not to be searched.

    Return:
        A list of verified emails.
    """
    # Grabbing the <Platform> objects
    platforms = platform_selection.get_platforms_by_name(platformNames, mode="phonefy", exclude_platform_names=exclude_platform_names)

    results = []
    for num in numbers:
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.get_info(query=num, mode="phonefy")
            if entities != {}:
                results += json.loads(entities)
    return results


def get_parser():
    DEFAULT_VALUES = configuration.get_configuration_values_for("phonefy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        exclude_list = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        exclude_list = []

    parser = argparse.ArgumentParser(description='phonefy - Piece of software that checks the existence of a given series of phones in a bunch of phone number lists associated to malicious activities.', prog='phonefy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    group_main_options = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    group_main_options.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    group_main_options.add_argument('-n', '--numbers', metavar='<phones>', nargs='+', action='store', help='the list of phones to process (at least one is required).')

    list_all = platform_selection.get_all_platform_names("phonefy")

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
    group_processing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    group_processing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    group_processing.add_argument('-p', '--platforms', metavar='<platform>', choices=list_all, nargs='+', required=False, default=DEFAULT_VALUES["platforms"] ,action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(list_all) + '. More than one option can be selected.')
    group_processing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    group_processing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')
    group_processing.add_argument('-w', '--web_browser', required=False, action='store_true', help='opening the URIs returned in the default web browser.')
    group_processing.add_argument('-x', '--exclude', metavar='<platform>', choices=list_all, nargs='+', required=False, default=exclude_list, action='store', help='select the platforms that you want to exclude from the processing.')


    # About options
    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """Main function to launch phonefy

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `get_parser()`.

    Args:
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point. If it is called by osrf
            the data is already parsed.

    Returns:
        A list of i3visio entities.
    """
    if params == None:
        parser = get_parser()
        args = parser.parse_args(params)
    else:
        args = params

    results = []

    if not args.quiet:
        print(general.title(banner.text))

    saying_hello = f"""
     Phonefy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

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

        print(f"\n{start_time}\tStarting search in different platform(s)... Relax!\n")
        print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))
        try:
            results = process_phone_list(platformNames=args.platforms, numbers=args.numbers, exclude_platform_names=args.exclude)
        except KeyboardInterrupt:
            print(general.error("\n[!] Process manually stopped by the user. Workers terminated without providing any result.\n"))

        # Trying to store the information recovered
        if args.output_folder != None:
            # Verifying an output folder was selected
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)
            # Grabbing the results
            file_header = os.path.join(args.output_folder, args.file_header)
            for ext in args.extension:
                # Generating output files
                general.export_usufy(results, ext, file_header)

        # Showing the information gathered if requested
        if not args.quiet:
            now = dt.datetime.now()
            print(f"\n{now}\tResults obtained:\n")
            print(general.success(general.osrf_to_text_export(results)))

            if args.web_browser:
                general.open_results_in_browser(results)

            now = dt.datetime.now()
            print(f"\n{now}\tYou can find all the information collected in the following files:")
            for ext in args.extension:
                # Showing the output files
                print("\t" + general.emphasis(file_header + "." + ext))

            # Showing the execution time...
            end_time = dt.datetime.now()
            print(f"\n{end_time}\tFinishing execution...\n")
            print("Total time consumed:\t" + general.emphasis(str(end_time-start_time)) + "\n")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

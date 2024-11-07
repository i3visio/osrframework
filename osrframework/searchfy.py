################################################################################
#
#    Copyright 2015-2021 Félix Brezo and Yaiza Rubio
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
from osrframework.utils import banner, platform_selection, configuration, general


def perform_search(platform_names=[], queries=[], exclude_platform_names=[]):
    """Performs the search on selected platforms.

    Args:
        platform_names: List of platform names to search.
        queries: List of queries to perform.
        exclude_platform_names: List of platforms to exclude from search.

    Returns:
        list: A list of collected entities.
    """
    platforms = platform_selection.get_platforms_by_name(
        platform_names, mode="searchfy", exclude_platform_names=exclude_platform_names
    )
    results = []
    for query in queries:
        for platform in platforms:
            entities = platform.get_info(query=query, mode="searchfy")
            if entities != "[]":
                results.extend(json.loads(entities))
    return results


def get_parser():
    """Defines the argument parser.

    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    DEFAULT_VALUES = configuration.get_configuration_values_for("searchfy")
    exclude_list = DEFAULT_VALUES.get("exclude_platforms", [])

    parser = argparse.ArgumentParser(
        description='searchfy - OSRFramework tool to perform queries across platforms.',
        prog='searchfy',
        epilog='Refer to README.md or visit <http://twitter.com/i3visio>.',
        add_help=False,
        conflict_handler='resolve'
    )
    parser._optionals.title = "Input options (one required)"

    group_main = parser.add_mutually_exclusive_group(required=True)
    group_main.add_argument('--license', action='store_true', help='Shows the GPLv3+ license and exits.')
    group_main.add_argument('-q', '--queries', metavar='<searches>', nargs='+', help='List of queries to be performed.')

    all_platforms = platform_selection.get_all_platform_names("searchfy")

    group_processing = parser.add_argument_group('Processing arguments')
    group_processing.add_argument(
        '-e', '--extension', metavar='<output_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx'],
        default=DEFAULT_VALUES.get("extension", ["csv"]), help='Output extension for summary files. Default: csv.'
    )
    group_processing.add_argument(
        '-F', '--file_header', metavar='<header>', default=DEFAULT_VALUES.get("file_header", "profiles"),
        help='Header for output filenames. Default: profiles.<extension>.'
    )
    group_processing.add_argument(
        '-o', '--output_folder', metavar='<output_folder>', default=DEFAULT_VALUES.get("output_folder", "."),
        help='Folder for generated documents. Created if it does not exist.'
    )
    group_processing.add_argument(
        '-p', '--platforms', metavar='<platform>', choices=all_platforms, nargs='+', default=DEFAULT_VALUES.get("platforms", []),
        help=f'Select platforms to search. Available options: {all_platforms}.'
    )
    group_processing.add_argument(
        '-w', '--web_browser', action='store_true', help='Opens URIs in the default web browser.'
    )
    group_processing.add_argument(
        '-x', '--exclude', metavar='<platform>', choices=all_platforms, nargs='+', default=exclude_list,
        help='Exclude platforms from processing.'
    )

    group_about = parser.add_argument_group('About arguments')
    group_about.add_argument('-h', '--help', action='help', help='Shows this help message and exits.')
    group_about.add_argument('--version', action='version', version=f'[%(prog)s] OSRFramework {osrframework.__version__}', help='Shows the version.')

    return parser


def main(params=None):
    """Main function to launch searchfy.

    Args:
        params (list, optional): List of command-line parameters. Defaults to None.

    Returns:
        list: List of i3visio entities.
    """
    parser = get_parser()
    args = parser.parse_args(params)

    if args.license:
        general.showLicense()
        return []

    print(general.title(banner.text))
    print(general.info("""
     Searchfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2021

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{}>.
""".format(general.LICENSE_URL)))

    start_time = dt.datetime.now()
    print(f"{start_time}\tStarting search across selected platform(s)...\n")

    try:
        results = perform_search(platform_names=args.platforms, queries=args.queries, exclude_platform_names=args.exclude)
    except KeyboardInterrupt:
        print(general.error("\n[!] Process manually stopped. No results were returned.\n"))
        return []

    if args.extension:
        os.makedirs(args.output_folder, exist_ok=True)
        file_header = os.path.join(args.output_folder, args.file_header)

        for ext in args.extension:
            general.export_usufy(results, ext, file_header)

    print(f"\nResults obtained:\n{general.success(general.osrf_to_text_export(results))}")

    if args.web_browser:
        general.open_results_in_browser(results)

    end_time = dt.datetime.now()
    print(f"\n{end_time}\tExecution finished.\n")
    print(f"Total time:\t{str(end_time - start_time)}")
    if args.platforms:
        avg_time = (end_time - start_time).total_seconds() / len(args.platforms)
        print(f"Average seconds/query:\t{avg_time:.2f} seconds\n")
    print(banner.footer)

    return results


if __name__ == "__main__":
    main(sys.argv[1:])
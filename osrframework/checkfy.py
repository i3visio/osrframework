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
import re

import osrframework
import osrframework.domains.email_providers as email_providers

import osrframework.utils.banner as banner
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general


def create_emails(nicks=None, nicks_file=None):
    """Method that globally permits to generate the emails to be checked.

    Args:
        nicks: List of aliases.
        nicks_file: The filepath to the aliases file.

    Returns:
        list: list of emails to be checked.
    """
    candidate_emails = set()
    if nicks is not None:
        for nick in nicks:
            for domain in email_providers.domains:
                candidate_emails.add(f"{nick}@{domain}")
    elif nicks_file is not None:
        with open(nicks_file, "r") as file:
            nicks = file.read().splitlines()
            for nick in nicks:
                for domain in email_providers.domains:
                    candidate_emails.add(f"{nick}@{domain}")
    return candidate_emails


def verify_emails(emails=[], reg_exp_pattern="^.+$"):
    """Method to perform the mail verification process.

    Args:
        emails: List of emails to verify.
        reg_exp_pattern: Pattern that should match.

    Returns:
        list: A list containing the results that match.
    """
    emails_matched = set()

    for i, e in enumerate(emails):
        if re.match(reg_exp_pattern, e):
            emails_matched.add(e)

    return list(emails_matched)


def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    DEFAULT_VALUES = configuration.get_configuration_values_for("checkfy")

    parser = argparse.ArgumentParser(
        description='checkfy - Finding potential email addresses based on a list of known aliases (either provided as arguments or read from a file) and a known pattern. Default values can be io',
        add_help=False,
        prog='checkfy',
        conflict_handler='resolve',
        epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.'
    )
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    group_main_options = parser.add_mutually_exclusive_group(required=True)
    group_main_options.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    group_main_options.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help='the list of nicks to be checked in the domains selected.')
    group_main_options.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help='the file with the list of nicks to be checked in the domains selected.')

    # Configuring the processing options
    group_processing = parser.add_mutually_exclusive_group(required=True)
    group_processing.add_argument('-m', '--email-pattern', metavar='<pattern>', action='store', help='The email pattern that the generated email address SHOULD match. The pattern type can be configured using `--type`.')

    # Configuring the application options
    group_options = parser.add_argument_group('Other options', 'Configuring other options.')
    group_options.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES.get("output_folder", "./"), action='store', help=f'output folder for the generated files. Default: {DEFAULT_VALUES.get("output_folder", "./")}.')
    group_options.add_argument('-t', '--type', metavar='<type>', default=DEFAULT_VALUES.get("pattern_type", "twitter"), action='store', choices=["twitter", "regexp"], help=f'The type of pattern provided. It can be either the style used by Twitter to show the pattern suggestions or a regular expression. Default: {DEFAULT_VALUES.get("pattern_type", "twitter")}.', required=False)
    group_options.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')

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
        list: Returns a list with i3visio entities.
    """
    if params is None:
        parser = get_parser()
        args = parser.parse_args(params)
    else:
        args = params

    results = []
    if not args.quiet:
        print(general.title(banner.text))

        saying_hello = """
     Checkfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{}>.
""".format(general.LICENSE_URL)
    print(general.info(saying_hello))

    if args.license:
        general.showLicense()
    else:
        if args.type == "twitter":
            pattern = args.email_pattern.replace(".", "\.")
            pattern = pattern.replace("*", ".")
            pattern = "^{}$".format(pattern)
        elif args.type == "regexp":
            pattern = args.email_pattern

        start_time = dt.datetime.now()
        print(f"{str(start_time)}\tPattern type identified as '{args.type}'. Regular expression: '{pattern}'.\n")

        # Processing the options returned to remove the "all" option
        if args.nicks:
            emails = create_emails(nicks=args.nicks)
        else:
            # nicks_file
            emails = create_emails(nicks_file=args.nicks_file)

        now = dt.datetime.now()
        print(f"{str(now)}\tTrying to identify possible emails {general.emphasis(str(len(emails)))} email(s)... Relax!\n")
        print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        # Perform searches, using different Threads
        results = verify_emails(emails, pattern)

        # Sorting list
        results.sort()
        now = dt.datetime.now()
        print(f"{now}\tTask finished. Validated emails:\n")
        print(general.success(json.dumps(results, indent=2, sort_keys=True)))
        print()
        now = dt.datetime.now()
        print(f"{now}\tUp to {general.emphasis(str(len(results)))} possible emails found.\n")


        # Trying to store the information recovered
        if args.output_folder is not None:
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)

            output_path = os.path.join(args.output_folder, "possible_emails.txt")

            print(f"Writing the results onto the file:\n\t{general.emphasis(output_path)}")

            with open(output_path, "w") as file:
                for res in results:
                    file.write(f"{res}\n")

        # Showing the execution time...
        if not args.quiet:
            # Showing the execution time...
            end_time = dt.datetime.now()
            print(f"\n{end_time}\tFinishing execution...\n")
            print(f"Total time used:\t{general.emphasis(str(end_time-start_time))}")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

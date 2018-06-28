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
import re

import osrframework
import osrframework.domains.email_providers as email_providers

import osrframework.utils.banner as banner
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general


def createEmails(nicks=None, nicksFile=None):
    """
    Method that globally permits to generate the emails to be checked.

    Args:
    -----
        nicks: List of aliases.
        nicksFile: The filepath to the aliases file.

    Returns:
    --------
        list: list of emails to be checked.
    """
    candidate_emails = set()
    if nicks != None:
        for n in nicks:
            for e in email_providers.domains:
                candidate_emails.add("{}@{}".format(n, e))
    elif nicksFile != None:
        with open(nicksFile, "r") as iF:
            nicks = iF.read().splitlines()
            for n in nicks:
                for e in email_providers.domains:
                    candidate_emails.add("{}@{}".format(n, e))
    return candidate_emails


def verifyEmails(emails=[], regExpPattern="^.+$"):
    """
    Method to perform the mail verification process.

    Arguments
    ---------
        emails: List of emails to verify.
        regExpPattern: Pattern that should match.

    Returns
    -------
        list: A list containing the results that match.
    """
    emailsMatched = set()

    for i, e in enumerate(emails):
        if re.match(regExpPattern, e):
            emailsMatched.add(e)

    print(regExpPattern)

    return list(emailsMatched)


def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("domainfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        excludeList = []

    parser = argparse.ArgumentParser(description='checkfy - Finding potential email addresses based on a list of known aliases and a pattern.', prog='checkfy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be checked in the domains selected.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-p', '--pattern',  metavar='<pattern>',  action='store', help='The pattern that the generated email address SHOULD match.', required=True)
    groupProcessing.add_argument('-t', '--type',  metavar='<type>', default="twitter", action='store', choices=["twitter", "regexp"], help='The type of pattern provided. It can be either the style used by Twitter to show the pattern suggestions or a regular expression.', required=False)
    groupProcessing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')

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

    Results:
    --------
        list: Returns a list with i3visio entities.
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
checkfy | Copyright (C) F. Brezo and Y. Rubio (i3visio) 2018

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit """ + general.LICENSE_URL + "\n"
        print(general.title(sayingHello))

    if args.license:
        general.showLicense()
    else:
        # Processing the options returned to remove the "all" option
        if args.nicks:
            emails = createEmails(nicks=args.nicks)
        else:
            # nicks_file
            emails = createEmails(nicksFile=args.nicks_file)

        # Showing the execution time...
        if not args.quiet:
            startTime= dt.datetime.now()
            print(str(startTime) + "\tTrying to identify possible emails " + general.emphasis(str(len(emails))) + " email(s)... Relax!\n")
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        print(args.pattern)
        if args.type == "twitter":
            pattern = args.pattern.replace(".", "\.")
            pattern = pattern.replace("*", ".")
            pattern = "^{}$".format(pattern)
        elif args.type == "regexp":
            pattern = args.pattern

        # Perform searches, using different Threads
        results = verifyEmails(emails, pattern)

        # Sorting list
        results.sort()
        print("\nProcess finished.")
        print("\nValidated emails:\n")
        print(general.success(json.dumps(results, indent=2, sort_keys=True)))
        print("\nUp to " + general.emphasis(str(len(results))) + " possible emails foundd.\n")


        # Trying to store the information recovered
        if args.output_folder != None:
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)

            outputPath = os.path.join(args.output_folder, "possible_emails.txt")

            print("Writing the results onto the file:\n\t" + general.emphasis(outputPath))

            with open(outputPath, "w") as oF:
                for r in results:
                    oF.write(r+"\n")

        # Showing the execution time...
        if not args.quiet:
            # Showing the execution time...
            endTime= dt.datetime.now()
            print("\n" + str(endTime) +"\tFinishing execution...\n")
            print("Total time used:\t" + general.emphasis(str(endTime-startTime)))
            print("Average seconds/query:\t" + general.emphasis(str((endTime-startTime).total_seconds()/len(emails))) +" seconds\n")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

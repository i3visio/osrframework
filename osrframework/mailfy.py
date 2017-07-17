#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2015-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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


__author__ = "Felix Brezo, Yaiza Rubio"
__copyright__ = "Copyright 2015-2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "AGPLv3+"
__version__ = "v6.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import datetime as dt
import time
import json
# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool
import os
import signal
import sys

# Email verification libraries
import emailahoy
import validate_email

import osrframework.utils.banner as banner
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general

# Pending
#188.com", "21cn.cn", "popo.163.com", "vip.126.com", "vip.163.com", "vip.188.com"

EMAIL_DOMAINS = [
    "126.com",
    "163.com",
    "189.cn",
    #"aaathats3as.com",
    "btinternet.com",
    #"cocaine.ninja",
    #"cock.lu",
    #"cock.email",
    #"firemail.cc",
    #"getbackinthe.kitchen",
    "gmail.com",
    #"hitler.rocks",
    "hushmail.com",
    "icloud.com",
    "keemail.me",
    "lycos.com",
    "me.com",
    #"memeware.net",
    #"noob.com",
    "protonmail.ch",
    "protonmail.com",
    "rediffmail.com",
    "seznam.cz",
    "tuta.io",
    "tutamail.com",
    "tutanota.com",
    "tutanota.de",
    #"waifu.club",
    #"wp.pl",
    "ya.ru",
    "yandex.com",
    "yeah.net",
    "zoho.com"
]


def getMoreInfo(e):
    """Method that calls different third party API.

        :param e:   Email to verify.

        :result:
    """
    # Grabbing the email
    email = {}
    email["type"] = "i3visio.email"
    email["value"] = e
    email["attributes"] = []

    # Grabbing the alias
    alias = {}
    alias["type"] = "i3visio.alias"
    alias["value"] = e.split("@")[0]
    alias["attributes"] = []

    # Grabbing the domain
    domain= {}
    domain["type"] = "i3visio.domain"
    domain["value"] = e.split("@")[1]
    domain["attributes"] = []

    return email, alias, domain


def weCanCheckTheseDomains(email):
    """
    Method that verifies if a domain can be safely verified.

    Args:
    -----
        email: the email whose domain will be verified.

    Returns:
    --------
        bool: it represents whether the domain can be verified.
    """
    # Known platform not to be working...
    notWorking = [
        "@aol.com",
        "@bk.ru",
        "@breakthru.com",
        "@gmx.",
        "@hotmail.co",
        "@inbox.com",
        "@latinmail.com",
        "@libero.it",
        "@mail.ru",
        "@mail2tor.com",
        "@outlook.com",
        "@rambler.ru",
        "@rocketmail.com",
        "@starmedia.com",
        "@ukr.net"
        "@yahoo.",
        "@ymail."
    ]

    #notWorking = []
    for n in notWorking:
        if n in email:
            print(general.warning("WARNING: the domain of '" + email + "' has been blacklisted by mailfy.py as it CANNOT BE VERIFIED."))
            return False

    emailDomains = EMAIL_DOMAINS
    safe = False

    for e in emailDomains:
        if e in email:
            safe =  True
            break

    if not safe:
        print(general.warning("WARNING: the domain of '" + email + "' will not be safely verified."))
    return True


def grabEmails(emails=None, emailsFile=None, nicks=None, nicksFile=None, domains = EMAIL_DOMAINS, excludeDomains = []):
    """
    Method that generates a list of emails.

    Args:
    -----
        emails: any premade list of emails.
        emailsFile: the filepath to the emails file (one per line).
        nicks: a list of aliases.
        nicksFile: the filepath to the aliases file (one per line).
        domains: the domains where the aliases will be tested.

    Returns:
    --------
        list: the list of emails that will be verified.
    """
    email_candidates = []

    if emails != None:
        email_candidates = emails
    elif emailsFile != None:
        # Reading the emails file
        with open(emailsFile, "r") as iF:
            email_candidates = iF.read().splitlines()
    elif nicks != None:
        # Iterating the list of nicks
        for n in nicks:
            # Iterating the list of possible domains to build the emails
            for d in domains:
                if d not in excludeDomains:
                    email_candidates.append(n+"@"+d)
    elif nicksFile != None:
        # Reading the list of nicks
        with open(nicksFile, "r") as iF:
            nicks = iF.read().splitlines()
            # Iterating the list of nicks
            for n in nicks:
                # Iterating the list of possible domains to build the emails
                for d in domains:
                    if d not in excludeDomains:
                        email_candidates.append(n+"@"+d)
    return email_candidates


def pool_function(args):
    """
    A wrapper for being able to launch all the threads.

    We will use python-emailahoy library for the verification in non-Windows
    systems as it is faster than validate_email. In Windows systems the latter
    is preferred.

    Args:
    -----
        args: reception of the parameters for getPageWrapper as a tuple.

    Returns:
    --------
        A dictionary representing whether the verification was ended
        successfully. The format is as follows:
        ```
        {"platform": "str(domain["value"])", "status": "DONE", "data": aux}
        ```
    """
    is_valid = True

    try:
        if sys.platform == 'win32':
            is_valid = validate_email.validate_email(args, verify=True)
        else:
            is_valid = emailahoy.verify_email_address(args)
    except Exception, e:
        print(general.warning("WARNING. An error was found when performing the search. You can omit this message.\n" + str(e)))
        is_valid = False

    if is_valid:
        email, alias, domain = getMoreInfo(args)
        aux = {}
        aux["type"] = "i3visio.profile"
        aux["value"] = domain["value"] + " - " + alias["value"]
        aux["attributes"] = []
        aux["attributes"].append(email)
        aux["attributes"].append(alias)
        aux["attributes"].append(domain)

        return {"platform": str(domain["value"]), "status": "DONE", "data": aux}
    else:
        return {"platform": str(domain["value"]), "status": "DONE", "data": {}}


def performSearch(emails=[], nThreads=16, secondsBeforeTimeout=5):
    """
    Method to perform the mail verification process.

    Args:
    -----
        emails: list of emails to be verified.
        nThreads: the number of threads to be used. Default: 16 threads.
        secondsBeforeTimeout: number of seconds to wait before raising a
            timeout. Default: 5 seconds.

    Returns:
    --------
        TODO.
    """
    # Getting starting time
    _startTime = time.time()

    def hasRunOutOfTime(oldEpoch):
        """
        Function that checks if a given time has passed.

        It verifies whether the oldEpoch has passed or not by checking if the
        seconds passed are greater.

        Arguments
        ---------
            oldepoch: Seconds passed since 1970 as returned by `time.time()`.

        Returns
        -------
            A boolean representing whether it has run out of time.
        """
        now = time.time()
        return now - oldEpoch >= secondsBeforeTimeout

    results = []
    args = []

    # Grabbing all the emails that would be validated
    for e in emails:
        if weCanCheckTheseDomains(e):
            args.append((e))

    # Returning None if no valid domain has been returned
    if len(args) == 0:
        return results

    # If the process is executed by the current app, we use the Processes. It is faster than pools.
    if nThreads <= 0 or nThreads > len(args):
        nThreads = len(args)

    # Launching the Pool
    # ------------------
    # Example catched from: https://stackoverflow.com/questions/11312525/catch-ctrlc-sigint-and-exit-multiprocesses-gracefully-in-python
    try:
        original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        pool = Pool(nThreads)
        signal.signal(signal.SIGINT, original_sigint_handler)
    except ValueError:
        # To avoid: ValueError: signal only works in main thread
        pool = Pool(nThreads)

    poolResults = []
    try:
        def log_result(result):
            # This is called whenever foo_pool(i) returns a result.
            # result_list is modified only by the main process, not the pool workers.
            poolResults.append(result)

        for m in emails:
            # We need to create all the arguments that will be needed
            parameters = ( m, )
            pool.apply_async (pool_function, args= parameters, callback = log_result )

        # Waiting for results to be finished or time to pass
        while len(poolResults) < len(emails) and not hasRunOutOfTime(_startTime):
            pass

        # Closing normal termination
        pool.close()
    except KeyboardInterrupt:
        print(general.warning("\n[!] Process manually stopped by the user. Terminating workers.\n"))
        pool.terminate()

        pending = ""

        print(general.warning("[!] The following platforms were not processed:"))
        for m in emails:
            processed = False
            for result in poolResults:
                if str(m) in json.dumps(result["data"]):
                    processed = True
                    break
            if not processed:
                print("\t- " + str(p))
                pending += " " + str(m)

        print("\n")
        print(general.warning("If you want to relaunch the app with these platforms you can always run the command with: "))
        print("\t mailfy.py ... -p " + general.emphasis(pending))
        print("\n")
        print(general.warning("If you prefer to avoid these platforms you can manually evade them for whatever reason with: "))
        print("\t mailfy.py ... -x " + general.emphasis(pending))
        print("\n")
    pool.join()

    # Processing the results
    # ----------------------
    for serArray in poolResults:
        data = serArray["data"]
        # We need to recover the results and check if they are not an empty json or None
        if data != None and data != {}:
            results.append(data)

    pool.close()

    return results

def main(args):
    """
    Main function to launch phonefy.

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `getParser()`.

    Args:
    -----
        args: The parameters as processed by this modules `getParser()`.

    Results:
    --------
        Returns a list with i3visio entities.
    """
    results = []

    if not args.quiet:
        print(general.title(banner.text))

        sayingHello = """
mailfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit """ + general.LICENSE_URL + "\n"
        print(general.title(sayingHello))

        # Displaying a warning if this is being run in a windows system
        if sys.platform == 'win32':
            print(general.warning("""OSRFramework has detected that you are running mailfy.py in a Windows system.
As the "emailahoy" library is NOT working properly there, "validate_email" will
be used instead. Verification may be slower though."""))

    if args.license:
        general.showLicense()
    else:
        # Processing the options returned to remove the "all" option
        if "all" in args.domains:
            domains = EMAIL_DOMAINS
        else:
            # processing only the given domains and excluding the ones provided
            domains = []
            for d in args.domains:
                if d not in args.exclude:
                    domains.append(d)

        if args.create_emails:
            emails = grabEmails(nicksFile=args.create_emails, domains=domains, excludeDomains=args.exclude)
        else:
            emails = grabEmails(emails=args.emails, emailsFile=args.emails_file, nicks=args.nicks, nicksFile=args.nicks_file, domains=domains, excludeDomains=args.exclude)


        # Showing the execution time...
        if not args.quiet:
            startTime= dt.datetime.now()
            print(str(startTime) +"\tStarting search in " + general.emphasis(str(len(emails))) + " different emails:\n"+ json.dumps(emails, indent=2, sort_keys=True) + "\n")
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))
        # Perform searches, using different Threads
        results = performSearch(emails, args.threads)

        # Trying to store the information recovered
        if args.output_folder != None:
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
            print(str(now) + "\tA summary of the results obtained are shown in the following table:\n")
            print(general.success(unicode(general.usufyToTextExport(results))))

            now = dt.datetime.now()
            print("\n" + str(now) + "\tYou can find all the information collected in the following files:")
            for ext in args.extension:
                # Showing the output files
                print(general.emphasis("\t" + fileHeader + "." + ext))

        # Showing the execution time...
        if not args.quiet:
            endTime= dt.datetime.now()
            print("\n" + str(endTime) +"\tFinishing execution...\n")
            print("Total time used:\t" + general.emphasis(str(endTime-startTime)))
            print("Average seconds/query:\t" + general.emphasis(str((endTime-startTime).total_seconds()/len(emails))) +" seconds\n")

        if not args.quiet:
            # Urging users to place an issue on Github...
            print(banner.footer)

    return results


def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("mailfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_domains"]]
    except:
        excludeList = []

    parser = argparse.ArgumentParser(description='mailfy.py - Checking the existence of a given mail.', prog='mailfy.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-m', '--emails', metavar='<emails>', nargs='+', action='store', help = 'the list of emails to be checked.')
    groupMainOptions.add_argument('-M', '--emails_file', metavar='<emails_file>', action='store', help = 'the file with the list of emails.')
    groupMainOptions.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('--create_emails', metavar='<nicks_file>',  action='store', help = 'the file with the list of nicks to be created in the domains selected.')
    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    #groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'mtz', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-d', '--domains',  metavar='<candidate_domains>',  nargs='+', choices=['all'] + EMAIL_DOMAINS, action='store', help='list of domains where the nick will be looked for.', required=False, default=DEFAULT_VALUES["domains"])
    groupProcessing.add_argument('-x', '--exclude', metavar='<domain>', choices=EMAIL_DOMAINS, nargs='+', required=False, default=excludeList, action='store', help="select the domains to be excluded from the search.")
    # Getting a sample header for the output files
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default = int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 16). If 0, the maximum number possible will be used, which may make the system feel unstable.')
    groupProcessing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    #groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +" " +__version__, help='shows the version of the program and exists.')

    return parser

if __name__ == "__main__":
    # Grabbing the parser
    parser = getParser()

    args = parser.parse_args()

    # Calling the main function
    main(args)

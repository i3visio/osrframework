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
import time
import json
# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool, TimeoutError
import os
import signal
import sys

# Email verification libraries
import emailahoy
import validate_email

import osrframework
import osrframework.thirdparties.haveibeenpwned_com.hibp as hibp
import osrframework.utils.banner as banner
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general

# Pending
#188.com", "21cn.cn", "popo.163.com", "vip.126.com", "vip.163.com", "vip.188.com"

EMAIL_DOMAINS = [
    "126.com",
    "163.com",
    "gmail.com",
    "icloud.com",
    "me.com",
    "protonmail.ch",
    "protonmail.com",
    "rediffmail.com",
    "seznam.cz",
    "tuta.io",
    "tutamail.com",
    "tutanota.com",
    "tutanota.de",
    "ya.ru",
    "yandex.com",
    "yeah.net",
    "zoho.com"
]


LEAKED_DOMAINS = [
    "126.com",
    "163.com",
    "189.cn",
    "aol.com",
    "bk.ru",
    "breakthru.com",
    "btinternet.com",
    "gmail.com",
    "gmx.com",
    "gmx.de",
    "hotmail.com",
    "hushmail.com",
    "icloud.com",
    "inbox.com",
    "keemail.me",
    "latinmail.com",
    "libero.it",
    "lycos.com",
    "me.com",
    "mail.ru",
    "mail2tor.com",
    "outlook.com",
    "protonmail.ch",
    "protonmail.com",
    "rambler.ru",
    "rocketmail.com",
    "rediffmail.com",
    "seznam.cz",
    "starmedia.com",
    "tuta.io",
    "tutamail.com",
    "tutanota.com",
    "tutanota.de",
    "ya.ru",
    "yahoo.com",
    "yandex.com",
    "yandex.ru",
    "yeah.net",
    "zoho.com"
]


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
            print("\t[*] Verification of '{}' aborted. Details:\n\t\t{}".format(general.warning(email), "This domain CANNOT be verified using mailfy."))
            return False

    emailDomains = EMAIL_DOMAINS
    safe = False

    for e in EMAIL_DOMAINS:
        if e in email:
            safe =  True

    if not safe:
        print("\t[*] Verification of '{}' aborted. Details:\n\t\t{}".format(general.warning(email), "This domain CANNOT be verified using mailfy."))
        return False
    return True


def grabEmails(emails=None, emailsFile=None, nicks=None, nicksFile=None, domains=EMAIL_DOMAINS, excludeDomains=[]):
    """
    Method that generates a list of emails.

    Args:
    -----
        emails: Any premade list of emails.
        emailsFile: Filepath to the emails file (one per line).
        nicks: A list of aliases.
        nicksFile: Filepath to the aliases file (one per line).
        domains: Domains where the aliases will be tested.
        excludeDomains: Domains to be excluded from the created list.

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


def processMailList(platformNames=[], emails=[]):
    """
    Method to perform the email search.

    Args:
    -----
        platformNames: List of names of the platforms.
        emails: List of numbers to be queried.

    Return:
    -------
        A list of verified emails.
    """
    # Grabbing the <Platform> objects
    platforms = platform_selection.getPlatformsByName(platformNames, mode="mailfy")

    results = []
    for e in emails:
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.getInfo(query=e, mode="mailfy")
            if entities != {}:
                results += json.loads(entities)
    return results


def pool_function(args):
    """
    A wrapper for being able to launch all the threads.

    We will use python-emailahoy library for the verification.

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
        checker = emailahoy.VerifyEmail()
        status, message = checker.verify_email_smtp(args, from_host='gmail.com', from_email='sample@gmail.com')
        if status == 250:
            print("\t[*] Verification of '{}' status: {}. Details:\n\t\t{}".format(general.success(args), general.success("SUCCESS ({})".format(str(status))), message.replace('\n', '\n\t\t')))
            is_valid = True
        else:
            print("\t[*] Verification of '{}' status: {}. Details:\n\t\t{}".format(general.error(args), general.error("FAILED ({})".format(str(status))), message.replace('\n', '\n\t\t')))
            is_valid = False
    except Exception, e:
        print(general.warning("WARNING. An error was found when performing the search. You can omit this message.\n" + str(e)))
        is_valid = False

    aux = {}
    aux["type"] = "i3visio.profile"
    aux["value"] = "Email - " + args
    aux["attributes"] =  general.expandEntitiesFromEmail(args)
    platform = aux["attributes"][2]["value"].title()
    aux["attributes"].append({
            "type": "i3visio.platform",
            "value": platform,
            "attributes": []
        }
    )

    if is_valid:
        return {"platform": platform, "status": "DONE", "data": aux}
    else:
        return {"platform": platform, "status": "DONE", "data": {}}


def performSearch(emails=[], nThreads=16, secondsBeforeTimeout=5):
    """
    Method to perform the mail verification process.

    Args:
    -----
        emails: list of emails to be verified.
        platforms: list of strings representing the wrappers to be used.
        nThreads: the number of threads to be used. Default: 16 threads.
        secondsBeforeTimeout: number of seconds to wait before raising a
            timeout. Default: 5 seconds.

    Returns:
    --------
        The results collected.
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
            """
            Callback to log the results by apply_async
            """
            poolResults.append(result)

        for m in emails:
            parameters = ( m, )
            res = pool.apply_async(pool_function, args=parameters, callback=log_result)
            try:
                res.get(3)
            except TimeoutError as e:
                general.warning("\n[!] Process timeouted for '{}'.\n".format(parameters))
        pool.close()
    except KeyboardInterrupt:
        print(general.warning("\n[!] Process manually stopped by the user. Terminating workers.\n"))
        pool.terminate()

        pending = ""

        print(general.warning("[!] The following email providers were not processed:"))
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


def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("mailfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_domains"]]
    except:
        excludeList = []

    # Recovering all the possible options
    platOptions = platform_selection.getAllPlatformNames("mailfy")

    parser = argparse.ArgumentParser(description='mailfy - Checking the existence of a given mail.', prog='mailfy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-m', '--emails', metavar='<emails>', nargs='+', action='store', help = 'the list of emails to be checked.')
    groupMainOptions.add_argument('-M', '--emails_file', metavar='<emails_file>', action='store', help = 'the file with the list of emails.')
    groupMainOptions.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('--create_emails', metavar='<nicks_file>',  action='store', help = 'the file with the list of nicks to be created in the domains selected.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-d', '--domains',  metavar='<candidate_domains>',  nargs='+', choices=['all'] + EMAIL_DOMAINS, action='store', help='list of domains where the nick will be looked for.', required=False, default=DEFAULT_VALUES["domains"])
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-p', '--platforms', metavar='<platform>', choices=platOptions, nargs='+', required=False, default=["all"], action='store', help='select the platforms where you want to perform the search amongst the following: {}. More than one option can be selected.'.format(str(platOptions)))
    groupProcessing.add_argument('-x', '--exclude', metavar='<domain>', choices=EMAIL_DOMAINS, nargs='+', required=False, default=excludeList, action='store', help="select the domains to be excluded from the search.")
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default = int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 16). If 0, the maximum number possible will be used, which may make the system feel unstable.')
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
            None when this is called by an entry_point. If it is called by osrf
            the data is already parsed.

    Returns:
    --------
        A list of i3visio entities.
    """
    if params == None:
        parser = getParser()
        args = parser.parse_args(params)
    else:
        args = params

    results = []

    if not args.quiet:
        print(general.title(banner.text))

        sayingHello = """
          Mailfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2018

    This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
    are welcome to redistribute it under certain conditions. For additional info,
    visit <{}>.
    """.format(general.LICENSE_URL)
        print(general.info(sayingHello))
        # Displaying a warning if this is being run in a windows system
        if sys.platform == 'win32':
            print(general.warning("""OSRFramework has detected that you are running mailfy.py in a Windows system.
As the "emailahoy" library is NOT working properly there, "validate_email" will
be used instead. Verification may be slower though."""))

    if args.license:
        general.showLicense()
    else:
        # processing only the given domains and excluding the ones provided
        extra_domains = []

        for d in args.domains:
            if d not in args.exclude and not d == "all":
                extra_domains.append(d)

        # Two different arrays are mantained since there are some domains that cannot be safely verified
        if args.create_emails:
            potentially_existing_emails = grabEmails(
                nicksFile=args.create_emails,
                domains=EMAIL_DOMAINS + extra_domains,
                excludeDomains=args.exclude
            )
            potentially_leaked_emails = grabEmails(
                nicksFile=args.create_emails,
                domains=LEAKED_DOMAINS + extra_domains,
                excludeDomains=args.exclude
            )
        else:
            potentially_existing_emails = grabEmails(
                emails=args.emails,
                emailsFile=args.emails_file,
                nicks=args.nicks,
                nicksFile=args.nicks_file,
                domains=EMAIL_DOMAINS + extra_domains,
                excludeDomains=args.exclude
            )
            potentially_leaked_emails = grabEmails(
                emails=args.emails,
                emailsFile=args.emails_file,
                nicks=args.nicks,
                nicksFile=args.nicks_file,
                domains=LEAKED_DOMAINS + extra_domains,
                excludeDomains=args.exclude
            )

        emails = list(set(potentially_leaked_emails + potentially_existing_emails))

        # Showing the execution time...
        if not args.quiet:
            startTime = dt.datetime.now()
            print("{}\tStarting search of {} different emails:\n{}\n".format(
                str(startTime),
                general.emphasis(str(len(emails))),
                json.dumps(emails, indent=2, sort_keys=True))
            )

        if not args.quiet:
            now = dt.datetime.now()
            print("\n{}\tStep 1. Trying to determine if the emails provided do exist...\n".format(str(now)))
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        # Perform searches, using different Threads
        results = performSearch(potentially_existing_emails, nThreads=args.threads)

        if not args.quiet:
            now = dt.datetime.now()
            print("\n{}\tStep 2. Checking if the emails have been used to register socialmedia accounts...\n".format(str(now)))
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        registered = processMailList(platformNames=args.platforms, emails=potentially_existing_emails)
        results += registered

        if not args.quiet:
            if len(results) > 0:
                for r in registered:
                    print("\t[*] Registered account found: {}".format(general.success(r["value"])))
            else:
                print("\t[*] Registered account found: {}".format(general.error("None")))

            now = dt.datetime.now()
            print("\n{}\tStep 3. Verifying if the provided emails have  been leaked somewhere?\n".format(str(now)))
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        # Verify the existence of the mails found as leaked emails.
        for query in potentially_leaked_emails:
            # Iterate through the different leak platforms
            leaks = hibp.checkIfEmailWasHacked(query)

            if len(leaks) > 0:
                if not args.quiet:
                    if len(leaks) > 0:
                        print("\t[*] '{}' has been found in at least {} different leaks.".format(general.success(query), general.success(str(len(leaks)))))
                    else:
                        print("\t[*] '{}' has NOT been found in any leak.".format(general.error(query)))
            else:
                if not args.quiet:
                    print("\t[*] '{}' has NOT been found on any leak yet.".format(general.error(query)))

            results += leaks

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
            print("\n{}\tResults obtained:\n".format(str(now)))
            print(general.success(general.usufyToTextExport(results)))

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

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

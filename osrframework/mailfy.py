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
import time
import json
# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool, TimeoutError
import os
import signal
import sys

# Email verification libraries
from emailahoy3 import verify_email_address

import osrframework
import osrframework.thirdparties.haveibeenpwned_com.hibp as hibp
import osrframework.thirdparties.dehashed_com.dehashed as dehashed
import osrframework.thirdparties.viewdns_info.viewdns as viewdns
import osrframework.utils.banner as banner
import osrframework.utils.config_api_keys as config_api_keys
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general
import osrframework.utils.platform_selection as platform_selection


EMAIL_DOMAINS = [
    "protonmail.ch",         # Expected value on successful matches
    "protonmail.com",
    "ya.ru",
    "yandex.com",
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


def email_is_verifiable(email):
    """Method that verifies if a domain can be safely verified

    Args:
        email (str): the email whose domain will be verified.

    Returns:
        Bool. it represents whether the domain can be verified.
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

    for n in notWorking:
        if n in email:
            print("\t[*] Verification of '{}' aborted. Details:\n\t\t{}".format(general.warning(email), "This domain CANNOT be verified using EmailAhoy."))
            return False

    emailDomains = EMAIL_DOMAINS
    safe = False

    for e in EMAIL_DOMAINS:
        if e in email:
            safe = True

    if not safe:
        print("\t[*] Verification of '{}' aborted. Details:\n\t\t{}".format(general.warning(email), "This domain CANNOT be verified using EmailAhoy."))
        return False
    return True


def grab_emails(emails=None, emails_file=None, nicks=None, nicks_file=None, domains=EMAIL_DOMAINS, exclude_domains=[]):
    """Method that generates a list of emails

    Args:
        emails (list): Any premade list of emails.
        emails_file (str): Filepath to the emails file (one per line).
        nicks (list): A list of aliases.
        nicks_file (str): Filepath to the aliases file (one per line).
        domains (list): Domains where the aliases will be tested.
        exclude_domains (list): Domains to be excluded from the created list.

    Returns:
        list. The list of emails that will be verified.
    """
    email_candidates = []

    if emails != None:
        email_candidates = emails
    elif emails_file != None:
        # Reading the emails file
        with open(emails_file, "r") as file:
            email_candidates = file.read().splitlines()
    elif nicks != None:
        # Iterating the list of nicks
        for n in nicks:
            # Iterating the list of possible domains to build the emails
            for d in domains:
                if d not in exclude_domains:
                    email_candidates.append(n+"@"+d)
    elif nicks_file != None:
        # Reading the list of nicks
        with open(nicks_file, "r") as file:
            nicks = file.read().splitlines()
            # Iterating the list of nicks
            for n in nicks:
                # Iterating the list of possible domains to build the emails
                for d in domains:
                    if d not in exclude_domains:
                        email_candidates.append(n+"@"+d)
    return email_candidates


def pool_function(args):
    """A wrapper for being able to launch all the threads

    We will use python-emailahoy library for the verification.

    Args:
        args: reception of the parameters for getPageWrapper as a tuple.

    Returns:
        dict. A dictionary representing whether the verification was ended
        successfully. The format is as follows:
        ```
        {"platform": "str(domain["value"])", "status": "DONE", "data": aux}
        ```
    """
    def confirm_found(email, status):
        """Method that confirms the existence of an email

        This method is needed since different email providers may behave differently.

        Args:
            email (str): The email to search.
            status (int): emailahoy3 returned status.

        Returns:
            bool.
        """
        # Dependening on the email
        ok_is_1 = [
            "protonmail.ch",         # Expected value on successful matches
            "protonmail.com",
        ]

        for domain in ok_is_1:
            if domain in args and status == 1:
                return True

        ok_is_0 = [
            "ya.ru",
            "yandex.com",
        ]
        if args in ok_is_0:
            if domain in args and status == 0:
                return True
        return False

    try:
        status = verify_email_address(args)
        is_valid = confirm_found(args, status)

        if is_valid:
            print(f"\t[*] Verification of '{general.success(args)}' status: {general.success(f'Email found ({status})')}")
        else:
            print(f"\t[*] Verification of '{general.error(args)}' status: {general.error(f'Email not found ({status})')}")
    except Exception as e:
        print(general.warning("WARNING. An error was found when performing the search. You can omit this message.\n" + str(e)))
        is_valid = False

    entities = general.expand_entities_from_email(args)
    platform = entities[2]["value"].title()

    if is_valid:
        aux = {}
        aux["type"] = "com.i3visio.Profile"
        aux["value"] = "Email - " + args
        aux["attributes"] = entities

        aux["attributes"].append({
                "type": "com.i3visio.Platform",
                "value": platform,
                "attributes": []
            }
        )
        return {"platform": platform, "status": "DONE", "data": aux}
    else:
        return {"platform": platform, "status": "ERROR", "data": {}}


def verify_with_emailahoy_step_1(emails=[], num_threads=16, seconds_before_timeout=5):
    """Method to perform the mail verification process

    Args:
        emails (list): list of emails to be verified.
        platforms (list): list of strings representing the wrappers to be used.
        num_threads (int): the number of threads to be used. Default: 16 threads.
        seconds_before_timeout (int): number of seconds to wait before raising a
            timeout. Default: 5 seconds.

    Returns:
        The results collected.
    """
    results = []

    args = []

    # Grabbing all the emails that would be validated
    for email in emails:
        if email_is_verifiable(email):
            args.append((email))

    # Returning None if no valid domain has been returned
    if len(args) == 0:
        return results

    # If the process is executed by the current app, we use the Processes. It is faster than pools.
    if num_threads <= 0 or num_threads > len(args):
        num_threads = len(args)

    # Launching the Pool
    # ------------------
    # Example catched from: https://stackoverflow.com/questions/11312525/catch-ctrlc-sigint-and-exit-multiprocesses-gracefully-in-python
    try:
        original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        pool = Pool(num_threads)
        signal.signal(signal.SIGINT, original_sigint_handler)
    except ValueError:
        # To avoid: ValueError: signal only works in main thread
        pool = Pool(num_threads)

    pool_results = []

    def log_result(result):
        """Callback to log the results by apply_async"""
        pool_results.append(result)

    for email in emails:
        parameters = (email, )
        res = pool.apply_async(pool_function, args=parameters, callback=log_result)
        try:
            res.get(3)
        except TimeoutError:
            general.warning(f"\n[!] Process timeouted for '{parameters}'.\n")
    pool.close()
    pool.join()

    # Processing the results
    # ----------------------
    for serArray in pool_results:
        data = serArray["data"]
        # We need to recover the results and check if they are not an empty json or None
        if data is not None and data != {}:
            results.append(data)

    pool.close()

    return results


def process_mail_list_step_2(platforms=[], emails=[]):
    """Method to perform the email search

    Args:
        platforms (list): List of platforms to be searched.
        emails (list): List of numbers to be queried.

    Returns:
        list. A list of verified emails.
    """
    results = []
    print(f"\n\t[*] Starting the research of {len(emails)} email(s) in {len(platforms)} platform(s)... This may take a while.")
    for i, e in enumerate(emails):
        print(f"\n\t[*] {i+1}/{len(emails)} Checking '{general.title(e)}'...")
        for pla in platforms:
            # This returns a json.txt!
            entities = pla.get_info(query=e, mode="mailfy")
            data = json.loads(entities)
            if data:
                results += data
    return results


def get_parser():
    DEFAULT_VALUES = configuration.get_configuration_values_for("mailfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        exclude_list = [DEFAULT_VALUES["exclude_domains"]]
    except:
        exclude_list = []

    # Recovering all the possible options
    plat_options = platform_selection.get_all_platform_names("mailfy")

    parser = argparse.ArgumentParser(description='mailfy - Checking the existence of a given mail.', prog='mailfy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    group_main_options = parser.add_mutually_exclusive_group(required=True)
    group_main_options.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    group_main_options.add_argument('-m', '--emails', metavar='<emails>', nargs='+', action='store', help = 'the list of emails to be checked.')
    group_main_options.add_argument('-M', '--emails-file', metavar='<emails_file>', action='store', help = 'the file with the list of emails.')
    group_main_options.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the domains selected.')
    group_main_options.add_argument('-N', '--nicks-file', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be checked in the domains selected.')
    group_main_options.add_argument('--create-emails', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be created in the domains selected.')

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    group_processing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    group_processing.add_argument('-d', '--domains', metavar='<candidate_domains>', nargs='+', choices=['all'] + EMAIL_DOMAINS, action='store', help='list of domains where the nick will be looked for.', required=False, default=DEFAULT_VALUES["domains"])
    group_processing.add_argument('-o', '--output-folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    group_processing.add_argument('-p', '--platforms', metavar='<platform>', choices=plat_options, nargs='+', required=False, default=["all"], action='store', help='select the platforms where you want to perform the search amongst the following: {}. More than one option can be selected.'.format(str(plat_options)))
    group_processing.add_argument('-x', '--exclude', metavar='<domain>', choices=EMAIL_DOMAINS, nargs='+', required=False, default=exclude_list, action='store', help="select the domains to be excluded from the search.")
    group_processing.add_argument('-F', '--file-header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    group_processing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default = int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 16). If 0, the maximum number possible will be used, which may make the system feel unstable.')
    group_processing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')

    # About options
    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """Main function to launch mailfy

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `get_parser()`.

    Args:
        params: A list with the parameters as grabbed by the terminal. It is
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

    if not args.quiet:
        print(general.title(banner.text))

        saying_hello = f"""
          Mailfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

    This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
    are welcome to redistribute it under certain conditions. For additional info,
    visit <{general.LICENSE_URL}>.
    """
        print(general.info(saying_hello))
        # Displaying a warning if this is being run in a windows system
        if sys.platform == 'win32':
            print(general.warning("""OSRFramework has detected that you are running mailfy in a Windows system.
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
            potentially_existing_emails = grab_emails(
                nicks_file=args.create_emails,
                domains=EMAIL_DOMAINS + extra_domains,
                exclude_domains=args.exclude
            )
            potentially_leaked_emails = grab_emails(
                nicks_file=args.create_emails,
                domains=LEAKED_DOMAINS + extra_domains,
                exclude_domains=args.exclude
            )
        else:
            potentially_existing_emails = grab_emails(
                emails=args.emails,
                emails_file=args.emails_file,
                nicks=args.nicks,
                nicks_file=args.nicks_file,
                domains=EMAIL_DOMAINS + extra_domains,
                exclude_domains=args.exclude
            )
            potentially_leaked_emails = grab_emails(
                emails=args.emails,
                emails_file=args.emails_file,
                nicks=args.nicks,
                nicks_file=args.nicks_file,
                domains=LEAKED_DOMAINS + extra_domains,
                exclude_domains=args.exclude
            )

        emails = list(set(potentially_leaked_emails + potentially_existing_emails))

        if not args.quiet:
            start_time = dt.datetime.now()
            print(f"\n{start_time}\t{general.emphasis('Step 1/5')}. Trying to determine if any of the following {general.emphasis(str(len(potentially_existing_emails)))} emails exist using emailahoy3...\n{general.emphasis(json.dumps(potentially_existing_emails, indent=2))}\n")
            print(general.emphasis("\tPress <Ctrl + C> to skip this step...\n"))

        # Perform searches, using different Threads
        try:
            results = verify_with_emailahoy_step_1(potentially_existing_emails, num_threads=args.threads)
        except KeyboardInterrupt:
            print(general.warning("\tStep 1 manually skipped by the user...\n"))
            results = []

        # Grabbing the <Platform> objects
        platforms = platform_selection.get_platforms_by_name(args.platforms, mode="mailfy")
        names = [p.platformName for p in platforms]

        if not args.quiet:
            now = dt.datetime.now()
            print(f"\n{now}\t{general.emphasis('Step 2/5')}. Checking if the emails have been used to register accounts in {general.emphasis(str(len(platforms)))} platforms...\n{general.emphasis(json.dumps(names, indent=2))}\n")
            print(general.emphasis("\tPress <Ctrl + C> to skip this step...\n"))

        try:
            registered = process_mail_list_step_2(platforms=platforms, emails=emails)
        except KeyboardInterrupt:
            print(general.warning("\tStep 2 manually skipped by the user...\n"))
            registered = []

        results += registered

        if not args.quiet:
            if len(results) > 0:
                for r in registered:
                    print(f"\t[*] Linked account found: {general.success(r['value'])}")
            else:
                print(f"\t[*] No account found.")

            now = dt.datetime.now()
            print(f"\n{now}\t{general.emphasis('Step 3/5')}. Verifying if the provided emails have been leaked somewhere using HaveIBeenPwned.com...\n")
            print(general.emphasis("\tPress <Ctrl + C> to skip this step...\n"))

        all_keys = config_api_keys.get_list_of_api_keys()
        try:
            # Verify the existence of the mails found as leaked emails.
            for query in potentially_leaked_emails:
                # Iterate through the different leak platforms
                leaks = hibp.check_if_email_was_hacked(query, api_key=all_keys["haveibeenpwned_com"]["api_key"])

                if len(leaks) > 0:
                    if not args.quiet:
                        print(f"\t[*] '{general.success(query)}' has been found in at least {general.success(len(leaks))} different leaks.")
                else:
                    if not args.quiet:
                        print(f"\t[*] '{general.error(query)}' has NOT been found on any leak yet.")

                results += leaks
        except KeyError:
            # API_Key not found
            config_path = os.path.join(configuration.get_config_path()["appPath"], "api_keys.cfg")
            print(general.warning(f"No API found for HaveIBeenPwned. Request one at <https://haveibeenpwned.com/API/Key> and add it to '{config_path}'."))
        except KeyboardInterrupt:
            print(general.warning("\tStep 3 manually skipped by the user...\n"))

        if not args.quiet:
            now = dt.datetime.now()
            print(f"\n{now}\t{general.emphasis('Step 4/5')}. Verifying if the provided emails have been leaked somewhere using Dehashed.com...\n")
            print(general.emphasis("\tPress <Ctrl + C> to skip this step...\n"))

        try:
            # Verify the existence of the mails found as leaked emails.
            for query in emails:
                try:
                    # Iterate through the different leak platforms
                    leaks = dehashed.check_if_email_was_hacked(query)
                    if len(leaks) > 0:
                        if not args.quiet:
                            print(f"\t[*] '{general.success(query)}' has been found in at least {general.success(len(leaks))} different leaks as shown by Dehashed.com.")
                    else:
                        if not args.quiet:
                            print(f"\t[*] '{general.error(query)}' has NOT been found on any leak yet.")

                    results += leaks
                except Exception as e:
                    print(general.warning(f"Something happened when querying Dehashed.com about '{email}'. Omitting..."))
        except KeyboardInterrupt:
            print(general.warning("\tStep 4 manually skipped by the user...\n"))

        if not args.quiet:
            now = dt.datetime.now()
            print(f"\n{now}\t{general.emphasis('Step 5/5')}. Verifying if the provided emails have registered a domain using ViewDNS.info...\n")
            print(general.emphasis("\tPress <Ctrl + C> to skip this step...\n"))

        try:
            # Verify the existence of the mails found as leaked emails.
            for query in potentially_leaked_emails:
                try:
                    # Iterate through the different leak platforms
                    domains = viewdns.check_reverse_whois(query)

                    if len(domains) > 0:
                        if not args.quiet:
                            print(f"\t[*] '{general.success(query)}' has registered at least {general.success(len(domains))} different domains as shown by ViewDNS.info.")
                    else:
                        if not args.quiet:
                            print(f"\t[*] '{general.error(query)}' has NOT registered a domain yet.")

                    results += domains
                except Exception as e:
                    print(general.warning(f"Something happened when querying Viewdns.info about '{query}'. Omitting..."))
        except KeyboardInterrupt:
            print(general.warning("\tStep 5 manually skipped by the user...\n"))

        # Trying to store the information recovered
        if args.output_folder != None:
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)
            # Grabbing the results
            fileHeader = os.path.join(args.output_folder, args.file_header)
            for ext in args.extension:
                # Generating output files
                general.export_usufy(results, ext, fileHeader)

        # Showing the information gathered if requested
        if not args.quiet:
            now = dt.datetime.now()
            print(f"\n{now}\tResults obtained:\n")
            print(general.success(general.osrf_to_text_export(results)))

            now = dt.datetime.now()
            print(f"\n{now}\tYou can find all the information collected in the following files:")
            for ext in args.extension:
                # Showing the output files
                print(general.emphasis("\t" + fileHeader + "." + ext))

        # Showing the execution time...
        if not args.quiet:
            end_time = dt.datetime.now()
            print("\n{end_time}\tFinishing execution...\n")
            print("Total time used:\t" + general.emphasis(str(end_time - start_time)))

        if not args.quiet:
            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

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
import signal
import socket
# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool

import whois

import osrframework
import osrframework.domains.gtld as gtld
import osrframework.domains.cctld as cctld
import osrframework.domains.generic_tld as generic_tld
import osrframework.domains.geographic_tld as geographic_tld
import osrframework.domains.brand_tld as brand_tld
import osrframework.domains.other_subdomains as other_subdomains
import osrframework.utils.banner as banner
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general


# Defining the TLD dictionary based on <https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains>
TLD = {}
# Global TLD
TLD["global"] = gtld.tld
# Country Code TLD
TLD["cc"] = cctld.tld
# Generic TLD
TLD["generic"] = generic_tld.tld
# Geographic TLD
TLD["geographic"] = geographic_tld.tld
# Brand TLD
TLD["brand"] = brand_tld.tld
# Other TLD
#TLD["other"] = other_subdomains.tld


def get_whois_info(domain):
    """Method that trie to recover the whois info from a domain

    Args:
        domain: The domain to verify.

    Returns:
        dict: A dictionary containing the result as an i3visio entity with its
            `value`, `type` and `attributes`.

    Raises:
        Exception in case the whois fails.
    """
    print(f"[i] Running whois for '{general.info(domain)}'...")
    new = []

    # Grabbing the aliases
    try:
        tmp = {}
        tmp["type"] = "com.i3visio.Alias"
        tmp["value"] = str(domain.split(".")[0])
        tmp["attributes"] = []
        new.append(tmp)
    except Exception:
        pass

    info = whois.whois(domain)

    if info.status is None:
        raise Exception("UnknownDomainError: " + domain + " could not be resolved.")

    # Grabbing the emails
    try:
        emails = {}
        emails["type"] = "com.i3visio.Email"
        if not isinstance(info.emails, list):
            aux = [info.emails]
            emails["value"] = json.dumps(aux)
        else:
            emails["value"] = json.dumps(info.emails)
        emails["attributes"] = []
        new.append(emails)
    except Exception:
        pass

    # Grabbing the country
    try:
        if info.country:
            tmp = {}
            tmp["type"] = "com.i3visio.Location.Country"
            tmp["value"] = info.country
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the state
    try:
        if info.state:
            tmp = {}
            tmp["type"] = "com.i3visio.Location.State"
            tmp["value"] = info.state
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the address
    try:
        if info.address:
            tmp = {}
            tmp["type"] = "com.i3visio.Location.Address"
            tmp["value"] = info.address
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the zipcode
    try:
        if info.zipcode:
            tmp = {}
            tmp["type"] = "com.i3visio.Location.Zipcode"
            tmp["value"] = info.zipcode
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the creation date
    try:
        if info.creation_date:
            tmp = {}
            tmp["type"] = "com.i3visio.Date.Creation"
            tmp["value"] = info.creation_date[0].isoformat(' ', 'seconds')
            tmp["attributes"] = []
            new.append(tmp)
    except Exception as e:
        pass

    # Grabbing the updated date
    try:
        if info.update_date:
            tmp = {}
            tmp["type"] = "com.i3visio.Date.Update"
            tmp["value"] = info.update_date[0].isoformat(' ', 'seconds')
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the expiration date
    try:
        if info.expiration_date:
            tmp = {}
            tmp["type"] = "com.i3visio.Date.Expiration"
            tmp["value"] = info.expiration_date[0].isoformat(' ', 'seconds')
            tmp["attributes"] = []
            new.append(tmp)
    except Exception:
        pass

    # Grabbing the regitrar
    try:
        tmp = {}
        tmp["type"] = "com.i3visio.Registrar"
        tmp["value"] = str(info.registrar)
        tmp["attributes"] = []
        new.append(tmp)
    except Exception:
        pass

    # Grabbing the regitrar
    try:
        tmp = {}
        tmp["type"] = "com.i3visio.Fullname"
        try:
            tmp["value"] = str(info.name)
        except Exception:
            tmp["value"] = info.name
        tmp["attributes"] = []
        new.append(tmp)
    except Exception:
        pass

    return new


def create_domains(tlds, nicks=None, nicks_file=None):
    """Method that globally permits to generate the domains to be checked

    Args:
        tlds (list): List of tlds.
        nicks (list): List of aliases.
        nicks_file (str): The filepath to the aliases file.

    Returns:
        list: The list of domains to be checked.
    """
    domain_candidates = []
    if nicks is not None:
        for nick in nicks:
            for tld in tlds:
                tmp = {
                    "domain" : nick + tld["tld"],
                    "type" : tld["type"],
                    "tld": tld["tld"]
                }
                domain_candidates.append(tmp)
    elif nicks_file is not None:
        with open(nicks_file, "r") as file:
            nicks = file.read().splitlines()
            for nick in nicks:
                for tld in tlds:
                    tmp = {
                        "domain" : nick + tld["tld"],
                        "type" : tld["type"],
                        "tld": tld["tld"]
                    }
                    domain_candidates.append(tmp)
    return domain_candidates


def is_blackListed(ipv4):
    """Method that checks if an IPv4 is blackslited

    There are some providers that resolve always. We have identified these IP
    so we have to perform an additional chdeck to confirm that the returned
    IPv4 is not a false positive.

    Args:
        ipv4: The IP to be verified.

    Returns:
        bool: It returns whether the IP is blacklisted.
    """
    return ipv4 in [
        "45.79.222.138",
        "88.198.29.97",
        "91.144.20.76",
        "127.0.0.1",
        "127.0.0.2",
        "127.0.53.53",
        "141.8.226.58",
        "144.76.162.245",
        "173.230.131.38",
        "109.95.242.11",
        "188.93.95.11",
        "173.230.141.80",
        "198.74.54.240",
        "64.70.19.203",
        "199.34.229.100",
        "109.95.244.12",
        "8.23.224.108",
        "203.119.4.201"
    ]


def pool_function(domain, launch_whois=False):
    """Wrapper for being able to launch all the threads of getPageWrapper.

    Args:
        domain: We receive the parameters as a dictionary.
        ```
        {
            "domain" : ".com",
            "type" : "global"
        }
        ```
        launch_whois: Whether the whois info will be launched.

    Returns:
        dict: A dictionary containing the following values:
        `{"platform" : str(domain), "status": "DONE", "data": aux}`
    """
    try:
        if domain["type"] != "other" and launch_whois:
            whois_info = get_whois_info(domain["domain"])
            print(f"[i] Whois data retrieved from '{general.info(domain['domain'])}'.")
        else:
            whois_info = None
    except Exception:
        # If something happened... Log the answer
        whois_info = None
        print(general.warning(f"[!] Something happened when running whois of '{domain['domain']}'."))

    try:
        aux = {}
        aux["type"] = "com.i3visio.Result"
        aux["value"] = "Domain Info - " + domain["domain"]
        if whois_info:
            aux["attributes"] = whois_info
        else:
            aux["attributes"] = []

        # Performing whois info and adding if necessary
        tmp = {}
        tmp["type"] = "com.i3visio.Domain"
        tmp["value"] = domain["domain"]
        tmp["attributes"] = []
        aux["attributes"].append(tmp)

        tmp = {}
        tmp["type"] = "com.i3visio.Domain.TLD.Type"
        tmp["value"] = domain["type"]
        tmp["attributes"] = []
        aux["attributes"].append(tmp)

        ipv4 = socket.gethostbyname(domain["domain"])

        # Check if this ipv4 normally throws false positives
        if is_blackListed(ipv4) and not whois_info:
            return {"platform": str(domain), "status": "ERROR", "data": {}}

        #If we arrive here... The domain resolves so we add the info:
        tmp = {}
        tmp["type"] = "com.i3visio.IPv4"
        tmp["value"] = ipv4
        tmp["attributes"] = []

        aux["attributes"].append(tmp)

        return {"platform" : str(domain), "status": "DONE", "data": aux}
    except Exception:
        if whois_info:
            return {"platform" : str(domain), "status": "DONE", "data": aux}

    return {"platform" : str(domain), "status": "ERROR", "data": {}}

def perform_search(domains=[], nThreads=16, launch_whois=False):
    """Method to perform the mail verification process

    Args:
        domains: List of domains to check.
        nThreads: Number of threads to use.
        launch_whois: Sets if whois queries will be launched.

    Returns:
        list: A list containing the results as i3visio entities.
    """
    results = []

    # Returning None if no valid domain has been returned
    if len(domains) == 0:
        return results

    # If the process is executed by the current app, we use the Processes. It is faster than pools.
    if nThreads <= 0 or nThreads > len(domains):
        nThreads = len(domains)

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

    pool_results = []
    try:
        def log_result(result):
            # This is called whenever foo_pool(i) returns a result.
            # result_list is modified only by the main process, not the pool workers.
            pool_results.append(result)

        for d in domains:
            # We need to create all the arguments that will be needed
            parameters = (d, launch_whois,)
            pool.apply_async(pool_function, args=parameters, callback=log_result)

        # Waiting for results to be finished
        while len(pool_results) < len(domains):
            pass
        # Closing normal termination
        pool.close()
    except KeyboardInterrupt:
        print(general.warning("\nProcess manually stopped by the user. Terminating workers.\n"))
        pool.terminate()
        print(general.warning("The following domains were not processed:"))
        pending_tld = ""
        for dom in domains:
            for processed_domain in pool_results:
                if str(dom) == processed_domain["platform"]:
                    break
            print(general.warning(f"\t- {dom['domain']}"))
            pending_tld += f" {dom['tld']}"

        print(general.warning("\n[!] If you want to relaunch the app with the remaining domains, you can always run the command with: "))
        print(general.warning(f"\t domainfy ... -t none -u {pending_tld}"))
        print(general.warning("\n[!] Otherwise, if you prefer to avoid these platforms in future searches, you can manually avoid them using: "))
        print(general.warning(f"\t domainfy ... -x {pending_tld}"))
    pool.join()

    # Processing the results
    # ----------------------
    for ser_array in pool_results:
        data = ser_array["data"]
        # We need to recover the results and check if they are not an empty json or None
        if data is not None and data != {}:
            results.append(data)
    return results


def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    DEFAULT_VALUES = configuration.get_configuration_values_for("domainfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        exclude_list = [DEFAULT_VALUES["exclude_platforms"]]
    except Exception:
        exclude_list = []

    parser = argparse.ArgumentParser(description='domainfy - Checking the existence of domains that resolev to an IP address.', prog='domainfy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    group_main_options = parser.add_mutually_exclusive_group(required=True)
    group_main_options.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help='the list of nicks to be checked in the domains selected.')
    group_main_options.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help='the file with the list of nicks to be checked in the domains selected.')
    group_main_options.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    group_processing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    group_processing.add_argument('-o', '--output-folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    group_processing.add_argument('-t', '--tlds', metavar='<tld_type>', nargs='+', choices=["all", "none"] + list(TLD.keys()), action='store', help='list of TLD types where the nick will be looked for.', required=False, default=DEFAULT_VALUES["tlds"])
    group_processing.add_argument('-u', '--user-defined', metavar='<new_tld>', nargs='+', action='store', help='additional TLD that will be searched.', required=False, default=DEFAULT_VALUES["user_defined"])
    group_processing.add_argument('-x', '--exclude', metavar='<domain>', nargs='+', required=False, default=exclude_list, action='store', help="select the domains to be avoided. The format should include the initial '.'.")
    group_processing.add_argument('-F', '--file-header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    group_processing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 16). If 0, the maximum number possible will be used, which may make the system feel unstable.')
    group_processing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')
    group_processing.add_argument('--whois', required=False, action='store_true', default=False, help='tells the program to launch whois queries.')

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

    saying_hello = f"""
    Domainfy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{general.LICENSE_URL}>.
"""
    print(general.info(saying_hello))

    if args.license:
        general.showLicense()
    else:
        # Processing the options returned to remove the "all" option
        tlds = []
        if "all" in args.tlds:
            for type_tld in TLD.keys():
                for tld in TLD[type_tld]:
                    if tld not in args.exclude:
                        tlds.append({"tld": tld, "type": type_tld})
        elif "none" in args.tlds:
            pass
        else:
            for type_tld in TLD.keys():
                if type_tld in args.tlds:
                    for tld in TLD[type_tld]:
                        if tld not in args.exclude:
                            tlds.append({"tld": tld, "type": type_tld})

        for new in args.user_defined:
            if new not in args.exclude:
                if new[0] == ".":
                    tlds.append({"tld": new, "type": "user_defined"})
                else:
                    tlds.append({"tld": "." + new, "type": "user_defined"})

        if args.nicks:
            domains = create_domains(tlds, nicks=args.nicks)
        else:
            # nicks_file
            domains = create_domains(tlds, nicks_file=args.nicks_file)

        # Showing the execution time...
        if not args.quiet:
            startTime = dt.datetime.now()
            print(f"{startTime}\tTrying to get information about {general.emphasis(str(len(domains)))} domain(s)…\n")
            if len(domains) > 200:
                print("""        Note that a full '-t all' search may take around 3.5 mins. If that's too
        long for you, try narrowing the search using '-t cc' or similar arguments.
        Otherwise, just wait and keep calm!
                """)
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

        # Perform searches, using different Threads
        results = perform_search(domains, args.threads, args.whois)

        # Trying to store the information recovered
        if args.output_folder is not None:
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
            print(f"\n{now}\t{general.success(len(results))} results obtained:\n")
            try:
                print(general.success(general.osrf_to_text_export(results)))
            except Exception:
                print(general.warning("\nSomething happened when exporting the results. The Json will be shown instead:\n"))
                print(general.warning(json.dumps(results, indent=2)))

            now = dt.datetime.now()
            print(f"\n{now}\tYou can find all the information collected in the following files:")
            for ext in args.extension:
                # Showing the output files
                print(f"\t{general.emphasis(file_header + '.' + ext)}")

        # Showing the execution time...
        if not args.quiet:
            # Showing the execution time...
            endTime = dt.datetime.now()
            print("\n{}\tFinishing execution...\n".format(endTime))
            print("Total time used:\t" + general.emphasis(str(endTime-startTime)))
            print("Average seconds/query:\t" + general.emphasis(str((endTime-startTime).total_seconds()/len(domains))) +" seconds\n")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return results


if __name__ == "__main__":
    main(sys.argv[1:])

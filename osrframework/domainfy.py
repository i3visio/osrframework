#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2016-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

'''
domainfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.  For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
__author__ = "Felix Brezo, Yaiza Rubio"
__copyright__ = "Copyright 2016-2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v5.2"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"

import argparse
import datetime as dt
import socket
import json
import os
import whois
import sys

# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool

import osrframework.utils.banner as banner
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general

import osrframework.domains.gtld as gtld
import osrframework.domains.cctld as cctld
import osrframework.domains.generic_tld as generic_tld
import osrframework.domains.geographic_tld as geographic_tld
import osrframework.domains.brand_tld as brand_tld
import osrframework.domains.other_subdomains as other_subdomains

import signal

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
# Brand TLD
TLD["other"] = other_subdomains.tld

def getNumberTLD():
    '''
        Counting the total number of TLD being processed.
    '''
    total = 0
    for typeTld in TLD.keys():
        total+= len(TLD[typeTld])
    return total

def getWhoisInfo(domain):
    '''
        Method that trie to recover the whois info from a domain.

        :param domain:   domain to verify.

        :result:
    '''
    new = []

    # Grabbing the aliases
    try:
        emails = {}
        emails["type"] = "i3visio.alias"
        emails["value"] = str(domain.split(".")[0])
        emails["attributes"] = []
        new.append(emails)
    except:
        pass

    info = whois.whois(domain)

    if info.status == None:
        raise Exception("UnknownDomainError: " + domain + " could not be resolved.")

    # Grabbing the emails
    try:
        emails = {}
        emails["type"] = "i3visio.email"
        if type(info.emails) is not list:
            aux = [info.emails]
            emails["value"] = json.dumps(aux)
        else:
            emails["value"] = json.dumps(info.emails)
        emails["attributes"] = []
        new.append(emails)
    except:
        pass

    # Grabbing the country
    try:
        tmp = {}
        tmp["type"] = "i3visio.location.country"
        tmp["value"] = str(info.country)
        tmp["attributes"] = []
        new.append(tmp)
    except:
        pass

    # Grabbing the regitrar
    try:
        tmp = {}
        tmp["type"] = "i3visio.registrar"
        tmp["value"] = str(info.registrar)
        tmp["attributes"] = []
        new.append(tmp)
    except:
        pass

    # Grabbing the regitrar
    try:
        tmp = {}
        tmp["type"] = "i3visio.fullname"
        try:
            tmp["value"] = str(info.name)
        except:
            tmp["value"] = info.name
        tmp["attributes"] = []
        new.append(tmp)
    except:
        pass

    return new

def createDomains(tlds, nicks=None, nicksFile=None):
    '''
        Method that globally permits to generate the domains to be checked.

        :param tlds:  list of tlds.
        :param nicks:   list of aliases.
        :param nicksFile:  filepath to the aliases file.

        :result:    list of domains to be checked

    '''
    domain_candidates = []
    if nicks != None:
        for n in nicks:
            for t in tlds:
                tmp = {
                    "domain" : n + t["tld"],
                    "type" : t["type"],
                    "tld": t["tld"]
                }
                domain_candidates.append(tmp)
    elif nicksFile != None:
        with open(nicksFile, "r") as iF:
            nicks = iF.read().splitlines()
            for n in nicks:
                for t in tlds:
                    tmp = {
                        "domain" : n + t["tld"],
                        "type" : t["type"],
                        "tld": t["tld"]
                    }
                    domain_candidates.append(tmp)
    return domain_candidates


def isBlackListed(ipv4):
    """There are some providers that resolve always. We have identified these IP
        so we have to perform an additional chdeck to confirm that the returned
        IPv4 is not a false positive.
    """
    BLACKLISTED = [
        "45.79.222.138",
        "88.198.29.97",
        "91.144.20.76",
        "127.0.0.1",
        "127.0.0.2",
        "127.0.53.53",
        "141.8.226.58",
        "144.76.162.245"
    ]

    if ipv4 in BLACKLISTED:
        return True
    else:
        return False

def pool_function(domain):
    """
        Wrapper for being able to launch all the threads of getPageWrapper.
        :param domain: We receive the parameters as a dictionary.
        {
            "domain" : ".com",
            "type" : "global"
        }
    """
    is_valid = True
    try:
        ipv4 = socket.gethostbyname(domain["domain"])

        # Check if this ipv4 normally throws false positives
        if isBlackListed(ipv4):
            return {"platform" : str(domain), "status": "ERROR", "data": {}}

        #If we arrive here... The domain exists!!
        aux = {}
        aux["type"] = "i3visio.result"
        aux["value"] = "Domain Info - " + domain["domain"]
        # Performing whois info
        try:
            aux["attributes"] = getWhoisInfo(domain["domain"])
        except Exception as e:
            # If something happened... Well, we'll return an empty attributes array.
            aux["attributes"] = []

        tmp = {}
        tmp["type"] = "i3visio.domain"
        tmp["value"] =  domain["domain"]
        tmp["attributes"] = []

        aux["attributes"].append(tmp)

        tmp = {}
        tmp["type"] = "i3visio.tld_type"
        tmp["value"] =  domain["type"]
        tmp["attributes"] = []

        aux["attributes"].append(tmp)

        tmp = {}
        tmp["type"] = "i3visio.ipv4"
        tmp["value"] =  ipv4
        tmp["attributes"] = []

        aux["attributes"].append(tmp)

        return {"platform" : str(domain), "status": "DONE", "data": aux}
    except Exception as e:
        return {"platform" : str(domain), "status": "ERROR", "data": {}}

def performSearch(domains=[], nThreads=16):
    '''
        Method to perform the mail verification process.

        :param domains: List of domains to check.

        :return:
    '''
    results = []

    # Using threads in a pool if we are not running the program in main
    args = []

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

    poolResults = []
    try:
        def log_result(result):
            # This is called whenever foo_pool(i) returns a result.
            # result_list is modified only by the main process, not the pool workers.
            poolResults.append(result)

        for d in domains:
            # We need to create all the arguments that will be needed
            parameters = ( d, )
            pool.apply_async (pool_function, args= parameters, callback = log_result )

        # Waiting for results to be finished
        while len(poolResults) < len(domains):
            pass
        # Closing normal termination
        pool.close()
    except KeyboardInterrupt:
        print "\nProcess manually stopped by the user. Terminating workers.\n"
        pool.terminate()
        print "The following domains were not processed:"
        pending_tld = ""
        for d in domains:
            processed = False
            for processedDomain in poolResults:
                if str(d) == processedDomain["platform"]:
                    processed = True
                    break
            if not processed:
                print "\t- " + str(d["domain"])
                pending_tld += " " + str(d["tld"])
        print
        print "[!] If you want to relaunch the app with these domains you can always run the command with: "
        print "\t domainfy.py ... -t none -u " + pending_tld
        print
        print "[!] If you prefer to avoid these platforms you can manually evade them for whatever reason with: "
        print "\t domainfy.py ... -x " + pending_tld
        print
    pool.join()


    # Processing the results
    # ----------------------
    for serArray in poolResults:
        data = serArray["data"]
        # We need to recover the results and check if they are not an empty json or None
        if data != None and data != {}:
            results.append(data)
    return results

def main(args):
    '''
        Main program of domainfy.

        :param args: Arguments received in the command line.
    '''
    sayingHello = """domainfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit <http://www.gnu.org/licenses/gpl-3.0.txt>."""
    if not args.quiet:
        print banner.text

        print sayingHello
        print

    # Processing the options returned to remove the "all" option
    tlds = []
    if "all" in args.tlds:
        for typeTld in TLD.keys():
            for tld in TLD[typeTld]:
                if tld not in args.exclude:
                    tlds.append({ "tld" : tld, "type" : typeTld })
    elif "none" in args.tlds:
        pass
    else:
        for typeTld in TLD.keys():
            if typeTld in args.tlds:
                for tld in TLD[typeTld]:
                    if tld not in args.exclude:
                        tlds.append({ "tld" : tld, "type" : typeTld })

    for new in args.user_defined:
        if new not in args.exclude:
            tlds.append( {"tld": new, "type": "user_defined"})

    if args.nicks:
        domains = createDomains(tlds, nicks = args.nicks)
    else:
        # nicks_file
        domains = createDomains(tlds, nicksFile = args.nicks_file)

    # Showing the execution time...
    if not args.quiet:
        startTime= dt.datetime.now()
        print str(startTime) +"\tStarting the lookup in up to " + str(len(tlds))+ " different domains. Be patient!"
        print
        print "\tPress <Ctrl + C> to stop..."
        print
    # Perform searches, using different Threads
    results = performSearch(domains, args.threads)

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
        print "A summary of the results obtained are shown in the following table:"
        try:
            print str(general.usufyToTextExport(results))
        except:
            print results
        print

        print "You can find all the information collected in the following files:"
        for ext in args.extension:
            # Showing the output files
            print "\t-" + fileHeader + "." + ext
    # Showing the execution time...
    if not args.quiet:
        print
        endTime= dt.datetime.now()
        print str(endTime) +"\tFinishing execution..."
        print
        print "Total time used:\t" + str(endTime-startTime)
        print "Average seconds/query:\t" + str((endTime-startTime).total_seconds()/len(domains)) +" seconds"
        print

    # Urging users to place an issue on Github...
    if not args.quiet:
        print
        print "Did something go wrong? Is a platform reporting false positives? Do you need to integrate a new one?"
        print "Then, place an issue in the Github project: <https://github.com/i3visio/osrframework/issues>."
        print "Note that otherwise, we won't know about it!"
        print

    return results

def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("domainfy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        excludeList = []

    parser = argparse.ArgumentParser(description='domainfy.py - Checking the existence of domains.', prog='domainfy.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the domains selected.')
    groupMainOptions.add_argument('-N', '--nicks_file', metavar='<nicks_file>', action='store', help = 'the file with the list of nicks to be checked in the domains selected.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    #groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'mtz', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-t', '--tlds',  metavar='<tld_type>',  nargs='+', choices=["all", "none"] + TLD.keys(), action='store', help='List of tld types where the nick will be looked for.', required=False, default=DEFAULT_VALUES["tlds"])
    groupProcessing.add_argument('-u', '--user_defined',  metavar='<new_tld>',  nargs='+', action='store', help='Additional TLD that will be searched.', required=False, default = DEFAULT_VALUES["user_defined"])
    groupProcessing.add_argument('-x', '--exclude', metavar='<domain>', nargs='+', required=False, default=excludeList, action='store', help="select the domains to be avoided. The format should include the initial '.'.")

    # Getting a sample header for the output files
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default= int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 16). If 0, the maximum number possible will be used, which may make the system feel unstable.')
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

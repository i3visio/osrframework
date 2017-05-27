#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2014-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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
usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
    python usufy.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2014-2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v5.2"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import json
import os
import datetime as dt
import traceback

# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool

# configuration and utils
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.banner as banner
import osrframework.utils.benchmark as benchmark
import osrframework.utils.browser as browser
import osrframework.utils.general as general

# logging imports
import osrframework.utils.logger
import logging

# Preparing to capture interruptions smoothly
import signal


def fuzzUsufy(fDomains = None, fFuzzStruct = None):
    '''
        Method to guess the usufy path against a list of domains or subdomains.

        :param fDomains:    a list to strings containing the domains and (optionally) a nick.
        :param fFuzzStruct:    a list to strings containing the transforms to be performed.

        :return:    Dictionary of {domain: url}.
    '''
    logger = logging.getLogger("osrframework.usufy")

    if fFuzzStruct == None:
        # Loading these structures by default
        fuzzingStructures = [
                    "http://<DOMAIN>/<USERNAME>",
                    "http://<DOMAIN>/~<USERNAME>",
                    "http://<DOMAIN>/?action=profile;user=<USERNAME>",
                    "http://<DOMAIN>/causes/author/<USERNAME>",
                    "http://<DOMAIN>/channel/<USERNAME>",
                    "http://<DOMAIN>/community/profile/<USERNAME>",
                    "http://<DOMAIN>/component/comprofiler/userprofiler/<USERNAME>",
                    "http://<DOMAIN>/details/@<USERNAME>",
                    "http://<DOMAIN>/foros/member.php?username=<USERNAME>",
                    "http://<DOMAIN>/forum/member/<USERNAME>",
                    "http://<DOMAIN>/forum/member.php?username=<USERNAME>",
                    "http://<DOMAIN>/forum/profile.php?mode=viewprofile&u=<USERNAME>",
                    "http://<DOMAIN>/home/<USERNAME>",
                    "http://<DOMAIN>/index.php?action=profile;user=<USERNAME>",
                    "http://<DOMAIN>/member_profile.php?u=<USERNAME>",
                    "http://<DOMAIN>/member.php?username=<USERNAME>",
                    "http://<DOMAIN>/members/?username=<USERNAME>",
                    "http://<DOMAIN>/members/<USERNAME>",
                    "http://<DOMAIN>/members/view/<USERNAME>",
                    "http://<DOMAIN>/mi-espacio/<USERNAME>",
                    "http://<DOMAIN>/u<USERNAME>",
                    "http://<DOMAIN>/u/<USERNAME>",
                    "http://<DOMAIN>/user-<USERNAME>",
                    "http://<DOMAIN>/user/<USERNAME>",
                    "http://<DOMAIN>/user/<USERNAME>.html",
                    "http://<DOMAIN>/users/<USERNAME>",
                    "http://<DOMAIN>/usr/<USERNAME>",
                    "http://<DOMAIN>/usuario/<USERNAME>",
                    "http://<DOMAIN>/usuarios/<USERNAME>",
                    "http://<DOMAIN>/en/users/<USERNAME>",
                    "http://<DOMAIN>/people/<USERNAME>",
                    "http://<DOMAIN>/profil/<USERNAME>",
                    "http://<DOMAIN>/profile/<USERNAME>",
                    "http://<DOMAIN>/profile/page/<USERNAME>",
                    "http://<DOMAIN>/rapidforum/index.php?action=profile;user=<USERNAME>",
                    "http://<DOMAIN>/social/usuarios/<USERNAME>",
                    "http://<USERNAME>.<DOMAIN>",
                    "http://<USERNAME>.<DOMAIN>/user/"
                ]
    else:
        try:
            fuzzingStructures = fFuzzStruct.read().splitlines()
        except:
            logger.error("Usufy could NOT open the following file: " + fFuzzStruct )

    res = {}

    lines = fDomains.read().splitlines()

    # Going through all the lines
    for l in lines:
        domain = l.split()[0]
        print "Performing tests for" + domain + "..."

        # selecting the number of nicks to be tested in this domain
        nick = l.split()[1]

        # Choosing the errors from the input file
        #errors = l.split('\t')[2:]

        # possibleURLs found
        possibleURL = []

        for struct in fuzzingStructures:
            # initiating list
            urlToTry = struct.replace("<DOMAIN>", domain)
            test = urlToTry.replace("<USERNAME>", nick.lower())
            print "Processing "+ test + "..."
            i3Browser = browser.Browser()
            try:
                html = i3Browser.recoverURL(test)
                if nick in html:
                    possibleURL.append(test)
                    print "\tPossible usufy found!!!\n"
            except:
                logger.error("The resource could not be downloaded.")

        #print possibleURL
        res[domain] = possibleURL

    print json.dumps(res, indent = 2)
    return res


def getPageWrapper(p, nick, rutaDescarga, avoidProcessing = True, avoidDownload = True, outQueue=None):
    '''
        Method that wraps the call to the getInfo. Before it was getUserPage.

        List of parameters that the method receives:
        :param pName:        platform where the information is stored. It is a string.
        :param nick:        nick to be searched.
        :param rutaDescarga:    local file where saving the obtained information.
        :param avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).
        :param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).
        :param outQueue:    Queue where the information will be stored.
        :param maltego:        parameter to tell usufy.py that he has been invoked by Malego.

           :return:
            None if a queue is provided. Note that the values will be stored in the outQueue or a dictionary is returned.
    '''
    logger = logging.getLogger("osrframework.usufy")

    logger.debug("\tLooking for profiles in " + str(p) + "...")
    #res = p.getUserPage(nick, rutaDescarga, avoidProcessing = avoidProcessing, avoidDownload = avoidDownload)
    try:
        res = p.getInfo(query=nick, mode="usufy", process=True)#rutaDescarga, avoidProcessing = avoidProcessing, avoidDownload = avoidDownload)

        if res != []:
            if outQueue != None:
                #logger.info("\t" + (str(p) +" - User profile found: ").ljust(40, ' ') + url)
                # Storing in the output queue the values
                outQueue.put((res))
            else:
                # If no queue was given, return the value normally
                return res
        else:
            logger.debug("\t" + str(p) +" - User profile not found...")
        return []
    except:
        print "ERROR: something happened when processing " + str(p) +". You may like to deactivate this wrapper if the error persist."
        return []


def pool_function(p, nick, rutaDescarga, avoidProcessing = True, avoidDownload = True, outQueue=None):
    '''
        Wrapper for being able to launch all the threads of getPageWrapper.
        :param args: We receive the parameters for getPageWrapper as a tuple.
    '''
    try:
        res = getPageWrapper(p, nick, rutaDescarga, avoidProcessing, avoidDownload, outQueue)
        return {"platform" : str(p), "status": "DONE", "data": res}
    except Exception as e:
        print "\tERROR: " + str(p)
        return {"platform" : str(p), "status": "ERROR", "data": []}


def processNickList(nicks, platforms=None, rutaDescarga="./", avoidProcessing=True, avoidDownload=True, nThreads=12, maltego=False, verbosity=1, logFolder="./logs"):
    '''
        Method that receives as a parameter a series of nicks and verifies whether those nicks have a profile associated in different social networks.

        List of parameters that the method receives:
        :param nicks:        list of nicks to process.
        :param platforms:    list of <Platform> objects to be processed.
        :param rutaDescarga:    local file where saving the obtained information.
        :param avoidProcessing:    boolean var that defines whether the profiles will NOT be processed.
        :param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).
        :param maltego:        parameter to tell usufy.py that he has been invoked by Malego.
        :param verbosity:    the level of verbosity to be used.
        :param logFolder:    the path to the log folder.

        :return:
            Returns a dictionary where the key is the nick and the value another dictionary where the keys are the social networks and te value is the corresponding URL.
    '''
    osrframework.utils.logger.setupLogger(loggerName="osrframework.usufy", verbosity=verbosity, logFolder=logFolder)
    logger = logging.getLogger("osrframework.usufy")

    if platforms == None:
        platforms = platform_selection.getAllPlatformNames("usufy")

    # Defining the output results variable
    res = []
    # Processing the whole list of terms...
    for nick in nicks:
        logger.info("Looking for '" + nick + "' in " + str(len(platforms)) + " different platforms:\n" +str( [ str(plat) for plat in platforms ] ) )

        # If the process is executed by the current app, we use the Processes. It is faster than pools.
        if nThreads <= 0 or nThreads > len(platforms):
            nThreads = len(platforms)
        logger.info("Launching " + str(nThreads) + " different threads...")

        # Using threads in a pool if we are not running the program in main
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

            for plat in platforms:
                # We need to create all the arguments that will be needed
                parameters = ( plat, nick, rutaDescarga, avoidProcessing, avoidDownload, )
                pool.apply_async (pool_function, args= parameters, callback = log_result )

            # Waiting for results to be finished
            while len(poolResults) < len(platforms):
                #print "Waiiting to finish all!"
                pass
            # Closing normal termination
            pool.close()
        except KeyboardInterrupt:
            print "\n[!] Process manually stopped by the user. Terminating workers.\n"
            pool.terminate()
            print "[!] The following platforms were not processed:"
            pending = ""
            for p in platforms:
                processed = False
                for processedPlatform in poolResults:
                    if str(p) == processedPlatform["platform"]:
                        processed = True
                        break
                if not processed:
                    print "\t- " + str(p)
                    pending += " " + str(p).lower()
            print
            print "[!] If you want to relaunch the app with these platforms you can always run the command with: "
            print "\t usufy.py ... -p " + pending
            print
            print "[!] If you prefer to avoid these platforms you can manually evade them for whatever reason with: "
            print "\t usufy.py ... -x " + pending
            print
        pool.join()

        profiles = []

        # Processing the results
        # ----------------------
        for serArray in poolResults:
            data = serArray["data"]
            # We need to recover the results and check if they are not an empty json or None
            if data != None:
                array = json.loads(data)
                for r in array:
                    if r != "{}":
                        profiles.append(r)
        res+=profiles
    return res


def main(args):
    '''
        Main function. This function is created in this way so as to let other applications make use of the full configuration capabilities of the application.
    '''
    # Recovering the logger
    # Calling the logger when being imported
    osrframework.utils.logger.setupLogger(loggerName="osrframework.usufy", verbosity=args.verbose, logFolder=args.logfolder)
    # From now on, the logger can be recovered like this:
    logger = logging.getLogger("osrframework.usufy")
    # Printing the results if requested
    if not args.maltego:
        print banner.text

        sayingHello = """usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions. For additional info, visit <http://www.gnu.org/licenses/gpl-3.0.txt>."""
        logger.info(sayingHello)
        print sayingHello
        print
        logger.info("Starting usufy.py...")

    if args.license:
        logger.info("Looking for the license...")
        # showing the license
        try:
            with open ("COPYING", "r") as iF:
                contenido = iF.read().splitlines()
                for linea in contenido:
                    print linea
        except Exception:
            try:
                # Trying to recover the COPYING file...
                with open ("/usr/share/osrframework/COPYING", "r") as iF:
                    contenido = iF.read().splitlines()
                    for linea in contenido:
                        print linea
            except:
                logger.error("ERROR: there has been an error when opening the COPYING file.\n\tThe file contains the terms of the GPLv3 under which this software is distributed.\n\tIn case of doubts, verify the integrity of the files or contact contacto@i3visio.com.")
    elif args.fuzz:
        logger.info("Performing the fuzzing tasks...")
        res = fuzzUsufy(args.fuzz, args.fuzz_config)
        logger.info("Recovered platforms:\n" + str(res))
    else:
        logger.debug("Recovering the list of platforms to be processed...")
        # Recovering the list of platforms to be launched
        listPlatforms = platform_selection.getPlatformsByName(platformNames=args.platforms, tags=args.tags, mode="usufy", excludePlatformNames=args.exclude)
        logger.debug("Platforms recovered.")

        if args.info:
            # Information actions...
            if args.info == 'list_platforms':
                infoPlatforms="Listing the platforms:\n"
                for p in listPlatforms:
                    infoPlatforms += "\t\t" + (str(p) + ": ").ljust(16, ' ') + str(p.tags)+"\n"
                logger.info(infoPlatforms)
                return infoPlatforms
            elif args.info == 'list_tags':
                logger.info("Listing the tags:")
                tags = {}
                # Going through all the selected platforms to get their tags
                for p in listPlatforms:
                    for t in p.tags:
                        if t not in tags.keys():
                            tags[t] = 1
                        else:
                            tags[t] += 1
                infoTags = "List of tags:\n"
                # Displaying the results in a sorted list
                for t in tags.keys():
                    infoTags += "\t\t" + (t + ": ").ljust(16, ' ') + str(tags[t]) + "  time(s)\n"
                logger.info(infoTags)
                return infoTags
            else:
                pass

        # performing the test
        elif args.benchmark:
            logger.warning("The benchmark mode may last some minutes as it will be performing similar queries to the ones performed by the program in production. ")
            logger.info("Launching the benchmarking tests...")
            platforms = platform_selection.getAllPlatformNames("usufy")
            res = benchmark.doBenchmark(platforms)
            strTimes = ""
            for e in sorted(res.keys()):
                strTimes += str(e) + "\t" + str(res[e]) + "\n"
            logger.info(strTimes)
            return strTimes

        # showing the tags of the usufy platforms
        elif args.show_tags:
            logger.info("Collecting the list of tags...")
            tags = platform_selection.getAllPlatformNamesByTag("usufy")
            logger.info(json.dumps(tags, indent=2))
            print "This is the list of platforms grouped by tag."
            print
            print json.dumps(tags, indent=2, sort_keys=True)
            print
            print "[Tip] Remember that you can always launch the platform using the -t option followed by any of the aforementioned."
            print
            return tags

        # Executing the corresponding process...
        else:
            # Showing the execution time...
            if not args.maltego:
                startTime= dt.datetime.now()
                print str(startTime) +"\tStarting search in " + str(len(listPlatforms)) + " platform(s)... Relax!"
                print
                print "\tPress <Ctrl + C> to stop..."
                print

            # Defining the list of users to monitor
            nicks = []
            logger.debug("Recovering nicknames to be processed...")
            if args.nicks:
                for n in args.nicks:
                    # TO-DO
                    #     A trick to avoid having the processing of the properties when being queried by Maltego
                    if "properties.i3visio" not in n:
                        nicks.append(n)
            else:
                # Reading the nick files
                try:
                    nicks = args.list.read().splitlines()
                except:
                    logger.error("ERROR: there has been an error when opening the file that stores the nicks.\tPlease, check the existence of this file.")

            # Definning the results
            res = []

            if args.output_folder != None:
                # if Verifying an output folder was selected
                logger.debug("Preparing the output folder...")
                if not args.maltego:
                    if not os.path.exists(args.output_folder):
                        logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
                        os.makedirs(args.output_folder)
                # Launching the process...
                ###try:
                res = processNickList(nicks, listPlatforms, args.output_folder, avoidProcessing = args.avoid_processing, avoidDownload = args.avoid_download, nThreads=args.threads, verbosity= args.verbose, logFolder=args.logfolder)
                ###except Exception as e:
                    ###print "Exception grabbed when processing the nicks: " + str(e)
                    ###print traceback.print_stack()
            else:
                try:
                    res = processNickList(nicks, listPlatforms, nThreads=args.threads, verbosity= args.verbose, logFolder=args.logfolder)
                except Exception as e:
                    print "Exception grabbed when processing the nicks: " + str(e)
                    print traceback.print_stack()

            logger.info("Listing the results obtained...")
            # We are going to iterate over the results...
            strResults = "\t"

            # Structure returned
            """
            [
                {
                  "attributes": [
                    {
                      "attributes": [],
                      "type": "i3visio.uri",
                      "value": "http://twitter.com/i3visio"
                    },
                    {
                      "attributes": [],
                      "type": "i3visio.alias",
                      "value": "i3visio"
                    },
                    {
                      "attributes": [],
                      "type": "i3visio.platform",
                      "value": "Twitter"
                    }
                  ],
                  "type": "i3visio.profile",
                  "value": "Twitter - i3visio"
                }
                ,
                ...
            ]
            """
            for r in res:
                # The format of the results (attributes) for a given nick is a list as follows:

                for att in r["attributes"]:
                    # iterating through the attributes
                    platform = ""
                    uri = ""
                    for details in att["attributes"]:
                        if details["type"] == "i3visio.platform":
                            platform = details["value"]
                        if details["type"] == "i3visio.uri":
                            uri = details["value"]
                    try:
                        strResults+= (str(platform) + ":").ljust(16, ' ')+ " "+ str(uri)+"\n\t\t"
                    except:
                        pass

                logger.info(strResults)

            # Generating summary files for each ...
            if args.extension:
                # Storing the file...
                logger.info("Creating output files as requested.")
                if not args.maltego:
                    # Verifying if the outputPath exists
                    if not os.path.exists (args.output_folder):
                        logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
                        os.makedirs(args.output_folder)

                    # Grabbing the results
                    fileHeader = os.path.join(args.output_folder, args.file_header)

                    # Iterating through the given extensions to print its values
                    for ext in args.extension:
                        # Generating output files
                        general.exportUsufy(res, ext, fileHeader)

            # Generating the Maltego output
            if args.maltego:
                general.listToMaltego(res)
            # Printing the results if requested
            else:
                print "A summary of the results obtained are shown in the following table:"
                #print res
                print unicode(general.usufyToTextExport(res))

                print

                if args.web_browser:
                    general.openResultsInBrowser(res)

                print "You can find all the information collected in the following files:"
                for ext in args.extension:
                    # Showing the output files
                    print "\t-" + fileHeader + "." + ext

                # Showing the execution time...
                print
                endTime= dt.datetime.now()
                print str(endTime) +"\tFinishing execution..."
                print
                print "Total time used:\t" + str(endTime-startTime)
                print "Average seconds/query:\t" + str((endTime-startTime).total_seconds()/len(listPlatforms)) +" seconds"
                print

                # Urging users to place an issue on Github...
                print
                print "Did something go wrong? Is a platform reporting false positives? Do you need to integrate a new one?"
                print "Then, place an issue in the Github project: <https://github.com/i3visio/osrframework/issues>."
                print "Note that otherwise, we won't know about it!"
                print

            return res


def getParser():
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("usufy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        excludeList = []

    # Recovering all the possible options
    platOptions = platform_selection.getAllPlatformNames("usufy")

    parser = argparse.ArgumentParser(description='usufy.py - Piece of software that checks the existence of a profile for a given user in up to ' + str(len(platOptions)-1)+ ' different platforms.', prog='usufy.py', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    # Defining the mutually exclusive group for the main options
    groupMainOptions = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    groupMainOptions.add_argument('--info', metavar='<action>', choices=['list_platforms', 'list_tags'], action='store', help='select the action to be performed amongst the following: list_platforms (list the details of the selected platforms), list_tags (list the tags of the selected platforms). Afterwards, it exists.')
    groupMainOptions.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')
    groupMainOptions.add_argument('-b', '--benchmark',  action='store_true', default=False, help='perform the benchmarking tasks.')
    groupMainOptions.add_argument('-f', '--fuzz', metavar='<path_to_fuzzing_list>', action='store', type=argparse.FileType('r'), help='this option will try to find usufy-like URLs. The list of fuzzing platforms in the file should be (one per line): <BASE_DOMAIN>\t<VALID_NICK>')
    groupMainOptions.add_argument('-l', '--list',  metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
    groupMainOptions.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')
    groupMainOptions.add_argument('--show_tags',  action='store_true', default=False, help='it will show the platforms grouped by tags.')

    # Selecting the platforms where performing the search
    groupPlatforms = parser.add_argument_group('Platform selection arguments', 'Criteria for selecting the platforms where performing the search.')
    groupPlatforms.add_argument('-p', '--platforms', metavar='<platform>', choices=platOptions, nargs='+', required=False, default=DEFAULT_VALUES["platforms"], action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(platOptions) + '. More than one option can be selected.')
    groupPlatforms.add_argument('-t', '--tags', metavar='<tag>', default = [], nargs='+', required=False, action='store', help='select the list of tags that fit the platforms in which you want to perform the search. More than one option can be selected.')
    groupPlatforms.add_argument('-x', '--exclude', metavar='<platform>', choices=platOptions, nargs='+', required=False, default=excludeList, action='store', help='select the platforms that you want to exclude from the processing.')

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
    groupProcessing.add_argument('--avoid_download', required=False, action='store_true', default=False, help='argument to force usufy NOT to store the downloadable version of the profiles.')
    groupProcessing.add_argument('--avoid_processing', required=False, action='store_true', default=False, help='argument to force usufy NOT to perform any processing task with the valid profiles.')
    groupProcessing.add_argument('--fuzz_config',  metavar='<path_to_fuzz_list>', action='store', type=argparse.FileType('r'), help='path to the fuzzing config details. Wildcards such as the domains or the nicknames should come as: <DOMAIN>, <USERNAME>.')
    groupProcessing.add_argument('--nonvalid', metavar='<not_valid_characters>', required=False, default = '\\|<>=', action='store', help="string containing the characters considered as not valid for nicknames." )
    groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'mtz', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES["extension"], action='store', help='output extension for the summary files. Default: xls.')
    groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    groupProcessing.add_argument('-m', '--maltego', required=False, action='store_true', help='parameter specified to let usufy.py know that he has been launched by a Maltego Transform.')
    groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES["output_folder"], action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    groupProcessing.add_argument('-w', '--web_browser', required=False, action='store_true', help='opening the uris returned in the default web browser.')
    # Getting a sample header for the output files
    groupProcessing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES["file_header"], action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=int(DEFAULT_VALUES["threads"]), type=int, help='write down the number of threads to be used (default 32). If 0, the maximum number possible will be used, which may make the system feel unstable.')

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +__version__, help='shows the version of the program and exists.')

    return parser


if __name__ == "__main__":
    # Grabbing the parser
    parser = getParser()

    args = parser.parse_args()

    # Calling the main function
    main(args)

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
import colorama
colorama.init(autoreset=True)
import datetime as dt
import json
# global issues for multiprocessing
from multiprocessing import Process, Queue, Pool
import os
# Preparing to capture interruptions smoothly
import signal
import sys
import time
import traceback
import textwrap

# configuration and utils
import osrframework
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.banner as banner
import osrframework.utils.benchmark as benchmark
import osrframework.utils.browser as browser
import osrframework.utils.general as general
from osrframework.utils.exceptions import *


def fuzzUsufy(fDomains = None, fFuzzStruct = None):
    """
    Method to guess the usufy path against a list of domains or subdomains.

    Args:
        fDomains: A list to strings containing the domains and (optionally) a
            nick.
        fFuzzStruct: A list to strings containing the transforms to be
            performed.

    Returns:
        dict: A dictionary of the form of `{"domain": "url"}`.
    """
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
            print("Usufy could NOT open the following file: " + fFuzzStruct)

    res = {}

    lines = fDomains.read().splitlines()

    # Going through all the lines
    for l in lines:
        domain = l.split()[0]
        print("Performing tests for" + domain + "...")

        # selecting the number of nicks to be tested in this domain
        nick = l.split()[1]

        # possibleURLs found
        possibleURL = []

        for struct in fuzzingStructures:
            # initiating list
            urlToTry = struct.replace("<DOMAIN>", domain)
            test = urlToTry.replace("<USERNAME>", nick.lower())
            print("Processing "+ test + "...")
            i3Browser = browser.Browser()
            try:
                html = i3Browser.recoverURL(test)
                if nick in html:
                    possibleURL.append(test)
                    print(general.success("\tPossible usufy found!!!\n"))
            except:
                print("The resource could not be downloaded.")

        res[domain] = possibleURL

    print(json.dumps(res, indent = 2))
    return res


def pool_function(p, nick, rutaDescarga, avoidProcessing=True, avoidDownload=True, verbosity=1):
    """
    Wrapper for being able to launch all the threads of getPageWrapper.

    We receive the parameters for getPageWrapper as a tuple.

    Args:
        pName: Platform where the information is stored. It is a string.
        nick: Nick to be searched.
        rutaDescarga: Local file where saving the obtained information.
        avoidProcessing: Boolean var that defines whether the profiles will NOT
            be processed (stored in this version).
        avoidDownload: Boolean var that defines whether the profiles will NOT be
            downloaded (stored in this version).
        verbosity: The verbosity level: 1, shows errors; 2, shows warnings.

    Returns:
        A dictionary with the following structure:
        {
        	"platform": "Platform",
        	"status": "DONE",
        	"data": "<data>"
        }
        Data is None or a serialized representation of the dictionary.
    """
    try:
        res = p.get_info(
            query=nick,
            mode="usufy"
        )
        return {"platform" : str(p), "status": "Ok", "data": res}

    except Exception as e:
        if (isinstance(e, OSRFrameworkError) and verbosity >= 1) and (isinstance(e, OSRFrameworkException) and verbosity >= 2):
            print(str(e))
        return {"platform" : str(p), "status": e, "data": e.generic}


def process_nick_list(nicks, platforms=None, rutaDescarga="./", avoidProcessing=True, avoidDownload=True, nThreads=12, verbosity=1, logFolder="./logs"):
    """
    Process a list of nicks to check whether they exist.

    This method receives as a parameter a series of nicks and verifies whether
    those nicks have a profile associated in different social networks.

    Args:
        nicks: List of nicks to process.
        platforms: List of <Platform> objects to be processed.
        rutaDescarga: Local file where saving the obtained information.
        avoidProcessing: A boolean var that defines whether the profiles will
            NOT be processed.
        avoidDownload: A boolean var that defines whether the profiles will NOT
            be downloaded.
        verbosity: The level of verbosity to be used.
        logFolder: The path to the log folder.

    Returns:
        A dictionary where the key is the nick and the value another dictionary
        where the keys are the social networks and the value is the
        corresponding URL.
    """
    if platforms is None:
        platforms = platform_selection.get_all_platform_names("usufy")

    # Defining the output results variable
    res = []
    # Processing the whole list of terms...
    for nick in nicks:
        # If the process is executed by the current app, we use the Processes. It is faster than pools.
        if nThreads <= 0 or nThreads > len(platforms):
            nThreads = len(platforms)

        # Using threads in a pool if we are not running the program in main
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

            for plat in platforms:
                # We need to create all the arguments that will be needed
                parameters = (plat, nick, rutaDescarga, avoidProcessing, avoidDownload, verbosity)
                pool.apply_async(pool_function, args=parameters, callback=log_result,)

            # Waiting for results to be finished
            while len(pool_results) < len(platforms):
                time.sleep(1)

            # Closing normal termination
            pool.close()
        except KeyboardInterrupt:
            print(general.warning("\n[!] Process manually stopped by the user. Terminating workers.\n"))
            pool.terminate()
            print(general.warning("[!] The following platforms were not processed:"))
            pending = ""
            for p in platforms:
                processed = False
                for processedPlatform in pool_results:
                    if str(p) == processedPlatform["platform"]:
                        processed = True
                        break
                if not processed:
                    print("\t- " + str(p))
                    pending += " " + str(p).lower()
            print("\n")
            print(general.warning("If you want to relaunch the app with these platforms you can always run the command with: "))
            print("\t usufy ... -p " + general.emphasis(pending))
            print("\n")
            print(general.warning("If you prefer to avoid these platforms you can manually evade them for whatever reason with: "))
            print("\t usufy ... -x " + general.emphasis(pending))
            print("\n")
        pool.join()

        # Collecting the results
        profiles = []
        errors = {}
        warnings = {}

        for info in pool_results:
            if info["status"] == "Ok":
                array = json.loads(info["data"])
                for r in array:
                    if r != "{}":
                        profiles.append(r)
            else:
                e = info["status"]
                if isinstance(e, OSRFrameworkError):
                    aux = errors.get(e.__class__.__name__, {})
                    aux["info"] = info["data"]
                    aux["counter"] = aux.get("counter", 0) + 1
                    errors[e.__class__.__name__] = aux
                else:
                    aux = warnings.get(e.__class__.__name__, {})
                    aux["info"] = info["data"]
                    aux["counter"] = aux.get("counter", 0) + 1
                    warnings[e.__class__.__name__] = aux
        res += profiles

        if errors:
            now = dt.datetime.now()
            print(f"\n{now}\tSome errors where found in the process:")
            for key, value in errors.items():
                print(textwrap.fill("- {} (found: {}). Details:".format(general.error(key), general.error(value["counter"])), 90, initial_indent="\t"))
                print(textwrap.fill("\t{}".format(value["info"]), 80, initial_indent="\t"))

        if warnings and verbosity >= 2:
            now = dt.datetime.now()
            print("\n{}\tSome warnings where found in the process:".format(now))
            for key, value in warnings.items():
                print(textwrap.fill("- {} (found: {}). Details:".format(general.warning(key), general.warning(value["counter"])), 90, initial_indent="\t"))
                print(textwrap.fill("\t{}".format(value["info"]), 80, initial_indent="\t"))

    return res


def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    DEFAULT_VALUES = configuration.get_configuration_values_for("usufy")
    # Capturing errors just in case the option is not found in the configuration
    try:
        excludeList = [DEFAULT_VALUES["exclude_platforms"]]
    except:
        excludeList = []

    # Recovering all the possible options
    platOptions = platform_selection.get_all_platform_names("usufy")

    parser = argparse.ArgumentParser(description= 'usufy - Piece of software that checks the existence of a profile for a given user in dozens of different platforms.', prog='usufy', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')
    parser._optionals.title = "Input options (one required)"

    # Adding the main options
    group_mainOptions = parser.add_mutually_exclusive_group(required=True)
    group_mainOptions.add_argument('--info', metavar='<action>', choices=['list_platforms', 'list_tags'], action='store', help='select the action to be performed amongst the following: list_platforms (list the details of the selected platforms), list_tags (list the tags of the selected platforms). Afterwards, it exists.')
    group_mainOptions.add_argument('-b', '--benchmark', action='store_true', default=False, help='perform the benchmarking tasks.')
    group_mainOptions.add_argument('-f', '--fuzz', metavar='<path_to_fuzzing_list>', action='store', type=argparse.FileType('r'), help='this option will try to find usufy-like URLs. The list of fuzzing platforms in the file should be (one per line): <BASE_DOMAIN>\t<VALID_NICK>')
    group_mainOptions.add_argument('-l', '--list', metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
    group_mainOptions.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')
    group_mainOptions.add_argument('--show_tags', action='store_true', default=False, help='it will show the platforms grouped by tags.')

    # Selecting the platforms where performing the search
    groupPlatforms = parser.add_argument_group('Platform selection arguments', 'Criteria for selecting the platforms where performing the search.')
    groupPlatforms.add_argument('-p', '--platforms', metavar='<platform>', choices=platOptions, nargs='+', required=False, default=DEFAULT_VALUES.get("platforms", []), action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(platOptions) + '. More than one option can be selected.')
    groupPlatforms.add_argument('-t', '--tags', metavar='<tag>', default = [], nargs='+', required=False, action='store', help='select the list of tags that fit the platforms in which you want to perform the search. More than one option can be selected.')
    groupPlatforms.add_argument('-x', '--exclude', metavar='<platform>', choices=platOptions, nargs='+', required=False, default=excludeList, action='store', help='select the platforms that you want to exclude from the processing.')

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
    group_processing.add_argument('--avoid_download', required=False, action='store_true', default=False, help='argument to force usufy NOT to store the downloadable version of the profiles.')
    group_processing.add_argument('--avoid_processing', required=False, action='store_true', default=False, help='argument to force usufy NOT to perform any processing task with the valid profiles.')
    group_processing.add_argument('--fuzz_config', metavar='<path_to_fuzz_list>', action='store', type=argparse.FileType('r'), help='path to the fuzzing config details. Wildcards such as the domains or the nicknames should come as: <DOMAIN>, <USERNAME>.')
    group_processing.add_argument('--nonvalid', metavar='<not_valid_characters>', required=False, default = '\\|<>=', action='store', help="string containing the characters considered as not valid for nicknames." )
    group_processing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'gml', 'json', 'ods', 'png', 'txt', 'xls', 'xlsx' ], required=False, default=DEFAULT_VALUES.get("extension", ["csv"]), action='store', help='output extension for the summary files. Default: csv.')
    group_processing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')
    group_processing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default=DEFAULT_VALUES.get("output_folder", "."), action='store', help='output folder for the generated documents. While if the paths does not exist, usufy will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
    group_processing.add_argument('-w', '--web_browser', required=False, action='store_true', help='opening the uris returned in the default web browser.')
    group_processing.add_argument('-F', '--file_header', metavar='<alternative_header_file>', required=False, default=DEFAULT_VALUES.get("file_header", "profiles"), action='store', help='Header for the output filenames to be generated. If None was provided the following will be used: profiles.<extension>.' )
    group_processing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=int(DEFAULT_VALUES.get("threads", 0)), type=int, help='write down the number of threads to be used (default 32). If 0, the maximum number possible will be used, which may make the system feel unstable.')

    # About options
    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - minimal; 1 - normal (default); 2 - debug.', type=int)
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exits.')

    return parser


def main(params=None):
    """ain function to launch usufy

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `get_parser()`.

    Args:
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point. If it is called by osrf
            the data is already parsed.

    Returns:
        dict: A Json representing the matching results.
    """
    if params is None:
        parser = get_parser()
        args = parser.parse_args(params)
    else:
        args = params

    print(general.title(banner.text))

    saying_hello = f"""
      Usufy | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{general.LICENSE_URL}>.

"""
    print(general.info(saying_hello))

    if args.fuzz:
        res = fuzzUsufy(args.fuzz, args.fuzz_config)
    else:
        # Recovering the list of platforms to be launched
        list_platforms = platform_selection.get_platforms_by_name(platform_names=args.platforms, tags=args.tags, mode="usufy", exclude_platform_names=args.exclude)

        if args.info:
            # Information actions...
            if args.info == 'list_platforms':
                info_platforms ="Listing the platforms:\n"
                for p in list_platforms:
                    info_platforms += "\t\t" + (str(p) + ": ").ljust(16, ' ') + str(p.tags)+"\n"
                return info_platforms
            elif args.info == 'list_tags':
                tags = {}
                # Going through all the selected platforms to get their tags
                for p in list_platforms:
                    for t in p.tags:
                        if t not in tags.keys():
                            tags[t] = 1
                        else:
                            tags[t] += 1
                info_tags = "List of tags:\n"
                # Displaying the results in a sorted list
                for t in tags.keys():
                    info_tags += "\t\t" + (t + ": ").ljust(16, ' ') + str(tags[t]) + "  time(s)\n"
                return info_tags
            else:
                pass

        # performing the test
        elif args.benchmark:
            platforms = platform_selection.get_all_platform_names("usufy")
            res = benchmark.do_benchmark(platforms)
            str_times = ""
            for e in sorted(res.keys()):
                str_times += str(e) + "\t" + str(res[e]) + "\n"
            return str_times

        # showing the tags of the usufy platforms
        elif args.show_tags:
            tags = platform_selection.get_all_platform_names_by_tag("usufy")
            print(general.info("This is the list of platforms grouped by tag.\n"))
            print(json.dumps(tags, indent=2, sort_keys=True))
            print(general.info("[Tip] Remember that you can always launch the platform using the -t option followed by any of the aforementioned.\n"))

        # Executing the corresponding process...
        else:
            # Showing the execution time...
            start_time = dt.datetime.now()
            print(f"{start_time}\tStarting search in {general.emphasis(str(len(list_platforms)))} platform(s)... Relax!\n")
            print(general.emphasis("\tPress <Ctrl + C> to stop...\n"))

            # Defining the list of users to monitor
            nicks = []
            if args.nicks:
                for n in args.nicks:
                    nicks.append(n)
            else:
                # Reading the nick files
                try:
                    nicks = args.list.read().splitlines()
                except:
                    print(general.error("ERROR: there has been an error when opening the file that stores the nicks.\tPlease, check the existence of this file."))

            # Definning the results
            res = []

            if args.output_folder != None:
                # if Verifying an output folder was selected
                if not os.path.exists(args.output_folder):
                    os.makedirs(args.output_folder)
                # Launching the process...
                res = process_nick_list(nicks, list_platforms, args.output_folder, avoidProcessing = args.avoid_processing, avoidDownload = args.avoid_download, nThreads=args.threads, verbosity= args.verbose, logFolder=args.logfolder)

            else:
                try:
                    res = process_nick_list(nicks, list_platforms, nThreads=args.threads, verbosity= args.verbose, logFolder=args.logfolder)
                except Exception as e:
                    print(general.error("Exception grabbed when processing the nicks: " + str(e)))
                    print(general.error(traceback.print_stack()))

            # We are going to iterate over the results...
            str_results = "\t"

            # Structure returned
            """
            [
                {
                  "attributes": [
                    {
                      "attributes": [],
                      "type": "com.i3visio.URI",
                      "value": "http://twitter.com/i3visio"
                    },
                    {
                      "attributes": [],
                      "type": "com.i3visio.Alias",
                      "value": "i3visio"
                    },
                    {
                      "attributes": [],
                      "type": "com.i3visio.Platform",
                      "value": "Twitter"
                    }
                  ],
                  "type": "com.i3visio.Profile",
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
                        if details["type"] == "com.i3visio.Platform":
                            platform = details["value"]
                        if details["type"] == "com.i3visio.URI":
                            uri = details["value"]
                    try:
                        str_results += (str(platform) + ":").ljust(16, ' ')+ " "+ str(uri)+"\n\t\t"
                    except:
                        pass

            # Generating summary files for each ...
            if args.extension:
                # Verifying if the outputPath exists
                if not os.path.exists (args.output_folder):
                    os.makedirs(args.output_folder)

                # Grabbing the results
                file_header = os.path.join(args.output_folder, args.file_header)

                # Iterating through the given extensions to print its values
                for ext in args.extension:
                    # Generating output files
                    general.export_usufy(res, ext, file_header)

            now = dt.datetime.now()
            print(f"\n{now}\tResults obtained ({general.emphasis(len(res))}):\n")
            print(general.success(general.osrf_to_text_export(res)))

            if args.web_browser:
                general.open_results_in_browser(res)

            now = dt.datetime.now()
            print("\n" + str(now) + "\tYou can find all the information here:")
            for ext in args.extension:
                # Showing the output files
                print("\t" + general.emphasis(file_header + "." + ext))

            # Showing the execution time...
            end_time = dt.datetime.now()
            print(f"\n{end_time}\tFinishing execution...\n")
            print("Total time consumed:\t" + general.emphasis(str(end_time-start_time)))
            print("Average seconds/query:\t" + general.emphasis(str((end_time-start_time).total_seconds()/len(list_platforms))) +" seconds\n")

            # Urging users to place an issue on Github...
            print(banner.footer)

    if params:
        return res


if __name__ == "__main__":
    main(sys.argv[1:])

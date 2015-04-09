# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
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
usufy-launcher.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2015
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
	python usufy-launcher.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2015, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v0.8.2"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse

import osrframework.usufy.config_usufy as config
import osrframework.usufy.processing as processing

import osrframework.wrappers.platforms as platforms

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='usufy-launcher.py - Piece of software that checks the existence of a profile for a given user in a bunch of different platforms.', prog='usufy-launcher.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Defining the mutually exclusive group for the main options
	general = parser.add_mutually_exclusive_group(required=True)
	# Adding the main options
	general.add_argument('--info', metavar='<action>', choices=['list_platforms', 'list_tags'], action='store', help='select the action to be performed amongst the following: list_platforms (list the details of the selected platforms), list_tags (list the tags of the selected platforms). Afterwards, it exists.')
	general.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')	
	general.add_argument('-b', '--benchmark',  action='store_true', default=False, help='perform the benchmarking tasks.')
	general.add_argument('-f', '--fuzz', metavar='<path_to_fuzzing_list>', action='store', type=argparse.FileType('r'), help='this option will try to find usufy-like URLs. The list of fuzzing platforms in the file should be (one per line): <BASE_URL>\t<VALID_NICK>')
	general.add_argument('-l', '--list',  metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
	general.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')

	platOptions = platforms.getAllPlatformParametersByMode("usufy")

	
	# Selecting the platforms where performing the search
	groupPlatforms = parser.add_argument_group('Platform selection arguments', 'Criteria for selecting the platforms where performing the search.')
	groupPlatforms.add_argument('-p', '--platforms', metavar='<platform>', choices=platOptions, nargs='+', required=False, default =['all'] ,action='store', help='select the platforms where you want to perform the search amongst the following: ' + str(platOptions) + '. More than one option can be selected.')
	groupPlatforms.add_argument('-t', '--tags', metavar='<tag>', default = [], nargs='+', required=False, action='store', help='select the list of tags that fit the platforms in which you want to perform the search. More than one option can be selected.')

	# Configuring the processing options
	groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
	groupProcessing.add_argument('--avoid_download', required=False, action='store_true', default=False, help='argument to force usufy NOT to store the downloadable version of the profiles.')
	groupProcessing.add_argument('--avoid_processing', required=False, action='store_true', default=False, help='argument to force usufy NOT to perform any processing task with the valid profiles.')
	groupProcessing.add_argument('--fuzz_config',  metavar='<path_to_fuzz_list>', action='store', type=argparse.FileType('r'), help='path to the fuzzing config details. Wildcards such as the domains or the nicknames should come as: <DOMAIN>, <USERNAME>.')
	groupProcessing.add_argument('--nonvalid', metavar='<not_valid_characters>', required=False, default = '\\|<>=', action='store', help="string containing the characters considered as not valid for nicknames." )
	groupProcessing.add_argument('-c', '--credentials', metavar='<path_to_credentials_file', required=False, default = './creds.txt', action='store', help='path to the credentials file. If none was provided, ./creds.txt is assumed.')	
	groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'json', 'maltego'], required=False, action='store', help='output extension for the summary files. Default: csv.')
	groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')		
	groupProcessing.add_argument('-m', '--maltego', required=False, action='store_true', help='Parameter specified to let usufy.py know that he has been launched by a Maltego Transform.')
	groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default = './results', action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
	groupProcessing.add_argument('-q', '--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')
    # [TO-DO]: to be revisited
	groupProcessing.add_argument('-s', '--squatting', metavar='<level>',  nargs='+', choices=['basic', 'l33t', 'local', 'years', 'words', 'all'], required=False, default=[], action='store', help="select the level of profilesquatting to be looked for (in order of execution): words (for adding sensitive words such as 'real', 'home', 'news', etc.); l33t (l33t m0d3);  years (ending in numbers); local (looking for localized endings: '_es', '_en', '_fr', etc.); basic (changing '-', '.' and ' '); and all.")
	groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=32, type=int, help='write down the number of threads to be used (default 32). If 0, the maximum number possible will be used, which may make the system feel unstable.')

	# About options
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
	groupAbout.add_argument('--version', action='version', version='%(prog)s ' +__version__, help='shows the version of the program and exists.')

	args = parser.parse_args()	

	# Calling the main function
	processing.usufy_main(args)

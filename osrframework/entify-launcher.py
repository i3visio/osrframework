# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of OSRFramework.
#
#	OSRFramework is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import argparse

import osrframework.entify.processing as processing


import osrframework.entify.config_entify as config
# logging imports
import logging

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='entify-launcher.py - entify-launcher.py is a program designed to extract using regular expressions all the entities from the files on a given folder. This software also provides an interface to look for these entities in any given text.', prog='entify-launcher.py', epilog="", add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Adding the main options
	# Defining the mutually exclusive group for the main options
	general = parser.add_mutually_exclusive_group(required=True)
	listAll = config.getAllRegexpNames()
	general.add_argument('-r', '--regexp', metavar='<name>', choices=listAll, action='store', nargs='+', help='select the regular expressions to be looked for amongst the following: ' + str(listAll))
	general.add_argument('-R', '--new_regexp', metavar='<regular_expression>', action='store', nargs='+', help='add a new regular expression, for example, for testing purposes.')	

	# Adding the main options
	# Defining the mutually exclusive group for the main options
	groupInput = parser.add_mutually_exclusive_group(required=True)
	groupInput.add_argument('-i', '--input_folder',  metavar='<path_to_input_folder>', default=None, action='store',  help='path to the folder to analyse.')
	groupInput.add_argument('-w', '--web',  metavar='<url>',  action='store', default=None, help='URI to be recovered and analysed.')
	
	# adding the option
	groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the processing parameters.')
	groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['json'], required=False, default = ['json'], action='store', help='output extension for the summary files (if not provided, json is assumed).')
	groupProcessing.add_argument('-o', '--output_folder',  metavar='<path_to_output_folder>',  action='store', help='path to the output folder where the results will be stored.', required=False)
	groupProcessing.add_argument('--recursive', action='store_true', default=False, required=False, help='Variable to tell the system to perform a recursive search on the folder tree.')	
	groupProcessing.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
	groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')	

	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.5.0', help='shows the version of the program and exists.')

	args = parser.parse_args()	

	processing.entify_main(args)

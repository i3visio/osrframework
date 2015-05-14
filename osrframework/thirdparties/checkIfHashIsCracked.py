# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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

import osrframework.thirdparties.md5crack_com.checkIfHashIsCracked as md5crack_com

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='A library that wraps a search onto md5crack.com.', prog='checkIfHashIsCracked.py', epilog="NOTE: if not provided, the API key will be searched in the config_api_keys.py file.", add_help=False)
	# Adding the main options
	# Defining the mutually exclusive group for the main options
	parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to md5crack.com.', required=True)		
	parser.add_argument('-a', '--api_key', action='store', help='API key in md5crack.com to be used.', required=False, default=None)
	
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

	args = parser.parse_args()		
	
	print json.dumps(md5crack_com.checkIfHashIsCracked(hash=args.query, api_key=args.api_key), indent=2)



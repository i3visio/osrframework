# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
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
import json
import sys
import urllib2

def checkIfHashIsCracked(hash=None):
	"""
		Method that checks if the given hash is stored in the md5db.net website.

		:param hash:	hash to verify.

		:return:	Resolved hash. If nothing was found, it will return an empty list.

	"""

	apiURL = "http://md5db.net/api/" + str(hash).lower()

	try:

		# Getting the result of the query from MD5db.net
		data = urllib2.urlopen(apiURL).read()
		return data

	except:
		# No information was found, then we return a null entity
		return []

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='A library that wraps a search onto md5db.net.', prog='checkIfHashIsCracked.py', epilog="", add_help=False)
	# Adding the main options
	# Defining the mutually exclusive group for the main options
	parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to md5db.net.', required=True)
	
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

	args = parser.parse_args()		
	print "Resolved hash for " + args.query + ":\n"
	print json.dumps(checkIfHashIsCracked(hash=args.query), indent=2)



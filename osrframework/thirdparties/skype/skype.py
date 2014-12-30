# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of apify. You can redistribute it and/or modify
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

import Skype4Py
import sys
import json

import codecs
import sys
import os
import argparse


def checkInSkype(query=None):
	''' 
		Method that checks if the given email is associated to any Skype account using the Skype4Py api. 

		:param query:	query to be performed to verify.

		:return:	A Python structure for the Json received.
	'''

	# Instatinate Skype object, all further actions are done
	# using this object.
	skype = Skype4Py.Skype()

	# Start Skype if it's not already running.
	if not skype.Client.IsRunning:
		skype.Client.Start()

	# Set our application name.
	skype.FriendlyName = 'Apify - Skype'

	# Attach to Skype. This may cause Skype to open a confirmation
	# dialog.
	skype.Attach()

	# Set up an event handler.
	def new_skype_status(status):
		# If Skype is closed and reopened, it informs us about it
		# so we can reattach.
		if status == Skype4Py.apiAttachAvailable:
			skype.Attach()
	skype.OnAttachmentStatus = new_skype_status
	
	# Search for users and display their Skype name, full name
	# and country.

	resultados = skype.SearchForUsers(query)

	jsonData = []
	for user in resultados:
		userData = {}
		
		userData ["i3visio.alias"] = user.Handle
		try:
			userData ["i3visio.aliases"] = user.Aliases
			userData ["i3visio.person"] = user.FullName
			userData ["i3visio.location.country"] = user.Country
			userData ["i3visio.location.province"] =  user.Province
			userData ["i3visio.location.city"] = user.City
			userData ["i3visio.homepage"] = user.Homepage
			userData ["i3visio.birthday"] = user.Birthday
			userData ["i3visio.phone.home"] = user.PhoneHome
			userData ["i3visio.phone.mobile"] = user.PhoneMobile
			userData ["i3visio.phone.office"] = user.PhoneOffice
			userData ["i3visio.lastonline"] = user.LastOnline
			userData ["i3visio.online"] = user.OnlineStatus
			userData ["i3visio.text"] = user.MoodText
		except:
			# Sth happened when parsing
			pass	
		jsonData.append(userData)


	return jsonData
	
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='apify.skype.py - library that wraps a search onto Skype4Py.', prog='skype.py', epilog="", add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Adding the main options
	# Defining the mutually exclusive group for the main options
	general = parser.add_mutually_exclusive_group(required=True)
	general.add_argument('-a', '--alias', metavar='<alias>', action='store', help='alias to be searched')		
	general.add_argument('-e', '--email', metavar='<email>', action='store', help='email to be searched')
	
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

	args = parser.parse_args()		
	
	if args.alias != None:
		checkInSkype(args.alias)
	elif args.email != None:
		checkInSkype(args.email)



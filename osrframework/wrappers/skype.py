# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of usufy.py.
#
#	Usufy is free software: you can redistribute it and/or modify
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

# Logging
import logging
import os

from platforms import Platform
import i3visiotools.general as general

import Skype4Py

class Skype(Platform):
	""" 
		A <Platform> object for Skype.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "Skype"
		# Add the tags for the platform
		self.tags = ["messaging"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		# Add the URL below
		# N/A
		#self.url = "http://www.skype.com/users/" + self.NICK_WILDCARD
		# Add the strings to look for when an error appears
		# N/A
		#self.notFoundText = ["<b>Top 5 contestants:</b>"]
		self.forbiddenList = []

		self._needsCredentials = True

		# Fields found. This attribute will be feeded when running the program.
		self.foundFields = {}

	def processProfile(self, info=None, nick=None, url=None):
		'''
		'''
		# splitting info
		pairs = info.split('; ')
		for p in pairs:
			parts = p.split(':')
			if len(parts) == 2:
				self.foundFields[parts[0]] = parts[1]
			else:
				# something happened that should not have happened
				pass

		return self.foundFields

	def getUserPage(self, nick, outputF=None, avoidProcessing=True, avoidDownload=True):
		''' 
			This public method is in charge of recovering the information from the user profile in Skype.
			
			List of parameters used by this method:
				nick:		nick to search
				outputF:	will contain a valid path to the outputFolder
				avoidProcessing:will define whether a further process is performed
	
			Return values:
				url	URL del usuario en cuestión una vez que se haya confirmado su validez.
				None	En el caso de que no se haya podido obtener una URL válida.
		'''
		try:
			logger = logging.getLogger("usufy")
			# Verifying if the nick is a correct nick
			if self._isValidUser(nick):
				logger.debug("Starting Skype client...")

				logger.warning("A Skype client must be set up... Note that the program will need a valid session of Skype having been started. If you were performing too many searches, the server may block or ban your account depending on the ToS. Please run this program under your own responsibility.")
				# Instantiate Skype object, all further actions are done
				# using this object.
				skype = Skype4Py.Skype()

				# Start Skype if it's not already running.
				if not skype.Client.IsRunning:
					skype.Client.Start()
					if not skype.Client.IsRunning:
						logger.error("The Skype application could NOT be started...")
						return None
			
				# Set our application name.
				skype.FriendlyName = 'Usufy with Skype4Py'

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
		
				# Dealing with UTF8
				import codecs
				import sys

				UTF8Writer = codecs.getwriter('utf8')
				sys.stdout = UTF8Writer(sys.stdout)

				info = None
	
				# Search for users and display their Skype name, full name
				# and country.

				resultados = skype.SearchForUsers(nick)
	
				for user in resultados:
					#res = unicode(user.Handle) + ";" + unicode(user.FullName )
						#+ ";" + user.Country + ";" + user.Homepage + ";" + user.Birthday + ";" + user.City + ";" + user.PhoneMobile
					#print user.Handle, user.Aliases, user.FullName, user.Country, user.Province, user.City, user.Homepage, user.Birthday, user.PhoneHome, user.PhoneMobile, user.PhoneOffice, user.LastOnline, user.OnlineStatus, user.MoodText
					#print res
					#print str(user.FullName)
					#oF.write(user.Handle + ";" + user.FullName + ";" + user.Country + ";" + user.Province + ";" + user.City + ";" + user.Homepage + ";" + user.Birthday + "; + user.PhoneHome +";" + user.PhoneMobile + ";" + user.PhoneOffice  +  ";" + user.LastOnline + ";" + user.OnlineStatus + ";" + user.MoodText)
					if user.Handle.lower() == nick.lower():
						#info = "Username:"#Aliases;Nombre Completo;País;Provincia;Ciudad;Página web;Tfno.Casa;Tfno.Móvil;TfnoOficina;OnlineStatus;MoodText\n"
						#info += user.Handle + ";" #+ str(user.Aliases) +";" + user.FullName + ";" + user.Country + ";" + user.Province + ";" + user.City + ";" + user.Homepage + ";"  + user.PhoneHome +";" + user.PhoneMobile + ";" + user.PhoneOffice  +  ";" + user.OnlineStatus + ";" + user.MoodText +'\n'
						info = "i3visio.profile:" + user.Handle +"; "
						try:
							info += "i3visio.aliases:" + str(user.Aliases)+"; i3visio.fullname:" + str(user.FullName) + "; i3visio.platform:skype://" + user.Handle
						except:
							# Capturing exception in case any kind of special character was found
							pass
				if info != None:
					if not avoidProcessing:
						# Storing file if the user has NOT said to avoid the process...	
						logger.debug("Storing the file...")	

						strTime = general.getCurrentStrDatetime()


						outputPath = os.path.join(outputF, nick)
						if not os.path.exists(outputPath):
							os.makedirs(outputPath)

						# Generating the raw output file
						rawFolder = os.path.join(outputPath, "raw")
						if not os.path.exists(rawFolder):
							os.makedirs(rawFolder)
						rawFilename = os.path.join( rawFolder, nick + "_" + str(self).lower() + "_" + strTime + ".html")
						logger.debug("Writing file: " + rawFilename)
						with open (rawFilename, "w") as oF:
							oF.write(info)
						logger.debug("File saved: " + rawFilename)

						# Generating the raw output file
						procFolder = os.path.join(outputPath, "proc")
						if not os.path.exists(procFolder):
							os.makedirs(procFolder)
						procFilename = os.path.join( procFolder, nick + "_" + str(self).lower() + "_" + strTime + ".json")
						logger.debug("Writing file: " + procFilename)

						# Recovering the processed data
						res = self.processProfile(info, nick, None)


						with open (procFilename, "w") as oF:
							oF.write(general.dictToJson(res))
						logger.debug("File saved: " + procFilename)

						# Calculating md5 and update raw and processed history
						rawHistoryName = os.path.join( outputPath, "history_raw.csv" )
						procHistoryName = os.path.join( outputPath, "history_proc.csv" )
						with open (rawHistoryName, "a") as oF:
							oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
						with open (procHistoryName, "a") as oF:
							oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")

						return res
					else:
					#	raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
						return {}

				else:
					# the user was not found
					logger.debug((str(self) + ":").ljust(18, ' ') + "The user '" + nick + "' will not be processed in this platform." )
					return None
			else:
				# The user is not valid
				return None
		except:
			logger.error("A major problem occurred when trying to launch Skype. Check if this program is already opened.")

	def needsCredentials(self):
		''' 
			Returns if it needsCredentials.
			IT captures the exception if the option does not exist. This way we do not have to recode all the platforms
		'''
		try:
			return self._needsCredentials		
		except:
			return False

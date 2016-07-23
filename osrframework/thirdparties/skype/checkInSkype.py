# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This program is part of apify. You can redistribute it and/or modify
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

import argparse
import codecs
import json
import os
import Skype4Py
import sys

def checkInSkype(query=None):
    ''' 
        Method that checks if the given email is associated to any Skype account using the Skype4Py API. 

        :param query:    query to be performed to verify.

        :return:    a Python structure for the Json received. If nothing was found, it will return an empty dictionary.
    '''
    jsonData = []
    try:
        # Instantianting Skype object, all further actions are done
        # using this object.
        #print "[*] Instantiating the Skype object..."
        skype = Skype4Py.Skype()

        # Start Skype if it's not already running.
        try:
            #print "[*] Checking if Skype is running..."
            if not skype.Client.IsRunning:
                print "[!] Skype is NOT running. Trying to open the client..."
                skype.Client.Start()

            # Set our application name.
            skype.FriendlyName = 'OSRFramework - Skype'

            # Attach to Skype. This may cause Skype to open a confirmation
            # dialog.
            try:
                #print "[*] Attaching the session"
                skype.Attach()

                # Set up an event handler.
                def new_skype_status(status):
                    # If Skype is closed and reopened, it informs us about it
                    # so we can reattach.
                    print "[!] Trying to reattach the handler..."
                    if status == Skype4Py.apiAttachAvailable:
                        skype.Attach()
                skype.OnAttachmentStatus = new_skype_status

                #print "[*] We will try to perform the Skype searches now..."
                try:    
                    # Search for users and display their Skype name, full name
                    # and country.

                    resultados = skype.SearchForUsers(query)

                    #print "[*] Results found: " + str(len(resultados))
                    for user in resultados:
                        userData = {}
                    
                        userData ["type"] = "i3visio.profile"
                        userData ["value"] = "Skype - " + user.Handle
                        userData ["attributes"] = []
                        atts = {}	            
                        atts ["i3visio.platform"] = "Skype"
                        atts ["i3visio.search"] = query
                        try:
                            if str(user.Handle) != "":
                                atts ["i3visio.alias"] = str(user.Handle)
                            if str(user.Aliases) != "[]":                    
                                atts ["i3visio.aliases"] = str(user.Aliases)
                            if str(user.Homepage) != "":
                                atts ["i3visio.uri.homepage"] = str(user.Homepage)
                            if str(user.Birthday) != "None":
                                atts ["i3visio.birthday"] = str(user.Birthday)
                            if str(user.PhoneHome) != "":
                                atts ["i3visio.phone.home"] = str(user.PhoneHome)
                            if str(user.PhoneMobile) != "":
                                atts ["i3visio.phone.mobile"] = str(user.PhoneMobile)
                            if str(user.PhoneOffice) != "":
                                atts ["i3visio.phone.office"] = str(user.PhoneOffice)
                            if str(user.LastOnline) != "0.0":
                                atts ["i3visio.lastonline"] = str(user.LastOnline)
                            if str(user.OnlineStatus) != "":
                                atts ["i3visio.online"] = str(user.OnlineStatus)
                            if str(user.MoodText) != "":
                                atts ["i3visio.text"] = str(user.MoodText)
                            if str(user.FullName) != "":
                                atts ["i3visio.fullname"] = str(user.FullName)
                            if str(user.Country) != "":
                                atts ["i3visio.location.country"] = str(user.Country)
                            if str(user.Province) != "":
                                atts ["i3visio.location.province"] =  str(user.Province)
                            if str(user.City) != "":
                                atts ["i3visio.location.city"] = str(user.City)

                        except:
                            # Sth happened when parsing
                            #print "WARNING: something happened when parsing the attributes in Skype. A problem with The program will continue with the execution..."
                            pass
                        for key in atts.keys():
                            aux = {}
                            aux["type"] = key
                            aux["value"] = atts[key]
                            aux["attributes"] = []
                            userData ["attributes"].append(aux)
                        jsonData.append(userData)
                    #print "[* ] We are in checkInSkype.py: " + str(jsonData) 

                except Exception as e:
                    print "[!] WARNING. Something happened when performing the search in Skype."
                    print "[!] Exception grabbed: " + str(e) 
                    print "[!] In spite of this message, execution is going on."
                    print

            except Exception as e:
                print "[!] WARNING. Something happened when trying to attach OSRFramework to a valid Skype session."
                print "[!] Exception grabbed: " + str(e) 
                print "[!] In spite of this message, execution is going on."
                print

        except Exception as e:
            print "[!] WARNING. Something happened when trying to create a valid Skype session."
            print "[!] Exception grabbed: " + str(e) 
            print "[!] This usually happens when you do NOT have any version of Skype installed in this machine."
            print "[!] In spite of this message, execution is going on."
            print

    except Exception as e:
        print "WARNING. Something happened when trying to link to a valid Skype session."
        print "Exception grabbed: " + str(e) 
        print "This usually happens when you do NOT have any version of Skype logged in in this machine. Although you may omit this message, you can also fix it by: "
        print "\ta) Install any version of Skype log in"
        print "\tb) If Skype is installed, the log in window will be appearing. You will need to log in and perform the search again (or run it with '-p skype' only) to get results from Skype."        
        print "In spite of this message, execution is going on."
        print

    #print "Returning the following info from checkInSkype: " + str(jsonData)
    return jsonData

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps a search onto Skype4Py.', prog='checkInSkype.py', epilog="NOTE: you must be logged in into Skype to use this program.", add_help=False)

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    general.add_argument('-q', '--query', metavar='<text_to_search>', action='store', help='query to be launched.')        
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        
    
    print json.dumps(checkInSkype(args.query), indent = 2)

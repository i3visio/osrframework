# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
mailfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2015
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
    python mailfy.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2015, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v0.1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import json

import osrframework.utils.platform_selection as platform_selection
# From emailahoy code
import emailahoy

# For the manual checkout
import DNS, smtplib, socket

# For the timeout function
from osrframework.utils.timeout import timeout

def getMoreInfo(email):
    '''
        Method that calls different third party API.
        
        :param email:   Email to verify.
        
        :result:    
    '''
    attributes = []
    
    # TO-DO
    
    return attributes

# TO-DO:
# Needs verification and further work.
"""@timeout(5)
def manualEmailCheck(mail):
    """
        Manually checking whether a mail is being sent.
        
        :param mail:    Email to check.
        
        :result:
    """
    DNS.DiscoverNameServers()
    #print "checking %s..."%(mail)
    hostname = mail[mail.find('@')+1:]
    mx_hosts = DNS.mxlookup(hostname)
    failed_mx = True
    for mx in mx_hosts:
            smtp = smtplib.SMTP()
            try:
                    smtp.connect(mx[1])
                    # print "Stage 1 (MX lookup & connect) successful."
                    failed_mx = False
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((mx[1], 25))
                    s.recv(1024)
                    s.send("HELO %s\n"%(mx[1]))
                    s.recv(1024)
                    s.send("MAIL FROM:< test@test.com>\n")
                    s.recv(1024)
                    s.send("RCPT TO:<%s>\n"%(mail))
                    result = s.recv(1024)
                    #print result
                    if result.find('Recipient address rejected') > 0:
                            #print "Failed at stage 2 (recipient does not exist)"
                            pass
                    else:
                            #print "Adress valid."
                            failed_mx = False
                    s.send("QUIT\n")
                    break
            except smtplib.SMTPConnectError:
                    continue
    if failed_mx:
            #print "Failed at stage 1 (MX lookup & connect)."
            pass
    #print ""
    if not failed_mx:
            return True
    return False
"""

def performSearch(emails=[]):
    ''' 
        Method to perform the mail verification process.
        
        :param emails: List of emails.
        
        :return:
    '''   
    results = []

    for e in emails:
            if emailahoy.verify_email_address(e):
                aux = {}
                aux["type"] = "i3visio.email"
                aux["value"] = e
                aux["attributes"] = getMoreInfo(e)

                results.append(aux)
            else:
                pass
                """ try:
                    if not "gmail.com" in e and manualEmailCheck(e):
                        aux = {}
                        aux["type"] = "i3visio.email"
                        aux["value"] = e
                        aux["attributes"] = getMoreInfo(e)

                        results.append(aux)
                except:
                    # Probably a Timeout exception
                    pass"""
    return results

def mailfy_main(args):
    ''' 
        Main program.
        
        :param args: Arguments received in the command line.
    '''
    emails = []
    if args.emails != None:
        emails = args.emails
    elif args.emails_file != None:
        with open(args.emails_file, "r") as iF:
            emails = iF.read().splitlines()
    elif args.nicks != None:
        for n in args.nicks:
            for d in args.domains:
                emails.append(n+"@"+d)
    elif args.nicks_file != None:
        with open(args.emails_file, "r") as iF:
            nicks = iF.read().splitlines()    
            for n in nicks:
                for d in args.domains:
                    emails.append(n+"@"+d)
                    
    results = performSearch(emails=emails)

    # Printing the results
    if not args.quiet:
        print json.dumps(results, indent=2) 

    # Writing the results onto a file
    if args.output_file != None:
        with open(output_file, "w") as oF:
            oF.write(json.dumps(results, indent=2) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='mailfy.py - Checking the existence of a given mail.', prog='mailfy.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
    parser._optionals.title = "Input options (one required)"

    emailDomains = ["gmail.com"]

    # Defining the mutually exclusive group for the main options
    general = parser.add_mutually_exclusive_group(required=True)
    # Adding the main options
    general.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3+ license and exists.')    
    general.add_argument('-e', '--emails', metavar='<emails>', nargs='+', action='store', help = 'the list of emails to be checked.')
    general.add_argument('-E', '--emails_file', metavar='<emails_file>', nargs='+', action='store', help = 'the file with the list of emails.')    
    general.add_argument('-n', '--nicks', metavar='<nicks>', nargs='+', action='store', help = 'the list of nicks to be checked in the following platforms: ' +str(emailDomains))
    general.add_argument('-N', '--nicks_file', metavar='<nicks_file>', nargs='+', action='store', help = 'the file with the list of nicks to be checked in the following platforms: '+str(emailDomains))    

    # Configuring the processing options
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which mailfy will process the identified profiles.')
    #groupProcessing.add_argument('-L', '--logfolder', metavar='<path_to_log_folder', required=False, default = './logs', action='store', help='path to the log folder. If none was provided, ./logs is assumed.')        
    groupProcessing.add_argument('-o', '--output_file',  metavar='<path_to_output_file>',  action='store', help='path to the output file where the results will be stored in json format.', required=False)
    groupProcessing.add_argument('-d', '--domains',  metavar='<candidate_domains>>',  action='store', help='list of domains where the nick will be looked for.', required=False, default = emailDomains)    
    groupProcessing.add_argument('--quiet', required=False, action='store_true', default=False, help='tells the program not to show anything.')        

    # About options
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    #groupAbout.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' +__version__, help='shows the version of the program and exists.')

    args = parser.parse_args()    

    # Calling the main function
    mailfy_main(args)

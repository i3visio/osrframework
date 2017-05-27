# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2014-207 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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
##################################################################################

import argparse
import json
import os
import random
import re
import sys
import urllib
import urllib2

import osrframework.utils.browser as browser
from osrframework.utils.credentials import Credential
import osrframework.utils.general as general
import osrframework.entify as entify
import osrframework.utils.config_api_keys as api_keys

# logging imports
import logging

class Platform():
    '''
        <Platform> class.
    '''
    def __init__(self):
        '''
            Constructor without parameters...
        '''
        pass

    def __init__(self, pName, tags):
        '''
            Constructor with parameters. This method permits the developer to instantiate dinamically Platform objects.
        '''
        self.platformName = pName
        # These tags will be the one used to label this platform
        self.tags = tags

        # Base URL
        self.baseURL = "http://plataform.com"

        # Trying to find an API... This line should be added in every  platform for which we have defined an API.
        # DO NOT FORGET TO IMPORT THE APIWRAPPER, i. e.:
        # from osrframework.api import TwitterAPIWrapper as TwitterAPIWrapper
        self.wrapperAPI = None

        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = False
        self.isValidMode["searchfy"] = False

        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        #self.url["usufy"] = "http://anyurl.com/user/" + "<usufy>"
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"

        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}
        self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        self.needsCredentials["searchfy"] = False

        # Array of credentials to be used
        self.creds = []

        ###################
        # Valid queries #
        ###################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.*' will match any query.
        self.validQuery["phonefy"] = ".*"
        self.validQuery["usufy"] = ".*"
        self.validQuery["searchfy"] = ".*"

        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        #self.notFoundText["usufy"] = []
        #self.notFoundText["searchfy"] = []

        #########################
        # Fields to be searched #
        #########################
        self.fieldsRegExp = {}

        # Definition of regular expressions to be searched in phonefy mode
        #self.fieldsRegExp["phonefy"] = {}
        # Example of fields:
        #self.fieldsRegExp["phonefy"]["i3visio.location"] = ""

        # Definition of regular expressions to be searched in usufy mode
        #self.fieldsRegExp["usufy"] = {}
        # Example of fields:
        #self.fieldsRegExp["usufy"]["i3visio.location"] = ""

        # Definition of regular expressions to be searched in searchfy mode
        #self.fieldsRegExp["searchfy"] = {}
        # Example of fields:
        #self.fieldsRegExp["searchfy"]["i3visio.location"] = ""

    def createURL(self, word, mode="phonefy"):
        '''
            Method to create the URL replacing the word in the appropriate URL.

            :param word:   Word to be searched.
            :param mode:    Mode to be executed.

            :return:    The URL to be queried.
        '''
        try:
            if mode == "base":
                if word[0] == "/":
                    return self.baseURL+word[1:], word
                else:
                    return self.baseURL+word, word
            else:
                try:
                    return self.url[mode].replace("<"+mode+">", urllib.pathname2url(word)), word
                except:
                    pass
        except:
            pass
            # TO-DO: BaseURLNotFoundExceptionThrow base URL not found for the mode.

    def getInfo(self, query=None, process = False, mode="phonefy", qURI=None):
        '''
            Method that checks the presence of a given query and recovers the first list of complains.

            :param query:   Query to verify.
            :param proces:  Calling the processing function.
            :param mode:    Mode to be executed.
            :param qURI:    A query to be checked

            :return:    Python structure for the html processed.
        '''
        # Defining variables for this process
        results = []
        data = ""
        if not self.modeIsValid(mode=mode):
            # TO-DO: InvalidModeException
            return json.dumps(results)

        # Verrifying if the mode is valid
        if not self._isValidQuery(query, mode=mode):
            # TO-DO: InvalidQueryException
            return json.dumps(results)

        # Verifying if the platform has an API defined
        try:
            if type(self.wrapperAPI) != "<type 'NoneType'>":
                if mode == "phonefy":
                    pass
                elif mode == "usufy":
                    results = self.wrapperAPI.get_user(query)
                    # Manually appending the URL
                    for r in results:
                        aux = {}
                        aux["type"]="i3visio.uri"
                        alias=r["value"].split(' - ')[1]
                        qURL, query = self.createURL(word=alias, mode="usufy")
                        aux["value"]= qURL
                        aux["attributes"]= []
                        r["attributes"].append(aux)

                elif mode == "searchfy":
                    results = self.wrapperAPI.search_users(query)
                    # Manually appending the URL
                    for r in results:
                        aux = {}
                        aux["type"]="i3visio.uri"
                        alias=r["value"].split(' - ')[1]
                        qURL, query = self.createURL(word=alias, mode="usufy")
                        aux["value"]= qURL
                        aux["attributes"]= []
                        r["attributes"].append(aux)
            else:
                # NoneType returned
                pass
        # The platform does not have a Wrapper defined for its API... Then we will use the traditional approach...
        except:
            # Creating the query URL for that mode
            if qURI != None:
                qURL = qURI
            else:
                qURL, query = self.createURL(word=query, mode=mode)
            i3Browser = browser.Browser()
            try:
                # check if it needs creds
                if self.needsCredentials[mode]:
                    authenticated = self._getAuthenticated(i3Browser)
                    if authenticated:
                        # Accessing the resources
                        data = i3Browser.recoverURL(qURL)
                else:
                    # Accessing the resources
                    data = i3Browser.recoverURL(qURL)
            except:
                # No information was found, then we return a null entity
                # TO-DO: i3BrowserException
                return json.dumps(results)

            # Verifying if the platform exists
            if self.somethingFound(data, mode=mode):

                if mode == "phonefy":
                    r = {}
                    r["type"] = "i3visio.phone"
                    r["value"] = self.platformName + " - " + query
                    r["attributes"] = []

                    # Appending platform URI
                    aux = {}
                    aux["type"] = "i3visio.uri"
                    aux["value"] = qURL
                    aux["attributes"] = []
                    r["attributes"].append(aux)

                    # Appending platform name
                    aux = {}
                    aux["type"] = "i3visio.platform"
                    aux["value"] = self.platformName
                    aux["attributes"] = []
                    r["attributes"].append(aux)

                    # Iterating if requested to extract more entities from the URI
                    if process:
                        # This function returns a json text!
                        r["attributes"] += json.loads(self.processData(data=data, mode=mode))
                    # Appending the result to results: in this case only one profile will be grabbed
                    results.append(r)

                elif mode == "usufy":
                    r = {}
                    r["type"] = "i3visio.profile"
                    r["value"] = self.platformName + " - " + query
                    r["attributes"] = []

                    # Appending platform URI
                    aux = {}
                    aux["type"] = "i3visio.uri"
                    aux["value"] = qURL
                    aux["attributes"] = []
                    r["attributes"].append(aux)
                    # Appending the alias
                    aux = {}
                    aux["type"] = "i3visio.alias"
                    aux["value"] = query
                    aux["attributes"] = []
                    r["attributes"].append(aux)
                    # Appending platform name
                    aux = {}
                    aux["type"] = "i3visio.platform"
                    aux["value"] = self.platformName
                    aux["attributes"] = []
                    r["attributes"].append(aux)


                    # Iterating if requested to extract more entities from the URI
                    if process:
                        # This function returns a json text!
                        r["attributes"] += json.loads(self.processData(data=data, mode=mode))

                    # Appending the result to results: in this case only one profile will be grabbed
                    results.append(r)

                elif mode == "searchfy":
                    # Recovering all the found aliases...
                    ids = re.findall(self.searchfyAliasRegexp, data, re.DOTALL)

                    for j, i in enumerate(ids):
                        r = {}
                        r["type"] = "i3visio.profile"
                        r["value"] = self.platformName + " - " + i
                        r["attributes"] = []

                        # Appending platform URI
                        aux = {}
                        aux["type"] = "i3visio.uri"
                        # Creating the URI based on the base URL for the new profiles...
                        uri, alias = self.createURL(word=i, mode="base")
                        #uri=self.baseURL+i

                        aux["value"] = uri

                        aux["attributes"] = []
                        r["attributes"].append(aux)
                        # Appending the alias
                        aux = {}
                        aux["type"] = "i3visio.alias"
                        aux["value"] = alias
                        aux["attributes"] = []
                        r["attributes"].append(aux)
                        # Appending platform name
                        aux = {}
                        aux["type"] = "i3visio.platform"
                        aux["value"] = self.platformName
                        aux["attributes"] = []
                        r["attributes"].append(aux)
                        # Appending the query performed to grab this items
                        aux = {}
                        aux["type"] = "i3visio.search"
                        aux["value"] = query
                        aux["attributes"] = []
                        r["attributes"].append(aux)

                        # TO-DO:
                        # Perform additional procesing
                        # Iterating the requested profiles to extract more entities from the URI would be slow!
                        """if process:
                            # This function returns a json text in usufy format for the returned objects.
                            r["attributes"] += json.loads(self.getInfo(process = True, mode="usufy", qURI=uri, query=i))
                        # Appending the result to results: in this case only one profile will be grabbed"""
                        results.append(r)
        return json.dumps(results)

    def modeIsValid(self, mode):
        '''
            Verification of whether the mode is a correct option to be used.

            :param mode:    Mode to be executed.

            :return:    True if the mode exists in the three main folders.
        '''
        if mode in self.isValidMode.keys():
            if mode in self.isValidMode.keys():
                return True
        return False

    def processData(self, uri=None, data = None, mode=None):
        '''
            Method to process and extract the entities of a URL of this type.

            :param uri: The URI of this platform to be processed.
            :param data: The information from which the info will be extracted. This way, info will not be downloaded twice.
            :param mode:    Mode to be executed.

            :return:    A list of the entities found.
        '''
        if data == None:
            # Accessing the resource
            i3Browser = browser.Browser()
            try:
                # check if it needs creds
                if self.needsCredentials[mode]:
                    authenticated = self._getAuthenticated(i3Browser)
                    if authenticated:
                        # Accessing the resources
                        data = i3Browser.recoverURL(uri)
                else:
                    # Accessing the resources
                    data = i3Browser.recoverURL(uri)
            except:
                # No information was found, then we return a null entity
                # TO-DO: i3BrowserException
                return json.dumps({})
        #else:
        #    return json.dumps({})
        info = []

        # Searchfy needs an special treatment to recover the results
        if mode != "searchfy":
            # Iterating through all the type of fields
            for field in self.fieldsRegExp[mode].keys():
                # Recovering the RegularExpression
                try:
                    # Using the old approach of "Start" + "End"
                    regexp = self.fieldsRegExp[mode][field]["start"]+"([^\)]+)"+self.fieldsRegExp[mode][field]["end"]

                    tmp = re.findall(regexp, data)

                    # Now we are performing an operation just in case the "end" tag is found  in the results, which would mean that the tag selected matches something longer in the data.
                    values = []
                    for t in tmp:
                        if self.fieldsRegExp[mode][field]["end"] in t:

                            values.append(t.split(self.fieldsRegExp[mode][field]["end"])[0])
                        else:
                            values.append(t)

                except:
                    # Using the compact approach if start and end tags do not exist.
                    regexp = self.fieldsRegExp[mode][field]

                    values = re.findall(regexp, data)

                for val in values:
                    aux = {}
                    aux["type"] = field
                    aux["value"] = val
                    aux["attributes"] = []
                    if aux not in info:
                        info.append(aux)
        # Searchfy results
        else:
            # Grabbing the results for the search
            resultText = re.findall(searchfyAliasRegexp, data)
            # Analysing each and every result to parse it...
            for resURI in resultText:
                r = {}
                r["type"] = "i3visio.uri"
                r["value"] = resURI
                r["attributes"] = []
                """# Iterating through all the type of fields
                i3Browser = browser.Browser()
                try:
                    # check if the profile needs credentials in usufy mode
                    if self.needsCredentials["usufy"]:
                        authenticated = self._getAuthenticated(i3Browser)
                        if authenticated:
                            # Accessing the resources
                            data = i3Browser.recoverURL(resURI)
                    else:
                        # Accessing the resources
                        data = i3Browser.recoverURL(resURI)
                except:
                    data = ""
                for field in self.fieldsRegExp["usufy"].keys():
                    # Building the regular expression if the format is a "start" and "end" approach... Easier to understand but less compact.
                    try:
                        # Using the old approach of "Start" + "End"
                        regexp = self.fieldsRegExp["usufy"][field]["start"]+"([^\)]+)"+self.fieldsRegExp["usufy"][field]["end"]

                        # Parsing the result for the text
                        tmp = re.findall(regexp, data)

                        # Now we are performing an operation just in case the "end" tag is found  in the results, which would mean that the tag selected matches something longer in the data.
                        values = []
                        for t in tmp:
                            if self.fieldsRegExp["usufy"][field]["end"] in t:

                                values.append(t.split(self.fieldsRegExp["usufy"][field]["end"])[0])
                            else:
                                values.append(t)
                    # In the case of a compact approach being used. This would happen if start and end tags do not exist, but the expected behaviour is the same.
                    except:
                        regexp = self.fieldsRegExp["usufy"][field]

                        values = re.findall(regexp, data)

                    if field == "i3visio.uri":
                        for val in values:
                            r["value"] =  val
                    else:
                        for val in values:
                            aux = {}
                            aux["type"] = field
                            aux["value"] = val
                            aux["attributes"] = []
                            if aux not in r["attributes"]:
                                r["attributes"].append(aux) """
                r["attributes"] = json.loads(self.getInfo(process = True, mode="usufy", qURI=resURI))
                info.append(r)
        return json.dumps(info)

    def somethingFound(self,data,mode="phonefy"):
        '''
            Verifying if something was found.

            :param data:    Data where the self.notFoundText will be searched.
            :param mode:    Mode to be executed.

            :return: Returns True if exists.
        '''
        #try:
        for text in self.notFoundText[mode]:
            if text in data:
                return False
        return True
        #except:
        #    pass
        #    # TO-DO: Throw notFoundText not found for this mode.

    def __str__(self):
        '''
            Function to represent the text when printing the object

            :return:    self.platformName
        '''
        try:
            return self.parameterName
        except:
            return self.platformName

    def __eq__(self, obj):
        '''
            Function to check if two wrappers are the same based on the convention.

            :return:    True or False
        '''
        return self.platformName == obj.platformName

    def _getAuthenticated(self, browser):
        '''
            Getting authenticated. This method will be overwritten.

            :param browser: The browser in which the user will be authenticated.
        '''
        # check if we have creds
        if len(self.creds) > 0:
            # choosing a cred
            c = random.choice(self.creds)
            # adding the credential
            browser.setNewPassword(url, c.user, c.password)
            return True
        else:
            logger.debug("No credentials have been added and this platform needs them.")
            return False

    def _isValidQuery(self, query, mode="phonefy"):
        '''
            Method to verify if a given query is processable by the platform. The system looks for the forbidden characters in self.Forbidden list.

            :param query:
            :param mode:    To be chosen amongst phonefy, usufy and searchfy.
            :return:    True | False
        '''
        # Verifying if the mode supports such a query
        try:
            # Checking if the query matched the compiled regexp
            compiledRegexp = re.compile("^" + self.validQuery[mode] + "$")
            if  compiledRegexp.match(query):
                """print "VALID query:"
                print "\tmode: ", mode
                print "\tquery: ", query"""
                return True
            else:
                # The query would have returned a bigger array
                """print "Invalid query:"
                print "\tMode: ", mode
                print "\tQuery: ", query"""
                return False
        except Exception as e:
            # If something happened... just returning True
            print "Oops. Something happened when validating the query:"
            print "\tError: ", str(e)
            print "\tMode: ", mode
            print "\tQuery: ", query
            print "\tPlatform: ", self.platformName
            return True


    def setCredentials(self, cred):
        """
            Getting the credentials and appending it to self.creds.
        """
        try:
            self.creds.append(cred)
        except:
            pass

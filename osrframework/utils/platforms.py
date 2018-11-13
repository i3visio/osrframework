# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2014-2018 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
import osrframework.utils.general as general
import osrframework.entify as entify
import osrframework.utils.config_api_keys as api_keys
from osrframework.utils.credentials import Credential
from osrframework.utils.exceptions import *

# logging imports
import logging

class Platform(object):
    """
    <Platform> class.
    """
    def __init__(self):
        """
        Constructor without parameters...
        """
        pass

    def __init__(self, pName, tags):
        """
        Constructor with parameters.

        This method permits the developer to instantiate dinamically Platform objects.
        """
        self.platformName = "Demo"
        self.tags = ["demo"]
        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "i3visio.alias": "My alias: ([^<]+)",
                },
                "needs_credentials": False,
                "not_found_text": "<h1>404</h1>",
                "query_validator": ".+",
                "url": "http://demo.demo/user/{placeholder}",
            },
            "searchfy": {
                "debug": False,
                "extra_fields": {
                    "i3visio.alias": "My alias: ([^<]+)",
                },
                "needs_credentials": False,
                "not_found_text": "<h1>404</h1>",
                "query_validator": ".+",
                "url": "http://demo.demo/user/{placeholder}",
                # Needed function to extract aliases from the website
                "alias_regexp": "demo.demo/(.+)"
            },
            # Reimplementation needed of check_mailfy
            "mailfy": {},
        }

    def createURL(self, word, mode="phonefy"):
        """
        Method to create the URL replacing the word in the appropriate URL.

        Args:
        -----
            word: Word to be searched.
            mode: Mode to be executed.

        Return:
        -------
            The URL to be queried.
        """
        try:
            return self.modes[mode]["url"].format(placeholder=urllib.pathname2url(word))
        except:
            if mode == "base":
                if word[0] == "/":
                    return self.baseURL+word[1:], word
                else:
                    return self.baseURL+word
            else:
                try:
                    return self.url[mode].replace("<"+mode+">", urllib.pathname2url(word))
                except:
                    pass
        return None


    def launchQueryForMode(self, query=None, mode=None):
        """
        Method that launches an i3Browser to collect data.

        Args:
        -----
            query: The query to be performed
            mode: The mode to be used to build the query.

        Return:
        -------
            A string containing the recovered data or None.
        """
        # Creating the query URL for that mode
        qURL = self.createURL(word=query, mode=mode)
        i3Browser = browser.Browser()

        try:
            # Check if it needs creds
            if self.needsCredentials[mode]:
                self._getAuthenticated(i3Browser, qURL)
                data = i3Browser.recoverURL(qURL)
            else:
                # Accessing the resources
                data = i3Browser.recoverURL(qURL)
            return data
        except KeyError:
            print(general.error("[*] '{}' is not a valid mode for this wrapper ({}).".format(mode, self.__class__.__name__)))

        return None


    def getInfo(self, query=None, process=False, mode="phonefy", qURI=None):
        """
        Method that checks the presence of a given query and recovers the first list of complains.

        Args:
        -----
            query: Query to verify.
            process: Calling the processing function.
            mode: Mode to be executed.
            qURI: A query to be checked.

        Return:
        -------
            Python structure for the html processed.

        Raises:
        -------
            NoCredentialsException.
            NotImplementedModeError.
            BadImplementationError.
        """
        results = []
        data = ""

        if self._modeIsValid(mode=mode) and self._isValidQuery(query, mode=mode):
            if mode in ["mailfy", "phonefy", "searchfy", "usufy"]:
                try:
                    results = getattr(self, "do_{}".format(mode))(query)
                except AttributeError as e:
                    raise NotImplementedModeError(str(self), mode)

        return json.dumps(results)


    def _modeIsValid(self, mode):
        """
        Verification of whether the mode is a correct option to be used.

        Args:
        -----
            mode: Mode to be executed.

        Return:
        -------
            True if the mode exists in the three main folders.
        """
        try:
            # Suport for version 2 of wrappers
            return mode in self.modes.keys()
        except AttributeError as e:
            # Legacy for mantaining old wrappers
            if mode in self.isValidMode.keys():
                if mode in self.isValidMode.keys():
                    return True
        return False


    def __str__(self):
        """
        Function to represent the text when printing the object

        Return:
        -------
            self.platformName
        """
        try:
            return self.parameterName
        except:
            return self.platformName


    def __eq__(self, obj):
        """
        Function to check if two wrappers are the same based on the convention

        Return:
        -------
            True or False
        """
        try:
            return self.platformName == obj.platformName
        except:
            return False
    # ------------------
    # Internal functions
    # ------------------

    def _getAuthenticated(self, browser, url):
        """
        Getting authenticated.

        This method may be overwritten.

        TODO: update to version 2 of the wrappers.

        Args:
        -----
            browser: The browser in which the user will be authenticated.
            url: The URL to get authenticated in.

        Return:
        -------
            True or False.

        Raises:
        ------
            NoCredentialsException: If no valid credentials have been found.
            BadImplementationError: If an expected attribute is missing.
        """
        # check if we have creds
        try:
            if len(self.creds) > 0:
                # TODO: in choosing a cred there is an uneeded nesting of arrays
                c = random.choice(self.creds)[0]
                # adding the credential
                browser.setNewPassword(url, c.user, c.password)
                return True
            else:
                raise NoCredentialsException(str(self))
        except AttributeError as e:
            raise BadImplementationError(str(e))


    def _isValidQuery(self, query, mode="phonefy"):
        """
        Method to verify if a given query is processable by the platform.

        The system looks for the forbidden characters in self.Forbidden list.

        Args:
        -----
            query: The query to be launched.
            mode: To be chosen amongst mailfy, phonefy, usufy, searchfy.
        Return:
        -------
            True | False
        """
        try:
            # Suport for version 2 of wrappers
            validator = self.modes[mode].get("query_validator")
            if validator:
                try:
                    compiledRegexp = re.compile(
                        "^{expr}$".format(
                            expr=validator
                        )
                    )
                    return compiledRegexp.match(query)
                except AttributeError as e:
                    return True

        except AttributeError as e:
            # Legacy for mantaining old wrappers
            compiledRegexp = re.compile("^{r}$".format(r=self.validQuery[mode]))
            return compiledRegexp.match(query)


    def _somethingFound(self, data, mode="phonefy"):
        """
        Verifying if something was found.

        Args:
        -----
            data: Data where the self.notFoundText will be searched.
            mode: Mode to be executed.

        Return:
        -------
            True if exists.
        """
        if data:
            try:
                for text in self.notFoundText[mode]:
                    if text in data:
                        return False
                return True
            except AttributeError as e:
                # Update to version 2 of the wrappers.
                verifier = self.modes.get(mode)
                if verifier:
                    if verifier.get("not_found_text", "") in data:
                        return False
                    else:
                        return True
        return False


    # ---------
    # Verifiers
    # ---------

    def check_mailfy(self, query, kwargs={}):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
        -----
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Return:
        -------
            Returns the collected data if exists or None if not.
        """
        data = self.launchQueryForMode(query=query, mode="mailfy")
        if self._somethingFound(data, mode="mailfy"):
            return data
        return None

    def do_mailfy(self, query, **kwargs):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return an equivalent array.

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
            A list of elements to be appended. A sample output format is as follows:
            [
              {
                "attributes": [
                  {
                    "attributes": [],
                    "type": "i3visio.email",
                    "value": "contacto@i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.alias",
                    "value": "contacto"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.domain",
                    "value": "i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "i3visio.platform",
                    "value": "Twitter"
                  }
                ],
                "type": "i3visio.profile",
                "value": "Twitter - contacto@i3visio.com"
              }
            ]
        """
        if self.check_mailfy(query, kwargs):
            expandedEntities = general.expandEntitiesFromEmail(query)
            r = {
                "type": "i3visio.profile",
                "value": self.platformName + " - " + query,
                "attributes": expandedEntities + [
                    {
                        "type": "i3visio.platform",
                        "value": self.platformName,
                        "attributes": []
                    }
                ]
            }
            return [r]
        return []

    def check_searchfy(self, query, kwargs={}):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
        -----
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Return:
        -------
            Returns the collected data if exists or None if not.
        """
        data = self.launchQueryForMode(query=query, mode="searchfy")
        if self._somethingFound(data, mode="searchfy"):
            return data
        return None

    def do_searchfy(self, query, **kwargs):
        """
        Verifying a searchfy query in this platform.

        This might be redefined in any class inheriting from Platform.

        Performing additional procesing may be possible by iterating the requested profiles
        to extract more entities from the URI would be slow. Sample code may be:

            if kwargs["process"]:
                r["attributes"] += json.loads(self.getInfo(process=True, mode="usufy", qURI=uri, query=i))

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
            A list of elements to be appended.
        """
        results = []
        print("[*] Launching search using the {} module...".format(self.__class__.__name__))
        test = self.check_searchfy(query, kwargs)

        if test:
            try:
                # Recovering all the found aliases in the traditional way
                ids = re.findall(self.searchfyAliasRegexp, test, re.DOTALL)
            except:
                # Version 2 of the wrappers
                verifier = self.modes.get(mode)
                
                if verifier and verifier.get("alias_extractor"):
                    ids = re.findall(verifier.get("alias_extractor"), test, re.DOTALL)
                else:
                    return []
                    
            for j, alias in enumerate(ids):
                r = {
                    "type": "i3visio.profile",
                    "value": self.platformName + " - " + alias,
                    "attributes": []
                }

                # Appending platform name
                aux = {}
                aux["type"] = "i3visio.platform"
                aux["value"] = self.platformName
                aux["attributes"] = []
                r["attributes"].append(aux)
                
                # Appending the alias
                aux = {}
                aux["type"] = "i3visio.alias"
                aux["value"] = alias
                aux["attributes"] = []
                r["attributes"].append(aux)
                
                # Appending the query performed to grab this items
                aux = {}
                aux["type"] = "i3visio.search"
                aux["value"] = query
                aux["attributes"] = []
                r["attributes"].append(aux)
                
                # Appending platform URI
                try:                    
                    aux = {}
                    aux["type"] = "i3visio.uri"
                    uri = self.createURL(word=alias, mode="usufy")
                    aux["value"] = uri
                    aux["attributes"] = []
                    r["attributes"].append(aux)
                except NameError:
                    pass

                # Appending the result to results: in this case only one profile will be grabbed"""
                results.append(r)
        return results
        

    def check_phonefy(self, query, kwargs={}):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
        -----
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Return:
        -------
            Returns the collected data if exists or None if not.
        """
        data = self.launchQueryForMode(query=query, mode="phonefy")
        if self._somethingFound(data, mode="phonefy"):
            return data
        return None

    def do_phonefy(self, query, **kwargs):
        """
        Verifying a phonefy query in this platform.

        This might be redefined in any class inheriting from Platform.

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
            A list of elements to be appended.
        """
        results = []

        test = self.check_phonefy(query, kwargs)

        if test:
            r = {
                "type": "i3visio.phone",
                "value": self.platformName + " - " + query,
                "attributes": []
            }

            try:
                aux = {
                    "type": "i3visio.uri",
                    "value": self.createURL(query, mode="phonefy"),
                    "attributes": []
                }
                r["attributes"].append(aux)
            except:
                pass

            aux = {
                "type": "i3visio.platform",
                "value": self.platformName,
                "attributes": []
            }
            r["attributes"].append(aux)

            # V2 of the wrappers
            r["attributes"] += self.process_phonefy(test)
            results.append(r)
            
        return results

    def process_phonefy(self, data):
        """
        Method to process and extract the entities of a phonefy

        Args:
        -----
            data: The information from which the info will be extracted. 
            
        Return:
        -------
            A list of the entities found.
        """
        mode = "phonefy"
        
        info = []

        try:
            # v2
            verifier = self.modes.get(mode, {}).get("extra_fields", {})
            for field in verifier.keys():
                regexp = verifier[field]
                values = re.findall(regexp, data)

                for val in values:
                    aux = {}
                    aux["type"] = field
                    aux["value"] = val
                    aux["attributes"] = []
                    if aux not in info:
                        info.append(aux)
        except AttributeError as e:
            # Legacy
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
        return info


    def check_usufy(self, query, **kwargs):
        """
        Verifying a mailfy query in this platform.

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
        -----
        query: The element to be searched.
        kwargs: Dictionary with extra parameters. Just in case.

        Return:
        -------
        Returns the collected data if exists or None if not.
        """
        data = self.launchQueryForMode(query=query, mode="usufy")
        if self._somethingFound(data, mode="usufy"):
            return data
        return None

    def do_usufy(self, query, **kwargs):
        """
        Verifying a usufy query in this platform.

        This might be redefined in any class inheriting from Platform.

        Args:
        -----
            query: The element to be searched.

        Return:
        -------
            A list of elements to be appended.
        """
        results = []

        test = self.check_usufy(query, **kwargs)

        if test:
            r = {
                "type": "i3visio.profile",
                "value": self.platformName + " - " + query,
                "attributes": []
            }

            # Appending platform URI
            aux = {}
            aux["type"] = "i3visio.uri"
            aux["value"] = self.createURL(word=query, mode="usufy")
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

            r["attributes"] += self.process_usufy(test)

            results.append(r)
        return results

    def process_usufy(self, data):
        """
        Method to process and extract the entities of a usufy

        Args:
        -----
            data: The information from which the info will be extracted. 
            
        Return:
        -------
            A list of the entities found.
        """
        mode = "usufy"
        info = []

        try:
            # v2
            verifier = self.modes.get(mode, {}).get("extra_fields", {})
            for field in verifier.keys():
                regexp = verifier[field]
                values = re.findall(regexp, data)

                for val in values:
                    aux = {}
                    aux["type"] = field
                    aux["value"] = val
                    aux["attributes"] = []
                    if aux not in info:
                        info.append(aux)
        except AttributeError as e:
            # Legacy
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
        return info


    def setCredentials(self, cred):
        """
            Getting the credentials and appending it to self.creds.
        """
        try:
            self.creds.append(cred)
        except:
            pass

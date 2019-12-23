################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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
################################################################################

import json
import random
import re
import urllib

import osrframework.utils.browser as browser
import osrframework.utils.general as general
from osrframework.utils.exceptions import *


class Platform(object):
    """<Platform> class"""
    def __init__(self):
        pass

    def __init__(self, name, tags):
        """Constructor with parameters

        This method permits the developer to instantiate dinamically Platform
        objects."""
        self.platformName = name.lower().title()
        self.tags = tags
        self.modes = {
            "usufy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.Location.Birth": "Born: [^<]+",    # Regular expresion to extract the alias
                },
                "needs_credentials": False,
                "not_found_text": "<h1>404</h1>",                   # Text that indicates a missing profile
                "query_validator": ".+",                            # Regular expression that the alias SHOULD match
                "url": "http://demo.demo/user/{placeholder}",       # Target URL where {placeholder} would be modified by the alias
            },
            "searchfy": {
                "debug": False,
                "extra_fields": {
                    "com.i3visio.Alias": "My alias: ([^<]+)",       # Regular expresion to extract the alias
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

    def create_url(self, word, mode="phonefy"):
        """Method to create the URL replacing the word in the appropriate URL

        Args:
            word (str): Word to be searched.
            mode (str): Mode to be executed.

        Returns:
            The URL to be queried.
        """
        try:
            return self.modes[mode]["url"].replace("{placeholder}", word)
        except:
            if mode == "base":
                if word[0] == "/":
                    return self.baseURL + word[1:], word
                else:
                    return self.baseURL + word
            else:
                try:
                    return self.url[mode].replace("<"+mode+">", word)
                except:
                    pass
        return None

    def launch_query_for_mode(self, query=None, mode=None):
        """Method that launches an i3Browser to collect data

        Args:
            query: The query to be performed
            mode: The mode to be used to build the query.

        Returns:
            A string containing the recovered data or None."""
        # Creating the query URL for that mode
        qURL = self.create_url(word=query, mode=mode)
        i3Browser = browser.Browser()
        try:
            # Check if it needs creds
            needs_credentials =False
            try:
                # Suport for version 2 of wrappers
                if self.modes[mode]["needs_credentials"]:
                    needs_credentials = True
            except AttributeError as e:
                if self.needsCredentials[mode]:
                    needs_credentials = True

            if needs_credentials:
                self._getAuthenticated(i3Browser, qURL)
                data = i3Browser.recover_url(qURL)
            else:
                # Accessing the resources
                data = i3Browser.recover_url(qURL)
            return data
        except KeyError:
            print(general.error("[*] '{}' is not a valid mode for this wrapper ({}).".format(mode, self.__class__.__name__)))

        return None

    def get_info(self, query=None, mode="phonefy"):
        """Method that checks the presence of a given query

        It recovers the first list of complains.

        Args:
            query (str): Query to verify.
            mode (str): Mode to be executed.

        Returns:
            Python structure for the html processed.

        Raises:
            NoCredentialsException.
            NotImplementedModeError.
            BadImplementationError.
        """
        results = []
        data = ""

        if self._mode_is_valid(mode=mode) and self._is_valid_query(query, mode=mode):
            if mode in ["mailfy", "phonefy", "searchfy", "usufy"]:
                try:
                    results = getattr(self, "do_{}".format(mode))(query)
                except AttributeError as e:
                    raise NotImplementedModeError(str(self), mode)

        return json.dumps(results)

    def _mode_is_valid(self, mode):
        """Verification of whether the mode is a correct option to be used in the platform

        Args:
            mode (str): Mode to be executed.

        Returns:
            bool. True if the mode exists.
        """
        try:
            # Suport for version 2 of wrappers
            return mode in self.modes.keys()
        except AttributeError as e:
            # Legacy for mantaining old wrappers
            return self.isValidMode.get(mode, False)
        return False

    def __str__(self):
        """Function to represent the text when printing the object

        Returns:
            self.platformName
        """
        try:
            return self.parameterName
        except:
            return self.platformName


    def __eq__(self, obj):
        """Function to check if two wrappers are the same based

        Returns:
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
        """Getting authenticated

        This method may be overwritten.
        TODO: update to version 2 of the wrappers.

        Args:
            browser: The browser in which the user will be authenticated.
            url: The URL to get authenticated in.

        Returns:
            True or False.

        Raises:
            NoCredentialsException: If no valid credentials have been found.
            BadImplementationError: If an expected attribute is missing.
        """
        # check if we have creds
        try:
            if len(self.creds) > 0:
                # TODO: in choosing a cred there is an uneeded nesting of arrays
                c = random.choice(self.creds)[0]
                # adding the credential
                browser.setNewPassword(c.user, c.password)
                return True
            else:
                raise NoCredentialsException(str(self))
        except AttributeError as e:
            raise BadImplementationError(str(e))


    def _is_valid_query(self, query, mode="phonefy"):
        """Method to verify if a given query is processable by the platform.

        The system looks for the forbidden characters in self.Forbidden list.

        Args:
            query: The query to be launched.
            mode: To be chosen amongst mailfy, phonefy, usufy, searchfy.

        Returns:
            bool.
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


    def _something_found(self, data, mode):
        """Verifying if something was found by trying to fin the not found text

        Args:
            data: Data where the self.notFoundText will be searched.
            mode: Mode to be executed.

        Returns:
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

    def check_mailfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Returns:
            Returns the collected data if exists or None if not.
        """
        data = self.launch_query_for_mode(query=query, mode="mailfy")
        if self._something_found(data, mode="mailfy"):
            return data
        return None

    def do_mailfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return an equivalent array.

        Args:
            query: The element to be searched.

        Returns:
            A list of elements to be appended. A sample output format is as follows:
            [
              {
                "attributes": [
                  {
                    "attributes": [],
                    "type": "com.i3visio.Email",
                    "value": "contacto@i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Alias",
                    "value": "contacto"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Domain",
                    "value": "i3visio.com"
                  },
                  {
                    "attributes": [],
                    "type": "com.i3visio.Platform",
                    "value": "Twitter"
                  }
                ],
                "type": "com.i3visio.Profile",
                "value": "Twitter - contacto@i3visio.com"
              }
            ]
        """
        if self.check_mailfy(query, **kwargs):
            expandedEntities = general.expand_entities_from_email(query)
            r = {
                "type": "com.i3visio.Profile",
                "value": self.platformName + " - " + query,
                "attributes": expandedEntities + [
                    {
                        "type": "com.i3visio.Platform",
                        "value": self.platformName,
                        "attributes": []
                    }
                ]
            }
            return [r]
        return []

    def check_searchfy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Returns:
            Returns the collected data if exists or None if not.
        """
        data = self.launch_query_for_mode(query=query, mode="searchfy")
        if self._something_found(data, mode="searchfy"):
            return data
        return None

    def do_searchfy(self, query, **kwargs):
        """Verifying a searchfy query in this platform

        This might be redefined in any class inheriting from Platform.

        Performing additional procesing may be possible by iterating the requested profiles
        to extract more entities from the URI would be slow. Sample code may be:

            if kwargs["process"]:
                r["attributes"] += json.loads(self.get_info(process=True, mode="usufy", qURI=uri, query=i))

        Args:
            query: The element to be searched.

        Returns:
            A list of elements to be appended.
        """
        results = []
        print(f"[*] Launching search using the {self.__class__.__name__} module...")
        test = self.check_searchfy(query, **kwargs)

        if test:
            # Add flexibility
            try:
                try:
                    regexp = self.searchfyAliasRegexp
                    entity_type = "com.i3visio.Alias"
                except AttributeError:
                    regexp = self.searchfyEmailRegexp
                    entity_type = "com.i3visio.Email"

                # Recovering all the found aliases in the traditional way
                ids = re.findall(regexp, test, re.DOTALL)
            except:
                # Version 2 of the wrappers
                verifier = self.modes.get("searchfy")

                if verifier and verifier.get("alias_regexp"):
                    entity_type = "com.i3visio.Alias"
                    ids = re.findall(verifier.get("alias_regexp"), test, re.DOTALL)
                if verifier and verifier.get("email_regexp"):
                    entity_type = "com.i3visio.Email"
                    ids = re.findall(verifier.get("email_regexp"), test, re.DOTALL)

            for j, alias in enumerate(ids):
                r = {
                    "type": "com.i3visio.Profile",
                    "value": self.platformName + " - " + alias,
                    "attributes": []
                }

                # Appending platform name
                aux = {}
                aux["type"] = "com.i3visio.Platform"
                aux["value"] = self.platformName
                aux["attributes"] = []
                r["attributes"].append(aux)

                # Appending the alias
                aux = {}
                aux["type"] = entity_type
                aux["value"] = alias
                aux["attributes"] = []
                r["attributes"].append(aux)

                # Appending the query performed to grab this items
                aux = {}
                aux["type"] = "com.i3visio.Search"
                aux["value"] = query
                aux["attributes"] = []
                r["attributes"].append(aux)

                # Appending platform URI
                try:
                    aux = {}
                    aux["type"] = "com.i3visio.URI"
                    uri = self.create_url(word=alias, mode="base")
                    aux["value"] = uri
                    aux["attributes"] = []
                    r["attributes"].append(aux)
                except AttributeError:
                    aux = {}
                    aux["type"] = "com.i3visio.URI"
                    uri = self.create_url(word=alias, mode="usufy")
                    aux["value"] = uri
                    aux["attributes"] = []
                    r["attributes"].append(aux)

                if entity_type == "com.i3visio.Email":
                    r["attributes"] += general.expand_entities_from_email(alias)

                # Appending the result to results: in this case only one profile will be grabbed"""
                results.append(r)
        return results

    def check_phonefy(self, query, **kwargs):
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform.
        The only condition is that any of this should return a dictionary as defined.

        Args:
            query (str): The element to be searched.
            kwargs (dict): Dictionary with extra parameters. Just in case.

        Returns:
            Returns the collected data if exists or None if not.
        """
        data = self.launch_query_for_mode(query=query, mode="phonefy")
        if self._something_found(data, mode="phonefy"):
            return data
        return None

    def do_phonefy(self, query, **kwargs):
        """Verifying a phonefy query in this platform

        This might be redefined in any class inheriting from Platform.

        Args:
            query (str): The element to be searched.

        Returns:
            A list of elements to be appended.
        """
        results = []

        test = self.check_phonefy(query, **kwargs)

        if test:
            r = {
                "type": "com.i3visio.Phone",
                "value": self.platformName + " - " + query,
                "attributes": []
            }

            try:
                aux = {
                    "type": "com.i3visio.URI",
                    "value": self.create_url(query, mode="phonefy"),
                    "attributes": []
                }
                r["attributes"].append(aux)
            except:
                pass

            aux = {
                "type": "com.i3visio.Platform",
                "value": self.platformName,
                "attributes": []
            }
            r["attributes"].append(aux)

            # V2 of the wrappers
            r["attributes"] += self.process_phonefy(test)
            results.append(r)

        return results

    def process_phonefy(self, data):
        """Method to process and extract the entities of a phonefy

        Args:
            data: The information from which the info will be extracted.

        Returns:
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
        """Verifying a mailfy query in this platform

        This might be redefined in any class inheriting from Platform. The only
        condition is that any of this should return a dictionary as defined.

        Args:
            query: The element to be searched.
            kwargs: Dictionary with extra parameters. Just in case.

        Returns:
            Returns the collected data if exists or None if not.
        """
        data = self.launch_query_for_mode(query=query, mode="usufy")
        if self._something_found(data, mode="usufy"):
            return data
        return None

    def do_usufy(self, query, **kwargs):
        """Verifying a usufy query in this platform

        This might be redefined in any class inheriting from Platform.

        Args:
            query: The element to be searched.

        Returns:
            A list of elements to be appended.
        """
        results = []

        test = self.check_usufy(query, **kwargs)

        if test:
            r = {
                "type": "com.i3visio.Profile",
                "value": self.platformName + " - " + query,
                "attributes": []
            }

            # Appending platform URI
            aux = {}
            aux["type"] = "com.i3visio.URI"
            aux["value"] = self.create_url(word=query, mode="usufy")
            aux["attributes"] = []
            r["attributes"].append(aux)
            # Appending the alias
            aux = {}
            aux["type"] = "com.i3visio.Alias"
            aux["value"] = query
            aux["attributes"] = []
            r["attributes"].append(aux)
            # Appending platform name
            aux = {}
            aux["type"] = "com.i3visio.Platform"
            aux["value"] = self.platformName
            aux["attributes"] = []
            r["attributes"].append(aux)

            r["attributes"] += self.process_usufy(test)

            results.append(r)
        return results

    def process_usufy(self, data):
        """Method to process and extract the entities of a usufy

        Args:
            data: The information from which the info will be extracted.

        Returns:
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
        """Getting the credentials and appending it to self.creds"""
        try:
            self.creds.append(cred)
        except:
            pass

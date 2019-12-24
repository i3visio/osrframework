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

from configparser import ConfigParser
import os
import random

import requests

import osrframework.utils.configuration as configuration


class Browser():
    """Utility used to code a Browser and to wrap the requests methods.

    Attributes:
        auth (tuple): The username and password authentication.
        proxies (list): A list of proxies.
        timeout (int): The number of seconds to wait until timeout.
        user_agents (list): The list of User Agents recognised for this browser.
    """
    def __init__(self):
        """Recovering an instance of a new Browser"""
        self.auth = None
        self.user_agents = []
        self.proxies = {}
        self.timeout = 2

        # Trying to read the configuration
        # --------------------------------
        # If a current.cfg has not been found, creating it by copying from default
        config_path = os.path.join(configuration.get_config_path()["appPath"], "browser.cfg")

        # Checking if the configuration file exists
        if not os.path.exists(config_path):
            try:
                # Copy the data from the default folder
                default_config_path = os.path.join(configuration.get_config_path()["appPathDefaults"], "browser.cfg")

                with open(default_config_path) as file:
                    cont = file.read()
                    with open(config_path, "w") as output_file:
                        output_file.write(cont)
            except Exception:
                print("WARNING. No configuration file could be found and the default file was not found either, so configuration will be set as default.")
                print(str(e))
                print()
                # Storing configuration as default
                self.user_agents = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36']
                self.proxies = {}

                return None

        # Reading the configuration file
        config = ConfigParser()
        config.read(config_path)

        proxy = {}

        # Iterating through all the sections, which contain the platforms
        for conf in config.sections():
            if conf == "Browser":
                # Iterating through parametgers
                for (param, value) in config.items(conf):
                    if param == "user_agent":
                        if value != '':
                            self.user_agents.append(value)
                        else:
                            self.user_agents = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36']
                    if param == "timeout":
                        try:
                            self.timeout = int(value)
                        except:
                            self.timeout = 2
            else:
                proxy[conf] = {}
                # Iterating through parameters
                for (param, value) in config.items(conf):
                    if value != '':
                        proxy[conf][param] = value

        # Configuring the proxy as it will be used by br.set_proxies
        for p in proxy.keys():
            # p ~= ProxyHTTP --> Protocol = p.lower()[5:]
            #print p, p.lower()[5:], proxy[p]
            try:
                # Adding credentials if they exist
                self.proxies[ p.lower()[5:] ] = proxy[p]["username"] + ":" + proxy[p]["password"]  + "@" + proxy[p]["host"] + ":" + proxy[p]["port"]
            except:
                try:
                    self.proxies[ p.lower()[5:] ] = proxy[p]["host"] + ":" + proxy[p]["port"]
                except:
                    # We are not adding this protocol to be proxied
                    pass

    def recover_url(self, url):
        """Public method to recover a resource.

        Args:
            url (str): The URL to be collected.

        Returns:
            Returns a resource that has to be read, for instance, with
                html = self.br.read()
        """
        headers = {
            "User-Agent": self.getUserAgent(),
        }

        # Opening the resource
        try:
            r = requests.get(
                url,
                headers=headers,
                auth=self.auth
            )
            return r.text
        except Exception:
            # Something happened. Maybe the request was forbidden?
            return None

    def setNewPassword(self, username, password):
        """Public method to manually set the credentials for a url in the browser

        Args:
            username (str): The username of the session.
            password (str): The password of the session.
        """
        self.auth = (username, password)

    def getUserAgent(self):
        """This method will be called whenever a new query will be executed

        Returns:
            Returns a string with the User Agent.
        """
        if self.user_agents:
            # User-Agent (this is cheating, ok?)
            return random.choice(self.user_agents)
        else:
            return "Python3"

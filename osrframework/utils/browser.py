# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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

# Required libraries
import mechanize
import cookielib
import ConfigParser
import random
import os


import osrframework.utils.configuration as configuration

# logging imports
import logging

class Browser():
    """
        Utility used to code a Browser.
    """
    def __init__(self):
        """
            Recovering an instance of a new Browser.
        """

        # Browser
        self.br = mechanize.Browser()

        # Cookie Jar
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)

        # Browser options
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(False)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(False)
        self.br.set_handle_robots(False)
        self.br.set_handled_schemes(['http', 'https'])

        # Follows refresh 0 but not hangs on refresh > 0
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Defining User Agents
        self.userAgents = []

        # Handling proxies
        self.proxies = {}
        self.timeout = 2

        # Want debugging messages?
        #self.br.set_debug_http(True)
        #self.br.set_debug_redirects(True)
        #self.br.set_debug_responses(True)

        # Trying to read the configuration
        # --------------------------------
        # If a current.cfg has not been found, creating it by copying from default
        configPath = configuration.getConfigPath("browser.cfg")
        configPath = os.path.join(configuration.getConfigPath()["appPath"], "browser.cfg")

        # Checking if the configuration file exists
        if not os.path.exists(configPath):
            try:
                # Copy the data from the default folder
                defaultConfigPath = os.path.join(configuration.getConfigPath()["appPathDefaults"], "browser.cfg")

                with open(defaultConfigPath) as iF:
                    cont = iF.read()
                    with open(configPath, "w") as oF:
                        oF.write(cont)
            except Exception, e:
                print "WARNING. No configuration file could be found and the default file was not found either, so configuration will be set as default."
                print str(e)
                print
                # Storing configuration as default
                self.userAgents = ['Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0']
                self.proxies = {}

                return None

        # Reading the configuration file
        config = ConfigParser.ConfigParser()
        config.read(configPath)

        proxy = {}

        # Iterating through all the sections, which contain the platforms
        for conf in config.sections():
            if conf == "Browser":
                # Iterating through parametgers
                for (param, value) in config.items(conf):
                    if param == "user_agent":
                        if value != '':
                            self.userAgents.append(value)
                        else:
                            self.userAgents = ['Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0']
                    if param == "timeout":
                        try:
                            self.timeout = int(value)
                        except:
                            self.timeout = 2
            else:
                proxy[conf] = {}
                # Iterating through parametgers
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
                    
    def recoverURL(self,url):
        """
            Public method to recover a resource.
                url
                Platform

            Returns:
                Returns a resource that has to be read, for instance, with html = self.br.read()
        """

        logger = logging.getLogger("osrframework.utils")

        # Configuring user agents...
        self.setUserAgent()

        # Configuring proxies
        if "https://" in url:
            self.setProxy(protocol = "https")
        else:
            self.setProxy(protocol = "http")

        # Giving special treatment for .onion platforms
        if ".onion" in url:
            try:
                # TODO: configuring manually the tor bundle
                pass
            except:
                # TODO: capturing the error and eventually trying the tor2web approach
                #url = url.replace(".onion", ".tor2web.org")
                pass
            url = url.replace(".onion", ".onion.cab")

        logger.debug("Retrieving the resource: " + url)
        # Opening the resource
        recurso = self.br.open(url, timeout=self.timeout)

        logger.debug("Reading html code from: " + url)
        # [TO-DO]
        #    Additional things may be done here to load javascript.
        html = recurso.read()

        return html

    def setNewPassword(self, url, username, password):
        """
            Public method to manually set the credentials for a url in the browser.
        """
        self.br.add_password(url, username, password)

    def setProxy(self, protocol="http"):
        """
            Public method to set a proxy for the browser.
        """
        # Setting proxy
        try:
            new = { protocol: self.proxies[protocol]}
            self.br.set_proxies( new )
        except:
            # No proxy defined for that protocol
            pass

    def setUserAgent(self, uA=None):
        """
            This method will be called whenever a new query will be executed.

            :param uA:    Any User Agent that was needed to be inserted. This parameter is optional.

            :return:    Returns True if a User Agent was inserted and False if no User Agent could be inserted.
        """
        logger = logging.getLogger("osrframework.utils")

        if not uA:
            # Setting the User Agents
            if self.userAgents:
                # User-Agent (this is cheating, ok?)
                logger = logging.debug("Selecting a new random User Agent.")
                uA = random.choice(self.userAgents)
            else:
                logger = logging.debug("No user agent was inserted.")
                return False

        #logger.debug("Setting the user agent:\t" + str(uA))

        self.br.addheaders = [ ('User-agent', uA), ]
        #self.br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), ('Accept-Encoding', 'none'), ('Accept-Language', 'es-es,es;q=0.8'), ('Connection', 'keep-alive')]
        #self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        return True

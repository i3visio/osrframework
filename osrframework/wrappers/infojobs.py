# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import argparse
import json
import re
import sys
import urllib2

import osrframework.utils.general as general
from osrframework.utils.platforms import Platform

class Infojobs(Platform):
    """
        A <Platform> object for Infojobs.
    """
    def __init__(self):
        """
            Constructor...
        """
        self.platformName = "Infojobs"
        self.tags = ["jobs"]

        # Valid modes
        self.isValidMode = {
            "mailfy": True,
            "phonefy": False,
            "searchfy": False,
            "usufy": False,
        }

        self.url = {}

        self.needsCredentials = {
            "mailfy": False
        }

        self.validQuery = {
            "mailfy": ".+"
        }


        self.fieldsRegExp = {}

        # Definition of regular expressions to be searched in usufy mode
        self.fieldsRegExp["mailfy"] = {}

        ################
        # Fields found #
        ################
        # This attribute will be feeded when running the program.
        self.foundFields = {}


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
        import requests

        s = requests.Session()

        # Getting the first response to grab the csrf_token
        r1 = s.get('https://www.infojobs.net')

        # Launching the query to Instagram
        r2 = s.post(
            'https://www.infojobs.net/candidate/profile/check-email-registered.xhtml',
            data={"email": query},
        )

        if '{"email_is_secure":true,"email":true}' in r2.text:
            return r2.text
        return None

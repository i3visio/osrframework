# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
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
import cfscrape
import json
import requests
import sys
import time

def checkIfEmailWasHacked(email=None, sleepSeconds=0.5):
    """
    Method that checks if the given email is stored in the HIBP website.

    This function automatically waits a second to avoid problems with the API
    rate limit. An example of the json received:
    ```
        [{"Title":"Adobe","Name":"Adobe","Domain":"adobe.com","BreachDate":"2013-10-4","AddedDate":"2013-12-04T00:12Z","PwnCount":152445165,"Description":"The big one. In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and <a href=\"http://stricture-group.com/files/adobe-top100.txt\" target=\"_blank\">many were quickly resolved back to plain text</a>. The unencrypted hints also <a href=\"http://www.troyhunt.com/2013/11/adobe-credentials-and-serious.html\" target=\"_blank\">disclosed much about the passwords</a> adding further to the risk that hundreds of millions of Adobe customers already faced.","DataClasses":["Email addresses","Password hints","Passwords","Usernames"]}]
    ```

    Args:
    -----
        email: Email to verify in HIBP.

    Returns:
    --------
        A python structure for the json received. If nothing was found, it will
        return an empty list.
    """
    # Sleeping just a little bit
    time.sleep(sleepSeconds)

    print("\t[*] Bypassing Cloudflare Restriction...")
    ua = 'osrframework 0.18'
    useragent = {'User-Agent': ua}
    cookies, user_agent = cfscrape.get_tokens('https://haveibeenpwned.com/api/v2/breachedaccount/test@example.com', user_agent=ua)

    leaks = []

    apiURL = "https://haveibeenpwned.com/api/v2/breachedaccount/{}".format(email)

    # Accessing the HIBP API
    time.sleep(sleepSeconds)
    # Building API query
    data = requests.get(
        apiURL,
        headers=useragent,
        cookies=cookies,
        verify=True
    ).text

    # Reading the text data onto python structures
    jsonData = json.loads(data)

    try:
        for e in jsonData:
            # Building the i3visio like structure
            new = {}
            new["value"] = "(HIBP) " + e.get("Name")
            new["type"] = "i3visio.platform_leaked"
            new["attributes"] = [
                {
                    "value": "@source",
                    "type": "haveibeenpwned.com",
                    "attributes": []
                },
                {
                    "value": "i3visio_uri",
                    "type": apiURL,
                    "attributes": []
                },
                {
                    "value": "@pwn_count",
                    "type": e.get("PwnCount"),
                    "attributes": []
                },
                {
                    "value": "@added_date",
                    "type": e.get("AddedDate"),
                    "attributes": []
                },
                {
                    "value": "@breach_date",
                    "type": e.get("BreachDate"),
                    "attributes": []
                },
                {
                    "value": "@description",
                    "type": e.get("Description"),
                    "attributes": []
                }
            ]
            leaks.append(new)
    except:
        print("ERROR: Something happenned when using HIBP API.")
        return []

    return leaks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps an account search onto haveibeenpwned.com.', prog='checkIfEmailWasHacked.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to haveibeenpwned.com.', required=True)

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()
    print("Results found for " + args.query + ":\n")
    print(json.dumps(checkIfEmailWasHacked(email=args.query), indent=2))

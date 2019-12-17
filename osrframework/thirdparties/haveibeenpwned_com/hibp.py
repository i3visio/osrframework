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

import argparse
import json
import os
import time

import cfscrape
import requests

import osrframework.utils.general as general
import osrframework.utils.configuration as configuration


def check_if_email_was_hacked(email=None, sleep_seconds=1, api_key=None):
    """Method that checks if the given email is stored in the HIBP website.

    This function automatically waits a second to avoid problems with the API
    rate limit. An example of the json received:
    ```
        [{"Title":"Adobe","Name":"Adobe","Domain":"adobe.com","BreachDate":"2013-10-4","AddedDate":"2013-12-04T00:12Z","PwnCount":152445165,"Description":"The big one. In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and <a href=\"http://stricture-group.com/files/adobe-top100.txt\" target=\"_blank\">many were quickly resolved back to plain text</a>. The unencrypted hints also <a href=\"http://www.troyhunt.com/2013/11/adobe-credentials-and-serious.html\" target=\"_blank\">disclosed much about the passwords</a> adding further to the risk that hundreds of millions of Adobe customers already faced.","DataClasses":["Email addresses","Password hints","Passwords","Usernames"]}]
    ```

    Args:
        email (str): Email to verify in HIBP.
        sleep_seconds (int): Number of seconds to wait between calls.
        api_key (str): API key for Have I Been Pwned

    Returns:
        A python structure for the json received. If nothing was found, it will
        return an empty list.
    """
    leaks = []

    # Sleeping just a little bit
    time.sleep(sleep_seconds)

    print("\t[*] Bypassing Cloudflare Restriction...")
    ua = 'osrframework 0.20.0'

    if api_key is None:
        api_key = input("Insert the HIBP API KEY here:\t")

    headers = {
        'hibp-api-key': api_key,
        'User-Agent': ua
    }

    try:
        cookies, user_agent = cfscrape.get_tokens('https://haveibeenpwned.com/api/v3/breachedaccount/test@example.com', user_agent=ua)
    except requests.exceptions.HTTPError as e:
        print(f"\t[*] Unauthorised: '{str(e)}'")
        return leaks

    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    # Accessing the HIBP API
    time.sleep(sleep_seconds)

    # Building API query
    try:
        resp = requests.get(
            api_url,
            headers=headers,
            cookies=cookies,
            verify=True
        )
        data = resp.text
    except requests.exceptions.HTTPError as e:
        print(f"\t[*] Unauthorised: '{str(e)}'")
        return leaks

    # Reading the text data onto python structures
    try:
        jsonData = json.loads(data)

        for e in jsonData:
            # Building the i3visio like structure
            new = {}
            new["value"] = "(HIBP) " + e.get("Name") + " - " + email
            new["type"] = "com.i3visio.Profile"
            new["attributes"] = [
                {
                    "type": "com.i3visio.Platform.Leaked",
                    "value": e.get("Name"),
                    "attributes": []
                },
                {
                    "type": "@source",
                    "value": "haveibeenpwned.com",
                    "attributes": []
                },
                {
                    "type": "@source_uri",
                    "value": api_url,
                    "attributes": []
                },
                {
                    "type": "@pwn_count",
                    "value": e.get("PwnCount"),
                    "attributes": []
                },
                {
                    "type": "com.i3visio.Date.Known",
                    "value": e.get("AddedDate"),
                    "attributes": []
                },
                {
                    "type": "com.i3visio.Date.Breached",
                    "value": e.get("BreachDate"),
                    "attributes": []
                },
                {
                    "type": "@description",
                    "value": e.get("Description"),
                    "attributes": []
                }
            ] + general.expand_entities_from_email(email)
            leaks.append(new)
    except ValueError:
        return []
    except Exception:
        print("ERROR: Something happenned when using HIBP API.")
        return []

    return leaks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps an account search onto haveibeenpwned.com.', prog='checkIfEmailWasHacked.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<email>', action='store', help='query to be performed to haveibeenpwned.com.', required=True)

    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='%(prog)s 0.2.0', help='shows the version of the program and exists.')

    args = parser.parse_args()

    result = check_if_email_was_hacked(email=args.query)
    print(f"Results found for {args.query}:\n")
    print(json.dumps(result, indent=2))

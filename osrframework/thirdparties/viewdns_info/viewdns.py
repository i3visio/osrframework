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
import re
import time

import cfscrape
import requests

import osrframework.utils.general as general


def check_reverse_whois(query=None, sleep_seconds=1):
    """Method that checks if the given string is linked to a domain.

    Args:
        query (str): query to verify.
        sleep_seconds (int): Number of seconds to wait between calls.

    Returns:
        A python structure for the json received. If nothing was found, it will
        return an empty list.
    """
    results = []

    # Sleeping just a little bit
    time.sleep(sleep_seconds)

    target_url = f"https://viewdns.info/reversewhois/?q={query}"

    ua = 'osrframework 0.20.0'
    ua = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"

    headers = {
        'User-Agent': ua
    }

    try:
        cookies, user_agent = cfscrape.get_tokens(target_url, user_agent=ua)
    except requests.exceptions.HTTPError as e:
        print(f"\t[*] Unauthorised: '{str(e)}'")
        return leaks

    # Accessing the HIBP API
    time.sleep(sleep_seconds)

    # Building API query
    try:
        resp = requests.get(
            target_url,
            headers=headers,
            cookies=cookies,
            verify=True
        )
    except requests.exceptions.HTTPError as e:
        print(f"\t[*] Unauthorised: '{str(e)}'")
        return []

    domains_found = re.findall("Registrar</td></tr><tr><td>([^<]+)</td>", resp.text)

    # Reading the text data onto python structures
    try:
        for domain in domains_found:
            # Building the i3visio like structure
            new = {}
            new["value"] = f"(ViewDNS.info) {domain} - {query}"
            new["type"] = "com.i3visio.Profile"
            new["attributes"] = [
                {
                    "type": "com.i3visio.Domain",
                    "value": domain,
                    "attributes": []
                },
                {
                    "type": "@source",
                    "value": "viewdns.info",
                    "attributes": []
                },
                {
                    "type": "@source_uri",
                    "value": target_url,
                    "attributes": []
                }
            ] + general.expand_entities_from_email(query)
            results.append(new)
    except ValueError:
        return []
    except Exception:
        print("ERROR: Something happenned when using View.com.")
        return []

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps an account search onto viewdns.info reverse Whois service.', prog='viewdns.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<text>', action='store', help='query to be performed to viewdns.info.', required=True)

    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()

    result = check_reverse_whois(email=args.query)
    print(f"Results found for {args.query}:\n")
    print(json.dumps(result, indent=2))

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

import requests

import osrframework.utils.general as general


def check_if_email_was_hacked(email=None, sleep_seconds=1):
    """Method that checks if the given email is stored in the Dehashed website.

    Args:
        email (str): Email to verify.
        sleep_seconds (int): Number of seconds to wait between calls.

    Returns:
        A python structure for the json received. If nothing was found, it will
        return an empty list.
    """
    leaks = []

    # Sleeping just a little bit
    time.sleep(sleep_seconds)

    target_url = f"https://www.dehashed.com/search?query=\"{email}\""

    # Building API query
    resp = requests.get(
        target_url,
        verify=True
    )

    platforms_leaked = re.findall("found in (.+) dump", resp.text)

    # Reading the text data onto python structures
    try:
        for leak in platforms_leaked:
            # Building the i3visio like structure
            new = {}
            new["value"] = f"(Dehashed) {leak} - {email}"
            new["type"] = "com.i3visio.Profile"
            new["attributes"] = [
                {
                    "type": "com.i3visio.Platform.Leaked",
                    "value": leak,
                    "attributes": []
                },
                {
                    "type": "@source",
                    "value": "dehashed.com",
                    "attributes": []
                },
                {
                    "type": "@source_uri",
                    "value": target_url,
                    "attributes": []
                }
            ] + general.expand_entities_from_email(email)
            leaks.append(new)
    except ValueError:
        return []
    except Exception:
        print("ERROR: Something happenned when using Dehashed.com.")
        return []

    return leaks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A library that wraps an account search onto dehashed.com.', prog='dehashed.py', epilog="", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<email>', action='store', help='query to be performed to dehashed.com.', required=True)

    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()

    result = check_if_email_was_hacked(email=args.query)
    print(f"Results found for {args.query}:\n")
    print(json.dumps(result, indent=2))

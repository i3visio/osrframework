# !/usr/bin/python
# -*- coding: utf-8 -*-
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
import json
import requests
import sys
import time

def checkIfEmailWasHacked(email=None, sleepSeconds=0.5):
    """
    Method that checks if the given email is stored in hesidohackeado.com.

    This function automatically waits a second to avoid problems with the API
    rate limit. An example of the json received:
    ```
        {
            "status": "found",
            "query": "foo@bar.com",
            "results": 12,
            "data": [
                {
                    "title": "Gambling Pack - 35k1",
                    "author": "anon",
                    "verified": false,
                    "date_created": "2016-10-01T00:00:00+00:00",
                    "date_leaked": "2016-10-01T00:00:00+00:00",
                    "emails_count": 170345,
                    "details": "https:\/\/hesidohackeado.com\/leak\/fa343fba3636b4148296\/gambling-pack-35k1",
                    "source_url": "#",
                    "source_lines": 312624,
                    "source_size": 7008384,
                    "source_network": "darknet",
                    "source_provider": "anon"
                },
                …
            ]
        }

    ```

    Args:
    -----
        email: Email to verify in hesidohackeado.com.

    Returns:
    --------
        A python structure for the json received. If nothing was found, it will
        return an empty list.
    """
    # Sleeping a second
    time.sleep(sleepSeconds)

    # Building API query
    apiURL= "https://hesidohackeado.com/api?q=" + email
    # Accessing the HIBP API
    try:
        data = requests.get(apiURL).text
        # Reading the text data onto python structures
        jsonData = json.loads(data)

        if jsonData["status"] == "found":
            leaks = []

            # Building the i3visio like structure
            for e in jsonData["data"]:
                new = {}
                new["value"] = "(HSH) " + e["title"]
                new["type"] = "i3visio.platform_leaked"
                new["attributes"] = [
                    {
                        "value": "@source",
                        "type": "hesidohackeado.com",
                        "attributes": []
                    },
                    {
                        "value": "i3visio_uri",
                        "type": apiURL,
                        "attributes": []
                    },
                    {
                        "value": "@pwn_count",
                        "type": e['emails_count'],
                        "attributes": []
                    },
                    {
                        "value": "@added_date",
                        "type": e['date_created'],
                        "attributes": []
                    },
                    {
                        "value": "@breach_date",
                        "type": e['date_leaked'],
                        "attributes": []
                    },
                    {
                        "value": "@description",
                        "type": e['details'],
                        "attributes": []
                    },
                    {
                        "value": "@author",
                        "type": e['author'],
                        "attributes": []
                    }
                ]
                leaks.append(new)

            return leaks
        else:
            return []
    except:
        # Something happened so we return a null entity
        return []


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

#!/usr/bin/env python
# encoding: utf-8
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

#!/usr/bin/env python
# encoding: utf-8

import argparse
import json
import csv
import requests
import time

import osrframework.utils.config_api_keys as api_keys
from osrframework.utils.global_api import APIWrapper as APIWrapper

class TwitterAPIWrapper(APIWrapper):
    """Twitter API wrapper using requests for direct API interaction."""

    def __init__(self, api_data=None):
        """Constructor

        Args:
            api_data (dict): dictionary containing the credentials for the
                given platform.
        """
        if api_data is None:
            api_data = api_keys.get_list_of_api_keys()["twitter"]
        self.consumer_key = api_data["consumer_key"]
        self.consumer_secret = api_data["consumer_secret"]
        self.access_token = api_data["access_token"]
        self.access_secret = api_data["access_secret"]
        self.platformName = "Twitter"

    def _connectToAPI(self):
        """Generate headers with Bearer token for API calls."""
        bearer_token = self.access_token
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        return headers

    def _rate_limit_status(self):
        """Check API rate limits"""
        headers = self._connectToAPI()
        response = requests.get(
            "https://api.twitter.com/2/application/rate_limit_status", headers=headers
        )
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error: {response.status_code} - {response.text}")
        input("<Press ENTER to continue>")

    def _processUser(self, jUser):
        """Convert user data to i3visio-like format"""
        r = {
            "type": "com.i3visio.Profile",
            "value": self.platformName + " - " + jUser["username"],
            "attributes": []
        }
        attributes = {
            "@twitter_id": jUser["id"],
            "com.i3visio.Alias": jUser["username"],
            "com.i3visio.Name": jUser.get("name", "[N/A]"),
            "com.i3visio.Text": jUser.get("description", "[N/A]"),
            "com.i3visio.Platform": self.platformName,
            "com.i3visio.Location": jUser.get("location", "[N/A]"),
            "@created_at": jUser.get("created_at"),
            "@friends_count": jUser.get("friends_count", "[N/A]"),
            "@followers_count": jUser.get("followers_count", "[N/A]"),
            "@verified": str(jUser.get("verified", False)).lower()
        }
        for key, value in attributes.items():
            r["attributes"].append({"type": key, "value": value, "attributes": []})
        return r

    def _process_tweet(self, tweet):
        """Convert a tweet to a list format for CSV"""
        return [
            tweet["id_str"],
            tweet["created_at"],
            tweet["full_text"],
            tweet["source"],
            tweet.get("coordinates", "[N/A]"),
            tweet["retweet_count"],
            tweet["favorite_count"],
            tweet["lang"],
            tweet.get("place", "[N/A]"),
            tweet.get("geo", "[N/A]"),
            tweet["id"],
            tweet["user"]["screen_name"],
            "|".join([url["expanded_url"] for url in tweet["entities"].get("urls", [])]),
            "|".join([mention["screen_name"] for mention in tweet["entities"].get("user_mentions", [])])
        ]

    def get_all_docs(self, screen_name):
        """Retrieve all tweets by a user."""
        headers = self._connectToAPI()
        params = {
            "screen_name": screen_name,
            "count": 200,
            "tweet_mode": "extended"
        }
        response = requests.get(
            "https://api.twitter.com/1.1/statuses/user_timeline.json",
            headers=headers,
            params=params
        )
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return []

        tweets = response.json()
        alltweets = [self._process_tweet(tweet) for tweet in tweets]

        # Save tweets to CSV
        with open(f'{screen_name}_tweets.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                "_tweet_id", "_tweet_created_at", "_tweet_text", "_tweet_source",
                "_tweet_coordinates", "_tweet_retweet_count", "_tweet_favourite_count",
                "_tweet_lang", "i3visio_location", "_tweet_geo", "_twitter_id",
                "i3visio_alias", "i3visio_uri", "i3visio_alias_mentions",
            ])
            writer.writerows(alltweets)

        return alltweets

    def get_user(self, screen_name):
        """Retrieve user profile data"""
        headers = self._connectToAPI()
        response = requests.get(
            f"https://api.twitter.com/2/users/by/username/{screen_name}",
            headers=headers
        )
        if response.status_code == 200:
            user = response.json().get("data", {})
            return self._processUser(user)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}

    def get_followers(self, screen_name):
        """Retrieve followers of a user"""
        headers = self._connectToAPI()
        params = {
            "screen_name": screen_name,
            "count": 200
        }
        response = requests.get(
            "https://api.twitter.com/1.1/followers/list.json",
            headers=headers,
            params=params
        )
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return []

        followers = response.json().get("users", [])
        follower_data = [self._processUser(follower) for follower in followers]
        return follower_data

    def get_friends(self, screen_name):
        """Retrieve friends (following) of a user"""
        headers = self._connectToAPI()
        params = {
            "screen_name": screen_name,
            "count": 200
        }
        response = requests.get(
            "https://api.twitter.com/1.1/friends/list.json",
            headers=headers,
            params=params
        )
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return []

        friends = response.json().get("users", [])
        friends_data = [self._processUser(friend) for friend in friends]
        return friends_data

    def search_users(self, query, count=20):
        """Search for users based on a query"""
        headers = self._connectToAPI()
        params = {
            "q": query,
            "count": count
        }
        response = requests.get(
            "https://api.twitter.com/1.1/users/search.json",
            headers=headers,
            params=params
        )
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return []

        users = response.json()
        user_data = [self._processUser(user) for user in users]
        return user_data

def main(args):
    """Main function to handle user queries."""
    tAW = TwitterAPIWrapper()

    if args.type == "get_all_docs":
        results = tAW.get_all_docs(args.query)
    elif args.type == "get_user":
        results = tAW.get_user(args.query)
    elif args.type == "get_followers":
        results = tAW.get_followers(args.query)
    elif args.type == "get_friends":
        results = tAW.get_friends(args.query)
    elif args.type == "search_users":
        results = tAW.search_users(args.query)

    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A library that wraps searches onto the Twitter API.',
        prog='twitter_api.py',
        epilog="NOTE: API tokens are retrieved from api_keys.cfg configuration file.",
        add_help=False
    )
    parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='Query to be performed.', required=True)
    parser.add_argument('-t', '--type', action='store', choices=["get_all_docs", "get_user", "get_followers", "get_friends", "search_users"], required=True)

    args = parser.parse_args()
    main(args)

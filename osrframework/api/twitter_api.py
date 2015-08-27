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

import argparse
import json
import time
import tweepy #https://github.com/tweepy/tweepy
import csv

import osrframework.utils.config_api_keys as api_keys
from osrframework.utils.global_api import APIWrapper as APIWrapper

class TwitterAPIWrapper(APIWrapper):
    '''
        Twitter API wrapper using tweepy API.
    '''

    def __init__(self, api_data=api_keys.returnListOfAPIKeys()["twitter"]):
        '''
            :param api_data:    dictionary containing the credentials for the given platform.
        '''
        # Processing the results received by parameter
        self.consumer_key= api_data["consumer_key"] 
        self.consumer_secret= api_data["consumer_secret"] 
        self.access_key= api_data["access_key"] 
        self.access_secret = api_data["access_secret"]
        
        # The platformName, a bit redundant
        self.platformName = "Twitter"   

        #Twitter API credentials

    def _connectToAPI(self):
        '''
            :return: A tweepy.API object that performs the queries
        '''
        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)
        return api

    def _rate_limit_status(self, api=None, mode=None):
        '''
            Verifying the API limits
        '''
        if api == None:
            api = self.connectToAPI()
        
        if mode == None:
            print json.dumps(api.rate_limit_status(), indent=2)
            raw_input("Presionar")            
        else:
            # Testing if we have enough queries
            while True:
                allLimits = api.rate_limit_status()
                
                if mode == "get_user":
                    limit = allLimits["resources"]["users"]["/users/show/:id"]["limit"]
                    remaining = allLimits["resources"]["users"]["/users/show/:id"]["remaining"]
                    reset = allLimits["resources"]["users"]["/users/show/:id"]["reset"]
                elif mode == "get_followers":
                    limit = allLimits["resources"]["followers"]["/followers/ids"]["limit"]
                    remaining = allLimits["resources"]["followers"]["/followers/ids"]["remaining"]
                    reset = allLimits["resources"]["followers"]["/followers/ids"]["reset"]                     
                elif mode == "get_friends":
                    limit = allLimits["resources"]["friends"]["/friends/ids"]["limit"]
                    remaining = allLimits["resources"]["friends"]["/friends/ids"]["remaining"]
                    reset = allLimits["resources"]["friends"]["/friends/ids"]["reset"]     
                elif mode == "search_users":
                    limit = allLimits["resources"]["users"]["/users/search"]["limit"]
                    remaining = allLimits["resources"]["users"]["/users/search"]["remaining"]
                    reset = allLimits["resources"]["users"]["/users/search"]["reset"]
                else:
                    remaining = 1
                """elif mode == "get_users":
                    limit = allLimits["resources"]REPLACEME["limit"]
                    remaining = allLimits["resources"]REPLACEME["remaining"]
                    reset = allLimits["resources"]REPLACEME["reset"] """                    
                # Checking if we have enough remaining queries
                if remaining > 0:
                    #raw_input(str(remaining) + " queries yet...")
                    break
                else:
                    waitTime = 60
                    print "No more queries remaining, sleeping for " + str(waitTime) +" seconds..."
                    time.sleep(waitTime)
            
        return 0

    def _processUser(self, jUser):
        '''
            Convert tweepy.User to a i3visio-like user. This will process the returned JSON object that the API returns to transform it to the i3visio-like format. A sample answer is copied now when testing it to the @i3visio user in Twitter.
{
  "follow_request_sent": false, 
  "has_extended_profile": false, 
  "profile_use_background_image": true, 
  "profile_text_color": "333333", 
  "default_profile_image": false, 
  "id": 2594815981, 
  "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
  "verified": false, 
  "profile_location": null, 
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/491716630292881408/FBqYf9qv_normal.png", 
  "profile_sidebar_fill_color": "DDEEF6", 
  "entities": {
    "url": {
      "urls": [
        {
          "url": "http://t.co/Vus95W8ub6", 
          "indices": [
            0, 
            22
          ], 
          "expanded_url": "http://www.i3visio.com", 
          "display_url": "i3visio.com"
        }
      ]
    }, 
    "description": {
      "urls": [
        {
          "url": "http://t.co/SGty7or6SQ", 
          "indices": [
            30, 
            52
          ], 
          "expanded_url": "http://github.com/i3visio/osrframework", 
          "display_url": "github.com/i3visio/osrfra\u2026"
        }
      ]
    }
  }, 
  "followers_count": 21, 
  "profile_sidebar_border_color": "C0DEED", 
  "id_str": "2594815981", 
  "profile_background_color": "C0DEED", 
  "listed_count": 5, 
  "status": {
    "lang": "es", 
    "favorited": false, 
    "entities": {
      "symbols": [], 
      "user_mentions": [], 
      "hashtags": [], 
      "urls": []
    }, 
    "contributors": null, 
    "truncated": false, 
    "text": "Podemos confirmar que Alpify, aunque acabe en ...fy no es una aplicaci\u00f3n nuestra. ;) \u00a1A aprovechar lo que queda de domingo!", 
    "created_at": "Sun Aug 16 17:35:37 +0000 2015", 
    "retweeted": true, 
    "in_reply_to_status_id_str": null, 
    "coordinates": null, 
    "in_reply_to_user_id_str": null, 
    "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>", 
    "in_reply_to_status_id": null, 
    "in_reply_to_screen_name": null, 
    "id_str": "632968969662689280", 
    "place": null, 
    "retweet_count": 1, 
    "geo": null, 
    "id": 632968969662689280, 
    "favorite_count": 0, 
    "in_reply_to_user_id": null
  }, 
  "is_translation_enabled": false, 
  "utc_offset": null, 
  "statuses_count": 56, 
  "description": "Leading OSRFramework project (http://t.co/SGty7or6SQ) for researching in Open Sources. #security #osint #socialengineering", 
  "friends_count": 10, 
  "location": "Espa\u00f1a", 
  "profile_link_color": "0084B4", 
  "profile_image_url": "http://pbs.twimg.com/profile_images/491716630292881408/FBqYf9qv_normal.png", 
  "following": true, 
  "geo_enabled": false, 
  "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
  "name": "i3visio", 
  "lang": "en", 
  "profile_background_tile": false, 
  "favourites_count": 6, 
  "screen_name": "i3visio", 
  "notifications": false, 
  "url": "http://t.co/Vus95W8ub6", 
  "created_at": "Sun Jun 29 13:27:20 +0000 2014", 
  "contributors_enabled": false, 
  "time_zone": null, 
  "protected": false, 
  "default_profile": true, 
  "is_translator": false
}
                        
            :param jUser:   A Json representing the information of a profile as returned by the API.            
            
            
            :return: Dict in i3visio-like format.
        '''
        r = {}            
        r["type"] = "i3visio.profile"
        r["value"] = self.platformName + " - " + jUser["screen_name"]                
        r["attributes"] = []   
        
        # Appending platform URI
        """aux = {}
        aux["type"] = "i3visio.uri"
        aux["value"] = qURL
        aux["attributes"] = []           
        r["attributes"].append(aux) """
        # Appending the id
        aux = {}
        aux["type"] = "@id_str"
        aux["value"] = jUser["id_str"]
        aux["attributes"] = []           
        r["attributes"].append(aux)
        
        # Appending the alias
        aux = {}
        aux["type"] = "i3visio.alias"
        aux["value"] = jUser["screen_name"]
        aux["attributes"] = []           
        r["attributes"].append(aux)
        # Appending fullname
        aux = {}
        aux["type"] = "i3visio.fullname"
        aux["value"] = jUser["name"]
        aux["attributes"] = []
        r["attributes"].append(aux)
        # Appending description
        aux = {}
        aux["type"] = "i3visio.text"
        aux["value"] = jUser["description"]
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending platform name
        aux = {}
        aux["type"] = "i3visio.platform"
        aux["value"] = self.platformName
        aux["attributes"] = []
        r["attributes"].append(aux)
        # Appending location
        aux = {}
        aux["type"] = "i3visio.location"
        aux["value"] = jUser["location"]
        aux["attributes"] = []
        r["attributes"].append(aux)
        # Appending profile_location
        aux = {}
        aux["type"] = "i3visio.location.current"
        aux["value"] = jUser["profile_location"]
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending uri homepage      
        try:
            print "a"
            urls = jUser["entities" ]["url"]["urls"]
            print urls
            for url in urls:
                aux = {}
                aux["type"] = "i3visio.uri.homepage"
                aux["value"] = url["expanded_url"]
                aux["attributes"] = []
                r["attributes"].append(aux)                    
        except Exception as e:
            #print str(e)
            #Something happenned when parsing the URLS
            aux = {}
            aux["type"] = "i3visio.uri.homepage"
            aux["value"] = jUser["url"]
            aux["attributes"] = []
            r["attributes"].append(aux)        
        # Appending created_at
        aux = {}
        aux["type"] = "@created_at"
        aux["value"] = jUser["created_at"]
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending friends_count
        aux = {}
        aux["type"] = "@friends_count"
        aux["value"] = str(jUser["friends_count"])
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending followers_count
        aux = {}
        aux["type"] = "@followers_count"
        aux["value"] = str(jUser["followers_count"])
        aux["attributes"] = []
        r["attributes"].append(aux)    
        # Appending protected
        aux = {}
        aux["type"] = "@protected"
        aux["value"] = str(jUser["protected"]).lower()
        aux["attributes"] = []
        r["attributes"].append(aux)
        # Appending geo_enabled
        aux = {}
        aux["type"] = "@geo_enabled"
        aux["value"] = str(jUser["geo_enabled"]).lower()
        aux["attributes"] = []
        r["attributes"].append(aux)    
        # Appending language
        aux = {}
        aux["type"] = "@language"
        aux["value"] = jUser["lang"]
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending time_zone
        aux = {}
        aux["type"] = "@time_zone"
        aux["value"] = jUser["time_zone"]
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending verified
        aux = {}
        aux["type"] = "@verified"
        aux["value"] = str(jUser["verified"]).lower()
        aux["attributes"] = []
        r["attributes"].append(aux)        
        # Appending listed_count
        aux = {}
        aux["type"] = "@listed_count"
        aux["value"] = str(jUser["listed_count"])
        aux["attributes"] = []
        r["attributes"].append(aux) 
        # Appending publications_count
        aux = {}
        aux["type"] = "@publications_count"
        aux["value"] = str(jUser["statuses_count"])
        aux["attributes"] = []
        r["attributes"].append(aux)         
        # Appending favourites_count
        aux = {}
        aux["type"] = "@favourites_count"
        aux["value"] = str(jUser["favourites_count"])
        aux["attributes"] = []
        r["attributes"].append(aux)         
        # Appending suspended
        try:
            aux = {}
            aux["type"] = "@suspended"
            aux["value"] = str(jUser["suspended"]).lower()
            aux["attributes"] = []
            r["attributes"].append(aux)        
        except:
            pass
        return r
        
    def get_all_docs(self, screen_name):
        '''
            Method to get all the tweets emitted by a user.
            
            :param screen_name: The Twitter username.

            :return:    List of tweets.            
        '''
        # Connecting to the API
        api = self._connectToAPI()
    
        #initialize a list to hold all the tweepy Tweets
        alltweets = []    
    
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
        #save most recent tweets
        alltweets.extend(new_tweets)
    
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
    
        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print "Getting tweets before %s" % (oldest)
        
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
            #save most recent tweets
            alltweets.extend(new_tweets)
        
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
        
            print "... %s tweets downloaded so far" % (len(alltweets))
        #print alltweets
        """#transform the tweepy tweets into a 2D array that will populate the csv    
        outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
        #write the csv    
        with open('%s_tweets.csv' % screen_name, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)
    
        pass"""
        return alltweets

    def get_followers(self, query):
        '''
            Method to get the followers of a user.
            
            :param query:   Query to be performed.
            
            :return:    List of ids.
        '''
        # Connecting to the API        
        api = self._connectToAPI()
        
        # Verifying the limits of the API
        self._rate_limit_status(api=api, mode="get_followers")        
        
        # Making the call to the API
        try:
            friends_ids = api.followers_ids(query)
        except:
            return []
                    
        """res = []
        # Extracting the information from each profile
        for a in aux:
            us= self.getUser(a)
            res.append(self._processUser(us))"""
            
        return friends_ids

    def get_friends(self, query):
        '''
            Method to get the friends of a user.
            
            :param query:   Query to be performed.
            
            :return:    List of users.
        '''
        # Connecting to the API        
        api = self._connectToAPI()
        
        # Verifying the limits of the API
        self._rate_limit_status(api=api, mode="get_friends")
                
        # Making the call to the API
        try:
            friends_ids = api.friends_ids(query)
        except:
            return []
                    
        """res = []
        # Extracting the information from each profile
        for a in aux:
            us= self.getUser(a)
            res.append(self._processUser(us))"""
            
        return friends_ids        

        
    def get_user(self, screen_name):
        '''
            Method to perform the usufy searches.

            :param screen_name: nickname to be searched.        

            :return:    User.                        
        '''
        # Connecting to the API
        api = self._connectToAPI()

        # Verifying the limits of the API
        self._rate_limit_status(api=api, mode="get_user")
        
        aux = []
        try:
            user = api.get_user(screen_name)
            # Iterate through the results using user._json
            aux.append(user._json)
        except tweepy.error.TweepError as e:
            pass
        
        res = []
        # Extracting the information from each profile
        for a in aux:
            res.append(self._processUser(a))
        return res

    def search_users(self, query, n=20, maxUsers=60):
        '''
            Method to perform the searchfy searches.
            
            :param query:   Query to be performed.
            :param n:   Number of results per query.
            :param maxUsers:    Max. number of users to be recovered.
            
            :return:    List of users
        '''
        # Connecting to the API        
        api = self._connectToAPI()

        # Verifying the limits of the API
        self._rate_limit_status(api=api, mode="search_users")

        aux = []                
                
        page = 0

        # print "Getting page %s of new users..." % page+1        
        # Making the call to the API
        try:
            newUsers = api.search_users(query, n, page)
            
            for n in newUsers:
                aux.append(n._json)
            
            #keep grabbing tweets until there are no tweets left to grab
            while len(aux) < maxUsers & len(newUsers)>0:
                page+=1
                print "Getting page %s of new users..." % page
            
                # Grabbing new Users
                newUsers = api.search_users(query, n, page)
            
                # Save the users found
                aux.extend(newUsers)
        except:
            pass
                    
        res = []
        # Extracting the information from each profile
        for a in aux:
            res.append(self._processUser(a))
            
        return res


def main(args):
    '''
        Query manager.
    '''
    # Creating the instance
    tAW = TwitterAPIWrapper()
    
    # Selecting the query to be launched
    if args.type == "get_all_tweets":
        results = tAW.get_all_tweets(args.query)
        
    elif args.type == "get_user":
        results = tAW.get_user(args.query)
        
    elif args.type == "get_followers":
        results = tAW.get_followers(args.query)            

        print "... %s followers downloaded... " % (len(results))    
        #write the csv    
        with open('%s_followers.csv' % args.query, 'wb') as f:
            writer = csv.writer(f)
            for r in results:
                writer.writerow([args.query,str(r)])        
                       
    elif args.type == "get_friends":
        results = tAW.get_friends(args.query)            
        print "... %s friends downloaded... " % (len(results))    
        #write the csv    
        with open('%s_friends.csv' % args.query, 'wb') as f:
            writer = csv.writer(f)
            for r in results:
                writer.writerow([args.query,str(r)])        
        
    elif args.type == "search_users":
        results = tAW.search_users(args.query)                    
            
    return results
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A library that wraps searches onto the Twitter API.', prog='twitter_api.py', epilog="NOTE: if not provided, the API key will be searched in the config_api_keys.py file.", add_help=False)
    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-q', '--query', metavar='<hash>', action='store', help='query to be performed to md5crack.com.', required=True)        
    parser.add_argument('-t', '--type', action='store', choices=["get_all_tweets", "get_user", "get_followers", "get_friends", "search_users"], help='Type of query to be performed.', required=True)
    
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

    args = parser.parse_args()        

    results = main(args)
    
    print json.dumps(results, indent=2)
    print len(results)
    

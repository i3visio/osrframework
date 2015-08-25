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

    def _processUser(self, jUser):
        '''
            Convert tweepy.User to a i3visio-like user.
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
        # Appending uri homepage
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
        
        print json.dumps(api.rate_limit_status(), indent=2)
        raw_input("Presionar")
        
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
        print "wait for it"
        # Connecting to the API
        api = self._connectToAPI()
        print "here"
        aux = []
        try:
            user = api.get_user(screen_name)
            # Iterate through the results using user._json
            aux.append(user._json)
            #print json.dumps(user._json, indent=2)            
        except tweepy.error.TweepError as e:
            pass
        
        res = []
        # Extracting the information from each profile
        for a in aux:
            res.append(self._processUser(a))
        print res
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
    

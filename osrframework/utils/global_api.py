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
import csv

import osrframework.utils.config_api_keys as api_keys

class APIWrapper():
    '''
        Global API wrapper.
    '''

    def __init__(self, api_data=None):
        '''
            :param api_data:    dictionary containing the credentials for the given platform.
        '''
        pass        
        
    def get_user(self, screen_name):
        '''
            Method to perform the usufy searches.
                    
            :param screen_name: nickname to be searched.        

            :return:    User.
        '''
        return {}

    def search_users(self, query, n=20, maxUsers=60):
        '''
            Method to perform the searchfy searches.
                    
            :param query:   Query to be performed.
            :param n:   Number of results per query.
            :param maxUsers:    Max. number of users to be recovered.
            
            :return:    List of users.
        '''           
        return []
        
        
    def get_all_docs(self, screen_name):
        '''
            :param screen_name: nick from which we will try to recover the docs, i. e., tweets, publications, etc.
            
            :return:    List of publications, i. e., tweets, publications, etc.            
        '''
        return []


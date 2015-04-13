# -*- coding: cp1252 -*-
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

import osrframework.utils.credentials as credentials

##################################################
##################################################
# A
from osrframework.wrappers.adtriboo import Adtriboo
from osrframework.wrappers.anarchy101 import Anarchy101
from osrframework.wrappers.aporrealos import Aporrealos
from osrframework.wrappers.apsense import Apsense
from osrframework.wrappers.arduino import Arduino
from osrframework.wrappers.ariva import Ariva
from osrframework.wrappers.armorgames import Armorgames
from osrframework.wrappers.artbreak import Artbreak
from osrframework.wrappers.artician import Artician
from osrframework.wrappers.arto import Arto
from osrframework.wrappers.askfm import Askfm
from osrframework.wrappers.audiob import Audiob
from osrframework.wrappers.audioboo import Audioboo
from osrframework.wrappers.authorstream import Authorstream
from osrframework.wrappers.autospies import Autospies

# B
from osrframework.wrappers.backyardchickens import Backyardchickens
from osrframework.wrappers.badoo import Badoo
from osrframework.wrappers.behance import Behance
from osrframework.wrappers.bennugd import Bennugd
from osrframework.wrappers.bitbucket import Bitbucket
from osrframework.wrappers.bitcointalk import Bitcointalk
from osrframework.wrappers.bitly import Bitly
from osrframework.wrappers.blackplanet import Blackplanet
from osrframework.wrappers.bladna import Bladna
from osrframework.wrappers.blip import Blip
from osrframework.wrappers.blogspot import Blogspot
from osrframework.wrappers.bookmarky import Bookmarky
from osrframework.wrappers.bookofmatches import Bookofmatches
from osrframework.wrappers.boonex import Boonex
from osrframework.wrappers.bordom import Bordom
from osrframework.wrappers.boxedup import Boxedup
from osrframework.wrappers.breakcom import Breakcom
from osrframework.wrappers.bucketlistly import Bucketlistly
from osrframework.wrappers.burbuja import Burbuja
from osrframework.wrappers.burdastyle import Burdastyle
from osrframework.wrappers.buzznet import Buzznet

# C
from osrframework.wrappers.cafemom import Cafemom
from osrframework.wrappers.carbonmade import Carbonmade
from osrframework.wrappers.cardomain import Cardomain
from osrframework.wrappers.care2 import Care2
from osrframework.wrappers.castroller import Castroller
from osrframework.wrappers.causes import Causes
from osrframework.wrappers.ccsinfo import Ccsinfo
from osrframework.wrappers.chess import Chess
from osrframework.wrappers.cockos import Cockos
from osrframework.wrappers.connectingsingles import Connectingsingles
from osrframework.wrappers.couchsurfing import Couchsurfing

# D

# E

# F

# G

# H

# I

# J

# K

# L
from osrframework.wrappers.listspam import Listspam

# M

# N

# O

# P

# Q

# R

# S

# T
from osrframework.wrappers.twitter import Twitter

# U

# V

# W

# X

# Y
from osrframework.wrappers.youku import Youku
from osrframework.wrappers.youtube import Youtube

# Z
from osrframework.wrappers.zabbix import Zabbix
from osrframework.wrappers.zentyal import Zentyal
##################################################
##################################################


def getAllPlatformNames(mode):
    ''' 
        Method that defines the whole list of available parameters.
        
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].

        Return values:
            Returns a list [] of strings for the platform objects.
    '''
    # Recovering all the possible platforms installed
    allPlatforms = getAllPlatformObjects(mode=mode)
    # Defining the platOptions
    platOptions = []
    for p in allPlatforms:
        try:
            # E. g.: to use wikipedia instead of wikipedia_ca and so on
            parameter = p.parameterName
        except:
            parameter = p.platformName.lower()
        
        if parameter not in platOptions:
            platOptions.append(parameter)
    platOptions =  sorted(set(platOptions))
    platOptions.insert(0, 'all')
    return platOptions


def getPlatformsByName(platformNames = ['all'], mode = None, tags = []):
    ''' 
        Method that recovers the names of the <Platforms> in a given list.
        
        :param platformNames:    list of strings containing the possible platforms.
        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        :param tags:    Just in case the method to select the candidates is a series of tags.
        :return:    Array of <Platforms> classes.
    '''

    allPlatformsList = getAllPlatformObjects(mode)
    
    if 'all' in platformNames:
        return allPlatformsList

    platformList = []
    # going through the regexpList 
    for name in platformNames:
        for plat in allPlatformsList:
            added = False
            # Verifying if the parameter was provided
            if name == str(plat.platformName).lower():
                platformList.append(plat)
                added = True
                break    
            # Verifying if any of the platform tags match the original tag
            if not added:
                for t in plat.tags:
                    if t in tags:
                        platformList.append(plat)
                        break                    
    return platformList      


def getAllPlatformObjects(mode = None):
    ''' 
        Method that recovers ALL the list of <Platform> classes to be processed....

        :param mode:    The mode of the search. The following can be chosen: ["phonefy", "usufy", "searchfy"].
        
        :return:    Returns a list [] of <Platform> objects.
    '''
    listAll = []
    ##################################################
    ##################################################
    # A
    listAll.append(Adtriboo())
    listAll.append(Anarchy101())
    listAll.append(Aporrealos())
    listAll.append(Apsense())
    listAll.append(Arduino())
    listAll.append(Ariva())
    listAll.append(Armorgames())
    #listAll.append(Artbreak())
    listAll.append(Artician())
    listAll.append(Arto())
    listAll.append(Askfm())
    listAll.append(Audiob())
    listAll.append(Audioboo())
    listAll.append(Authorstream())
    listAll.append(Autospies())
    
    # B
    listAll.append(Backyardchickens())
    listAll.append(Badoo())
    listAll.append(Behance())
    listAll.append(Bennugd())
    listAll.append(Bitbucket())
    listAll.append(Bitcointalk())    
    listAll.append(Bitly())
    listAll.append(Blackplanet())
    listAll.append(Bladna())
    listAll.append(Blip())
    listAll.append(Blogspot())
    listAll.append(Bookmarky())
    listAll.append(Bookofmatches())
    listAll.append(Boonex())
    listAll.append(Bordom())
    listAll.append(Boxedup())
    listAll.append(Breakcom())
    listAll.append(Bucketlistly())
    listAll.append(Burbuja())
    listAll.append(Burdastyle())
    listAll.append(Buzznet())
    
    # C
    listAll.append(Cafemom())
    listAll.append(Carbonmade())
    listAll.append(Cardomain())
    listAll.append(Care2())
    listAll.append(Castroller())
    listAll.append(Causes())
    listAll.append(Ccsinfo())
    listAll.append(Chess())
    listAll.append(Cockos())
    listAll.append(Connectingsingles())
    listAll.append(Couchsurfing())    

    # D

    # E

    # F

    # G

    # H

    # I

    # J

    # K

    # L
    listAll.append(Listspam())
    
    # M

    # N

    # O

    # P

    # Q

    # R

    # S

    # T
    listAll.append(Twitter())

    # U

    # V

    # W

    # X

    # Y
    listAll.append(Youku())
    listAll.append(Youtube())
    
    # Z
    listAll.append(Zabbix())
    listAll.append(Zentyal())    
    ##################################################
    ##################################################

    creds = credentials.getCredentials()

    for p in listAll:
        # Verify if there are credentials to be loaded
        if p.platformName.lower() in creds.keys():
            p.setCredentials(creds[p.platformName.lower()])    
    
    if mode == None:
        return listAll
    else:
        # We are returning only those platforms which are required by the mode.
        selected = []
        for p in listAll:
            if p.isValidMode[mode]:
                selected.append(p)
        return selected
        
  

# -*- coding: cp1252 -*-
#
################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
################################################################################

import osrframework.utils.credentials as credentials

##################################################
##################################################
# A
from osrframework.wrappers.about import About
# Issue #103: Removed as this has been moved to Twago
#from osrframework.wrappers.adtriboo import Adtriboo
from osrframework.wrappers.ahmia import Ahmia
from osrframework.wrappers.anarchy101 import Anarchy101
from osrframework.wrappers.aporrealos import Aporrealos
from osrframework.wrappers.apsense import Apsense
from osrframework.wrappers.archive import Archive
from osrframework.wrappers.arduino import Arduino
from osrframework.wrappers.ariva import Ariva
from osrframework.wrappers.armorgames import Armorgames
#from osrframework.wrappers.artbreak import Artbreak
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
from osrframework.wrappers.bitcointa import Bitcointa
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
# Temporally deactivated
#from osrframework.wrappers.couchsurfing import Couchsurfing

# D
from osrframework.wrappers.dailymail import Dailymail
from osrframework.wrappers.dailymotion import Dailymotion
from osrframework.wrappers.deviantart import Deviantart
from osrframework.wrappers.digitalspy import Digitalspy
from osrframework.wrappers.disqus import Disqus
from osrframework.wrappers.doodle import Doodle
from osrframework.wrappers.douban import Douban
from osrframework.wrappers.dribbble import Dribbble
from osrframework.wrappers.drugbuyersforum import Drugbuyersforum
from osrframework.wrappers.drupal import Drupal

# E
from osrframework.wrappers.ebay import Ebay
from osrframework.wrappers.echatta import Echatta
from osrframework.wrappers.elmundo import Elmundo
from osrframework.wrappers.enfemenino import Enfemenino
# Credentials needed?
#from osrframework.wrappers.epinions import Epinions
from osrframework.wrappers.ethereum import Ethereum
from osrframework.wrappers.etsy import Etsy
from osrframework.wrappers.evilzone import Evilzone

# F
from osrframework.wrappers.facebook import Facebook
from osrframework.wrappers.facesaerch import Facesaerch
from osrframework.wrappers.fanbitcoin import Fanbitcoin
from osrframework.wrappers.fanpop import Fanpop
from osrframework.wrappers.fark import Fark
from osrframework.wrappers.favstar import Favstar
from osrframework.wrappers.flickr import Flickr
from osrframework.wrappers.flixster import Flixster
from osrframework.wrappers.foodspotting import Foodspotting
from osrframework.wrappers.forobtc import Forobtc
from osrframework.wrappers.forocoches import Forocoches
from osrframework.wrappers.forosperu import Forosperu
from osrframework.wrappers.foursquare import Foursquare
from osrframework.wrappers.freebase import Freebase
from osrframework.wrappers.freerepublic import Freerepublic
# Project discontinued on 9th April, 2015
#from osrframework.wrappers.friendfeed import Friendfeed

# G
from osrframework.wrappers.gamesheep import Gamesheep
from osrframework.wrappers.gametracker import Gametracker
from osrframework.wrappers.gapyear import Gapyear
from osrframework.wrappers.garage4hackers import Garage4hackers
from osrframework.wrappers.gather import Gather
from osrframework.wrappers.geeksphone import Geeksphone
from osrframework.wrappers.genspot import Genspot
from osrframework.wrappers.getsatisfaction import Getsatisfaction
from osrframework.wrappers.github import Github
from osrframework.wrappers.gitorious import Gitorious
from osrframework.wrappers.gogobot import Gogobot
from osrframework.wrappers.goodreads import Goodreads
from osrframework.wrappers.googleplus import GooglePlus
from osrframework.wrappers.gsmspain import Gsmspain

# H
from osrframework.wrappers.hellboundhackers import Hellboundhackers
from osrframework.wrappers.hi5 import Hi5
from osrframework.wrappers.hubpages import Hubpages

# I
from osrframework.wrappers.ibosocial import Ibosocial
# The website seems to be broken
#from osrframework.wrappers.identica import Identica
from osrframework.wrappers.imgur import Imgur
from osrframework.wrappers.infotelefonica import Infotelefonica
from osrframework.wrappers.instagram import Instagram
from osrframework.wrappers.instructables import Instructables
# Seems to have problems
#from osrframework.wrappers.interracialmatch import Interracialmatch
from osrframework.wrappers.intersect import Intersect
from osrframework.wrappers.intfiction import Intfiction
from osrframework.wrappers.islamicawakening import Islamicawakening
from osrframework.wrappers.issuu import Issuu
from osrframework.wrappers.ivoox import Ivoox
from osrframework.wrappers.ixgames import Ixgames


# J
from osrframework.wrappers.jamiiforums import Jamiiforums
#from osrframework.wrappers.justpaste import Justpaste

# K
from osrframework.wrappers.kali import Kali
from osrframework.wrappers.kanogames import Kanogames
from osrframework.wrappers.karmacracy import Karmacracy
from osrframework.wrappers.kickstarter import Kickstarter
from osrframework.wrappers.kimatel import Kimatel
from osrframework.wrappers.kinja import Kinja
from osrframework.wrappers.klout import Klout
from osrframework.wrappers.kongregate import Kongregate
from osrframework.wrappers.kupika import Kupika

# L
from osrframework.wrappers.lastfm import Lastfm
from osrframework.wrappers.linkedin import Linkedin
from osrframework.wrappers.listaspam import Listaspam
from osrframework.wrappers.livejournal import Livejournal
from osrframework.wrappers.looki import Looki

# M
from osrframework.wrappers.marca import Marca
from osrframework.wrappers.matchdoctor import Matchdoctor
from osrframework.wrappers.mcneel import Mcneel
from osrframework.wrappers.mediavida import Mediavida
from osrframework.wrappers.medium import Medium
from osrframework.wrappers.meneame import Meneame
from osrframework.wrappers.metacafe import Metacafe
from osrframework.wrappers.migente import Migente
from osrframework.wrappers.minecraft import Minecraft
from osrframework.wrappers.musicasacra import Musicasacra
from osrframework.wrappers.myeloma import Myeloma
from osrframework.wrappers.myspace import Myspace

# N
from osrframework.wrappers.naver import Naver
from osrframework.wrappers.netlog import Netlog
from osrframework.wrappers.netvibes import Netvibes
from osrframework.wrappers.newgrounds import Newgrounds
from osrframework.wrappers.nubelo import Nubelo

# O
from osrframework.wrappers.occupywallst import Occupywallst
from osrframework.wrappers.odnoklassniki import Odnoklassniki
from osrframework.wrappers.openframeworks import Openframeworks
from osrframework.wrappers.oroom import Oroom

# P
from osrframework.wrappers.pastebin import Pastebin
from osrframework.wrappers.pearltrees import Pearltrees
from osrframework.wrappers.peerbackers import Peerbackers
from osrframework.wrappers.periscope import Periscope
from osrframework.wrappers.photobucket import Photobucket
from osrframework.wrappers.pgpmit import PGPMIT
from osrframework.wrappers.pixls import Pixls
from osrframework.wrappers.pinterest import Pinterest
from osrframework.wrappers.pixinsight import Pixinsight
from osrframework.wrappers.pjrc import Pjrc
from osrframework.wrappers.plancast import Plancast
from osrframework.wrappers.pokerred import Pokerred
from osrframework.wrappers.pokerstrategy import Pokerstrategy
from osrframework.wrappers.pornhub import Pornhub
from osrframework.wrappers.proboards import Proboards
from osrframework.wrappers.px500 import Px500
#from osrframework.wrappers.pz import Pz

# Q
from osrframework.wrappers.qq import Qq
from osrframework.wrappers.quartermoonsaloon import Quartermoonsaloon

# R
from osrframework.wrappers.rankia import Rankia
from osrframework.wrappers.rapid import Rapid
from osrframework.wrappers.ratemypoo import Ratemypoo
from osrframework.wrappers.rebelmouse import Rebelmouse
from osrframework.wrappers.redtube import Redtube
# Issue #114
#from osrframework.wrappers.relatious import Relatious
from osrframework.wrappers.researchgate import Researchgate
from osrframework.wrappers.retailmenot import Retailmenot
from osrframework.wrappers.rojadirecta import Rojadirecta
from osrframework.wrappers.ruby import Ruby

# S
from osrframework.wrappers.scribd import Scribd
from osrframework.wrappers.sencha import Sencha
from osrframework.wrappers.sidereel import Sidereel
from osrframework.wrappers.skype import Skype
from osrframework.wrappers.slashdot import Slashdot
from osrframework.wrappers.slideshare import Slideshare
from osrframework.wrappers.smartcitizen import Smartcitizen
from osrframework.wrappers.sokule import Sokule
from osrframework.wrappers.soundcloud import Soundcloud
from osrframework.wrappers.sourceforge import Sourceforge
from osrframework.wrappers.spaniards import Spaniards
from osrframework.wrappers.spoj import Spoj
#from osrframework.wrappers.spotify import Spotify
from osrframework.wrappers.squidoo import Squidoo
from osrframework.wrappers.steamcommunity import Steamcommunity
from osrframework.wrappers.steinberg import Steinberg
from osrframework.wrappers.streakgaming import Streakgaming
from osrframework.wrappers.stuff import Stuff
# Issue  #113
#from osrframework.wrappers.stumbleupon import Stumbleupon

# T
from osrframework.wrappers.teamtreehouse import Teamtreehouse
from osrframework.wrappers.techcrunch import Techcrunch
# Issue #113
#from osrframework.wrappers.thecarcommunity import Thecarcommunity
from osrframework.wrappers.theguardian import Theguardian
from osrframework.wrappers.thehoodup import Thehoodup
from osrframework.wrappers.thepiratebay import Thepiratebay
from osrframework.wrappers.thesims import Thesims
from osrframework.wrappers.thestudentroom import Thestudentroom
#from osrframework.wrappers.torsearch import Torsearch
from osrframework.wrappers.tradimo import Tradimo
from osrframework.wrappers.travian import Travian
from osrframework.wrappers.tripadvisor import Tripadvisor
from osrframework.wrappers.tripit import Tripit
from osrframework.wrappers.trulia import Trulia
from osrframework.wrappers.tumblr import Tumblr
from osrframework.wrappers.tuporno import Tuporno
from osrframework.wrappers.twicsy import Twicsy
# Temporarily deactivated: 2015-06-21
from osrframework.wrappers.twitch import Twitch
from osrframework.wrappers.twitpic import Twitpic
from osrframework.wrappers.twitter import Twitter
from osrframework.wrappers.twoplustwo import Twoplustwo

# U
# Seems to be down: 2015-06-21
#from osrframework.wrappers.ukdebate import Ukdebate
from osrframework.wrappers.ummahforum import Ummahforum
from osrframework.wrappers.unsystem import Unsystem
from osrframework.wrappers.ustream import Ustream


# V
from osrframework.wrappers.vexforum import Vexforum
from osrframework.wrappers.videohelp import Videohelp
from osrframework.wrappers.vimeo import Vimeo
from osrframework.wrappers.virustotal import Virustotal
from osrframework.wrappers.vk import Vk

# W
from osrframework.wrappers.webtv import Webtv
from osrframework.wrappers.wefollow import Wefollow
from osrframework.wrappers.wikipediaar import WikipediaAr
from osrframework.wrappers.wikipediaca import WikipediaCa
from osrframework.wrappers.wikipediade import WikipediaDe
from osrframework.wrappers.wikipediaen import WikipediaEn
from osrframework.wrappers.wikipediaes import WikipediaEs
from osrframework.wrappers.wikipediaeu import WikipediaEu
from osrframework.wrappers.wikipediafr import WikipediaFr
from osrframework.wrappers.wikipediapt import WikipediaPt
from osrframework.wrappers.winamp import Winamp
from osrframework.wrappers.wishlistr import Wishlistr
# Issue #115
#from osrframework.wrappers.worldcarfans import Worldcarfans
from osrframework.wrappers.wordpress import Wordpress
from osrframework.wrappers.wykop import Wykop

# X
from osrframework.wrappers.xanga import Xanga
# Issue #120. Temporally deactivated
#from osrframework.wrappers.xat import Xat
from osrframework.wrappers.xing import Xing
from osrframework.wrappers.xtube import Xtube

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
            # We need to perform additional checks to verify the Wikipedia platforms, which are called with a single parameter
            try:
                if name == str(plat.parameterName).lower():
                    platformList.append(plat)
            except:
                pass
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
    # Requires javascript
    listAll.append(About())
    # Issue #102: Moved to Twago
    #listAll.append(Adtriboo())
    listAll.append(Ahmia())
    listAll.append(Anarchy101())
    listAll.append(Aporrealos())
    listAll.append(Apsense())
    listAll.append(Archive())
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
    listAll.append(Bitcointa())
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
    # Temporally deactivated
    #listAll.append(Couchsurfing())

    # D
    listAll.append(Dailymail())
    listAll.append(Dailymotion())
    listAll.append(Deviantart())
    listAll.append(Digitalspy())
    listAll.append(Disqus())
    listAll.append(Doodle())
    listAll.append(Douban())
    listAll.append(Dribbble())
    listAll.append(Drugbuyersforum())
    listAll.append(Drupal())

    # E
    listAll.append(Ebay())
    listAll.append(Echatta())
    listAll.append(Elmundo())
    listAll.append(Enfemenino())
    #listAll.append(Epinions())
    #listAll.append(Eqe())
    listAll.append(Ethereum())
    listAll.append(Etsy())
    # Issue 104: Temporally deactivated
    #listAll.append(Evilzone())

    # F
    listAll.append(Facebook())
    listAll.append(Facesaerch())
    listAll.append(Fanbitcoin())
    listAll.append(Fanpop())
    listAll.append(Fark())
    listAll.append(Favstar())
    listAll.append(Flickr())
    listAll.append(Flixster())
    listAll.append(Foodspotting())
    listAll.append(Forobtc())
    listAll.append(Forocoches())
    listAll.append(Forosperu())
    listAll.append(Foursquare())
    listAll.append(Freebase())
    listAll.append(Freerepublic())
    # Project discontinued on 9th April, 2015
    #listAll.append(Friendfeed())

    # G
    listAll.append(Gamesheep())
    listAll.append(Gametracker())
    listAll.append(Gapyear())
    listAll.append(Garage4hackers())
    listAll.append(Gather())
    listAll.append(Geeksphone())
    listAll.append(Genspot())
    listAll.append(Getsatisfaction())
    listAll.append(Github())
    listAll.append(Gitorious())
    listAll.append(Gogobot())
    listAll.append(Goodreads())
    listAll.append(GooglePlus())
    listAll.append(Gsmspain())

    # H
    listAll.append(Hellboundhackers())
    listAll.append(Hi5())
    listAll.append(Hubpages())

    # I
    listAll.append(Ibosocial())
    #listAll.append(Identica())
    listAll.append(Imgur())
    listAll.append(Infotelefonica())    
    listAll.append(Instagram())
    listAll.append(Instructables())
    #listAll.append(Interracialmatch())
    listAll.append(Intersect())
    listAll.append(Intfiction())
    #listAll.append(Islamicawakening())
    listAll.append(Issuu())
    listAll.append(Ivoox())
    listAll.append(Ixgames())

    # J
    listAll.append(Jamiiforums())
    # listAll.append(Justpaste())

    # K
    listAll.append(Kali())
    listAll.append(Kanogames())
    listAll.append(Karmacracy())
    listAll.append(Kickstarter())
    listAll.append(Kimatel())
    listAll.append(Kinja())
    listAll.append(Klout())
    listAll.append(Kongregate())
    listAll.append(Kupika())

    # L
    listAll.append(Lastfm())
    listAll.append(Linkedin())
    listAll.append(Listaspam())
    listAll.append(Livejournal())
    listAll.append(Looki())

    # M
    listAll.append(Marca())
    listAll.append(Matchdoctor())
    listAll.append(Mcneel())
    listAll.append(Mediavida())
    listAll.append(Medium())
    listAll.append(Meneame())
    listAll.append(Metacafe())
    listAll.append(Migente())
    listAll.append(Minecraft())
    listAll.append(Musicasacra())
    listAll.append(Myeloma())
    listAll.append(Myspace())

    # N
    listAll.append(Naver())
    listAll.append(Netlog())
    listAll.append(Netvibes())
    listAll.append(Newgrounds())
    listAll.append(Nubelo())

    # O
    listAll.append(Occupywallst())
    listAll.append(Odnoklassniki())
    listAll.append(Openframeworks())
    listAll.append(Oroom())

    # P
    listAll.append(Pastebin())
    listAll.append(Pearltrees())
    listAll.append(Peerbackers())
    listAll.append(Periscope())    
    listAll.append(Photobucket())
    listAll.append(PGPMIT())
    listAll.append(Pinterest())
    listAll.append(Pixinsight())
    listAll.append(Pixls())
    listAll.append(Pjrc())
    listAll.append(Plancast())
    listAll.append(Pokerred())
    listAll.append(Pokerstrategy())
    listAll.append(Pornhub())
    listAll.append(Proboards())
    listAll.append(Px500())
    # listAll.append(Pz())

    # Q
    listAll.append(Qq())
    listAll.append(Quartermoonsaloon())

    # R
    listAll.append(Rankia())
    listAll.append(Rapid())
    listAll.append(Ratemypoo())
    listAll.append(Rebelmouse())
    listAll.append(Redtube())
    # Issue #114
    #listAll.append(Relatious())
    listAll.append(Researchgate())
    listAll.append(Retailmenot())
    listAll.append(Rojadirecta())
    listAll.append(Ruby())

    # S
    listAll.append(Scribd())
    listAll.append(Sencha())
    listAll.append(Sidereel())
    listAll.append(Skype())
    listAll.append(Slashdot())
    listAll.append(Slideshare())
    listAll.append(Smartcitizen())
    listAll.append(Sokule())
    listAll.append(Soundcloud())
    listAll.append(Sourceforge())
    listAll.append(Spaniards())
    listAll.append(Spoj())
    #listAll.append(Spotify())
    listAll.append(Squidoo())
    listAll.append(Steamcommunity())
    listAll.append(Steinberg())
    listAll.append(Streakgaming())
    listAll.append(Stuff())
    # Issue 113
    #listAll.append(Stumbleupon())

    # T
    listAll.append(Teamtreehouse())
    listAll.append(Techcrunch())
    # Issue #113
    #listAll.append(Thecarcommunity())
    #listAll.append(Theguardian())
    listAll.append(Thehoodup())
    listAll.append(Thepiratebay())
    listAll.append(Thesims())
    listAll.append(Thestudentroom())
    #listAll.append(Torsearch())
    listAll.append(Tradimo())
    listAll.append(Travian())
    listAll.append(Tripadvisor())
    listAll.append(Tripit())
    listAll.append(Trulia())
    listAll.append(Tumblr())
    listAll.append(Tuporno())
    listAll.append(Twicsy())
    # Temporarily deactivated: 2015-06-21
    #listAll.append(Twitch())
    listAll.append(Twitpic())
    listAll.append(Twitter())
    listAll.append(Twoplustwo())

    # U
    # Seems to be down: 2015-06-21
    #listAll.append(Ukdebate())
    listAll.append(Ummahforum())
    listAll.append(Unsystem())
    listAll.append(Ustream())

    # V
    listAll.append(Vexforum())
    listAll.append(Videohelp())
    listAll.append(Vimeo())
    listAll.append(Virustotal())
    listAll.append(Vk())

    # W
    #listAll.append(Wefollow())
    listAll.append(Webtv())
    listAll.append(WikipediaAr())
    listAll.append(WikipediaCa())
    listAll.append(WikipediaDe())
    listAll.append(WikipediaEn())
    listAll.append(WikipediaEs())
    listAll.append(WikipediaEu())
    listAll.append(WikipediaFr())
    listAll.append(WikipediaPt())
    listAll.append(Winamp())
    listAll.append(Wishlistr())
    # Issue #115
    #listAll.append(Worldcarfans())
    listAll.append(Wordpress())
    listAll.append(Wykop())

    # X
    listAll.append(Xanga())
    # Issue #120. Temporally deactivated.
    #listAll.append(Xat())
    listAll.append(Xing())
    listAll.append(Xtube())

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

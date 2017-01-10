#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2015-2017 Félix Brezo and Yaiza Rubio
#
#    This program is free software. You can redistribute it and/or modify
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

'''
alias_generator.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2015-2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.  For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2015-2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import json

import osrframework.utils.banner as banner

# GLOBAL OPTIONS
SEPARATORS = ["_", ".", '']
COMMON_WORDS = ["666", "home", "mr", "news",  "official", "real", "xxx"]
LOCALES = ["ar", "en", "es", "fr", "ru"]
LEET_TRANSFORMS = {
    "a" : ["4"],
    "b" : ["8"],
    "e" : ["3"],
    "i" : ["1"],
    "l" : ["l"],
    "o" : ["0"],
    "s" : ["5"],
    "t" : ["7"],
    "z" : ["2"]
}


def main(name = None, surname1 = None, surname2 = None, city = None, country = None, year = None, useNumbers = False, useCommonWords = False, useLeet = False, useLocales = False, extraWords = [] ):
    '''
        Method that generates de given aliases.

        :param args: Options given by parameter

        :return:    Text matching the regular expression provided.
    '''
    # Lowering all the info received
    name = name.lower()
    surname1 = surname1.lower()
    surname2 = surname2.lower()
    year = year.lower()
    country = country.lower()
    city = city.lower()

    # Check if the value provided is a '' string
    if name == '':
        name = None
    if surname1 == '':
        surname1 = None
    if surname2 == '':
        surname2 = None
    if year == '':
        year = None
    if city == '':
        city = None
    if country == '':
        country = None

    print "Generation of new aliases..."

    lista = []

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing


    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2 + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + name + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2 + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + name + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2 + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + name + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + name + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + surname2[0] + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1[0] + "<SEPARATOR>" + surname2 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "<SEPARATOR>" + surname1 + "<SEPARATOR>" + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0:1] + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0:2] + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0:3] + "<SEPARATOR>" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    # AFTER THE CREATION, WE WILL PERFORM ADDITIONAL TRANSFORMATIONS
    # --------------------------------------------------------------

    # Creating the output list
    listaAdditions = []
    listaAdditions += lista

    # Adding common words
    if useCommonWords:
        print "We are in useCommonWords:" + str (useCommonWords)
        for n in lista:
            for w in COMMON_WORDS:
                try:
                    tmp = n + "<SEPARATOR>" + w
                    if tmp not in listaAdditions: listaAdditions.append(tmp)
                except:
                    pass # An element is missing

    # Adding extra words provided by the user
    for n in lista:
        for w in extraWords:
            try:
                tmp = n + "<SEPARATOR>" + w
                if tmp not in listaAdditions: listaAdditions.append(tmp)
            except:
                pass # An element is missing

    # Adding loales
    if useLocales:
        for n in lista:
            for l in LOCALES:
                try:
                    tmp = n + "<SEPARATOR>" + l
                    if tmp not in listaAdditions: listaAdditions.append(tmp)
                except:
                    pass # An element is missing

    # Appending Numbers to the nicks created
    if useNumbers:
        for n in lista:
            for i in range(100):
                try:
                    tmp = n + "<SEPARATOR>" + str(i).rjust(2, "0")
                    if tmp not in listaAdditions: listaAdditions.append(tmp)
                except:
                    pass # An element is missing



    # Appending Numbers to the nicks
    if useLeet:
        for n in lista:
            # This will store the variations of the nicks with all the possible combinations
            possibleChanges = []
            possibleChanges += [n]
            for k in LEET_TRANSFORMS.keys():
                try:
                    # Iterating through the list of possible changes found in the array
                    for change in LEET_TRANSFORMS[k]:
                        # Replacing the option
                        tmp = n.replace(k, change )
                        if tmp not in listaAdditions: listaAdditions.append(tmp)

                        # Applying all the possible changes
                        newAliases = []
                        for f in possibleChanges:
                            newAliases.append( f.replace(k, change ) )

                        # Adding the new changes
                        possibleChanges += newAliases

                except:
                    pass # An element is missing
            # Appending the possible combinations which include ALL the possible leet options
            for changedAll in possibleChanges:
                if changedAll not in listaAdditions: listaAdditions.append(changedAll)

    listaFinal = []

    # REMOVING THE "<SEPARATOR>" TAGS TO GET THE FINAL NICKNAMES
    for s in SEPARATORS:
        for n in listaAdditions:
            try:
                tmp = n.replace("<SEPARATOR>", s)
                lastChar = tmp[-1:]
                # Verifying if the last char is or not one of the separators to remove it
                if not lastChar in SEPARATORS:
                    if tmp not in listaFinal: listaFinal.append(tmp)
            except:
                pass # An element is missing


    # Sorting list
    listaFinal.sort()
    print
    print "Generated nicks:"
    print
    print json.dumps(listaFinal, indent=2, sort_keys=True)
    print
    print "Up to " + str(len(listaFinal)) + " nicks generated:"
    print
    print "Writing the results onto the file: " + args.outputFile
    oF=open(args.outputFile, "w")
    for l in listaFinal:
        oF.write(l+"\n")
    oF.close()

    return listaFinal

if __name__ == "__main__":
    print banner.text

    parser = argparse.ArgumentParser(description='alias_generator.py is a tool that tries to create possible aliases based on the inputs known from a person.', prog='alias_generator.py', epilog="", add_help=False)

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    #general = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-n', '--name', metavar='<NAME>', default=None, action='store', help='Name of the person.', required=False)
    parser.add_argument('-s1', '--surname1', metavar='<SURNAME_1>', default=None, action='store', help='First surname.', required=False)
    parser.add_argument('-s2', '--surname2', metavar='<SURNAME_2>', default=None, action='store', help='Second surname.', required=False)
    parser.add_argument('-c', '--city', metavar='<CITY>', default=None, action='store', help='A city linked to the profile.', required=False)
    parser.add_argument('-C', '--country', metavar='<COUNTRY>', default=None, action='store', help='A country.', required=False)
    parser.add_argument('-y', '--year', metavar='<YEAR>', default=None, action='store', help='Birth year.', required=False)
    parser.add_argument('-o', '--outputFile', metavar='<path_to_output_file>', default="./output.txt", action='store', help='Path to the output file.', required=False)

    # Other options
    groupSquatting = parser.add_argument_group('Profile squatting arguments', 'Showing additional configuration options for this program based on the original -s option in usufy.py.')
    groupSquatting.add_argument('--numbers', default=False, action='store_true', help='Adds numbers at the end of the nicknames.')
    groupSquatting.add_argument('--common_words', default=False, action='store_true', help='Adds some famous words at the end of the nicknames.')
    groupSquatting.add_argument('--leet', default=False, action='store_true', help='Adds the leet mode to change \'a\' by \'4\', \'e\' by \'3\', etc.')
    groupSquatting.add_argument('--locales', default=False, action='store_true', help='Adds ending linked to countries.')
    groupSquatting.add_argument('--extra_words', default=[], action='store', help='Adds new words to the nicknames provided by the user.')

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s '+__version__, help='shows the version of the program and exists.')

    args = parser.parse_args()

    extraWords = args.extra_words

    if args.name == None and args.surname1 == None and args.surname2 == None and args.city == None and args.country == None and args.year == None:
        print "Collecting information about the profile"
        print "----------------------------------------"
        print
        args.name=raw_input("Insert a name: ".ljust(35, " ")).replace(' ','')
        args.surname1=raw_input("Insert the first surname: ".ljust(35, " ")).replace(' ','')
        args.surname2=raw_input("Insert the second surname: ".ljust(35, " ")).replace(' ','')
        args.year=raw_input("Insert a year (e. g.: birthyear): ".ljust(35, " ")).replace(' ','')
        args.city=raw_input("Insert a city: ".ljust(35, " ")).replace(' ','')
        args.country=raw_input("Insert a country: ".ljust(35, " ")).replace(' ','')

        if args.extra_words == []:
            print "Additional transformations to be done"
            print "-------------------------------------"
            print
            inputText=raw_input("Extra words to add (',' separated): ".ljust(35, " ")).replace(' ','')
            extraWords += inputText.lower().split(',')

    lista=[]

    print
    print "-----------"
    print "Input data:"
    print "-----------"
    if args.name != "": print args.name
    if args.surname1 != "": print args.surname1
    if args.surname2 != "": print args.surname2
    if args.year != "": print args.year
    if args.city != "": print args.city
    if args.country != "": print args.country
    print

    main(name = args.name, surname1 = args.surname1, surname2 = args.surname2, city = args.city, country = args.country, year = args.year, useNumbers = args.numbers, useCommonWords = args.common_words, useLeet = args.leet, useLocales = args.locales, extraWords = extraWords )

    print
    print "Did something go wrong? Is a platform reporting false positives? Do you need to integrate a new one?"
    print "Then, place an issue in the Github project: <https://github.com/i3visio/osrframework/issues>."
    print "Note that otherwise, we won't know about it!"
    print

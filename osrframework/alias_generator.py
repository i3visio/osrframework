#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2015-2018 Félix Brezo and Yaiza Rubio
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

import osrframework
import osrframework.utils.banner as banner
import osrframework.utils.general as general

# GLOBAL OPTIONS
SEPARATORS = ["_", ".", '']
COMMON_WORDS = ["666", "home", "mr", "news",  "official", "real", "xxx"]
LOCALES = ["ar", "de", "en", "es", "fr", "ru"]
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


def generate(name=None, surname1=None, surname2=None, city=None, country=None, year=None, useNumbers=False, useCommonWords=False, useLeet=False, useLocales=False, extraWords=[]):
    """
    The method that generates the given aliases.

    It receives several parameters as parsed by this module's `getParser()`.
    Previously referenced as `main`.

    Args:
    -----
        name: String representing the known name of the investigated profile.
        surname1: String representing the first surname of the investigated
            profile.
        surname2: String representing the second surname of the investigated
            profile.
        city: String representing the city where the profile was born or works.
        country: String representing the country.
        year: String representing a year linked to the profile.
        useNumbers: Boolean representing whether to use random numbers.
        useCommonWords: Boolean representing whether to use known commond words
            to generate new nicknames.
        useNumbers: Boolean representing whether to use random numbers.
        useLeet: Boolean representing whether to modify certain letters by
            numbers using the leet (*133t*) codification.
        extraWords: A list of strings with extra words to be appended to the
            generatednicknames.

    Returns
    -------
        list: An ordered list of the nicknames generated.
    """
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

    print("\nGenerating new aliases...")

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
    print("\nProcess finished.")
    print("\nGenerated nicks:\n")
    print(general.success(json.dumps(listaFinal, indent=2, sort_keys=True)))
    print("\nUp to " + general.emphasis(str(len(listaFinal))) + " nicks generated.\n")

    return listaFinal

def getParser():
    parser = argparse.ArgumentParser(description='alias_generator is a tool that tries to create possible aliases based on the inputs known from a person.', prog='alias_generator', epilog="", add_help=False, conflict_handler='resolve')

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
    groupAbout.add_argument('--version', action='version', version='[%(prog)s] OSRFramework '+ osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """
    Main function to launch alias_generator.

    Args:
    -----
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point.
    """
    # Grabbing the parser
    parser = getParser()

    if params != None:
        args = parser.parse_args(params)
    else:
        args = parser.parse_args()

    print(general.title(banner.text))

    extraWords = args.extra_words

    if args.name == None and args.surname1 == None and args.surname2 == None and args.city == None and args.country == None and args.year == None:
        print("\nCollecting information about the profile")
        print("----------------------------------------\n")

        args.name = raw_input(general.emphasis("Insert a name: ".ljust(35, " "))).replace(' ','')
        args.surname1 = raw_input(general.emphasis("Insert the first surname: ".ljust(35, " "))).replace(' ','')
        args.surname2 = raw_input(general.emphasis("Insert the second surname: ".ljust(35, " "))).replace(' ','')
        args.year = raw_input(general.emphasis("Insert a year (e. g.: birthyear): ".ljust(35, " "))).replace(' ','')
        args.city = raw_input(general.emphasis("Insert a city: ".ljust(35, " "))).replace(' ','')
        args.country = raw_input(general.emphasis("Insert a country: ".ljust(35, " "))).replace(' ','')

        if args.extra_words == []:
            print("\nAdditional transformations to be added")
            print("--------------------------------------\n")
            inputText = raw_input(general.emphasis("Extra words to add (',' separated): ".ljust(35, " "))).replace(' ','')
            extraWords += inputText.lower().split(',')

    lista=[]

    print("\nInput data:")
    print("-----------\n")
    if args.name != "":
        print("Name: ".ljust(20, " ") + args.name)
    if args.surname1 != "":
        print("First Surname: ".ljust(20, " ") + args.surname1)
    if args.surname2 != "":
        print("Second Surname: ".ljust(20, " ") + args.surname2)
    if args.year != "":
        print("Year: ".ljust(20, " ") + args.year)
    if args.city != "":
        print("City: ".ljust(20, " ") + args.city)
    if args.country != "":
        print("Country: ".ljust(20, " ") + args.country)

    aliases = generate(
        name=args.name,
        surname1=args.surname1,
        surname2=args.surname2,
        city=args.city,
        country=args.country,
        year=args.year,
        useNumbers=args.numbers,
        useCommonWords=args.common_words,
        useLeet=args.leet,
        useLocales=args.locales,
        extraWords=extraWords
    )

    print("Writing the results onto the file:\n\t" + general.emphasis(args.outputFile))

    oF=open(args.outputFile, "w")
    for l in aliases:
        oF.write(l+"\n")
    oF.close()


    # Urging users to place an issue on Github...
    print(banner.footer)


if __name__ == "__main__":
    main(sys.argv[1:])

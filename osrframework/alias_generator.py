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
import datetime as dt
import json
import sys

import osrframework
import osrframework.utils.banner as banner
import osrframework.utils.general as general



# GLOBAL OPTIONS
SEPARATORS = ["_", ".", '']
COMMON_WORDS = ["666", "home", "dr", "mr", "mrs", "news", "official", "real", "xxx"]
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


def generate(name=None, surname1=None, surname2=None, city=None, country=None,
             year=None, use_numbers=False, use_common_words=False, use_leet=False,
             use_locales=False, extra_words=[]):
    """The method that generates the given aliases.

    It receives several parameters as parsed by this module's `get_parser()`.
    Previously referenced as `main`.

    Args:
        name: String representing the known name of the investigated profile.
        surname1: String representing the first surname of the investigated
            profile.
        surname2: String representing the second surname of the investigated
            profile.
        city: String representing the city where the profile was born or works.
        country: String representing the country.
        year: String representing a year linked to the profile.
        use_numbers: Boolean representing whether to use random numbers.
        use_common_words: Boolean representing whether to use known commond words
            to generate new nicknames.
        use_numbers: Boolean representing whether to use random numbers.
        use_leet: Boolean representing whether to modify certain letters by
            numbers using the leet (*133t*) codification.
        extra_words: A list of strings with extra words to be appended to the
            generatednicknames.

    Returns
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
    lista_additions = []
    lista_additions += lista

    # Adding common words
    if use_common_words:
        for nick in lista:
            for word in COMMON_WORDS:
                try:
                    tmp = f"{nick}<SEPARATOR>{word}"
                    if tmp not in lista_additions: lista_additions.append(tmp)
                    tmp = f"{word}<SEPARATOR>{nick}"
                    if tmp not in lista_additions: lista_additions.append(tmp)
                except Exception:
                    pass # An element is missing

    # Adding extra words provided by the user
    for nick in lista:
        for word in extra_words:
            try:
                tmp = f"{nick}<SEPARATOR>{word}"
                if tmp not in lista_additions: lista_additions.append(tmp)
            except Exception:
                pass # An element is missing

    # Adding loales
    if use_locales:
        for nick in lista:
            for local in LOCALES:
                try:
                    tmp = f"{nick}<SEPARATOR>{local}"
                    if tmp not in lista_additions: lista_additions.append(tmp)
                    tmp = f"{local}<SEPARATOR>{nick}"
                    if tmp not in lista_additions: lista_additions.append(tmp)
                except Exception:
                    pass # An element is missing

    # Appending Numbers to the nicks created
    if use_numbers:
        for nick in lista:
            for i in range(100):
                try:
                    tmp = f"{nick}<SEPARATOR>{str(i).rjust(2, '0')}"
                    if tmp not in lista_additions: lista_additions.append(tmp)
                except Exception:
                    pass # An element is missing

    # Appending Numbers to the nicks
    if use_leet:
        for nick in lista:
            # This will store the variations of the nicks with all the possible combinations
            possible_changes = [nick]
            for key in LEET_TRANSFORMS.keys():
                try:
                    # Iterating through the list of possible changes found in the array
                    for change in LEET_TRANSFORMS[key]:
                        # Replacing the option
                        tmp = nick.replace(key, change)
                        if tmp not in lista_additions: lista_additions.append(tmp)

                        # Applying all the possible changes
                        new_aliases = []
                        for former in possible_changes:
                            new_aliases.append(former.replace(key, change))

                        # Adding the new changes
                        possible_changes += new_aliases
                except Exception:
                    pass # An element is missing
            # Appending the possible combinations which include ALL the possible leet options
            for changed_all in possible_changes:
                if changed_all not in lista_additions: lista_additions.append(changed_all)

    lista_final = []

    # REMOVING THE "<SEPARATOR>" TAGS TO GET THE FINAL NICKNAMES
    for s in SEPARATORS:
        for n in lista_additions:
            try:
                tmp = n.replace("<SEPARATOR>", s)
                last_char = tmp[-1:]
                # Verifying if the last char is or not one of the separators to remove it
                if not last_char in SEPARATORS:
                    if tmp not in lista_final: lista_final.append(tmp)
            except Exception:
                pass # An element is missing


    # Sorting list
    lista_final.sort()
    # Showing the execution time...
    endTime = dt.datetime.now()
    print(f"\n{endTime}\tGeneration finished...\n")

    try:
        print("\nGenerated nicks:\n")
        print(general.success(json.dumps(lista_final, indent=2, sort_keys=True)))
    except UnicodeDecodeError:
        for nick in lista_final:
            print(general.success(nick))
        print(general.warning("\nThe input provided includes a Unicode character. You may try it again without it."))
    print(f"\nUp to {general.emphasis(str(len(lista_final)))} nicks generated.\n")

    return lista_final


def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    parser = argparse.ArgumentParser(description='alias_generator is a tool that tries to create possible aliases based on the inputs known from a person.', prog='alias_generator', epilog="", add_help=False, conflict_handler='resolve')

    # Adding the main options
    # Defining the mutually exclusive group for the main options
    parser.add_argument('-n', '--name', metavar='<NAME>', default=None, action='store', help='Name of the person.', required=False)
    parser.add_argument('-s1', '--surname1', metavar='<SURNAME_1>', default=None, action='store', help='First surname.', required=False)
    parser.add_argument('-s2', '--surname2', metavar='<SURNAME_2>', default=None, action='store', help='Second surname.', required=False)
    parser.add_argument('-c', '--city', metavar='<CITY>', default=None, action='store', help='A city linked to the profile.', required=False)
    parser.add_argument('-C', '--country', metavar='<COUNTRY>', default=None, action='store', help='A country.', required=False)
    parser.add_argument('-y', '--year', metavar='<YEAR>', default=None, action='store', help='Birth year.', required=False)
    parser.add_argument('-o', '--output-file', metavar='<path_to_output_file>', default="./output.txt", action='store', help='Path to the output file.', required=False)

    # Other options
    group_squatting = parser.add_argument_group('Profile squatting arguments', 'Showing additional configuration options for this program based on the original -s option in usufy.py.')
    group_squatting.add_argument('--numbers', default=False, action='store_true', help='Adds numbers at the end of the nicknames.')
    group_squatting.add_argument('--common-words', default=False, action='store_true', help='Adds some famous words at the end of the nicknames.')
    group_squatting.add_argument('--leet', default=False, action='store_true', help='Adds the leet mode to change \'a\' by \'4\', \'e\' by \'3\', etc.')
    group_squatting.add_argument('--locales', default=False, action='store_true', help='Adds ending linked to countries.')
    group_squatting.add_argument('--extra-words', default=[], nargs='+', action='store', help='Adds new words to the nicknames provided by the user.')

    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework '+ osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """Main function to launch alias_generator

    Args:
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point. If it is called by osrf
            the data is already parsed.
    """
    if params is None:
        parser = get_parser()
        args = parser.parse_args(params)
    else:
        args = params

    print(general.title(banner.text))

    extra_words = args.extra_words

    try:
        if args.name is None and args.surname1 is None and args.surname2 is None and args.city is None and args.country is None and args.year is None:
            print("\nCollecting information about the profile")
            print("----------------------------------------\n")

            args.name = input(general.emphasis("Insert a name: ".ljust(35, " "))).replace(' ','')
            args.surname1 = input(general.emphasis("Insert the first surname: ".ljust(35, " "))).replace(' ','')
            args.surname2 = input(general.emphasis("Insert the second surname: ".ljust(35, " "))).replace(' ','')
            args.year = input(general.emphasis("Insert a year (e. g.: birthyear): ".ljust(35, " "))).replace(' ','')
            args.city = input(general.emphasis("Insert a city: ".ljust(35, " "))).replace(' ','')
            args.country = input(general.emphasis("Insert a country: ".ljust(35, " "))).replace(' ','')

            if args.extra_words == []:
                print("\nAdditional transformations to be added")
                print("--------------------------------------\n")
                inputText = input(general.emphasis("Extra words to add (',' separated): ".ljust(35, " "))).replace(' ','')
                splitted = inputText.lower().split(',')
                if len(splitted) == 1 and splitted[0] == '':
                    args.extra_words = []
                else:
                    args.extra_words = splitted

    except KeyboardInterrupt:
        print("\n\nThe user manually aborted the program. Exiting...")
        sys.exit(2)

    lista = []

    print("\nInput data:")
    print("-----------\n")

    input_data = ""
    if args.name:
        input_data += "Name: ".ljust(20, " ") + general.info(args.name) + "\n"
    if args.surname1:
        input_data += "First Surname: ".ljust(20, " ") + general.info(args.surname1) + "\n"
    if args.surname2:
        input_data += "Second Surname: ".ljust(20, " ") + general.info(args.surname2) + "\n"
    if args.year:
        input_data += "Year: ".ljust(20, " ") + general.info(args.year) + "\n"
    if args.city:
        input_data += "City: ".ljust(20, " ") + general.info(args.city) + "\n"
    if args.country:
        input_data += "Country: ".ljust(20, " ") + general.info(args.country) + "\n"
    if args.extra_words:
        extra_words += args.extra_words
        input_data += "Extra words: ".ljust(20, " ") + general.info(" | ".join(extra_words))+ "\n"

    if not input_data:
        print(general.warning("No data provided."))
    else:
        print(input_data)

    aliases = generate(
        name=args.name,
        surname1=args.surname1,
        surname2=args.surname2,
        city=args.city,
        country=args.country,
        year=args.year,
        use_numbers=args.numbers,
        use_common_words=args.common_words,
        use_leet=args.leet,
        use_locales=args.locales,
        extra_words=extra_words
    )

    print("Writing the results onto the file:\n\t" + general.emphasis(args.output_file))

    with open(args.output_file, "w") as file:
        for nick in aliases:
            file.write(f"{nick}\n")

    # Urging users to place an issue on Github...
    print(banner.footer)


if __name__ == "__main__":
    main(sys.argv[1:])

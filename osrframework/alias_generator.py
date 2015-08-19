#!/usr/bin/env python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio
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
alias_generator.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2015
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.  For additional info, visit to <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2015, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3+"
__version__ = "v0.1.1"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse

def main(name = None, surname1 = None, surname2 = None, city = None, country = None, year = None):
    '''
        Method that generates de given aliases.
        
        :param args: Options given by parameter

        :return:    Text matching the regular expression provided.
    '''
    # Check if the value provided is a '' string
    if name == '':
        name = None
    if surname1 == '':
        surname1 = None
    if surname2 == '':
        surname2 = None
    if city == '':
        city = None
    if country == '':
        country = None
    if year == '':
        year = None        
    print "Generation of new aliases..."
    try:
        tmp = name + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2
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
        tmp = name + "." + surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1
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
        tmp = name + surname1[0] + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2 + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + name + country
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
        tmp = name + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + country
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
        tmp = name + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + year
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
        tmp = name + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + city
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + country
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + year
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "." + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "." + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "." + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "." + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "." + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "_" + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + surname2 + "_" + name + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1[0] + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + "_" + surname1[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + surname1 + "_" + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + surname2[0] + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name + surname1 + "_" + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1[0] + surname2 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing

    try:
        tmp = name[0] + "_" + surname1 + "." + year[-2:]
        if tmp not in lista: lista.append(tmp)
    except:
        pass # An element is missing    
   
    print lista

    print "Writing the results onto the file: " + args.outputFile
    oF=open(args.outputFile, "w")
    for l in lista:
        oF.write(l+"\n")
    oF.close()
    
    return lista
    
if __name__ == "__main__":
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
    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s '+__version__, help='shows the version of the program and exists.')

    args = parser.parse_args()    

    if args.name == None and args.surname1 == None and args.surname2 == None and args.city == None and args.country == None and args.year == None:
        args.name=raw_input("Insert a name:\t").replace(' ','')
        args.surname1=raw_input("Insert the first surname:\t").replace(' ','')
        args.surname2=raw_input("Insert the second surname:\t").replace(' ','') 
        args.city=raw_input("Insert a city:\t").replace(' ','') 
        args.country=raw_input("Insert a country:\t").replace(' ','') 
        args.year=raw_input("Insert a year (e. g.: birthyear):\t").replace(' ','') 

    lista=[]

    print
    print "-----------"
    print "Input data:"
    print "-----------"
    if args.name != "": print args.name
    if args.surname1 != "": print args.surname1
    if args.surname2 != "": print args.surname2
    if args.city != "": print args.city
    if args.country != "": print args.country
    if args.year != "": print args.year
    print 
    
    main(name = args.name, surname1 = args.surname1, surname2 = args.surname2, city = args.city, country = args.country, year= args.year)
    

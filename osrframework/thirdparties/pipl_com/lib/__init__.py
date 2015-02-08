# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of OSRFramework.
#
#	OSRFramework is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


import osrframework.utils.logger

# Calling the logger when being imported
osrframework.utils.logger.setupLogger(loggerName="osrframework.thirdparties.pipl_com.lib")


__version__ = '1.0'
"""Python implementation of Pipl's data model.
The data model is basically Record/Person objects (avaialable in 
osrframework.thirdparties.pipl_com.lib.containers) with their source (available in osrframework.thirdparties.pipl_com.lib.source)
and their fields (available in osrframework.thirdparties.pipl_com.lib.fields).
Importing can be done either with:
from osrframework.thirdparties.pipl_com.lib.containers import Record, Person
from osrframework.thirdparties.pipl_com.lib.fields import Name, Address
from osrframework.thirdparties.pipl_com.lib.source import Source
or simply with:
from osrframework.thirdparties.pipl_com.lib import Record, Person, Name, Address, Source
"""
from osrframework.thirdparties.pipl_com.lib.containers import Record, Person
from osrframework.thirdparties.pipl_com.lib.source import Source
from osrframework.thirdparties.pipl_com.lib.fields import *

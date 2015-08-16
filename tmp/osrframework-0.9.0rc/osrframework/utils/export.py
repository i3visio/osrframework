# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
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

# logging imports
import logging


def resultsToCSV(res):
	""" 
		Method to generate the text to be appended to a CSV file.

		:param res:	a dictionary with the information of the profiles
		
		:return:	csvText as the string to be written in a CSV file.				
	"""
	logger = logging.getLogger("osrframework.utils")
	logger.info( "Generating .csv...")
	csvText = "User\tPlatform\tURL\n"
	logger.debug("Going through all the keys in the dictionary...")
	for r in res.keys():
		for p in res[r].keys():
			csvText += str(r) + "\t" + str(p) + "\t" + res[r][p] + "\n" 
	logger.debug("Loading the dictionary onto a csv-style text...")
	return csvText




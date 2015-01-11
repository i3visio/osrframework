# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
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

import json
import sys
import urllib2

from osrframework.maltfy.lib.maltego import *
import osrframework.thirdparties.blockchain_info.getBitcoinAddressDetails as blockchain

def bitcoinAddressToBlockchainDetails(bitcoinAddress=None):
	''' 
		Method that checks if the given bitcoinAddress is stored in the HIBP website.

		:param bitcoinAddress:	bitcoinAddress to verify.

	'''

	jsonData = blockchain.getBitcoinAddressDetails(address=bitcoinAddress)
	
	me = MaltegoTransform()
	
	# Adding the data to the current Bitcoin address
	newEnt = me.addEntity("i3visio.bitcoin.address", bitcoinAddress)
	
	newEnt.setDisplayInformation(json.dumps(jsonData, sort_keys=True, indent=2))
	newEnt.addAdditionalFields("Final balance (nanobitcoins)", "Final balance (nanobitcoins)", True, str(jsonData["final_balance"]))
	newEnt.addAdditionalFields("Total sent (nanobitcoins)", "Total sent (nanobitcoins)", True, str(jsonData["total_sent"]))
	newEnt.addAdditionalFields("Total received (nanobitcoins)", "Total received (nanobitcoins)", True, str(jsonData["total_received"]))
	newEnt.addAdditionalFields("Number of transactions", "Number of transactions", True, str(jsonData["n_tx"]))
	
	# In this case, no new entity is added...
	# newEnt = me.addEntity(<name_of_i3visio_entity>,<value_of_the_entity>)

	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	bitcoinAddressToBlockchainDetails(bitcoinAddress=sys.argv[1])




import json
import sys

import osrframework.entify.processing as entify
import osrframework.maltfy.lib.constants as constants
from osrframework.maltfy.maltego import *
import osrframework.thirdparties.blockchain_info.getBitcoinAddressDetails as blockchain

def extractAllEntitiesFromI3visioText(argv):
	''' 
		Method that obtains all the entities in a given i3visio.Object that contains an i3visio.text property.

		:param argv:	the serialized entity.

		:return:	Nothing is returned but the code of the entities is created.
	'''
	me = MaltegoTransform()
	#me.parseArguments(argv);
	#data = sys.argv[1]

	# Trying to recover all the possible i3visio entities
	found_fields = {}

	#data = me.getVar("i3visio.text")
	data = sys.argv[1]
	entities = entify.getEntitiesByRegexp(data=data)	

	# This returns a dictionary like:
	# {'email': {'reg_exp': ['[a-zA-Z0-9\\.\\-]+@[a-zA-Z0-9\\.\\-]+\\.[a-zA-Z]+'], 'found_exp': ['bar@foo.com', 'foo@bar.com']}}

	#print entities
	#print json.dumps(entities, indent=2)
	for type_regexp in entities:
		for k in type_regexp.keys():
			for element in type_regexp[k]['found_exp']:
				if k == "i3visio.bitcoin.address":
					bitcoinAddress = str(element)
					newEnt = me.addEntity(k,str(element))
					# Looking for information on Blockchain
					jsonData = blockchain.getBitcoinAddressDetails(address=bitcoinAddress)
					# Adding the fields
					newEnt.setDisplayInformation(json.dumps(jsonData, sort_keys=True, indent=2))
					newEnt.addAdditionalFields("Final balance (nanobitcoins)", "Final balance (nanobitcoins)", True, str(jsonData["final_balance"]))
					newEnt.addAdditionalFields("Total sent (nanobitcoins)", "Total sent (nanobitcoins)", True, str(jsonData["total_sent"]))
					newEnt.addAdditionalFields("Total received (nanobitcoins)", "Total received (nanobitcoins)", True, str(jsonData["total_received"]))
					newEnt.addAdditionalFields("Number of transactions", "Number of transactions", True, str(jsonData["n_tx"]))					
				else:
					newEnt = me.addEntity(k,str(element))

	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	extractAllEntitiesFromI3visioText(sys.argv)



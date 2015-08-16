# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import json
import sys
import urllib2

from osrframework.transforms.lib.maltego import *
import osrframework.thirdparties.blockchain_info.getBitcoinAddressDetails as blockchain

def bitcoinAddressToBlockchainDetails(bitcoinAddress=None):
    ''' 
        Method that checks if the given bitcoinAddress is stored in the HIBP website.

        :param bitcoinAddress:    bitcoinAddress to verify.

    '''

    jsonData = blockchain.getBitcoinAddressDetails(address=bitcoinAddress)
    
    me = MaltegoTransform()
    
    newEntities = []
    
    aux = {}
    aux["type"] = "i3visio.bitcoin.address"
    aux["value"] = bitcoinAddress
    aux["attributes"] = []

    att ={}
    att["type"] = "@final_balance"
    att["value"] =  str(jsonData["final_balance"])
    att["attributes"] = []
    aux["attributes"].append(att)
    
    att ={}
    att["type"] = "@number_transactions"
    att["value"] =  str(jsonData["n_tx"])
    att["attributes"] = []
    aux["attributes"].append(att)                   

    att ={}
    att["type"] = "@total_received"
    att["value"] =  str(jsonData["total_received"])
    att["attributes"] = []
    aux["attributes"].append(att)                

    att ={}
    att["type"] = "@total_sent"
    att["value"] =  str(jsonData["total_sent"])
    att["attributes"] = []
    aux["attributes"].append(att)
   
    newEntities.append(aux)
        
    me.addListOfEntities(newEntities)
        
    # Returning the output text...
    me.returnOutput()    

    
if __name__ == "__main__":
    bitcoinAddressToBlockchainDetails(bitcoinAddress=sys.argv[1])



# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
##################################################################################


import hashlib
import json
import datetime
from osrframework.transforms.lib.maltego import MaltegoEntity, MaltegoTransform

import logging

def exportUsufy(data, ext, fileH):
    '''
        Method that exports a Usufy structure onto different formats.
        :param data: Data to export.
        :param ext: One of the following: csv, excel, json, ods.
        :param fileH: Fileheader for the output files.
    '''
    # Selecting the appropriate export function
    if ext == "csv":
        usufyToCsvExport(data, fileH+"."+ext)
    elif ext == "json":
        usufyToJsonExport(data, fileH+"."+ext)
    elif ext == "mtz":
        usufyToMaltegoExport(data, fileH+"."+ext)
    elif ext == "ods":
        usufyToOdsExport(data, fileH+"."+ext)
    elif ext == "txt":
        usufyToTextExport(data, fileH+"."+ext)        
    elif ext == "xls":
        usufyToXlsExport(data, fileH+"."+ext)
    elif ext == "xlsx":
        usufyToXlsxExport(data, fileH+"."+ext)
                
def usufyToJsonExport(d, fPath):
    '''
        Workaround to export to a json file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    jsonText =  json.dumps(d, indent=2, sort_keys=True)
    with open (fPath, "w") as oF:
        oF.write(jsonText)

def usufyToTextExport(d, fPath=None):
    '''
        Workaround to export to a .txt file.
        :param d: Data to export.
        :param fPath: File path. If None was provided, it will assume that it has to print it.
    '''
    import pyexcel as pe
    import pyexcel.ext.text as text    

    if fPath == None:
        isTerminal = True
    else:
        isTerminal = False
        
    try:
        oldData = get_data(fPath)
    except:
        # No information has been recovered
        oldData = {"Usufy sheet":[]}

    # Generating the new tabular data
    tabularData = _generateTabularData(d, {"Usufy sheet":[[]]}, True)
    # The tabular data contains a dict representing the whole book and we need only the sheet!!
    sheet = pe.Sheet(tabularData["Usufy sheet"])
    sheet.name = "Profiles recovered (" + getCurrentStrDatetime() +")."
    # Defining the headers
    sheet.name_columns_by_row(0)
    text.TABLEFMT = "grid" 
    try:
        with open(fPath, "w") as oF:
            oF.write(str(sheet))
    except:
        # If a fPath was not provided... We will only print the info:
        return sheet    


def _generateTabularData(res, oldTabularData = {}, isTerminal=False):
    '''
        Method that recovers the values and columns from the current structure
        This method is used by:
            - usufyToCsvExport
            - usufyToOdsExport
            - usufyToXlsExport
            - usufyToXlsxExport            
        :param res:    new data to export.
        :param oldTabularData:    the previous data stored.     
            {
              "Usufy sheet": [
                [
                  "i3visio.alias", 
                  "i3visio.platform", 
                  "i3visio.uri"
                ], 
                [
                  "i3visio", 
                  "Twitter", 
                  "https://twitter.com/i3visio", 
                ]
              ]
            }           
        :param isTerminal:    if isTerminal is activated, only information related to i3visio.alias, i3visio.platform and i3visio.uri will be displayed in the terminal.    
        :return:
            values, a dictionary containing all the information stored.
            headers, a list containing the headers used for the rows.
            Values is like:            
            {
              "Usufy sheet": [
                [
                  "i3visio.alias", 
                  "i3visio.platform", 
                  "i3visio.uri"
                ], 
                [
                  "i3visio", 
                  "Twitter", 
                  "https://twitter.com/i3visio", 
                ],
                [
                  "i3visio", 
                  "Github", 
                  "https://github.com/i3visio", 
                ]                
              ]
            }
            
    '''
    # Entities allowed for the output in terminal
    allowedInTerminal = ["i3visio.alias", "i3visio.uri", "i3visio.platform", "i3visio.fullname"]
    # Dictionary of profiles found found
    values = {}
    try:
        if not isTerminal:
            # Recovering the headers in the first line of the old Data
            headers = oldTabularData["Usufy sheet"][0]
        else:
            # Recovering only the printable headers if in Terminal mode
            oldHeaders = oldTabularData["Usufy sheet"][0]
            headers = []
            for h in oldHeaders:
                if h in allowedInTerminal:
                    headers.append(h)
    except:
        # No previous files... Easy...
        headers = []

    # We are assuming that we received a list of profiles. 
    for p in res:    
        # Creating the dictionaries
        values[p["value"]] = {}
                
        attributes = p["attributes"]
        # Processing all the attributes found
        for a in attributes:
            # Default behaviour for the output methods
            if not isTerminal:
                values[p["value"]][a["type"]] = a["value"]
                # Appending the column if not already included
                if a["type"] not in headers:
                    headers.append(a["type"])
            # Specific table construction for the terminal output
            else:
                if a["type"] in allowedInTerminal:
                    values[p["value"]][a["type"]] = a["value"]
                    # Appending the column if not already included
                    if str(a["type"]) not in headers:
                        headers.append(str(a["type"]))

    data = {}    
    # Note that each row should be a list!
    workingSheet = []

    # Appending the headers
    workingSheet.append(headers)

    # First, we will iterate through the previously stored values
    try:
        for dataRow in oldTabularData["Usufy sheet"][1:]:
            # Recovering the previous data
            newRow = []
            for cell in dataRow:
                newRow.append(cell)
            
            # Now, we will fill the rest of the cells with "N/A" values
            for i in range(len(headers)-len(dataRow)):
                # Printing a Not Applicable value
                newRow.append("N/A")
                
            # Appending the newRow to the data structure
            workingSheet.append(newRow)
    except:
        # No previous value found!
        pass

    # After having all the previous data stored an updated... We will go through the rest:
    for prof in values.keys():
        # Creating an empty structure
        newRow = []
        for col in headers:
            try:
                newRow.append(str(values[prof][col]))
            except:
                # Printing a Not Applicable value
                newRow.append("N/A")
        # Appending the newRow to the data structure
        workingSheet.append(newRow)

    # Storing the workingSheet onto the data structure to be stored
    data.update({"Usufy sheet": workingSheet})

    return data


def usufyToCsvExport(data, fPath):
    '''
        Workaround to export to a CSV file.
        :param data: Data to export.
        :param fPath: File path.
    '''
    # Dictionary of profiles found found
    values = {}
    headers = ["i3visio.alias"]

    # We are assuming that we received a list of profiles.
    for p in data:    
        alias = p["value"].split(' - ')[-1]
        # Creating the dictionaries
        values[p["value"]] = {}
        values[p["value"]]["i3visio.alias"] = alias
                
        attributes = p["attributes"]
        # Processing all the attributes found
        for a in attributes:
            values[p["value"]][a["type"]] = a["value"]
            # Appending the column if not already included
            if a["type"] not in headers:
                headers.append(a["type"])

    # We are assuming that we received a list of profiles.
    for p in data:    
        alias = p["value"].split(' - ')[-1]
        # Creating the dictionaries
        values[p["value"]] = {}
        values[p["value"]]["i3visio.alias"] = alias
                
        attributes = p["attributes"]
        # Processing all the attributes found
        for a in attributes:
            values[p["value"]][a["type"]] = a["value"]
            # Appending the column if not already included
            if a["type"] not in headers:
                headers.append(a["type"])
    # Generating output   
    csvText = ""
    # Printing the headers
    for col in headers:    
        csvText += col+"\t"
    csvText += "\n"
        
    for prof in values.keys():
        #csvText += alias + "\t"
        for col in headers:
            try:
                csvText += values[prof][col] + "\t"
            except:
                # Printing a Not Applicable value
                #print col
                csvText += "[N/A]\t"
        csvText += "\n"
        
    # Storing the file        
    with open (fPath, "w") as oF:
        oF.write(csvText)    

def usufyToOdsExport(d, fPath):
    '''
        Workaround to export to a .ods file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    from pyexcel_ods import get_data
    try:
        oldData = get_data(fPath)
    except:
        # No information has been recovered
        oldData = {"Usufy sheet":[]}
    
    # Generating the new tabular data
    tabularData = _generateTabularData(d, oldData)

    from pyexcel_ods import save_data
    # Storing the file        
    save_data(fPath, tabularData)    

def usufyToXlsExport(d, fPath):
    '''
        Workaround to export to a .xls file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    from pyexcel_xls import get_data
    try:
        oldData = get_data(fPath)
    except:
        # No information has been recovered
        oldData = {"Usufy sheet":[]}
    
    # Generating the new tabular data
    tabularData = _generateTabularData(d, oldData)
    from pyexcel_xls import save_data
    # Storing the file        
    save_data(fPath, tabularData)

def usufyToXlsxExport(d, fPath):
    '''
        Workaround to export to a .xlsx file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    from pyexcel_xlsx import get_data
    try:
        oldData = get_data(fPath)
    except:
        # No information has been recovered
        oldData = {"Usufy sheet":[]}
    
    # Generating the new tabular data
    tabularData = _generateTabularData(d, oldData)
    
    from pyexcel_xlsx import save_data
    # Storing the file        
    save_data(fPath, tabularData)

def usufyToMaltegoExport(profiles, fPath):
    '''
        Workaround to export to a Maltego file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    me = MaltegoTransform()
    # A dictionary with the structure:

    newEntities = []
    for profile in profiles:
	    # Defining the main entity
        """aux ={}
        aux["type"] = "i3visio.profile"
        aux["value"] =  "Skype - " + str(user["i3visio.alias"])
        aux["attributes"] = []    
                
        # Creation of a temp entity
        aux = {}
        aux["type"] = profile["value"]
        aux["value"] = profile["type"]
        aux["attributes"] = []"""
        newEntities.append(profile)
        
    me.addListOfEntities(newEntities)        
          
    # Storing the file        
    with open (fPath, "w") as oF:
        oF.write(me.getOutput())    

    
def listToMaltego(profiles):
    """ 
        Method to generate the text to be appended to a Maltego file. May need to be revisited.

        :param profiles:    a list of dictionaries with the information of the profiles: {"a_nick": [<list_of_results>]}
                    [
                        {
                          "attributes": [
                            {
                              "attributes": [], 
                              "type": "i3visio.uri", 
                              "value": "http://twitter.com/i3visio"
                            }, 
                            {
                              "attributes": [], 
                              "type": "i3visio.alias", 
                              "value": "i3visio"
                            }, 
                            {
                              "attributes": [], 
                              "type": "i3visio.platform", 
                              "value": "Twitter"
                            }
                          ], 
                          "type": "i3visio.profile", 
                          "value": "Twitter - i3visio"
                        }
                        ,
                        ...
                    ]                    
        
        :return:    maltegoText as the string to be written for a Maltego file.                
    """
    logger = logging.getLogger("osrframework.utils")
    logger.info( "Generating Maltego File...")

    maltegoText = ""
    logger.debug("Going through all the keys in the dictionary...")
    me = MaltegoTransform()
    # A dictionary with the structure:

    newEntities = []
    for profile in profiles:
	    # Defining the main entity
        """aux ={}
        aux["type"] = "i3visio.profile"
        aux["value"] =  "Skype - " + str(user["i3visio.alias"])
        aux["attributes"] = []    
                
        # Creation of a temp entity
        aux = {}
        aux["type"] = profile["value"]
        aux["value"] = profile["type"]
        aux["attributes"] = []"""
        newEntities.append(profile)
        
    me.addListOfEntities(newEntities)        
        
    # Getting the output text
    me.addUIMessage("Process completed!")    
    # Returning the output text...
    me.returnOutput()
    return me.getOutput()

def fileToMD5(filename, block_size=256*128, binary=False):
    '''
        :param filename:    Path to the file.
        :param block_size:    Chunks of suitable size. Block size directly depends on the block size of your filesystem to avoid performances issues. Blocks of 4096 octets (Default NTFS).
        :return:    md5 hash.
    '''
    md5 = hashlib.md5()
    with open(filename,'rb') as f: 
        for chunk in iter(lambda: f.read(block_size), b''): 
             md5.update(chunk)
    if not binary:
        return md5.hexdigest()
    return md5.digest()

def getCurrentStrDatetime():
    '''
        Generating the current Datetime with a given format.

        :return:    strTime
    '''
    # Generating current time
    i = datetime.datetime.now()
    strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
    return strTime
    
def getFilesFromAFolder(path):
    '''
        Getting all the files in a folder.
        
        :param path:    path in which looking for files.
        
        :return:    list of filenames.
    '''
    from os import listdir
    from os.path import isfile, join
    #onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    onlyFiles = []
    for f in listdir(path):
        if isfile(join(path, f)):
            onlyFiles.append(f)
    return onlyFiles
    

################################################################################
################################################################################
################################################################################    
'''

    Kept for legacy reasons to avoid other applications calling these functions to crash
    [TO-DO]
        - Verify full compatibility if these functions are removed
'''
################################################################################
################################################################################
################################################################################
def dictToJson(d):
    '''
        Workaround to convert any dictionary to json text.
        
        :param d:    Dictionary to convert to json.

        :return:    jsonText (string).
    '''
    # creating json
    jsonText =  json.dumps(d, indent=2, sort_keys=True)
    return jsonText

def dictToCSV(profiles):
    '''
        Workaround to convert any dictionary to CSV text.
        
        :param d:    Dictionary to convert to json.

        :return:    jsonText (string).
    '''
    # We are assuming that we received a list of profiles.
    values = {}
    #values['i3visio.profile'] = []
    values['i3visio.alias'] = []
    values['i3visio.platform'] = []    
    values['i3visio.uri'] = []        
    
    for p in profiles:
        #values['i3visio.profile'].append(p['i3visio.profile'])
        attributes = p["attributes"]

        for a in attributes:
            values[a["type"]].append(a["value"])
    
    csvText = ""
    # Printing the headers
    csvText += 'i3visio.alias'+"\t"
    csvText += 'i3visio.platform'+"\t"
    csvText += 'i3visio.uri'+"\n"
    
    # Printing the values
    for i in range(len(values['i3visio.alias'])):
        csvText += values['i3visio.alias'][i]+"\t"
        csvText += values['i3visio.platform'][i]+"\t"
        csvText += values['i3visio.uri'][i]+"\n"
    return csvText
    
    
def _generateTabularDataOld(res, isTerminal=False):
    '''
        Method that recovers the values and columns from the current structure
        This method is used by:
            - usufyToCsvExport
            - usufyToOdsExport
            - usufyToXlsExport
            - usufyToXlsxExport            
        :param res:    the data to export.
        :param isTerminal:    if isTerminal is activated, only information related to i3visio.alias, i3visio.platform and i3visio.uri will be displayed in the terminal.    
        :return:
            values, a dictionary containing all the information stored.
            headers, a list containing the headers used for the rows.
    '''
    # Entities allowed for the output in terminal
    allowedInTerminal = ["i3visio.alias", "i3visio.uri", "i3visio.platform", "i3visio.fullname"]
    # Dictionary of profiles found found
    values = {}
    headers = ["i3visio.alias"]
    # We are assuming that we received a list of profiles. 
    for p in res:    
        #print json.dumps(p, indent=2) 
        # Creating the dictionaries
        values[p["value"]] = {}
                
        attributes = p["attributes"]
        # Processing all the attributes found
        for a in attributes:
            # Default behaviour for the output methods
            if not isTerminal:
                values[p["value"]][a["type"]] = a["value"]
                # Appending the column if not already included
                if a["type"] not in headers:
                    headers.append(a["type"])
            # Specific table construction for the terminal output
            else:
                if a["type"] in allowedInTerminal:
                    values[p["value"]][a["type"]] = a["value"]
                    # Appending the column if not already included
                    if a["type"] not in headers:
                        headers.append(a["type"])                
    # The information is stored as:
    """
        {
            "Sheet 1" : [
                ["value at row 1 col A", "value at row 1 col B"], 
                ["value at row 2 col A", "value at row 2 col B"]
            ],
            "Sheet 2" : [
                ["value at row 1 col A", "value at row 1 col B"], 
                ["value at row 2 col A", "value at row 2 col B"],
                ["value at row 3 col A", "value at row 3 col B"]                
            ]            
        }
    """
    data = {}    
    # Note that each row should be a list!
    workingSheet = []

    # Appending the headers
    workingSheet.append(headers)

    for prof in values.keys():
        # Creating an empty structure
        newRow = []
        for col in headers:
            try:
                newRow.append(values[prof][col])
            except:
                # Printing a Not Applicable value
                newRow.append("N/A")
        # Appending the newRow to the data structure
        workingSheet.append(newRow)
        
    # Storing the workingSheet onto the data structure to be stored
    data.update({"Usufy sheet": workingSheet})
                
    return data    

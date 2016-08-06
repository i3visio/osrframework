# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
import sys
import os
from osrframework.transforms.lib.maltego import MaltegoEntity, MaltegoTransform

import networkx as nx
import logging

def exportUsufy(data, ext, fileH):
    '''
        Method that exports a Usufy structure onto different formats.
        :param data: Data to export.
        :param ext: One of the following: csv, excel, json, ods.
        :param fileH: Fileheader for the output files.
    '''
    # HACK!
    import sys
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")
    # Selecting the appropriate export function
    if ext == "csv":
        usufyToCsvExport(data, fileH+"."+ext)
    elif ext == "gml":
        usufyToGmlExport(data, fileH+"."+ext)
    elif ext == "json":
        usufyToJsonExport(data, fileH+"."+ext)
    elif ext == "mtz":
        usufyToMaltegoExport(data, fileH+"."+ext)
    elif ext == "ods":
        usufyToOdsExport(data, fileH+"."+ext)
    elif ext == "png":
        usufyToPngExport(data, fileH+"."+ext)
    elif ext == "txt":
        usufyToTextExport(data, fileH+"."+ext)
    elif ext == "xls":
        usufyToXlsExport(data, fileH+"."+ext)
    elif ext == "xlsx":
        usufyToXlsxExport(data, fileH+"."+ext)
    # HACK!
    import sys
    reload(sys)
    sys.setdefaultencoding("ascii")

def _generateTabularData(res, oldTabularData = {}, isTerminal=False, canUnicode=True):
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
              "OSRFramework": [
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
        :param canUnicode:      Variable that stores if the printed output can deal with Unicode characters.
        :return:
            values, a dictionary containing all the information stored.
            headers, a list containing the headers used for the rows.
            Values is like:
            {
              "OSRFramework": [
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
    def _grabbingNewHeader(h):
        '''
            Changing the starting @ for a '_' and changing the "i3visio." for "i3visio_". Changed in 0.9.4+.
        '''
        if h[0] == "@":
            h = h.replace("@","_")
        elif "i3visio." in h:
            h = h.replace("i3visio.", "i3visio_")
        return h

    # Entities allowed for the output in terminal
    allowedInTerminal = ["i3visio_alias", "i3visio_uri", "i3visio_platform", "i3visio_email", "i3visio_ipv4", "i3visio_phone", "i3visio_dni", "i3visio_domain"]
    # List of profiles found
    values = {}
    headers = ["_id"]
    try:
        if not isTerminal:
            # Recovering the headers in the first line of the old Data
            headers = oldTabularData["OSRFramework"][0]
        else:
            # Recovering only the printable headers if in Terminal mode
            oldHeaders = oldTabularData["OSRFramework"][0]
            headers = []
            for h in oldHeaders:
                if h == "i3visio_domain" or h == "i3visio.domain":
                    print h
                h = _grabbingNewHeader(h)
                if h in allowedInTerminal:
                    headers.append(h)
        # Changing the starting @ for a '_' and changing the "i3visio." for "i3visio_". Changed in 0.9.4+
        for i, h in enumerate(headers):
            h = _grabbingNewHeader(h)
            # Replacing the header
            headers[i] = h
    except:
        # No previous files... Easy...
        headers = ["_id"]

    # We are assuming that we received a list of profiles.
    for p in res:
        # Creating the dictionaries
        values[p["value"]] = {}
        attributes = p["attributes"]
        # Processing all the attributes found
        for a in attributes:
            # Grabbing the type in the new format
            h = _grabbingNewHeader(a["type"])

            # Default behaviour for the output methods
            if not isTerminal:
                values[p["value"]][h] = a["value"]
                # Appending the column if not already included
                if str(h) not in headers:
                    headers.append(str(h))
            # Specific table construction for the terminal output
            else:
                if h in allowedInTerminal:
                    values[p["value"]][h] = a["value"]
                    # Appending the column if not already included
                    if str(h) not in headers:
                        headers.append(str(h))

    data = {}
    # Note that each row should be a list!
    workingSheet = []

    # Appending the headers
    workingSheet.append(headers)

    # First, we will iterate through the previously stored values
    try:
        for dataRow in oldTabularData["OSRFramework"][1:]:
            # Recovering the previous data
            newRow = []
            for cell in dataRow:
                newRow.append(cell)

            # Now, we will fill the rest of the cells with "N/A" values
            for i in range(len(headers)-len(dataRow)):
                # Printing a Not Applicable value
                newRow.append("[N/A]")

            # Appending the newRow to the data structure
            workingSheet.append(newRow)
    except Exception, e:
        # No previous value found!
        #print str(e)
        pass

    # After having all the previous data stored an updated... We will go through the rest:
    for prof in values.keys():
        # Creating an empty structure
        newRow = []
        for i, col in enumerate(headers):
            try:
                if col == "_id":
                    newRow.append(len(workingSheet))
                else:
                    if canUnicode:
                        newRow.append(unicode(values[prof][col]))
                    else:
                        newRow.append(str(values[prof][col]))
            except UnicodeEncodeError as e:
                # Printing that an error was found
                newRow.append("[WARNING: Unicode Encode]")
            except:
                # Printing that this is not applicable value
                newRow.append("[N/A]")
        # Appending the newRow to the data structure
        workingSheet.append(newRow)

    # Storing the workingSheet onto the data structure to be stored
    data.update({"OSRFramework": workingSheet})

    return data

def usufyToJsonExport(d, fPath):
    '''
        Workaround to export to a json file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    oldData = []
    try:
        with open (fPath) as iF:
            oldText = iF.read()
            if oldText != "":
                oldData = json.loads(oldText)
    except:
        # No file found, so we will create it...
        pass

    jsonText =  json.dumps(oldData+d, indent=2, sort_keys=True)

    with open (fPath, "w") as oF:
        oF.write(jsonText)

def usufyToTextExport(d, fPath=None):
    '''
        Workaround to export to a .txt file.
        :param d: Data to export.
        :param fPath: File path. If None was provided, it will assume that it has to print it.
    '''
    # Manual check...
    if d == []:
        return "+------------------+\n| No data found... |\n+------------------+"

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
        oldData = {"OSRFramework":[]}

    # Generating the new tabular data
    tabularData = _generateTabularData(d, {"OSRFramework":[[]]}, True, canUnicode=False)

    # The tabular data contains a dict representing the whole book and we need only the sheet!!
    sheet = pe.Sheet(tabularData["OSRFramework"])
    sheet.name = "Profiles recovered (" + getCurrentStrDatetime() +")."
    # Defining the headers
    sheet.name_columns_by_row(0)
    text.TABLEFMT = "grid"
    try:
        with open(fPath, "w") as oF:
            oF.write(str(sheet))
    except Exception as e:
        # If a fPath was not provided... We will only print the info:
        return sheet


def usufyToCsvExport(d, fPath):
    '''
        Workaround to export to a CSV file.
        :param d: Data to export.
        :param fPath: File path.
    '''

    from pyexcel_io import get_data
    try:
        oldData = {"OSRFramework": get_data(fPath) }
    except:
        # No information has been recovered
        oldData = {"OSRFramework":[]}

    # Generating the new tabular data.
    tabularData = _generateTabularData(d, oldData)

    from pyexcel_io import save_data
    # Storing the file
    # NOTE: when working with CSV files it is no longer a dict because it is a one-sheet-format
    save_data(fPath, tabularData["OSRFramework"])

def usufyToOdsExport(d, fPath):
    '''
        Workaround to export to a .ods file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    from pyexcel_ods import get_data
    try:
        #oldData = get_data(fPath)
        # A change in the API now returns only an array of arrays if there is only one sheet.
        oldData = {"OSRFramework": get_data(fPath) }
    except:
        # No information has been recovered
        oldData = {"OSRFramework":[]}

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
        #oldData = get_data(fPath)
        # A change in the API now returns only an array of arrays if there is only one sheet.
        oldData = {"OSRFramework": get_data(fPath) }
    except:
        # No information has been recovered
        oldData = {"OSRFramework":[]}

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
        #oldData = get_data(fPath)
        # A change in the API now returns only an array of arrays if there is only one sheet.
        oldData = {"OSRFramework": get_data(fPath) }
    except:
        # No information has been recovered
        oldData = {"OSRFramework":[]}

    # Generating the new tabular data
    tabularData = _generateTabularData(d, oldData)

    from pyexcel_xlsx import save_data
    # Storing the file
    save_data(fPath, tabularData)

def _generateGraphData(data, oldData=nx.Graph()):
    '''
        Processing the data from i3visio structures to generate the nodes and edges of networkx graph library. It will create a new node for each and i3visio.<something> entities while it will add properties for all the attribute starting with "@".

        :param d: The i3visio structures containing a list of
        :param oldData: A graph structure representing the previous information.

        :return: A graph structure representing the updated information.
    '''
    def _addNewNode(ent, g):
        """
            :param ent:   The hi3visio-like entities to be used as the identifier.
                ent = {
                    "value":"i3visio",
                    "type":"i3visio.alias,
                }
            :param g:   The graph in which the entity will be stored.
            :return:    newAtts, newEntties
        """
        # Serialized entity
        serEnt = json.dumps(ent)

        # Calculating the hash
        h = hashlib.new('md5')
        h.update(serEnt)
        hashLabel = h.hexdigest()

        # Adding the node
        g.add_node(hashLabel)

        # Creating the main attributes such as the type and value
        g.node[hashLabel]["type"] = ent["type"]
        try:
            g.node[hashLabel]["value"] = unicode(ent["value"])
        except UnicodeEncodeError as e:
            # Printing that an error was found
            g.node[hashLabel]["value"] = "[WARNING: Unicode Encode]"
        except:
            # Printing that this is not applicable value
            g.node[hashLabel]["value"] = "[N/A]"

        return hashLabel

    def _processAttributes(elems, g):
        """
            :param elems:   List of i3visio-like entities.
            :param g:   The graph in which the entity will be stored.

            :return:    newAtts, newEntities
        """
        # Dict of attributes (to be stored as attributes for the given entity)
        newAtts = {}
        # List of new Entities (to be stored as attributes for the given entity)
        newEntities= []

        for att in elems:
            # If it is an attribute
            if att["type"][0] == "@":
                # Removing the @ and the  _ of the attributes
                attName = str(att["type"][1:]).replace('_', '')
                try:
                    newAtts[attName] = int(att["value"])
                except:
                    newAtts[attName] = att["value"]
            elif att["type"][:8] == "i3visio.":
                # Creating a dict to represent the pair: type, value entity.
                ent = {
                    "value":att["value"],
                    "type":att["type"].replace("i3visio.", "i3visio_"),
                }
                # Appending the new Entity to the entity list
                newEntities.append(ent)

                # Appending the new node
                hashLabel = _addNewNode(ent, g)

                # Make this recursive to link the attributes in each and every att
                newAttsInAttributes, newEntitiesInAttributes = _processAttributes(att["attributes"], g)

                # Updating the attributes to the current entity
                g.node[hashLabel].update(newAttsInAttributes)

                # Creating the edges (the new entities have also been created in the _processAttributes
                for new in newEntitiesInAttributes:
                    graphData.add_edge(hashLabel, json.dumps(new))
                    try:
                        # Here, we would add the properties of the edge
                        #graphData.edge[hashLabel][json.dumps(new)]["@times_seen"] +=1
                        pass
                    except:
                        # If the attribute does not exist, we would initialize it
                        #graphData.edge[hashLabel][json.dumps(new)]["@times_seen"] = 1
                        pass
            else:
                # An unexpected type
                pass

        return newAtts, newEntities

    graphData = oldData
    # Iterating through the results
    for elem in data:
        # Creating a dict to represent the pair: type, value entity.
        ent = {
            "value":elem["value"],
            "type":elem["type"],
        }

        # Appending the new node
        hashLabel = _addNewNode(ent, graphData)

        # Processing the attributes to grab the attributes (starting with "@..." and entities)
        newAtts, newEntities = _processAttributes(elem["attributes"], graphData)

        # Updating the attributes to the current entity
        graphData.node[hashLabel].update(newAtts)

        # Creating the edges (the new entities have also been created in the _processAttributes
        for new in newEntities:
            # Serializing the second entity
            serEnt = json.dumps(new)

            # Calculating the hash of the second entity
            h = hashlib.new('md5')
            h.update(serEnt)
            hashLabelSeconds = h.hexdigest()

            # Adding the edge
            graphData.add_edge(hashLabel, hashLabelSeconds)
            try:
                # Here, we would add the properties of the edge
                #graphData.edge[hashLabel][hashLabelSeconds]["times_seen"] +=1
                pass
            except:
                # If the attribute does not exist, we would initialize it
                #graphData.edge[hashLabel][hashLabelSeconds]["times_seen"] = 1
                pass

    return graphData

def usufyToGmlExport(d, fPath):
    '''
        Workaround to export to a gml file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    # Reading the previous gml file
    try:
        oldData=nx.read_gml(fPath)
    except UnicodeDecodeError as e:
        print "UnicodeDecodeError:\t" + str(e)
        print "Something went wrong when reading the .gml file relating to the decoding of UNICODE."
        import time as time
        fPath+="_" +str(time.time())
        print "To avoid losing data, the output file will be renamed to use the timestamp as:\n" + fPath + "_" + str(time.time())
        print
        # No information has been recovered
        oldData = nx.Graph()
    except Exception as e:
        # No information has been recovered
        oldData = nx.Graph()
    newGraph = _generateGraphData(d, oldData)

    # Writing the gml file
    nx.write_gml(newGraph,fPath)

def usufyToPngExport(d, fPath):
    '''
        Workaround to export to a png file.
        :param d: Data to export.
        :param fPath: File path.
    '''
    newGraph = _generateGraphData(d)

    import matplotlib.pyplot as plt
    # Writing the png file
    nx.draw(newGraph)
    plt.savefig(fPath)

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
    if len(newEntities)<=11:
        me.addUIMessage("All the entities have been displayed!")
    else:
        me.addUIMessage("Ooops! Too many entities to display!")
        me.addUIMessage("The following entities could not be added because of the limits in Maltego Community Edition:\n"+json.dumps(newEntities, indent=2))

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



import webbrowser as wb
import subprocess

def uriToBrowser(uri=None):
    '''
        Method that launches the URI in the default browser of the system. This returns no new entity.

        :param uri:    uri to open.
    '''
    # Temporally deactivating standard ouptut and error:
    #   Source: <https://stackoverflow.com/questions/2323080/how-can-i-disable-the-webbrowser-message-in-python>

    # Cloning stdout (1) and stderr (2)
    savout1 = os.dup(1)
    savout2 = os.dup(2)

    # Closing them
    os.close(1)
    os.close(2)
    os.open(os.devnull, os.O_RDWR)

    try:
        # Opening the Tor URI using onion.cab proxy
        if ".onion" in uri:
            wb.get().open(uri.replace(".onion", ".onion.cab"), new=2)
        else:
            wb.get().open(uri, new=2)
    finally:
        # Reopening them...
        os.dup2(savout1, 1)
        os.dup2(savout2, 2)


def openResultsInBrowser(res):
    print "Opening URIs in the default web browser..."

    for r in res:
        for att in r["attributes"]:
            if att["type"] == "i3visio.uri":
                uriToBrowser(att["value"])

# !/usr/bin/python
# -*- coding: cp1252 -*-
#
################################################################################
#
#    Copyright 2014-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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


import colorama
colorama.init(autoreset=True)
import datetime
import hashlib
import json
import logging
import networkx as nx
import os
import time
import urllib
import webbrowser as wb


LICENSE_URL = "https://www.gnu.org/licenses/agpl-3.0.txt"


def exportUsufy(data, ext, fileH):
    """
    Method that exports the different structures onto different formats.

    Args:
    -----
        data: Data to export.
        ext: One of the following: csv, excel, json, ods.
        fileH: Fileheader for the output files.

    Returns:
    --------
        Performs the export as requested by parameter.
    """
    if ext == "csv":
        usufyToCsvExport(data, fileH+"."+ext)
    elif ext == "gml":
        usufyToGmlExport(data, fileH+"."+ext)
    elif ext == "json":
        usufyToJsonExport(data, fileH+"."+ext)
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


def _generateTabularData(res, oldTabularData = {}, isTerminal=False, canUnicode=True):
    """
    Method that recovers the values and columns from the current structure

    This method is used by:
        - usufyToCsvExport
        - usufyToOdsExport
        - usufyToXlsExport
        - usufyToXlsxExport

    Args:
    -----
        res: New data to export.
        oldTabularData: The previous data stored.
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
        isTerminal: If isTerminal is activated, only information related to
            relevant utils will be shown.
        canUnicode: Variable that stores if the printed output can deal with
            Unicode characters.

    Returns:
    --------
        The values, as a dictionary containing all the information stored.
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
    """
    def _grabbingNewHeader(h):
        """
        Updates the headers to be general.

        Changing the starting @ for a '_' and changing the "i3visio." for
        "i3visio_". Changed in 0.9.4+.

        Args:
        -----
            h: A header to be sanitised.

        Returns:
        --------
            string: The modified header.
        """
        if h[0] == "@":
            h = h.replace("@", "_")
        elif "i3visio." in h:
            h = h.replace("i3visio.", "i3visio_")
        return h

    # Entities allowed for the output in terminal
    allowedInTerminal = [
        "i3visio_alias",
        "i3visio_uri",
        "i3visio_platform",
        "i3visio_email",
        "i3visio_ipv4",
        "i3visio_phone",
        "i3visio_dni",
        "i3visio_domain",
        "i3visio_platform_leaked",
        "_source"
    ]
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
                h = _grabbingNewHeader(h)
                if h in allowedInTerminal:
                    # Set to simplify the table shown in mailfy for leaked platforms
                    if h in ["i3visio_domain", "i3visio_alias"] and "_source" in old_headers:
                        pass
                    else:
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
    """
    Workaround to export to a json file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
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
    """
    Workaround to export to a .txt file or to show the information.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file. If None was provided, it will
            assume that it has to print it.

    Returns:
    --------
        unicode: It sometimes returns a unicode representation of the Sheet
            received.
    """
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
        return unicode(sheet)


def usufyToCsvExport(d, fPath):
    """
    Workaround to export to a CSV file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """

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
    """
    Workaround to export to a .ods file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
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
    """
    Workaround to export to a .xls file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
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
    """
    Workaround to export to a .xlsx file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
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
    """
    Processing the data from i3visio structures to generate nodes and edges

    This function uses the networkx graph library. It will create a new node
    for each and i3visio.<something> entities while it will add properties for
    all the attribute starting with "@".

    Args:
    -----
        d: The i3visio structures containing a list of
        oldData: A graph structure representing the previous information.

    Returns:
    --------
        A graph structure representing the updated information.
    """
    def _addNewNode(ent, g):
        """
            ent:   The hi3visio-like entities to be used as the identifier.
                ent = {
                    "value":"i3visio",
                    "type":"i3visio.alias,
                }
            g:   The graph in which the entity will be stored.
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
        Function that processes a list of elements to obtain new attributes.

        Args:
        -----
            elems: List of i3visio-like entities.
            g: The graph in which the entity will be stored.

        Returns:
        --------
            newAtts: Dict of attributes (to be stored as attributes for the
                given entity).
            newEntities: List of new Entities (to be stored as attributes for
                the given entity).
        """
        newAtts = {}
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
    """
    Workaround to export data to a .gml file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
    # Reading the previous gml file
    try:
        oldData=nx.read_gml(fPath)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:\t" + str(e))
        print("Something went wrong when reading the .gml file relating to the decoding of UNICODE.")
        import time as time
        fPath+="_" +str(time.time())
        print("To avoid losing data, the output file will be renamed to use the timestamp as:\n" + fPath + "_" + str(time.time()))
        print()
        # No information has been recovered
        oldData = nx.Graph()
    except Exception as e:
        # No information has been recovered
        oldData = nx.Graph()

    newGraph = _generateGraphData(d, oldData)

    # Writing the gml file
    nx.write_gml(newGraph,fPath)


def usufyToPngExport(d, fPath):
    """
    Workaround to export to a png file.

    Args:
    -----
        d: Data to export.
        fPath: File path for the output file.
    """
    newGraph = _generateGraphData(d)

    import matplotlib.pyplot as plt
    # Writing the png file
    nx.draw(newGraph)
    plt.savefig(fPath)


def fileToMD5(filename, block_size=256*128, binary=False):
    """
    A function that calculates the MD5 hash of a file.

    Args:
    -----
        filename: Path to the file.
        block_size: Chunks of suitable size. Block size directly depends on
            the block size of your filesystem to avoid performances issues.
            Blocks of 4096 octets (Default NTFS).
        binary: A boolean representing whether the returned info is in binary
            format or not.

    Returns:
    --------
        string: The  MD5 hash of the file.
    """
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
             md5.update(chunk)
    if not binary:
        return md5.hexdigest()
    return md5.digest()


def getCurrentStrDatetime():
    """
    Generating the current Datetime with a given format

    Returns:
    --------
        string: The string of a date.
    """
    # Generating current time
    i = datetime.datetime.now()
    strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
    return strTime


def getFilesFromAFolder(path):
    """
    Getting all the files in a folder.

    Args:
    -----
        path: The path in which looking for the files

    Returns:
    --------
        list: The list of filenames found.
    """
    from os import listdir
    from os.path import isfile, join
    #onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    onlyFiles = []
    for f in listdir(path):
        if isfile(join(path, f)):
            onlyFiles.append(f)
    return onlyFiles


def urisToBrowser(uris=[], autoraise=True):
    """
    Method that launches the URI in the default browser of the system

    This function temporally deactivates the standard ouptut and errors to
    prevent the system to show unwanted messages. This method is based on this
    question from Stackoverflow.
    https://stackoverflow.com/questions/2323080/how-can-i-disable-the-webbrowser-message-in-python

    Args:
    -----
        uri: a list of strings representing the URI to be opened in the browser.
    """

    # Cloning stdout (1) and stderr (2)
    savout1 = os.dup(1)
    savout2 = os.dup(2)

    # Closing them
    os.close(1)
    os.close(2)
    os.open(os.devnull, os.O_RDWR)

    try:
        for uri in uris:
            # Opening the Tor URI using onion.cab proxy
            if ".onion" in uri:
                wb.open(uri.replace(".onion", ".onion.city"), new=2, autoraise=autoraise)
            else:
                wb.open(uri, new=2, autoraise=autoraise)
    finally:
        # Reopening them...
        os.dup2(savout1, 1)
        os.dup2(savout2, 2)


def openResultsInBrowser(res):
    """
    Method that collects the URI from a list of entities and opens them

    Args:
    -----
        res: A list containing several i3visio entities.
    """
    print(emphasis("\n\tOpening URIs in the default web browser..."))

    urisToBrowser(["https://github.com/i3visio/osrframework"], autoraise=False)
    # Waiting 2 seconds to confirm that the browser is opened and prevent the OS from opening several windows
    time.sleep(2)

    uris = []
    for r in res:
        for att in r["attributes"]:
            if att["type"] == "i3visio.uri":
                uris.append(att["value"])

    urisToBrowser(uris)


def colorize(text, messageType=None):
    """
    Function that colorizes a message.

    Args:
    -----
        text: The string to be colorized.
        messageType: Possible options include "ERROR", "WARNING", "SUCCESS",
            "INFO" or "BOLD".

    Returns:
    --------
        string: Colorized if the option is correct, including a tag at the end
            to reset the formatting.
    """
    formattedText = text
    # Set colors
    if "ERROR" in messageType:
        formattedText = colorama.Fore.RED + formattedText
    elif "WARNING" in messageType:
        formattedText = colorama.Fore.YELLOW + formattedText
    elif "SUCCESS" in messageType:
        formattedText = colorama.Fore.GREEN + formattedText
    elif "INFO" in messageType:
        formattedText = colorama.Fore.BLUE + formattedText

    # Set emphashis mode
    if "BOLD" in messageType:
        formattedText = colorama.Style.BRIGHT + formattedText

    return formattedText + colorama.Style.RESET_ALL


def error(text):
    return colorize(text, ["ERROR", "BOLD"])


def warning(text):
    return colorize(text, ["WARNING"])


def success(text):
    return colorize(text, ["SUCCESS", "BOLD"])


def info(text):
    return colorize(text, ["INFO"])


def title(text):
    return colorize(text, ["INFO", "BOLD"])


def emphasis(text):
    return colorize(text, ["BOLD"])


def showLicense():
    """
    Method that prints the license if requested.

    It tries to find the license online and manually download it. This method
    only prints its contents in plain text.
    """
    print("Trying to recover the contents of the license...\n")
    try:
        # Grab the license online and print it.
        text = urllib.urlopen(LICENSE_URL).read()
        print("License retrieved from " + emphasis(LICENSE_URL) + ".")
        raw_input("\n\tPress " + emphasis("<ENTER>") + " to print it.\n")
        print(text)
    except:
        print(warning("The license could not be downloaded and printed."))

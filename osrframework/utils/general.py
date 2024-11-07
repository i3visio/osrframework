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

import datetime
import hashlib
import json
import os
import time
import urllib
import webbrowser as wb

import colorama
colorama.init(autoreset=True)
import networkx as nx
import pandas as pd
import xlwt
from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P
from openpyxl import Workbook
from datetime import datetime

LICENSE_URL = "https://www.gnu.org/licenses/agpl-3.0.txt"


def export_usufy(data, ext, fileH):
    """
    Method that exports the different structures onto different formats.

    Args:
        data: Data to export.
        ext: One of the following: csv, excel, json, ods.
        fileH: Fileheader for the output files.

    Returns:
        Performs the export as requested by parameter.
    """
    if ext == "csv":
        osrf_to_csv_export(data, fileH+"."+ext)
    elif ext == "gml":
        osrf_to_gml_export(data, fileH+"."+ext)
    elif ext == "json":
        osrf_to_json_export(data, fileH+"."+ext)
    elif ext == "ods":
        osrf_to_ods_export(data, fileH+"."+ext)
    elif ext == "png":
        osrf_to_png_export(data, fileH+"."+ext)
    elif ext == "txt":
        osrf_to_text_export(data, fileH+"."+ext)
    elif ext == "xls":
        osrf_to_xls_export(data, fileH+"."+ext)
    elif ext == "xlsx":
        osrf_to_xlsx_export(data, fileH+"."+ext)


def _generate_tabular_data(res, oldtabular_data={}, is_terminal=False):
    """
    Method that recovers the values and columns from the current structure

    This method is used by:
        - osrf_to_csv_export
        - osrf_to_ods_export
        - osrf_to_xls_export
        - osrf_to_xlsx_export

    Args:
        res: New data to export.
        oldtabular_data: The previous data stored.
        {
          "OSRFramework": [
            [
              "com.i3visio.Alias",
              "com.i3visio.Platform",
              "com.i3visio.URI"
            ],
            [
              "i3visio",
              "Twitter",
              "https://twitter.com/i3visio",
            ]
          ]
        }
        is_terminal: If is_terminal is activated, only information related to
            relevant utils will be shown.

    Returns:
        The values, as a dictionary containing all the information stored.
        Values is like:
        {
          "OSRFramework": [
            [
              "com.i3visio.Alias",
              "com.i3visio.Platform",
              "com.i3visio.URI"
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
    def _grabbing_new_header(h):
        """
        Updates the headers to be general.

        Changing the starting @ for a '_'. Changed in 0.9.4+.

        Args:
            h: A header to be sanitised.

        Returns:
            string: The modified header.
        """
        if h[0] == "@":
            h = h.replace("@", "_")
        return h

    # Entities allowed for the output in terminal
    allowed_in_terminal = [
        "com.i3visio.Alias",
        "com.i3visio.URI",
        "com.i3visio.Platform",
        "com.i3visio.Email",
        "com.i3visio.IPv4",
        "com.i3visio.Phone",
        "com.i3visio.DNI",
        "com.i3visio.Domain",
        "com.i3visio.Platform.Leaked",
    ]

    # List of profiles found
    values = {}
    headers = ["_id"]
    try:
        if not is_terminal:
            # Recovering the headers in the first line of the old Data
            headers = oldtabular_data["OSRFramework"][0]
        else:
            # Recovering only the printable headers if in Terminal mode
            old_headers = oldtabular_data["OSRFramework"][0]
            headers = []
            for h in old_headers:
                h = _grabbing_new_header(h)
                if h in allowed_in_terminal:
                    # Set to simplify the table shown in mailfy for leaked platforms
                    if h in ["com.i3visio.Domain", "com.i3visio.Alias"] and "_source" in old_headers:
                        pass
                    else:
                        headers.append(h)

        for i, h in enumerate(headers):
            if h[0] == "@":
                h = h.replace("@", "_")
                # Replacing the header
                headers[i] = h
    except Exception:
        # No previous files... Easy...
        headers = ["_id"]

    # Each result has a list of attributes
    for p in res:
        # Creating the dictionaries
        values[p["value"]] = {}
        attributes = p["attributes"]

        # Processing all the attributes found in the result object
        for a in attributes:
            # Grabbing the type in the new format
            h = _grabbing_new_header(a["type"])

            # Default behaviour for the output methods
            if not is_terminal:
                # Appending the column if not already included
                if h not in headers:
                    headers.append(str(h))
                values[p["value"]][h] = a["value"]
            # Specific table construction for the terminal output
            else:
                if h in allowed_in_terminal:
                    # Appending the column if not already included
                    if str(h) not in headers:
                        headers.append(str(h))
                    values[p["value"]][h] = a["value"]

    data = {}
    # Note that each row should be a list!
    working_sheet = []

    # Appending the headers
    working_sheet.append(headers)

    # First, we will iterate through the previously stored values
    try:
        for data_row in oldtabular_data["OSRFramework"][1:]:
            # Recovering the previous data
            new_row = []
            for cell in data_row:
                new_row.append(cell)

            # Now, we will fill the rest of the cells with "N/A" values
            for i in range(len(headers)-len(data_row)):
                # Printing a Not Applicable value
                new_row.append("[N/A]")

            # Appending the new_row to the data structure
            working_sheet.append(new_row)
    except Exception as e:
        # No previous value found!
        pass

    # After having all the previous data stored and updated... We will go through the rest:
    for prof in values.keys():
        # Creating an empty structure for the new row
        new_row = []
        for i, col in enumerate(headers):
            if col == "_id":
                new_row.append(len(working_sheet))
            else:
                try:
                    new_row.append(values[prof][col])
                except KeyError:
                    new_row.append("N/A")
        # Appending the new_row to the data structure
        working_sheet.append(new_row)

    # Storing the working_sheet onto the data structure to be stored
    data.update({"OSRFramework": working_sheet})

    return data


def osrf_to_json_export(d, file_path):
    """
    Workaround to export to a json file.

    Args:
        d: Data to export.
        file_path: File path for the output file.
    """
    old_data = []
    try:
        with open (file_path) as iF:
            oldText = iF.read()
            if oldText != "":
                old_data = json.loads(oldText)
    except:
        # No file found, so we will create it...
        pass

    jsonText =  json.dumps(old_data+d, indent=2, sort_keys=True)

    with open (file_path, "w") as oF:
        oF.write(jsonText)


def osrf_to_text_export(data, file_path=None):
    """
    Exporta datos a un archivo .txt o muestra la información en formato de tabla.

    Args:
        data (list): Datos a exportar.
        file_path: Ruta del archivo de salida. Si es None, se imprime en lugar de guardarse.

    Returns:
        str: Representación en formato de tabla de los datos, o None si se guarda en archivo.
    """
    if len(data) == 0:
        return "+------------------+\n| No data found... |\n+------------------+"

    # Crear un DataFrame con los datos
    try:
        # Convertir los datos en DataFrame
        df = pd.DataFrame(data)
        
        # Si hay columnas, asignar nombres automáticamente
        if df.empty:
            return "+------------------+\n| No data found... |\n+------------------+"

        # Exportar a archivo o mostrar como texto
        if file_path:
            df.to_csv(file_path, sep="\t", index=False)  # Exportar como texto con tabuladores
            return None
        else:
            return df.to_string(index=False)
    
    except Exception as e:
        return f"Error al exportar datos: {str(e)}"


def osrf_to_csv_export(data, file_path):
    """
    Exporta datos a un archivo CSV.

    Args:
        data (list): Datos a exportar.
        file_path: Ruta del archivo de salida.
    """
    # Crear un DataFrame a partir de los datos
    try:
        df = pd.DataFrame(data)
        
        # Verificar si hay datos en el DataFrame
        if df.empty:
            print("No hay datos para exportar.")
            return

        # Exportar el DataFrame a CSV
        df.to_csv(file_path, index=False)
        print(f"Datos exportados exitosamente a {file_path}")

    except Exception as e:
        print(f"Error al exportar los datos a CSV: {str(e)}")


def osrf_to_ods_export(data, file_path):
    """
    Exporta datos a un archivo .ods.

    Args:
        data (list): Datos a exportar, cada elemento en la lista debe ser una lista de filas.
        file_path: Ruta del archivo de salida.
    """
    # Crear un nuevo documento de hoja de cálculo ODS
    doc = OpenDocumentSpreadsheet()

    # Crear una nueva hoja de datos
    table = Table(name="OSRFramework")

    # Verificar si hay datos para exportar
    if not data:
        print("No hay datos para exportar.")
        return

    # Rellenar la hoja con los datos
    for row_data in data:
        row = TableRow()
        for cell_data in row_data:
            cell = TableCell()
            cell.addElement(P(text=str(cell_data)))
            row.addElement(cell)
        table.addElement(row)

    # Agregar la hoja de datos al documento
    doc.spreadsheet.addElement(table)

    # Guardar el archivo ODS
    doc.save(file_path)
    print(f"Datos exportados exitosamente a {file_path}")


def osrf_to_xls_export(data, file_path):
    """
    Workaround to export to a .xls file.

    Args:
        data (list): Data to export.
        file_path (str): File path for the output file.
    """
    # Crear un libro de Excel y una hoja
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("OSRFramework_" + datetime.now().strftime("%Y-%m-%d"))

    # Agregar encabezados
    headers = data[0].keys() if data else []
    for col, header in enumerate(headers):
        sheet.write(0, col, header)

    # Escribir los datos
    for row, record in enumerate(data, start=1):
        for col, (key, value) in enumerate(record.items()):
            sheet.write(row, col, value)

    # Guardar el archivo .xls
    workbook.save(file_path)


def osrf_to_xlsx_export(data, file_path):
    """
    Workaround to export to a .xlsx file.

    Args:
        data (list): Data to export.
        file_path (str): File path for the output file.
    """
    # Crear un libro de Excel y una hoja
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "OSRFramework_" + datetime.now().strftime("%Y-%m-%d")

    # Agregar encabezados
    headers = data[0].keys() if data else []
    sheet.append(headers)

    # Escribir los datos
    for record in data:
        row = [record.get(header, "") for header in headers]
        sheet.append(row)

    # Guardar el archivo .xlsx
    workbook.save(file_path)


def _generate_graph_data(data, old_data=None):
    """
    Processing the data from i3visio structures to generate nodes and edges.

    This function uses the networkx graph library. It will create a new node
    for each i3visio.<something> entity while adding properties for all attributes
    starting with "@".

    Args:
        data (list): The i3visio structures containing a list of entities.
        old_data: A graph structure representing the previous information.

    Returns:
        A graph structure representing the updated information.
    """
    if old_data is None:
        old_data = nx.Graph()
    
    def _addNewNode(ent, g):
        """
        Wraps the creation of a node.

        Args:
            ent: The hi3visio-like entities to be used as the identifier.
            g:   The graph in which the entity will be stored.

        Returns:
            The label used to represent this element.
        """
        label = str(ent["value"])  # Changed to str for Python 3 compatibility
        g.add_node(label)
        g.nodes[label]["type"] = ent["type"]
        return label

    def _processAttributes(elems, g):
        """
        Processes a list of elements to obtain new attributes.

        Args:
            elems (list): List of i3visio-like entities.
            g: The graph in which the entity will be stored.

        Returns:
            Tuple of (newAtts, newEntities) where:
            newAtts: Dict of attributes.
            newEntities: List of new entities.
        """
        newAtts = {}
        newEntities = []

        for att in elems:
            if att["type"][0] == "@":
                attName = att["type"][1:].replace('_', '')
                try:
                    newAtts[attName] = int(att["value"])
                except ValueError:
                    newAtts[attName] = att["value"]
            elif att["type"][:12] == "i3visio.":
                ent = {
                    "value": att["value"],
                    "type": att["type"],
                }
                newEntities.append(ent)
                hashLabel = _addNewNode(ent, g)
                newAttsInAttributes, newEntitiesInAttributes = _processAttributes(att["attributes"], g)
                g.nodes[hashLabel].update(newAttsInAttributes)
                for new in newEntitiesInAttributes:
                    g.add_edge(hashLabel, json.dumps(new))

        return newAtts, newEntities

    graphData = old_data
    for elem in data:
        ent = {
            "value": elem["value"],
            "type": elem["type"],
        }
        new_node = _addNewNode(ent, graphData)
        newAtts, newEntities = _processAttributes(elem["attributes"], graphData)
        graphData.nodes[new_node].update(newAtts)
        for other_node in newEntities:
            other_node_label = str(other_node["value"])  # Changed to str for Python 3 compatibility
            graphData.add_edge(new_node, other_node_label)

    return graphData


def osrf_to_gml_export(d, file_path):
    """Workaround to export data to a .gml file.

    Args:
        d: Data to export.
        file_path (str): File path for the output file.
    """
    # Reading the previous gml file
    try:
        old_data = nx.read_gml(file_path)
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:\t" + str(e))
        print("Something went wrong when reading the .gml file relating to the decoding of UNICODE.")
        import time as time
        file_path += "_" + str(time.time())
        print("To avoid losing data, the output file will be renamed to use the timestamp as:\n" + file_path + "_" + str(time.time()))
        print()
        # No information has been recovered
        old_data = nx.Graph()
    except Exception as e:
        # No information has been recovered
        old_data = nx.Graph()

    newGraph = _generate_graph_data(d, old_data)

    # Writing the gml file
    nx.write_gml(newGraph,file_path)


def osrf_to_png_export(d, file_path):
    """Workaround to export to a png file.

    Args:
        d: Data to export.
        file_path: File path for the output file.
    """
    newGraph = _generate_graph_data(d)

    import matplotlib.pyplot as plt
    # Writing the png file
    nx.draw(newGraph)
    plt.savefig(file_path)


def fileToMD5(filename, block_size=256*128, binary=False):
    """A function that calculates the MD5 hash of a file.

    Args:
        filename (str): Path to the file.
        block_size (int): Chunks of suitable size. Block size directly depends on
            the block size of your filesystem to avoid performances issues.
            Blocks of 4096 octets (Default NTFS).
        binary (bool): A boolean representing whether the returned info is in binary
            format or not.

    Returns:
        str: The  MD5 hash of the file.
    """
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
             md5.update(chunk)
    if not binary:
        return md5.hexdigest()
    return md5.digest()


def getCurrentStrDatetime():
    """Generating the current Datetime with a given format

    Returns:
        str: The string of a date.
    """
    # Generating current time
    i = datetime.datetime.now()
    strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
    return strTime


def getFilesFromAFolder(path):
    """
    Getting all the files in a folder.

    Args:
        path (str): The path in which looking for the files

    Returns:
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
    """Method that launches the URI in the default browser of the system

    This function temporally deactivates the standard ouptut and errors to
    prevent the system to show unwanted messages. This method is based on this
    question from Stackoverflow.
    https://stackoverflow.com/questions/2323080/how-can-i-disable-the-webbrowser-message-in-python

    Args:
        uri (str): a list of strings representing the URI to be opened in the browser.
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


def open_results_in_browser(res):
    """Method that collects the URI from a list of entities and opens them

    Args:
        res (list): A list containing several i3visio entities.
    """
    print(emphasis("\n\tOpening URIs in the default web browser..."))

    urisToBrowser(["https://github.com/i3visio/osrframework"], autoraise=False)
    # Waiting 2 seconds to confirm that the browser is opened and prevent the OS from opening several windows
    time.sleep(2)

    uris = []
    for r in res:
        for att in r["attributes"]:
            if att["type"] == "com.i3visio.URI":
                uris.append(att["value"])

    urisToBrowser(uris)


def colorize(text, messageType=None):
    """Function that colorizes a message.

    Args:
        text (str): The string to be colorized. If not a string, it is converted.
        messageType (str): Possible options include "ERROR", "WARNING", "SUCCESS",
            "INFO" or "BOLD".

    Returns:
        string: Colorized if the option is correct, including a tag at the end
            to reset the formatting.
    """
    formatted_text = str(text)

    # Set colors
    if "ERROR" in messageType:
        formatted_text = colorama.Fore.RED + formatted_text
    elif "WARNING" in messageType:
        formatted_text = colorama.Fore.YELLOW + formatted_text
    elif "SUCCESS" in messageType:
        formatted_text = colorama.Fore.GREEN + formatted_text
    elif "INFO" in messageType:
        formatted_text = colorama.Fore.BLUE + formatted_text

    # Set emphashis mode
    if "BOLD" in messageType:
        formatted_text = colorama.Style.BRIGHT + formatted_text

    return formatted_text + colorama.Style.RESET_ALL


def error(text):
    """Bolds the given text and uses a red font

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["ERROR", "BOLD"])


def warning(text):
    """Uses an orange font

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["WARNING"])


def success(text):
    """Bolds the given text and uses a green font

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["SUCCESS", "BOLD"])


def info(text):
    """Uses a blue font

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["INFO"])


def title(text):
    """Bolds the given text and uses a blue flont

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["INFO", "BOLD"])


def emphasis(text):
    """Bolds the given text

    Args:
        text (str): Object to be colorized.

    Returns:
        str. Colorized text.
    """
    return colorize(text, ["BOLD"])


def showLicense():
    """Method that prints the license if requested.

    It tries to find the license online and manually download it. This method
    only prints its contents in plain text.
    """
    print("Trying to recover the contents of the license...\n")
    try:
        # Grab the license online and print it.
        text = urllib.urlopen(LICENSE_URL).read()
        print("License retrieved from " + emphasis(LICENSE_URL) + ".")
        input("\n\tPress " + emphasis("<ENTER>") + " to print it.\n")
        print(text)
    except:
        print(warning("The license could not be downloaded and printed."))



def expand_entities_from_email(e):
    """Method that receives an email an creates linked entities

    Args:
        e (str): Email to verify.

    Returns:
        Three different values: email, alias and domain in a list.
    """
    # Grabbing the email
    email = {}
    email["type"] = "com.i3visio.Email"
    email["value"] = e
    email["attributes"] = []

    # Grabbing the alias
    alias = {}
    alias["type"] = "com.i3visio.Alias"
    alias["value"] = e.split("@")[0]
    alias["attributes"] = []

    # Grabbing the domain
    domain= {}
    domain["type"] = "com.i3visio.Domain"
    domain["value"] = e.split("@")[1]
    domain["attributes"] = []

    return [email, alias, domain]

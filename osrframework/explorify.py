#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
##################################################################################

'''
explorify.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2017
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.  For additional info, visit to <http://www.gnu.org/licenses/agpl-3.0.txt>.
'''

__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "AGPLv3+"
__version__ = "v1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import sys
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import PyQt4

import osrframework.utils.configuration as configuration
import osrframework.osrframework_server as osrframework_server


class ServerWrapper(threading.Thread):
    def __init__(self, host="localhost", port=30230):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        osrframework_server.app.run(host=host, port=port, debug=False)

# Starting GUI
def launch_explorify(backend="http://localhost:30230/", maximized=False):
    '''Method that launches a GUI to open the server.
    '''
    app = QApplication(sys.argv)

    # Loading settings
    PyQt4.QtWebKit.QWebSettings.globalSettings()
    settings = PyQt4.QtWebKit.QWebSettings.globalSettings()
    settings.setAttribute(PyQt4.QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
    settings.setAttribute(PyQt4.QtWebKit.QWebSettings.LocalContentCanAccessFileUrls, True)
    settings.setAttribute(PyQt4.QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)
    settings.setAttribute(PyQt4.QtWebKit.QWebSettings.JavascriptCanOpenWindows, True)

    web = QWebView()

    if maximized:
        web.showMaximized()
    else:
        web.setFixedSize(1400, 725)

    web.setWindowTitle('Explorify - A GUI for OSRFramework')

    # Open GUI
    web.load(QUrl(backend))
    web.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("osrframework-server")
    # Capturing errors just in case the option is not found in the configuration
    try:
        host = DEFAULT_VALUES["host"]
    except:
        host = localhost
    try:
        port = int(DEFAULT_VALUES["port"])
    except:
        port = 30230

    parser = argparse.ArgumentParser(description='explorify.py - A tool to explore the data from OSRFramework.', prog='explorify.py', epilog="Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.", add_help=False)
    parser._optionals.title = "Input options (one required)"

    # adding the option
    groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the processing parameters.')
    groupProcessing.add_argument('--host', metavar='<hostname>', default=host, required=False, action='store', help='selecting the host.')
    groupProcessing.add_argument('--port', metavar='<port>', default=port, type=int, required=False, action='store', help='selecting the port.')
    groupProcessing.add_argument('--show_maximized', default=False, required=False, action='store_true', help='choose to be opened maximized.')


    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s '+" " +__version__, help='shows the version of the program and exists.')

    args = parser.parse_args()

    # Starting server
    server = ServerWrapper(
        host=args.host,
        port=args.port
    )
    server.start()

    launch_explorify(backend="http://" + args.host + ":" + str(args.port), maximized=args.show_maximized)

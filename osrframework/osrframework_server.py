#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

__author__ = "Felix Brezo y Yaiza Rubio "
__copyright__ = "Copyright 2015-2017, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "AGPLv3+"
__version__ = "v1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import argparse
import json
import os
import shlex
import sys
import time

# Server code
import flask
from flask import Flask
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from flask import send_file

from werkzeug.utils import secure_filename

# OSRFramework libraries
import osrframework
import osrframework.domainfy as domainfy
import osrframework.entify as entify
import osrframework.mailfy as mailfy
import osrframework.phonefy as phonefy
import osrframework.searchfy as searchfy
import osrframework.usufy as usufy

import osrframework.utils.configuration as configuration
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.updates as updates
import osrframework.utils.general as general


# GLOBAL VARIABLES
# -----------------
# Important notice: this configuration makes STRONGLY UNADVISABLE to deploy this
#   server in a different place to localhost for security reasons.
# Creating the SECRET TOKEN
SECRET_TOKEN = ""
# Temporal data. A dictionary of extensions.
loaded_data = {}
# Data folder
configurationPaths = configuration.getConfigPath()
DATA_FOLDER = configurationPaths["appPathData"]
STATIC_FOLDER = os.path.join(configurationPaths["appPathServer"], "static")
TEMPLATES_FOLDER = os.path.join(configurationPaths["appPathServer"], "templates")
# Header filename
HEADER = "profiles"

# Starting the app
app = Flask(
    __name__,
    static_url_path='',
    static_folder=STATIC_FOLDER,
    template_folder=TEMPLATES_FOLDER
 )

@app.route("/")
def index():
    # Getting the status of the current OSRFramework installation
    try:
        hasUpdates, version = updates.hasUpdatesOnPypi("osrframework")
        if hasUpdates:
            notice = {
                "icon": "warning",
                "message": "OSRFramework's version is " + version + ", but there is a new release on Pypi (" + version + "). We encourage you to upgrade soon!" ,
                "type": "warning"
            }
        else:
            notice = {
                "icon": "thumbs-up",
                "message": "OSRFramework is updated to the latest version (" + version + ").",
                "type": "success"
            }
    except:
        notice = {
            "icon": "close",
            "message": "OSRFramework Server could not get connected to Pypi to find new versions. Current version is: " + str(osrframework.__version__) + ".",
            "type": "error"
        }
    return render_template('home.html', mt_home='class=current', notice=notice)


@app.route("/info")
def getInfo():
    info = {
        "__version__": "OSRFramework " + osrframework.__version__,
        "license": "AGPLv3",
        "server_time": _getServerTime()[1],
        "source_code": "https://github.com/i3visio/osrframework",
    }
    return flask.Response(
        json.dumps(
            info,
            indent=2,
            sort_keys=True
        ),
        status=200,
        mimetype="application/json"
    )


@app.route("/research")
@app.route("/research/<program>")
def research(program=None):
    """Prepare research UI for the main tools in the framework.
    """
    platOptions = platform_selection.getAllPlatformNames(program)

    if not program:
        return render_template('research.html', mt_research='class=current', mr_main='class=current')
    else:
        params = request.args.get('query_text')

        if params != None:
            # We perform an additional check to see if we are receiving an array
            if params[0] == "[":
                # TODO: make it more flexible. This is a workaround to process whois results
                params = params.replace("u'", "")
                params = params.replace("'", "")
                params = params.replace(",", "")
                params = params.replace("[", "")
                params = params.replace("]", "")
            return render_template('research-' + program + '.html', mt_research='class=current', query_text=params, plat_options=platOptions)
        else:
            return render_template('research-' + program + '.html', mt_research='class=current', plat_options=platOptions)


def buildCommandFromParams(program, params):
    strCommand = program + ".py "

    for p in params:
        strCommand += p + " "

    return strCommand

@app.route('/research/<program>', methods=['POST'])
def run(program):
    """Loading OSRFramework output...
    """
    platOptions = platform_selection.getAllPlatformNames(program)

    # Loading the stored global data
    global loaded_data
    global DATA_FOLDER
    output_folder = DATA_FOLDER

    answer = []

    form = request.form

    if "terminal-form" in form.keys():
        strParams = request.form['tex_command']

        # Splitting the query
        params = shlex.split(strParams)

        # Manually adding the data folder if NOT provided
        if "-o " not in strParams:
            params += ["-o", output_folder]

    elif "windowed-form" in form.keys():
        # Manually building params
        params = []

        # Iterating through all the attributes. We will use its name to identify them
        for key in form.keys():
            if key == "tex_query":
                # Adding the queries from the first text file
                if program != "searchfy":
                    params += ["-n"]
                else:
                    params += ["-q"]

                # Splitting the query
                splittedQuery = shlex.split(request.form[key])

                # Adding the parameters
                params += splittedQuery

            elif key == "select_platforms":
                # Adding the parameter depending on the platform
                if program == "domainfy":
                    params += ["-t"]
                elif program == "mailfy":
                    params += ["-d"]
                else:
                    params += ["-p"]

                # This is a MultiDict. We have to ad an iteration
                for pName in form.getlist(key):
                    params += [pName]

            elif "export_" in key:
                params += ["-e"]
                params += [key.split("_")[1]]

            elif key == "open_url":
                params += ["-w"]

            elif key == "tex_filename":
                params += ["-F"]
                params += [request.form[key]]

        params += ["-o", DATA_FOLDER]

    # Selecting the appropriate program
    if program == "domainfy":
        args = domainfy.getParser().parse_args(params)
    elif  program == "entify":
        args = entify.getParser().parse_args(params)
    elif program == "mailfy":
        args = mailfy.getParser().parse_args(params)
    elif program == "phonefy":
        args = phonefy.getParser().parse_args(params)
    elif program == "searchfy":
        args = searchfy.getParser().parse_args(params)
    elif program == "usufy":
        args = usufy.getParser().parse_args(params)

    # Return output. text/html is required for most browsers to show the text
    try:
        answer = runQuery(program=program, args=args)
    except:
        abort(400)

    # Reading CSV
    try:
        with open(os.path.join(args.output_folder, args.file_header + ".csv")) as iF:
            everything = iF.read().splitlines()
            loaded_data["csv"] = ""
            for i, line in enumerate(everything):
                loaded_data["csv"] += line
                # Checking if it is the last line. This is done to avoid extra lines.
                if i+1 != len (everything):
                    loaded_data["csv"] += "\n"
    except:
        pass

    return render_template(
        'research-' + program + '.html',
        mt_research='class=current',
        plat_options=platOptions,
        text_results=general.usufyToTextExport(answer),
        command=buildCommandFromParams(program, params)
    )


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['csv'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/explore", methods=['GET', 'POST'])
def explore():
    # Based on http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
    global loaded_data

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            notice = {
                "icon": "warning",
                "message": "No file was selected." ,
                "type": "warning"
            }
            return render_template('explore.html', mt_explore='class=current', alert=notice)

        # Checking if the file name is permitted
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # TODO: pretty unsafe as it is now
            # Recovering the loaded_data: !
            loaded_data["csv"] = ""
            everything = file.stream.read().splitlines()
            for i, line in enumerate(everything):
                loaded_data["csv"] += line
                # Checking if it is the last line. This is done to avoid extra lines.
                if i+1 != len (everything):
                    loaded_data["csv"] += "\n"
            return render_template('explore.html', mt_explore='class=current', csvData=loaded_data["csv"].decode('utf-8'))
        else:
            notice = {
                "icon": "close",
                "message": "This is not a valid extension. We only support CSV files.",
                "type": "error"
            }
            return render_template('explore.html', mt_explore='class=current', alert=notice)
    else:
        try:
            csvData=loaded_data["csv"].decode('utf-8')
            return render_template(
                'explore.html',
                mt_explore='class=current',
                csvData=csvData
            )
        except:
            return render_template(
                'explore.html',
                mt_explore='class=current'
            )


@app.route("/get_temporal_data/<fileName>")
def get_temporal_data(fileName):
    global loaded_data
    extension = fileName.split('.')[-1]
    if extension in loaded_data.keys():
        return loaded_data[extension]
    else:
        return "No data found."


def runQuery(program, args=[]):
    """Function that wraps the queries.
    """
    # Selecting the appropriate program
    if program == "domainfy":
        answer = domainfy.main(args)
    elif program == "entify":
        answer = entify.main(args)
    elif program == "mailfy":
        answer = mailfy.main(args)
    elif program == "phonefy":
        answer = phonefy.main(args)
    elif program == "searchfy":
        answer = searchfy.main(args)
    elif program == "usufy":
        answer = usufy.main(args)

    # Returning the output
    return answer


# --------------
# API Management
# --------------


@app.route('/api/v1/<command>/<query>')
def api_v1(command, query):
    """Loading API v1.0 executions...
        :param command: the command to be launched.
        :param query: the user name to be searched.

        This application can received a random number set by the administrator
        that may allow the one who performs the query to run code. Use it with
        caution.
    """
    # Splitting the query
    splittedQuery = shlex.split(query)

    # Get info froo OSRFramework configuration files
    if SECRET_TOKEN and SECRET_TOKEN == request.args.get('secret_token'):
        params =  splittedQuery
    else:
        params = [splittedQuery[0]]

    # Selecting the appropriate program
    if  command == "domainfy":
        args = domainfy.getParser().parse_args(['-n'] + params)
    elif  command == "entify":
        args = entify.getParser().parse_args(['-w'] + params)
    elif command == "mailfy":
        args = mailfy.getParser().parse_args(['-n'] + params)
    elif command == "phonefy":
        args = phonefy.getParser().parse_args(['-n'] + params)
    elif command == "searchfy":
        args = searchfy.getParser().parse_args(['-q'] + params)
    elif command == "usufy":
        args = usufy.getParser().parse_args(['-n'] + params)

    answer = runQuery(command, args)
    # Grabbing current Time
    osrfTimestamp, osrfDate = _getServerTime()

    if answer != None:
        return flask.Response(
            json.dumps({
                    "code": 200,
                    "content": answer,
                    'date': osrfDate,
                    "description": "200 OK. The response contains an entity corresponding to the requested resource.",
                    'timestamp': osrfTimestamp
                },
                indent=2,
                sort_keys=True
            ),
            status=200,
            mimetype="application/json"
        )
    else:
        abort(400)


def _getServerTime():
    """Get current time and date.
    """
    t = time.time()
    d = time.ctime(int(time.time()))
    return t, d


# ----------------
# Error Management
# ----------------


@app.errorhandler(400)
def general_error(error):
    """400 Bad Request. The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, too large size, invalid request message framing, or deceptive request routing).
    """
    return render_template(
        'error.html',
        errorCode='400',
        errorDescription="Client Error: 400 Bad Request. The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."
    ), 400


@app.errorhandler(403)
def not_found_error(error):
    """403 Forbidden. The request was a valid request, but the server is refusing to respond to it. The user might be logged in but does not have the necessary permissions for the resource.
    """
    return render_template(
        'error.html',
        errorCode='403',
        errorDescription='Client Error: 403 Forbidden. The request was a valid request, but the server is refusing to respond to it.'
    ), 403


@app.errorhandler(404)
def not_found_error(error):
    """404 Not Found. Thee requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
    """
    return render_template(
        'error.html',
        errorCode='404',
        errorDescription='Client Error: 404 Not Found. The requested resource could not be found but may be available again in the future. Subsequent requests by the client are permissible.',
    ), 404


# --------------
# Launching code
# --------------


if __name__ == "__main__":
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("osrframework-server")

    try:
        SECRET_TOKEN = DEFAULT_VALUES["secret_token"]
    except:
        SECRET_TOKEN = None

    try:
        # TODO: get file path from
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    except:
        app.config['UPLOAD_FOLDER'] = "/home/felix/"

    # Loading the server parser
    parser = argparse.ArgumentParser(
        description='OSRFramework Server - The tool that will start a local server.',
        prog='./osrframework-server.py',
        epilog="Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.",
        add_help=False
    )

    # adding the option
    groupServerConfiguration = parser.add_argument_group('Configuration arguments', 'Configuring the processing parameters.')
    groupServerConfiguration.add_argument('--host', metavar='<IP>', required=False, default=DEFAULT_VALUES["host"], action='store', help='choose the host in which the server will be accesible. If "0.0.0.0" is choosen, the server will be accesible by any remote machine. Use this carefully. Default: localhost.')
    groupServerConfiguration.add_argument('--port', metavar='<PORT>', required=False, default=DEFAULT_VALUES["port"], type=int, action='store', help='choose the port in which the server will be accesible. Use this carefully.')
    groupServerConfiguration.add_argument('--debug', required=False, default=DEFAULT_VALUES["debug"], action='store_true', help='choose whether error messages will be deployed. Do NOT use this for production.')

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s ' + " " + osrframework.__version__, help='shows the version of the program and exists.')

    # Parse args
    args = parser.parse_args()

    print osrframework.utils.banner.text
    print
    # Starting the server
    print "[*] Server started at " + "http://" + args.host + ":" + str(args.port) + "... You can access it in your browser."
    print "[*] Press <Ctrl + C> at any time to stop the server."

    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port
    )

    print "[*] OSRFramework server exited normally."

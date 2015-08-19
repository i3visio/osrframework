# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This file is part of OSRFramework.
#
#    OSRFramework is free software: you can redistribute it and/or modify
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

import logging
import os

def setupLogger(loggerName="osrframework", logFolder="./logs", verbosity=0):
    """ 
        Returns the logger to be used for the whole app. This method may be invoked if required by the launcher to update the verbosity syntax.
    
        :param loggerName:    Name of the package or app that is going to use this logger.
        :param logFolder:    Path to the folder where the information will be logged.
        :param verbosity:    Level of verbosity to be used: 
            - 0:    Only errors.
            - 1:    Standard output.
            - 2:    Verbose level with rich outputs.
            
        :return:    The logger already created.
    """
    logger = logging.getLogger(loggerName)

    # create a logging format
    loginFormat = '%(asctime)s [%(filename)s] - %(levelname)s:\n\t%(message)s\n'

    formatter = logging.Formatter(loginFormat)

    # first, defining the type of standard output and verbosity 
    if verbosity == 0:
        logging.basicConfig(level=logging.ERROR, format=loginFormat)
    elif verbosity == 1:
        logging.basicConfig(level=logging.INFO, format=loginFormat)
    elif verbosity == 2:
        logging.basicConfig(level=logging.DEBUG, format=loginFormat)

    # trying to store the logfile
    try:
        # verifying if the logs folder exist
        logFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), logFolder)
        if not os.path.exists(logFolder):
            os.makedirs(logFolder)
        # create a file handler
        logFile = os.path.join(logFolder, loggerName+".log")
    
        # This adds a handler to write on a file
        handler = logging.FileHandler(logFile)
        handler.setLevel(logging.DEBUG)
        formatterLogFile = logging.Formatter(loginFormat)
        handler.setFormatter(formatterLogFile)
    
        # add the handlers to the logger
        logger.addHandler(handler)
    except:
        logger.warning("The log file could not be created. No log will be stored for this session.")

    # Notifying correctly import
    #logger.debug(loggerName+ " successfully imported.")
    return logger

# -*- coding: cp1252 -*-
#
##################################################################################
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

import os
import random
import re

from osrframework.utils.browser import Browser
from osrframework.utils.credentials import Credential
import osrframework.utils.general as general
import osrframework.entify.processing as entify

# logging imports
import logging


class Platform():
    ''' 
        <Platform> class.
    '''
    def __init__(self):
        ''' 
            Constructor without parameters...
        '''
        pass

    def __init__(self, pName, tags, url, notFT, forChars, sco):
        ''' 
            Constructor with parameters. This method permits the developer to instantiate dinamically Platform objects.
        '''
        self.platformName = pName
        # These tags will be the one used to label this platform
        self.tags = tags
        # CONSTANT OF TEXT TO REPLACE
        self.NICK_WILDCARD = "HERE_GOES_THE_NICK"
        # Usually it will contain a phrase like  \"<HERE_GOES_THE_NICK>\" that will be the place where the nick will be included
        self.url = url
        # Text to find when the user was NOT found
        self.notFoundText = notFT
        # List of forbidden characters in this platform
        self.forbiddenList = forChars

        # TO-DO:
        #    self.credentials will be an optional parameter that includes a list of Credentials files
        self.creds = []

        # Delimiters of the current platform:
        self.fieldDelimiters = {}
        # Examples:
        # self.fieldDelimiters["name"] = {"start": "<person>", "end": "</person>"}
        # self.fieldDelimiters["email"] = {"start": "<email>", "end": "</email>"}

        # Ffields found. This attribute will be feeded when running the program.
        self.foundFields = {}
        
    def __str__(self):
        ''' 
            Función para obtener el texto que se representará a la hora de imprimir el objeto.
            
            :return:    self.platformName
        '''
        return self.platformName    
        
    def _genURL(self, nick):
        '''    
            Private method that returns an URL for a given nick. 
            :param nick:            

            :return:    string containing a URL
        '''
        return self.url.replace(self.NICK_WILDCARD, nick)

    def _genURLEnum(self, id):
        '''    
            Private method that returns an URL for a given id. 
            :param id:    is an int value.

            :return:    string containing a URL
        '''
        return self.urlEnumeration.replace("<HERE_GOES_THE_USER_ID>", str(id))        
        
    def _getAuthenticated(self, i3Browser):
        ''' 
            Getting authenticated. This method will be overwritten.
        '''
        # check if we have creds
        if len(self.creds) > 0:
            # choosing a cred
            c = random.choice(self.creds)
            #print url, c.user, c.password
            # adding the credential
            i3Browser.setNewPassword(url, c.user, c.password)

            # Finishing the authentication
            # [TO-DO]
            return False
        else:
            logger.debug("No credentials have been added and this platform needs them.")
            return False

    def _doesTheUserExist(self, html):
        ''' 
            Method that performs the verification of the existence or not of a given profile. This method may be rewrritten.
            
            :param html:    The html text in which the self.notFoundText
            :return :   None if the user was not found in the html text and the html text if the user DOES exist.            
        '''
        for t in self.notFoundText:
            if t in html:
                return None
        return html
        
    def _getResourceFromUser(self, url):
        ''' 
            Este método privado de la clase padre puede ser sobreescrito por cada clase hija si la verificación
            a realizar es más compleja que la verificación estándar.

            Valores retornados:
                html    Si el usuario en cuestión existe en esta red social.
                None    Si el usuario en cuestión no existe en esta red social.
        '''
        logger = logging.getLogger("osrframework.wrappers")
        
        logger.debug("Trying to recover the url: " + url)
        i3Browser = Browser()
        try:
            # check if it needs creds
            if self.needsCredentials():
                
                logger.debug("Trying to get authenticated in " + str(self) + "...")
                authenticated = self._getAuthenticated(i3Browser)
                if authenticated:
                    logger.debug("Recovering the targetted url (authenticated)...")
                    html = i3Browser.recoverURL(url)        
                else:
                    logger.debug("Something happened when trying to get authenticated... ")
                    return None
            else:
                
                logger.debug("Recovering the targetted url...")

                html = i3Browser.recoverURL(url)
                
        except :
            # no se ha conseguido retornar una URL de perfil, por lo que se devuelve None
            logger.debug("Something happened when trying to recover the resource... No file will be returned.")
            
            return None
        
        if self._doesTheUserExist(html):
            logger.debug("The key text has NOT been found in the downloaded file. The profile DOES exist and the html is returned.")
            
            return html
        else:
            # Returning that it does not exist
            logger.debug("The key text has been found in the downloaded file. The profile does NOT exist.")
            
            return None
        
    def _isValidUser(self, nick):
        '''    
            Method to verify if a given nick is processable by the platform. The system looks for the forbidden characters in self.Forbidden list.
            :param nick:

            :return:    True | False
        '''
        for letter in self.forbiddenList:
            if letter in nick:
                return False
        return True        

    def cleanFoundFields(self):
        ''' 
            Method that cleans up the fields recovered.
            
            [TO-DO]
        '''
        pass        
    
    def _getUserIdList(self, platformFolder, action):
        '''
        '''
        listUserId = []
        if not os.path.exists(platformFolder):
            # the platform is being created
            os.makedirs(platformFolder)        
            listUserId = range(self.iNumber, self.fNumber+1)
        else:
            folder = os.path.join(platformFolder, "raw")
            if not os.path.exists(folder):
                listUserId = range(self.iNumber, self.fNumber+1)
            else:                
                if action == "start":
                    # restarting the enumeration from the very beginning
                    listUserId = range(self.iNumber, self.fNumber+1)
                elif action == "update":
                    # Grabbing the list of already processed ids
                    filenames = general.getFilesFromAFolder(folder)
                    for f in filenames:
                        # extracting the "1" from 1_platform_date.html
                        id = f.split('_')[0]
                        listUserId.append(id)
                        # extracting the user id and appending
                        #id = int(cabecera.split('-')[1])
                        #if id not in listUserId:
                        #    listUserId.append(id)
                    lastIndex = listUserId[len(listUserId) - 1]
                    # appending 1% new possible indexes
                    for i in range(lastIndex, lastIndex+(lastIndex/100)):
                        listUserId.append(i)                        
        return listUserId
    
    """def collectProfiles(self, outputFolder= None, avoidProcessing = False, avoidDownload = False, action = "start"):
        '''
            Method that performs the user enumeration tasks
            
            :param outputFolder:    local file where saving the obtained information.
            :param avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).
            :param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).

            :return:    number of profiles processed
        '''
        logger = logging.getLogger("osrframework.wrappers")
        foundUsers = 0
        try:
            if not os.path.exists(outputFolder):
                os.makedirs(outputFolder)
            # Generating the raw output file
            platformFolder = os.path.join(outputFolder, str(self))
            
            listUserId = self._getUserIdList(platformFolder, action)
            
            # action:    start or update
            if action == "start" or action == "update":
                listUserId = self._getUserIdList(platformFolder, action)
                print "The system will try to look for " + str(len(listUserId)) + " user ids..."
                #logger.info("The system will try to look for " + str(len(listUserId)) + " user ids...")
                for id in listUserId:
                    urlEnum = self._genURLEnum(id)
                    html = self._getResourceFromUser(urlEnum)

                    if html != None:
                        # Generating current time
                        strTime = general.getCurrentStrDatetime()
                        if not avoidDownload:
                            # Storing file if the user has NOT said to avoid the process...    
                            logger.info("Storing the file...")    
                            # Generating the raw output folder
                            rawFolder = os.path.join(platformFolder, "raw")
                            if not os.path.exists(rawFolder):
                                os.makedirs(rawFolder)
                                
                            # Obtaining the rawFilename
                            rawFilename = os.path.join( rawFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".html")
                            print rawFilename
                            logger.debug("Writing file: " + rawFilename)
                            with open (rawFilename, "w") as oF:
                                oF.write(html)
                            logger.debug("File saved: " + rawFilename)
                            
                            # Calculating md5 and update raw and processed history
                            rawHistoryName = os.path.join( platformFolder, "history_raw.csv" )
                            with open (rawHistoryName, "a") as oF:
                                oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
                                
                        if not avoidProcessing:
                        
                            # Recovering the processed data
                            logger.info("Processing user #" + str(id))
                            res = self.processProfile(info=html, url=urlEnum)
                            
                            # Generating the proc output folder
                            procFolder = os.path.join(platformFolder, "proc")
                            if not os.path.exists(procFolder):
                                os.makedirs(procFolder)
                                
                            # Obtaining the procFilename
                            procFilename = os.path.join( procFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".json")
                            
                            logger.debug("Writing file: " + procFilename)
                            with open (procFilename, "w") as oF:
                                oF.write(res)
                            logger.debug("File saved: " + procFilename)
                            
                            # Calculating md5 and update the processed history
                            procHistoryName = os.path.join( platformFolder, "history_proc.csv" )
                            with open (procHistoryName, "a") as oF:
                                oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
                        foundUsers+=1
                    else:
                        #    raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
                        #    return None
                        logger.debug("User not found...")    
                        pass
            # action:    legacy
            else:
                # mode to recover html already downloaded
                legacyFolder = os.path.join(platformFolder, "legacy")
                # Grabbing the list of already processed ids
                filenames = general.getFilesFromAFolder(legacyFolder)
                for f in filenames:
                    id =  f.split('.')[0]
                    # opening file
                    html = ""
                    legacyFilename = os.path.join(legacyFolder, f)
                    with open(legacyFilename, 'r') as iF:
                        html = iF.read()
                    # Generating current time
                    strTime = general.getCurrentStrDatetime()
                    if not avoidDownload:
                        # Storing file if the user has NOT said to avoid the process...    
                        logger.debug("Storing user #" + str(id))
                        
                        # Generating the raw output folder if it does NOT exist
                        rawFolder = os.path.join(platformFolder, "raw")
                        if not os.path.exists(rawFolder):
                            os.makedirs(rawFolder)
                        
                        # Obtaining the rawFilename
                        rawFilename = os.path.join( rawFolder, id + "_" + str(self).lower() + "_" + strTime + ".html")
                        
                        # Writing the raw file
                        logger.debug("Writing file: " + rawFilename)
                        with open (rawFilename, "w") as oF:
                            oF.write(html)
                        logger.debug("File saved: " + rawFilename)
                        
                        # Calculating md5 and update raw and processed history
                        rawHistoryName = os.path.join( platformFolder, "history_raw.csv" )
                        
                        # Calculating md5 and update the raw history                        
                        with open (rawHistoryName, "a") as oF:
                            oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
                        
                    if not avoidProcessing:
                        # Recovering the processed data
                        logger.debug("Processing user #" + str(id))
                        urlEnum = self._genURLEnum(id)
                        res = self.processProfile(info=html, url=urlEnum)
    
                        # Generating the proc output folder
                        procFolder = os.path.join(platformFolder, "proc")
                        if not os.path.exists(procFolder):
                            os.makedirs(procFolder)
                            
                        # Obtaining the procFilename
                        procFilename = os.path.join( procFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".json")
                        
                        # Writing the proc file
                        logger.debug("Writing file: " + procFilename)
                        with open (procFilename, "w") as oF:
                            oF.write(res)
                        logger.debug("File saved: " + procFilename)
                        
                        # Calculating md5 and update the processed history
                        procHistoryName = os.path.join( platformFolder, "history_proc.csv" )
                        with open (procHistoryName, "a") as oF:
                            oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
                    foundUsers+=1
                
            return foundUsers
        except:
            pass
        pass
    """
    
    def getUserPage(self, nick, outputF="./", avoidProcessing=False, avoidDownload = False):
        ''' 
            This public method is in charge of recovering the information from the user profile.
            
            List of parameters used by this method:
            :param nick:        nick to search
            :param outputF:        will contain a valid path to the outputFolder
            :param avoidProcessing:boolean var that defines whether the profiles will NOT be processed .
            :param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded.
            :return:
                url    URL del usuario en cuestión una vez que se haya confirmado su validez.
                None    En el caso de que no se haya podido obtener una URL válida.
        '''
        logger = logging.getLogger("osrframework.wrappers")
        
        # Verifying if the nick is a correct nick
        if self._isValidUser(nick):
            logger.debug("Generating a URL...")
            url = self._genURL(nick)    
            
            # en función de la respuesta, se hace la comprobación de si el perfil existe o no
            html = self._getResourceFromUser(url) 
            
            if html != None:
                # Generating current time
                strTime = general.getCurrentStrDatetime()

                outputPath = os.path.join(outputF, nick)
                if not os.path.exists(outputPath):
                    os.makedirs(outputPath)
                if not avoidDownload:
                    # Storing file if the user has NOT said to avoid the process...    
                    logger.info("Storing the file...")    

                    # Generating the raw folder
                    rawFolder = os.path.join(outputPath, "raw")
                    if not os.path.exists(rawFolder):
                        os.makedirs(rawFolder)
                    
                    # Obtaining the rawFilename
                    rawFilename = os.path.join( rawFolder, nick + "_" + str(self).lower() + "_" + strTime + ".html")
                    # Writing the raw file
                    logger.debug("Writing file: " + rawFilename)
                    with open (rawFilename, "w") as oF:
                        oF.write(html)
                    logger.debug("File saved: " + rawFilename)
                    
                    # Calculating md5 and update raw history
                    rawHistoryName = os.path.join( outputPath, "history_raw.csv" )
                    logger.debug("Updating history file: " + rawHistoryName)
                    with open (rawHistoryName, "a") as oF:
                        oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
                    
                if not avoidProcessing:
                    # Generating the proc output folder
                    procFolder = os.path.join(outputPath, "proc")
                    if not os.path.exists(procFolder):
                        os.makedirs(procFolder)
                    
                    # Obtaining the procFilename
                    procFilename = os.path.join( procFolder, nick + "_" + str(self).lower() + "_" + strTime + ".json")
                    # Recovering the processed data
                    res = self.processProfile(info=html, nick=nick, url=url)        
                    
                    # Writing the proc file
                    logger.debug("Writing file: " + procFilename)
                    
                    with open (procFilename, "w") as oF:
                        oF.write(general.dictToJson(res))
                    logger.debug("File saved: " + procFilename)
                    
                    # Calculating md5 and update raw history
                    procHistoryName = os.path.join( outputPath, "history_proc.csv" )
                    logger.debug("Updating history file: " + procHistoryName)
                    with open (procHistoryName, "a") as oF:
                        oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
                    return res
            else:
            #    raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
                logger.debug("The user was NOT found.")
                return None
        else:
            # the user is not a valid one
            logger.debug((str(self) + ":").ljust(18, ' ') + "The user '" + nick + "' will not be processed in this platform." )
            return None

    def needsCredentials(self):
        ''' 
            Returns if it needsCredentials.
            IT captures the exception if the option does not exist. This way we do not have to recode all the platforms
        '''
        try:
            return self._needsCredentials        
        except:
            return False    

    
    def processProfile(self, info=None, nick=None, url=None):
        '''    
            Method to process an URL depending on the functioning of the site. By default, it stores the html downloaded on a file.
            This method might be overwritten by each and every class to perform different actions such as indexing the contents with tools like pysolr, for example.
            
            Example:
            {
                {
                    "type": "i3visio.alias",
                    "value": "febrezo",
                    "atributtes": [{
                        "type": "i3visio.url",
                        "value": "http://twitter.com/febrezo",
                        "atributtes": [{
                            "type": "i3visio.platform",
                            "value": "Twitter",
                            "atributtes": [],
                        }, ]
                    }, {
                        "type": "i3visio.url",
                        "value": "http://facebook.com/febrezo",
                        "atributtes": [{
                            "type": "i3visio.platform",
                            "value": "Facebook",
                            "atributtes": [],
                        }]
                    }, ]
                }, {
                    "type": "i3visio.alias",
                    "value": "i3visio",
                    "atributtes": [{
                        "type": "i3visio.url",
                        "value": "http://twitter.com/i3visio",
                        "atributtes": [{
                            "type": "i3visio.platform",
                            "value": "Twitter",
                            "atributtes": [],
                        }, ]
                    }, ]
                }
            }

            :return:     json text to be stored on a processed file.
        '''
        def escapingSpecialCharacters(aux):
            '''
            '''
            return aux
            escapingValues = ['(', ')', '[', ']', '-', '\\',]
            
            for esc in escapingValues:
                aux = aux.replace(esc, "\\" + esc)
            return aux
        
        def cleanSpecialChars(auxList):
            '''
            '''
            final = []
            cleaningChars = ["\n", "\t", "\r"]
            for elem in auxList:                
                for c in cleaningChars:
                    elem = elem.replace(c, '')
                # Deleting html tags from in between and putting an space instead
                elem = re.sub(r'<.+?>', ' ', elem)
                final.append(elem)
            return final


        logger = logging.getLogger("osrframework.wrappers")
        try:
            # Setting the profile
            self.foundFields["type"] = "i3visio.profile"
            self.foundFields["value"] = self.platformName + " - " + nick
            self.foundFields["attributes"] = []        
            
            # May be revisited in the future so as to add any additional check of whether the profile is correct.
            # Define an attribute for the uri
            aux_att = {}
            aux_att["type"] = "i3visio.uri"
            aux_att["value"] = url
            aux_att["attributes"] = []
            self.foundFields.append(aux_att)
            
            # Define an attribute for the alias
            aux_att = {}
            aux_att["type"] = "i3visio.alias"
            aux_att["value"] = nick
            aux_att["attributes"] = []
            self.foundFields.append(aux_att)
                        
            # Define an attribute for the platforms
            aux_att = {}
            aux_att["type"] = "i3visio.platform"
            aux_att["value"] = self.platformName
            aux_att["attributes"] = []
            self.foundFields.append(aux_att)
                        
            # TO-DO:
            # Looking for regular expressions in the profiles if requested
            #if getRegexp:
            #    self.foundFields += entify.getEntitiesByRegexp(data=info)
            
            # TO-DO:
            #print "Fields to check:\t" + str(self.fieldDelimiters.keys())
            # Going through all the possible fields for the platform
            # TO-DO: UPDATE THIS PART TO INCLUDE THE FOUND FIELDS AS ATTRIBUTES
            #for field in self.fieldDelimiters.keys():
            #    #print "-------------------"
            #    #print field
            #    delimiters = self.fieldDelimiters[field]
            #    start = escapingSpecialCharacters(delimiters["start"])
            #    end = escapingSpecialCharacters(delimiters["end"])
            #    # Example: 
            #    #    a = "blablablabalbal<person>James</person> asdadsasdasd <person>John</person>asdasd"
            #    #     values = re.findall("<person>(.*?)</person>", a)
            #    #    (result): ['James', 'John']
            #    #print "Regexp:\t" + start + "(.*?)" + end
            #    # re.DOTALL matches with the . any field including \n
            #    values = re.findall(start + "(.*?)" + end, info, re.DOTALL)
            #    #print "Values:\t" + str(values)
            #    # If something has been found, we store the fields
            #    if len(values) > 0:
            #        self.foundFields[field] = cleanSpecialChars(values)
            
            # Method that parametrised each and every field depending on its characteristics.
            #    This method WILL BE overwritten in each child class. By default, it does NOTHING
            #self.cleanFoundFields()
            
            #print general.dictToJson(self.foundFields)
            #return general.dictToJson(self.foundFields)
            return self.foundFields
        except:
            logger.debug("Something happened when processing " + str(self) + "... Are self.foundFields or self.fieldDelimiters defined?")
            # May be revisited in the future so as to add any additional check of whether the profile is correct.
            # Adding the basic values
            # Setting the profile
            aux = {}
            aux["type"] = "i3visio.profile"
            aux["value"] = self.platformName + " - " + nick
            aux["attributes"] = []        
            
            # May be revisited in the future so as to add any additional check of whether the profile is correct.
            # Define an attribute for the uri
            aux_att = {}
            aux_att["type"] = "i3visio.uri"
            aux_att["value"] = url
            aux_att["attributes"] = []
            aux["attributes"].append(aux_att)
            
            # Define an attribute for the alias
            aux_att = {}
            aux_att["type"] = "i3visio.alias"
            aux_att["value"] = nick
            aux_att["attributes"] = []
            aux["attributes"].append(aux_att)
                        
            # Define an attribute for the platforms
            aux_att = {}
            aux_att["type"] = "i3visio.platform"
            aux_att["value"] = self.platformName
            aux_att["attributes"] = []
            aux["attributes"].append(aux_att)
            return aux
            
    def setCredentials(self, creds):
        ''' 
            Setting Credentials
        '''
        self.creds = creds

    def hasUsufy(self):
        ''' 
            Determining if the current platform is a "usufy" platform or not.
            
            :return:    True if it contains a self.url and False if it is not the case.
        '''
        try: 
            if self.url is not None:
                return True
        except:
            return False
        
        
#####################################
#####################################

def getAllPlatformsByMode(mode=None):
    ''' 
        Method that defines the whole list of <Platform> objects to be processed... Note that <Facebook> or <Twitter> objects inherit from <Platform>.
        :param mode:    The mode of the search.  The following can be chosen: ["usufy"].

        Return values:
            Returns a list [] of <Platform> objects.
    '''
    listAll = getAllPlatforms()
    
    listPlatformsByMode = []
    
    for p in listAll:
        if mode == "usufy":
            if p.hasUsufy():
                listPlatformsByMode.append(p)
        # Add any new mode here: for instance, for "seafy"

    return listPlatformsByMode

def getAllPlatformParametersByMode(mode):
    ''' 
        Method that defines the whole list of available parameters.
        :param mode:    The mode of the search. The following can be chosen: ["usufy"].

        Return values:
            Returns a list [] of strings for the platform objects.
    '''
    # Recovering all the possible platforms installed
    allPlatforms = getAllPlatformsByMode(mode=mode)
    # Defining the platOptions
    platOptions = []
    for p in allPlatforms:
        try:
            # E. g.: to use wikipedia instead of wikipedia_ca and so on
            parameter = p.parameterName
        except:
            parameter = p.platformName.lower()
        
        if parameter not in platOptions:
            platOptions.append(parameter)
    platOptions =  sorted(set(platOptions))
    platOptions.insert(0, 'all')
    return platOptions
    

# Importing Classes of <Platform> objects that will be used in the script. The files are stored in the wrappers folder.
# For demo only
#from osrframework.wrappers.demo import Demo
from osrframework.wrappers.px500 import Px500
from osrframework.wrappers.adtriboo import Adtriboo
from osrframework.wrappers.anarchy101 import Anarchy101
from osrframework.wrappers.aporrealos import Aporrealos
from osrframework.wrappers.apsense import Apsense
from osrframework.wrappers.arduino import Arduino
from osrframework.wrappers.ariva import Ariva
from osrframework.wrappers.armorgames import Armorgames
from osrframework.wrappers.artbreak import Artbreak
from osrframework.wrappers.artician import Artician
from osrframework.wrappers.arto import Arto
from osrframework.wrappers.askfm import Askfm
from osrframework.wrappers.audiob import Audiob
from osrframework.wrappers.audioboo import Audioboo
from osrframework.wrappers.authorstream import Authorstream
from osrframework.wrappers.autospies import Autospies
from osrframework.wrappers.backyardchickens import Backyardchickens
from osrframework.wrappers.badoo import Badoo
from osrframework.wrappers.behance import Behance
from osrframework.wrappers.bennugd import Bennugd
from osrframework.wrappers.bitbucket import Bitbucket
from osrframework.wrappers.bitcointalk import Bitcointalk
from osrframework.wrappers.bitly import Bitly
from osrframework.wrappers.blackplanet import Blackplanet
from osrframework.wrappers.bladna import Bladna
from osrframework.wrappers.blip import Blip
from osrframework.wrappers.blogspot import Blogspot
from osrframework.wrappers.bookmarky import Bookmarky
from osrframework.wrappers.boonex import Boonex
from osrframework.wrappers.bookofmatches import Bookofmatches
from osrframework.wrappers.bordom import Bordom
from osrframework.wrappers.boxedup import Boxedup
from osrframework.wrappers.breakcom import Breakcom
from osrframework.wrappers.bucketlistly import Bucketlistly
from osrframework.wrappers.burbuja import Burbuja
from osrframework.wrappers.burdastyle import Burdastyle
from osrframework.wrappers.buzznet import Buzznet
from osrframework.wrappers.cafemom import Cafemom
from osrframework.wrappers.carbonmade import Carbonmade
from osrframework.wrappers.cardomain import Cardomain
from osrframework.wrappers.care2 import Care2
from osrframework.wrappers.castroller import Castroller
from osrframework.wrappers.causes import Causes
from osrframework.wrappers.ccsinfo import Ccsinfo
from osrframework.wrappers.chess import Chess
from osrframework.wrappers.cockos import Cockos
from osrframework.wrappers.connectingsingles import Connectingsingles
from osrframework.wrappers.couchsurfing import Couchsurfing
from osrframework.wrappers.dailymail import Dailymail
from osrframework.wrappers.dailymotion import Dailymotion
from osrframework.wrappers.deviantart import Deviantart
from osrframework.wrappers.digitalspy import Digitalspy
from osrframework.wrappers.disqus import Disqus
from osrframework.wrappers.doodle import Doodle
from osrframework.wrappers.douban import Douban
from osrframework.wrappers.dribbble import Dribbble
from osrframework.wrappers.drupal import Drupal
from osrframework.wrappers.drugbuyersforum import Drugbuyersforum
from osrframework.wrappers.ebay import Ebay
from osrframework.wrappers.echatta import Echatta
from osrframework.wrappers.elmundo import Elmundo
from osrframework.wrappers.enfemenino import Enfemenino
from osrframework.wrappers.epinions import Epinions
from osrframework.wrappers.eqe import Eqe
from osrframework.wrappers.ethereum import Ethereum
from osrframework.wrappers.etsy import Etsy
from osrframework.wrappers.evilzone import Evilzone
from osrframework.wrappers.facebook import Facebook
from osrframework.wrappers.fanpop import Fanpop
from osrframework.wrappers.fark import Fark
from osrframework.wrappers.favstar import Favstar
from osrframework.wrappers.flickr import Flickr
from osrframework.wrappers.flixster import Flixster
from osrframework.wrappers.foodspotting import Foodspotting
from osrframework.wrappers.forobtc import Forobtc
from osrframework.wrappers.forocoches import Forocoches
from osrframework.wrappers.forosperu import Forosperu
from osrframework.wrappers.foursquare import Foursquare
from osrframework.wrappers.freebase import Freebase
from osrframework.wrappers.freerepublic import Freerepublic
from osrframework.wrappers.friendfeed import Friendfeed
from osrframework.wrappers.gametracker import Gametracker
from osrframework.wrappers.gapyear import Gapyear
from osrframework.wrappers.garage4hackers import Garage4hackers
from osrframework.wrappers.gather import Gather
from osrframework.wrappers.geeksphone import Geeksphone
from osrframework.wrappers.genspot import Genspot
from osrframework.wrappers.getsatisfaction import Getsatisfaction
from osrframework.wrappers.github import Github
from osrframework.wrappers.gitorious import Gitorious
from osrframework.wrappers.gogobot import Gogobot
from osrframework.wrappers.goodreads import Goodreads
from osrframework.wrappers.googleplus import GooglePlus
from osrframework.wrappers.gsmspain import Gsmspain
from osrframework.wrappers.hellboundhackers import Hellboundhackers
from osrframework.wrappers.hi5 import Hi5
from osrframework.wrappers.ibosocial import Ibosocial
from osrframework.wrappers.identica import Identica
from osrframework.wrappers.imgur import Imgur
from osrframework.wrappers.instagram import Instagram
from osrframework.wrappers.instructables import Instructables
from osrframework.wrappers.interracialmatch import Interracialmatch
from osrframework.wrappers.intersect import Intersect
from osrframework.wrappers.intfiction import Intfiction
from osrframework.wrappers.islamicawakening import Islamicawakening
from osrframework.wrappers.issuu import Issuu
from osrframework.wrappers.ixgames import Ixgames
from osrframework.wrappers.jamiiforums import Jamiiforums
from osrframework.wrappers.kaboodle import Kaboodle
from osrframework.wrappers.kali import Kali
from osrframework.wrappers.karmacracy import Karmacracy
from osrframework.wrappers.kickstarter import Kickstarter
from osrframework.wrappers.kinja import Kinja
from osrframework.wrappers.klout import Klout
from osrframework.wrappers.kongregate import Kongregate
from osrframework.wrappers.kupika import Kupika
from osrframework.wrappers.lastfm import Lastfm
from osrframework.wrappers.linkedin import Linkedin
from osrframework.wrappers.livejournal import Livejournal
from osrframework.wrappers.looki import Looki
from osrframework.wrappers.marca import Marca
from osrframework.wrappers.matchdoctor import Matchdoctor
from osrframework.wrappers.mcneel import Mcneel
from osrframework.wrappers.mediavida import Mediavida
from osrframework.wrappers.medium import Medium
from osrframework.wrappers.meneame import Meneame
from osrframework.wrappers.metacafe import Metacafe
from osrframework.wrappers.migente import Migente
from osrframework.wrappers.minecraft import Minecraft
from osrframework.wrappers.musicasacra import Musicasacra
from osrframework.wrappers.myeloma import Myeloma
from osrframework.wrappers.myspace import Myspace
from osrframework.wrappers.naver import Naver
from osrframework.wrappers.netlog import Netlog
from osrframework.wrappers.netvibes import Netvibes
from osrframework.wrappers.occupywallst import Occupywallst
from osrframework.wrappers.odnoklassniki import Odnoklassniki
from osrframework.wrappers.openframeworks import Openframeworks
from osrframework.wrappers.oroom import Oroom
from osrframework.wrappers.pastebin import Pastebin
from osrframework.wrappers.pearltrees import Pearltrees
from osrframework.wrappers.peerbackers import Peerbackers
from osrframework.wrappers.photobucket import Photobucket
from osrframework.wrappers.pinterest import Pinterest
from osrframework.wrappers.pixinsight import Pixinsight
from osrframework.wrappers.pjrc import Pjrc
from osrframework.wrappers.plancast import Plancast
from osrframework.wrappers.pokerred import Pokerred
from osrframework.wrappers.pokerstrategy import Pokerstrategy
from osrframework.wrappers.pornhub import Pornhub
from osrframework.wrappers.proboards import Proboards
from osrframework.wrappers.pz import Pz
from osrframework.wrappers.qq import QQ
from osrframework.wrappers.quartermoonsaloon import Quartermoonsaloon
from osrframework.wrappers.rankia import Rankia
from osrframework.wrappers.rapid import Rapid
from osrframework.wrappers.ratemypoo import Ratemypoo
from osrframework.wrappers.rawtherapee import Rawtherapee
from osrframework.wrappers.rebelmouse import Rebelmouse
from osrframework.wrappers.redtube import Redtube
from osrframework.wrappers.relatious import Relatious
from osrframework.wrappers.researchgate import Researchgate
from osrframework.wrappers.rojadirecta import Rojadirecta
from osrframework.wrappers.ruby import Ruby
from osrframework.wrappers.scribd import Scribd
from osrframework.wrappers.sencha import Sencha
from osrframework.wrappers.skype import Skype
from osrframework.wrappers.slashdot import Slashdot
from osrframework.wrappers.slideshare import Slideshare
from osrframework.wrappers.smartcitizen import Smartcitizen
from osrframework.wrappers.sokule import Sokule
from osrframework.wrappers.soundcloud import Soundcloud
from osrframework.wrappers.sourceforge import Sourceforge
from osrframework.wrappers.spaniards import Spaniards
from osrframework.wrappers.spoj import Spoj
from osrframework.wrappers.spotify import Spotify
from osrframework.wrappers.squidoo import Squidoo
from osrframework.wrappers.steamcommunity import Steamcommunity
from osrframework.wrappers.steinberg import Steinberg
from osrframework.wrappers.streakgaming import Streakgaming
from osrframework.wrappers.stuff import Stuff
from osrframework.wrappers.stumbleupon import Stumbleupon
from osrframework.wrappers.teamtreehouse import Teamtreehouse
from osrframework.wrappers.techcrunch import Techcrunch
from osrframework.wrappers.thecarcommunity import Thecarcommunity
from osrframework.wrappers.theguardian import Theguardian
from osrframework.wrappers.thehoodup import Thehoodup
from osrframework.wrappers.thesims import Thesims
from osrframework.wrappers.thestudentroom import Thestudentroom
from osrframework.wrappers.tradimo import Tradimo
from osrframework.wrappers.travian import Travian
from osrframework.wrappers.tripadvisor import Tripadvisor
from osrframework.wrappers.tripit import Tripit
from osrframework.wrappers.trulia import Trulia
from osrframework.wrappers.tumblr import Tumblr
from osrframework.wrappers.tuporno import Tuporno
from osrframework.wrappers.tvtag import Tvtag
from osrframework.wrappers.twicsy import Twicsy
from osrframework.wrappers.twitch import Twitch
from osrframework.wrappers.twoplustwo import Twoplustwo
from osrframework.wrappers.twitpic import Twitpic
from osrframework.wrappers.twitter import Twitter
from osrframework.wrappers.ukdebate import Ukdebate
from osrframework.wrappers.ummahforum import Ummahforum
from osrframework.wrappers.unsystem import Unsystem
from osrframework.wrappers.ustream import Ustream
from osrframework.wrappers.vexforum import Vexforum
from osrframework.wrappers.vimeo import Vimeo
from osrframework.wrappers.videohelp import Videohelp
from osrframework.wrappers.virustotal import Virustotal
from osrframework.wrappers.vk import Vk
from osrframework.wrappers.wefollow import Wefollow
from osrframework.wrappers.wikipediaar import WikipediaAr
from osrframework.wrappers.wikipediaca import WikipediaCa
from osrframework.wrappers.wikipediade import WikipediaDe
from osrframework.wrappers.wikipediaen import WikipediaEn
from osrframework.wrappers.wikipediaes import WikipediaEs
from osrframework.wrappers.wikipediaeu import WikipediaEu
from osrframework.wrappers.winamp import Winamp
from osrframework.wrappers.wishlistr import Wishlistr
from osrframework.wrappers.wordpress import Wordpress
from osrframework.wrappers.wykop import Wykop
from osrframework.wrappers.xanga import Xanga
from osrframework.wrappers.xat import Xat
from osrframework.wrappers.xing import Xing
from osrframework.wrappers.xtube import Xtube
from osrframework.wrappers.youku import Youku
from osrframework.wrappers.youtube import Youtube
from osrframework.wrappers.zabbix import Zabbix
from osrframework.wrappers.zentyal import Zentyal
################################
# Automatically generated code #
################################
# <ADD_HERE_THE_NEW_IMPORTS>
# Add any additional import here
#from osrframework.wrappers.any_new_social_network import Any_New_Social_Network
# ...
# Please, notify the authors if you have written a new wrapper.
    
def getAllPlatforms():
    ''' 
        Method that defines the whole list of <Platform> objects to be processed... Note that <Facebook> or <Twitter> objects inherit from <Platform>.

        Return values:
            Returns a list [] of <Platform> objects.
    '''
    listAll = []
    listAll.append(Adtriboo())
    listAll.append(Anarchy101())
    listAll.append(Apsense())
    listAll.append(Aporrealos())
    listAll.append(Ariva())
    listAll.append(Arduino())
    listAll.append(Armorgames())
    listAll.append(Artbreak())
    listAll.append(Artician())
    listAll.append(Arto())
    listAll.append(Askfm())
    listAll.append(Audiob())
    listAll.append(Audioboo())
    listAll.append(Authorstream())
    listAll.append(Autospies())
    listAll.append(Backyardchickens())
    listAll.append(Badoo())
    listAll.append(Behance())
    listAll.append(Bennugd())
    listAll.append(Bitbucket())
    listAll.append(Bitcointalk())
    listAll.append(Bitly())
    listAll.append(Blackplanet())
    listAll.append(Bladna())
    listAll.append(Blip())
    listAll.append(Blogspot())
    listAll.append(Bookmarky())
    listAll.append(Bookofmatches())
    listAll.append(Boonex())
    listAll.append(Bordom())
    listAll.append(Boxedup())
    listAll.append(Breakcom())
    listAll.append(Bucketlistly())
    listAll.append(Burbuja())
    listAll.append(Burdastyle())
    listAll.append(Buzznet())
    listAll.append(Cafemom())
    listAll.append(Carbonmade())
    listAll.append(Cardomain())
    listAll.append(Care2())
    listAll.append(Castroller())
    listAll.append(Causes())
    listAll.append(Ccsinfo())
    listAll.append(Chess())
    listAll.append(Cockos())
    listAll.append(Connectingsingles())
    listAll.append(Couchsurfing())
    listAll.append(Dailymail())
    listAll.append(Dailymotion())
    listAll.append(Deviantart())
    listAll.append(Digitalspy())
    listAll.append(Disqus())
    listAll.append(Doodle())
    listAll.append(Douban())
    listAll.append(Dribbble())
    listAll.append(Drugbuyersforum())    
    listAll.append(Drupal())
    listAll.append(Ebay())
    listAll.append(Echatta())
    listAll.append(Elmundo())
    listAll.append(Enfemenino())
    listAll.append(Epinions())
    listAll.append(Eqe())
    listAll.append(Ethereum())
    listAll.append(Etsy())
    listAll.append(Evilzone())
    listAll.append(Facebook())
    listAll.append(Fanpop())
    listAll.append(Fark())
    listAll.append(Favstar())
    listAll.append(Flickr())
    listAll.append(Flixster())
    listAll.append(Foodspotting())
    listAll.append(Forobtc())    
    listAll.append(Forocoches())
    listAll.append(Forosperu())
    listAll.append(Foursquare())
    listAll.append(Freebase())
    listAll.append(Freerepublic())
    listAll.append(Friendfeed())
    listAll.append(Gametracker())
    listAll.append(Gapyear())
    listAll.append(Garage4hackers())
    listAll.append(Gather())
    listAll.append(Geeksphone())
    listAll.append(Genspot())
    listAll.append(Getsatisfaction())
    listAll.append(Github())
    listAll.append(Gitorious())
    listAll.append(Gogobot())
    listAll.append(Goodreads())
    listAll.append(GooglePlus())
    listAll.append(Gsmspain())
    listAll.append(Hellboundhackers())
    listAll.append(Hi5())
    listAll.append(Ibosocial())
    listAll.append(Identica())
    listAll.append(Imgur())
    listAll.append(Instagram())
    listAll.append(Interracialmatch())
    listAll.append(Intersect())
    listAll.append(Intfiction())
    listAll.append(Instructables())
    listAll.append(Islamicawakening())
    listAll.append(Issuu())
    listAll.append(Ixgames())
    listAll.append(Jamiiforums())
    listAll.append(Kaboodle())
    listAll.append(Kali())
    listAll.append(Karmacracy())
    listAll.append(Kickstarter())
    listAll.append(Kinja())
    listAll.append(Klout())
    listAll.append(Kongregate())
    listAll.append(Kupika())
    listAll.append(Lastfm())
    listAll.append(Linkedin())
    listAll.append(Livejournal())
    listAll.append(Looki())
    listAll.append(Marca())
    listAll.append(Matchdoctor())
    listAll.append(Mcneel())
    listAll.append(Mediavida())
    listAll.append(Medium())
    listAll.append(Meneame())
    listAll.append(Metacafe())
    listAll.append(Migente())
    listAll.append(Minecraft())
    listAll.append(Musicasacra())
    listAll.append(Myeloma())
    listAll.append(Myspace())
    listAll.append(Naver())
    listAll.append(Netlog())
    listAll.append(Netvibes())
    listAll.append(Occupywallst())
    listAll.append(Odnoklassniki())
    listAll.append(Openframeworks())
    listAll.append(Oroom())
    listAll.append(Pastebin())
    listAll.append(Pearltrees())
    listAll.append(Peerbackers())
    listAll.append(Photobucket())    
    listAll.append(Pinterest())
    listAll.append(Pixinsight())
    listAll.append(Pjrc())
    listAll.append(Plancast())
    listAll.append(Pokerred())
    listAll.append(Pokerstrategy())
    listAll.append(Pornhub())
    listAll.append(Proboards())
    listAll.append(Px500())
    listAll.append(Pz())
    listAll.append(QQ())
    listAll.append(Quartermoonsaloon())
    listAll.append(Rankia())
    listAll.append(Rapid())
    listAll.append(Ratemypoo())
    listAll.append(Rawtherapee())
    listAll.append(Rebelmouse())
    listAll.append(Redtube())
    listAll.append(Relatious())
    listAll.append(Researchgate())
    listAll.append(Rojadirecta())
    listAll.append(Ruby())
    listAll.append(Scribd())
    listAll.append(Sencha())
    listAll.append(Skype())
    listAll.append(Slashdot())
    listAll.append(Slideshare())
    listAll.append(Smartcitizen())
    listAll.append(Sokule())
    listAll.append(Soundcloud())
    listAll.append(Sourceforge())
    listAll.append(Spaniards())
    listAll.append(Spoj())
    listAll.append(Spotify())
    listAll.append(Squidoo())
    listAll.append(Steamcommunity())
    listAll.append(Steinberg())
    listAll.append(Streakgaming())
    listAll.append(Stuff())
    listAll.append(Stumbleupon())
    listAll.append(Teamtreehouse())
    listAll.append(Techcrunch())
    listAll.append(Thecarcommunity())
    listAll.append(Theguardian())
    listAll.append(Thehoodup())
    listAll.append(Thesims())
    listAll.append(Thestudentroom())
    listAll.append(Tradimo())
    listAll.append(Travian())
    listAll.append(Tripadvisor())
    listAll.append(Tripit())
    listAll.append(Trulia())
    listAll.append(Tumblr())
    listAll.append(Tuporno())
    listAll.append(Tvtag())
    listAll.append(Twicsy())
    listAll.append(Twitch())
    listAll.append(Twitpic())
    listAll.append(Twitter())
    listAll.append(Twoplustwo())
    listAll.append(Ukdebate())
    listAll.append(Ummahforum())
    listAll.append(Unsystem())
    listAll.append(Ustream())
    listAll.append(Vexforum())
    listAll.append(Videohelp())
    listAll.append(Vimeo())
    listAll.append(Virustotal())
    listAll.append(Vk())
    listAll.append(Wefollow())
    listAll.append(WikipediaAr())
    listAll.append(WikipediaCa())
    listAll.append(WikipediaDe())
    listAll.append(WikipediaEn())
    listAll.append(WikipediaEs())
    listAll.append(WikipediaEu())
    listAll.append(Winamp())
    listAll.append(Wishlistr())
    listAll.append(Wordpress())
    listAll.append(Wykop())
    listAll.append(Xanga())
    listAll.append(Xat())
    listAll.append(Xing())
    listAll.append(Xtube())
    listAll.append(Youku())
    listAll.append(Youtube())
    listAll.append(Zabbix())
    listAll.append(Zentyal())
    ################################
    # Automatically generated code #
    ################################
    # append to the list variable whatever new <Platform> object that you want to add.
    #listAll.append(Any_New_Social_Network())
    # <ADD_HERE_THE_NEW_PLATFORMS>

    # sorting the platforms
    return listAll

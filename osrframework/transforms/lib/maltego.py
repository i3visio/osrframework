# !/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
#   Copyright 2015-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
#    You should have received a copy of the Affero GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

#############################################################
# The code is based on an unlicensed Paterva's development. #
# The only disclaimer of this code is below.                #
#############################################################
# Maltego Python Local Transform Helper                     #
#   Version 0.2                                             #
#                                                           #
# Local transform specification can be found at:            #
#    http://ctas.paterva.com/view/Specification             #
#                                                           #
# For more help and other local transforms                  #
# try the forum or mail me:                                 #
#                                                           #
#   http://www.paterva.com/forum                            #
#                                                           #
#  Andrew MacPherson [ andrew <<at>> Paterva.com ]          #
#                                                           #
#############################################################

import sys
import json
import yaml


class MaltegoEntity(object):
    value = ""
    weight = 100
    displayInformation = None
    additionalFields = []
    iconURL = ""
    entityType = "Phrase"

    def __init__(self, eT=None, v=None):
        if (eT is not None):
            self.entityType = eT
        if (v is not None):
            self.value = sanitise(v)
        self.additionalFields = []
        self.displayInformation = None
        self.bookmarks = 4

    def setType(self, eT=None):
        if (eT is not None):
            self.entityType = eT

    def setValue(self, eV=None):
        if (eV is not None):
            self.value = sanitise(eV)

    def setWeight(self, w=None):
        if (w is not None):
            self.weight = w

    def setDisplayInformation(self, di=None):
        if (di is not None):
            self.displayInformation = di

    def addAdditionalFields(self, fieldName=None, displayName=None, matchingRule=False, value=None):
        self.additionalFields.append([sanitise(fieldName),sanitise(displayName),matchingRule,sanitise(value)])

    def setIconURL(self, iU=None):
        if (iU is not None):
            self.iconURL = iU

    def returnEntity(self):
        """Method to print the XML information that Maltego will be reading.
        """
        print self.getEntityText()

    def getEntityText(self):
        """Generating the Entity Type text based on the parameters of the entity.

            :return:    The entity text.
        """
        entityOutput = ""
        entityOutput +=     "<Entity Type=\"" + stringify(self.entityType) + "\">"
        entityOutput +=     "<Value>" + stringify(self.value) + "</Value>"
        entityOutput +=     "<Weight>" + stringify(self.weight) + "</Weight>"
        if (self.displayInformation is not None):
            entityOutput +=     "<DisplayInformation><Label Name=\"\" Type=\"text/html\"><![CDATA[" + stringify(self.displayInformation) + "]]></Label></DisplayInformation>"
        if (len(self.additionalFields) > 0):
            entityOutput +=     "<AdditionalFields>"
            for i in range(len(self.additionalFields)):
                if (stringify(self.additionalFields[i][2]) <> "strict"):
                    entityOutput +=     "<Field Name=\"" + stringify(self.additionalFields[i][0]) + "\" DisplayName=\"" + stringify(self.additionalFields[i][1]) + "\">" + stringify(self.additionalFields[i][3]) + "</Field>"
                else:
                    entityOutput +=     "<Field MatchingRule=\"" + stringify(self.additionalFields[i][2]) + "\" Name=\"" + stringify(self.additionalFields[i][0]) + "\" DisplayName=\"" + stringify(self.additionalFields[i][1]) + "\">" + stringify(self.additionalFields[i][3]) + "</Field>"
            entityOutput +=     "</AdditionalFields>"
        if (len(self.iconURL) > 0):
            entityOutput +=     "<IconURL>" + self.iconURL + "</IconURL>"
        entityOutput +=     "</Entity>"

        return entityOutput

class MaltegoTransform(object):
    entities = []
    exceptions = []
    UIMessages = []
    values = {}

    def __init__(self, argv = ""):
        """The initialization will automatically perform the parameter parsing.

            :param argv:    Parameters passed by Maltego.
        """
        values = {}
        value = None
        self.parseArguments(argv)


    def parseArguments(self, argv):
        try:
            if (argv[1] is not None):
                self.value = argv[1]
        except:
            # If no info was provided
            self.value = self.getVar("@value")
        if (len(argv) > 2):
            if (argv[2] is not None):
                vars = argv[2].split('#')
                for x in range(0, len(vars)):
                    vars_values = vars[x].split('=')
                    if (len(vars_values) == 2):
                        self.values[vars_values[0]] = vars_values[1]

    def getValue(self):
        if (self.value is not None):
            return self.value


    def getVar(self, varName):
        if (varName in self.values.keys()):
            if (self.values[varName] is not None):
                return self.values[varName]


    def getFatherEntity(self):
        """Method that returns the i3visio-like entity

            :param argv:    Parameters transferred,

            :return: An i3visio-like dictionary as the following:
                {
                    "type": "i3visio.object",
                    "value": "example",
                    "attributes": []
                }
        """
        try:
            # Trying to load the full json object onto a new dictionary
            temp = json.loads(self.getVar("@serialized"))
        except:
            # If the information is NOT found, it may be because the entity was created by the user...
            temp = {}
            # We will have to save the entity type to pass it even when
            aux = self.getVar("@entity_type")
            if aux != None:
                temp["type"] = aux
            else:
                # If by any circumsntance, the @entity_type is NOT passed, we will create an i3visio.object
                temp["type"] = "i3visio.object"
                #return {}
            temp["value"] = self.getValue()
            temp["attributes"] = []
        return temp


    def addEntity(self, enType, enValue):
        values = yaml.safe_load(enValue)

        self.addUIMessage("Value: " + enValue)

        if type(values) is not list:
             values = [values]

        for val in values:
            self.addUIMessage("Value: " + val.decode("utf-8"))
            me = MaltegoEntity(enType, val.decode("utf-8"))
            self.addEntityToMessage(me)

        return self.entities[len(self.entities)-len(values):]


    def displayNewEntity(self, ent, pendingEntities=[]):
        """Method that receives an i3visio-like object and build an entity from it.

            :param ent: the dict object containing the i3visio-like entity.
            :param pendingEntities:  list of entities which are to be shown in future executions of the transforms.
        """
        # Creating the new entities
        newEnts = self.addEntity(ent["type"], ent["value"])

        for newEnt in newEnts:
            # Establishing the new value for the entity..
            newEnt.addAdditionalFields("@value", "@value", True, stringify(ent["value"]))

            # Establishing the new entity type.
            newEnt.addAdditionalFields("@entity_type", "@entity_type", True, stringify(ent["type"]))

            # This field will contain the number of entities yet to be shown in the GUI
            newEnt.addAdditionalFields("@number_pending", "@number_pending", True, stringify(len(pendingEntities)))

            # This field will contain the entities that have not been shown yet in the GUI in its attribute field.
            newEnt.addAdditionalFields("@pending", "@pending", True, json.dumps(pendingEntities))

            # Creating the _serialized field containing a string representation of the object.
            newEnt.addAdditionalFields("@serialized", "@serialized", True, json.dumps(ent))

            # Iterating to create the new fields based on the attributes.
            for att in ent["attributes"]:
                newEnt.addAdditionalFields(att["type"], att["type"], True, att["value"])

            # Displaying the full information in the tab...
            newEnt.setDisplayInformation("<h3>" + stringify(ent["value"]) +"</h3><p>" + json.dumps(ent, indent=2) + "</p>")
            newEnt.setDisplayInformation(json.dumps(ent, indent=2))


    def addListOfEntities(self, newEntities):
        """Method to display a series of entities in a transform. Usable when the transform is expected to recover more than one entity to capture all the results.

            :param newEntities:    it is always a list containing the dicts representing the new entities to be added.
        """
        # Reviewed entities
        reviewedEntities =[]
        # Defining a list to include the already added entities.
        addedEntities = []

        nextID = 0
        # Generating up to 11 new entities
        for new in newEntities:
            # Increasing the iterating factor of the NEXT entity
            nextID+=1
            reviewedEntities.append(new)
            # We do this to avoid processing attributes which will start with '@'
            if new["value"][0] != "@":
                addedEntities.append(new)
            if len(addedEntities) >= 12:
                # We stop, as Maltego in the Community edition does NOT show more than 12 entities per transform. THIS WILL BE CHANGED IN FUTURE VERSIONS TO LET UPDATE THE PROPERTY NUM_PNEDING OF THE CURRENT ENTITY.
                self.addException("The entities to be shown is greater than 12, so not all entities can be shown in Community version.")
                break

        # Creating the addedEntities
        for ent in addedEntities:
            self.displayNewEntity(ent)

        if len(addedEntities) <= len(newEntities):
            self.addUIMessage("All the entities have been displayed!")
        else:
            self.addUIMessage("Ooops! Too many entities to display!")
            self.addUIMessage("The following entities could not be added because of the limits in Maltego Community Edition:\n"+json.dumps(json.dumps(newEntities, indent=2)))

        # Now, we are updating some information in the father entity. To display these updates, the father entity needs to be recreated to represent these updates
        # First of all, we recover the information of the transform that was called.
        ####fatherEnt = self.getFatherEntity()

        # Now, we want to collect all those entities which have not been displayed.
        ####pending = [ x for x in newEntities if x not in reviewedEntities ]
        # These entities will be stored in the father entity which will need to be recreated to store in a new variable "@pending"
        ####self.displayNewEntity(fatherEnt, pendingEntities = pending)


    def addEntityToMessage(self, maltegoEntity):
        self.entities.append(maltegoEntity)


    def addUIMessage(self, message, messageType="Inform"):
        # changed added to avoid problems when displaying messages that last more than one line
        lines = message.splitlines()
        for line in lines:
            # we add a just to make the texts more readable
            self.UIMessages.append([messageType, line.ljust(80, ".")])


    def addException(self, exceptionString):
        self.exceptions.append(exceptionString)


    def throwExceptions(self):
        print "<MaltegoMessage>"
        print "<MaltegoTransformExceptionMessage>"
        print "<Exceptions>"

        for i in range(len(self.exceptions)):
            print "<Exception>" + self.exceptions[i] + "</Exception>"
        print "</Exceptions>"
        print "</MaltegoTransformExceptionMessage>"
        print "</MaltegoMessage>"
        exit()


    def returnOutput(self):
        """Method that print the output text to let Maltego operate with it.
        """
        print self.getOutput()


    def getOutput(self):
        """Returning a the Output text.

            :return : Textual output to be displayed.
        """
        maltegoOutput = ""
        maltegoOutput += "<MaltegoMessage>"
        maltegoOutput += "<MaltegoTransformResponseMessage>"

        maltegoOutput += "<Entities>"
        for i in range(len(self.entities)):
            maltegoOutput += self.entities[i].getEntityText()
        maltegoOutput += "</Entities>"

        maltegoOutput += "<UIMessages>"
        for i in range(len(self.UIMessages)):
            maltegoOutput += "<UIMessage MessageType=\"" + self.UIMessages[i][0] + "\">" + self.UIMessages[i][1] + "</UIMessage>"
        maltegoOutput += "</UIMessages>"

        maltegoOutput += "</MaltegoTransformResponseMessage>"
        maltegoOutput += "</MaltegoMessage>"
        return maltegoOutput


    def writeSTDERR(self, msg):
        sys.stderr.write(stringify(msg))


    def heartbeat(self):
        self.writeSTDERR("+")


    def progress(self, percent):
        self.writeSTDERR("%" + stringify(percent))


    def debug(self, msg):
        self.writeSTDERR("D:" + stringify(msg))


def stringify(value):
    try:
        return sanitise(json.dumps(value)[1:-1])
    except:
        return sanitise(value)


def sanitise(value):
    replace_these = ["&", ">", "<", '\\"', "\\"]
    replace_with = ["&amp;", "&gt;", "&lt;", "", ""]
    tempvalue = value
    for i in range(0, len(replace_these)):
        tempvalue = tempvalue.replace(replace_these[i], replace_with[i])
    return tempvalue

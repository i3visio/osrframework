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
import sys
import json

class MaltegoEntity(object):
    value = "";
    weight = 100;
    displayInformation = None;
    additionalFields = [];
    iconURL = "";
    entityType = "Phrase"
    
    def __init__(self,eT=None,v=None):
        if (eT is not None):
            self.entityType = eT;
        if (v is not None):
            self.value = sanitise(v);
        self.additionalFields = [];
        self.displayInformation = None;
        self.bookmarks = 4;        
        
    def setType(self,eT=None):
        if (eT is not None):
            self.entityType = eT;
    
    def setValue(self,eV=None):
        if (eV is not None):
            self.value = sanitise(eV);
        
    def setWeight(self,w=None):
        if (w is not None):
            self.weight = w;
    
    def setDisplayInformation(self,di=None):
        if (di is not None):
            self.displayInformation = di;        
            
    def addAdditionalFields(self,fieldName=None,displayName=None,matchingRule=False,value=None):
        self.additionalFields.append([sanitise(fieldName),sanitise(displayName),matchingRule,sanitise(value)]);
    
    def setIconURL(self,iU=None):
        if (iU is not None):
            self.iconURL = iU;
            
    def returnEntity(self):
        ''' 
            Method to print the XML information that Maltego will be reading.
        '''
        print self.getEntityText()

    def getEntityText(self):
        ''' 
            Generating the Entity Type text based on the parameters of the entity.
            
            :return:    The entity text.
        '''
        entityOutput = ""
        entityOutput +=     "<Entity Type=\"" + str(self.entityType) + "\">";
        entityOutput +=     "<Value>" + str(self.value) + "</Value>";
        entityOutput +=     "<Weight>" + str(self.weight) + "</Weight>";
        if (self.displayInformation is not None):
            entityOutput +=     "<DisplayInformation><Label Name=\"\" Type=\"text/html\"><![CDATA[" + str(self.displayInformation) + "]]></Label></DisplayInformation>";
        if (len(self.additionalFields) > 0):
            entityOutput +=     "<AdditionalFields>";
            for i in range(len(self.additionalFields)):
                if (str(self.additionalFields[i][2]) <> "strict"):
                    entityOutput +=     "<Field Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
                else:
                    entityOutput +=     "<Field MatchingRule=\"" + str(self.additionalFields[i][2]) + "\" Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
            entityOutput +=     "</AdditionalFields>";
        if (len(self.iconURL) > 0):
            entityOutput +=     "<IconURL>" + self.iconURL + "</IconURL>";
        entityOutput +=     "</Entity>";

        return entityOutput

class MaltegoTransform(object):
    entities = []
    exceptions = []
    UIMessages = []
    values = {};
    
    def __init__(self, argv = ""):
        '''
            The initialization will automatically perform the parameter parsing.
            
            :param argv:    Parameters passed by Maltego.
        '''
        values = {}
        value = None
        self.parseArguments(argv)
        
    def parseArguments(self,argv):
        if (argv[1] is not None):
            self.value = argv[1];
            
        if (len(argv) > 2):
            if (argv[2] is not None):
                vars = argv[2].split('#');
                for x in range(0,len(vars)):
                    vars_values = vars[x].split('=')
                    if (len(vars_values) == 2):
                        self.values[vars_values[0]] = vars_values[1];
    
    def getValue(self):
        if (self.value is not None):
            return self.value;
    
    def getVar(self,varName):
        if (varName in self.values.keys()):
            if (self.values[varName] is not None):
                return self.values[varName];
    
    def addEntity(self,enType,enValue):
        me = MaltegoEntity(enType,enValue);
        self.addEntityToMessage(me);
        return self.entities[len(self.entities)-1];

    def getFatherEntity(self):
        '''
            Method that returns the i3visio-like entity
            
            :param argv:    Parameters transferred,
            
            :return: An i3visio-like dictionary as the following:
                {
                    "type": "i3visio.object",
                    "value": "example",
                    "attributes": []                               
                }
        '''      
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
                # If by any circumsntance, the _entity_type is NOT passed, we will create an i3visio.object
                temp["type"] = "i3visio.object"

            temp["value"] = self.getValue()
            temp["attributes"] = []
        return temp

    def displayNewEntity(self, ent, pendingEntities=[]):
        '''
            Method that receives an i3visio-like object and build an entity from it.
            
            :param ent: the dict object containing the i3visio-like entity.
            :param pendingEntities:  list of entities which are to be shown in future executions of the transforms.
        '''
        # Creating the new entity
        newEnt = self.addEntity(str(ent["type"]),str(ent["value"]))
        
        # Establishing the new entity type.
        newEnt.addAdditionalFields("@entity_type","@entity_type",True,str(ent["type"]))                          
        
        
        # This field will contain the number of entities yet to be shown in the GUI
        newEnt.addAdditionalFields("@number_pending","@number_pending",True,str(len(pendingEntities)))                  

        # This field will contain the entities that have not been shown yet in the GUI in its attribute field.
        newEnt.addAdditionalFields("@pending","@pending",True,json.dumps(pendingEntities))

        # Creating the _serialized field containing a string representation of the object.
        newEnt.addAdditionalFields("@serialized","@serialized",True,json.dumps(ent))        
            
        # Iterating to create the new fields based on the attributes. 
        for att in ent["attributes"]:
            newEnt.addAdditionalFields(att["type"], att["type"],True,att["value"])

        # Displaying the full information in the tab...
        #newEnt.setDisplayInformation("<h3>" + str(ent["value"]) +"</h3><p>" + json.dumps(ent, indent=2) + "</p>");    
        newEnt.setDisplayInformation(json.dumps(ent, indent=2))
        
    def addListOfEntities(self, newEntities):
        '''
            Method to display a series of entities in a transform. Usable when the transform is expected to recover more than one entity to capture all the results.
            
            :param newEntities:    it is always a list containing the dicts representing the new entities to be added.
        '''
        # Defining a list to include the already added entities.
        addedEntities = []

        # Generating up to 11 new entities
        for new in newEntities:
            addedEntities.append(new)            
            if len(addedEntities) >= 11:
                # We stop, as Maltego in the Community edition does NOT show more than 12 entities per transform.
                break

        # Creating the addedEntities
        for ent in addedEntities:
            self.displayNewEntity(ent)

        # Now, we are updating some information in the father entity. To display these updates, the father entity needs to be recreated to represent these updates
        # First of all, we recover the information of the transform that was called.
        fatherEnt = self.getFatherEntity()
        
        # Now, we want to collect all those entities which have not been displayed.
        pending = [ x for x in newEntities if x not in addedEntities ]        
        # These entities will be stored in the father entity which will need to be recreated to store in a new variable "@pending"
        self.displayNewEntity(fatherEnt, pendingEntities = pending)  
            
    
    def addEntityToMessage(self,maltegoEntity):
        self.entities.append(maltegoEntity);
        
    def addUIMessage(self,message,messageType="Inform"):
        self.UIMessages.append([messageType,message]);
    
    def addException(self,exceptionString):
        self.exceptions.append(exceptionString);
        
    def throwExceptions(self):
        print "<MaltegoMessage>";
        print "<MaltegoTransformExceptionMessage>";
        print "<Exceptions>"
        
        for i in range(len(self.exceptions)):
            print "<Exception>" + self.exceptions[i] + "</Exception>";
        print "</Exceptions>"    
        print "</MaltegoTransformExceptionMessage>";
        print "</MaltegoMessage>";
        exit();
        
    def returnOutput(self):
        '''
            Method that print the output text to let Maltego operate with it.
        '''
        print self.getOutput()
    
    def getOutput(self):
        ''' 
            Returning a the Output text.
            
            :return : Textual output to be displayed.
        '''
        maltegoOutput = ""
        maltegoOutput +="<MaltegoMessage>";
        maltegoOutput += "<MaltegoTransformResponseMessage>";
                        
        maltegoOutput += "<Entities>"
        for i in range(len(self.entities)):
            self.entities[i].returnEntity();
        maltegoOutput += "</Entities>"
                        
        maltegoOutput += "<UIMessages>"
        for i in range(len(self.UIMessages)):
            maltegoOutput += "<UIMessage MessageType=\"" + self.UIMessages[i][0] + "\">" + self.UIMessages[i][1] + "</UIMessage>";
        maltegoOutput += "</UIMessages>"
            
        maltegoOutput += "</MaltegoTransformResponseMessage>";
        maltegoOutput += "</MaltegoMessage>";
        return maltegoOutput

    def writeSTDERR(self,msg):
        sys.stderr.write(str(msg));
    
    def heartbeat(self):
        self.writeSTDERR("+");
    
    def progress(self,percent):
        self.writeSTDERR("%" + str(percent));
    
    def debug(self,msg):
        self.writeSTDERR("D:" + str(msg));
            


def sanitise(value):
    replace_these = ["&",">","<"];
    replace_with = ["&amp;","&gt;","&lt;"];
    tempvalue = value;
    for i in range(0,len(replace_these)):
        tempvalue = tempvalue.replace(replace_these[i],replace_with[i]);
    return tempvalue;

#######################################################
# The code is based on an unlicensed Paterva's development. 
# The only disclaimer of this code is below.
#######################################################
# Maltego Python Local Transform Helper               #
#   Version 0.2                              #
#                                                     #
# Local transform specification can be found at:      #
#    http://ctas.paterva.com/view/Specification          #
#                                                     #
# For more help and other local transforms            #
# try the forum or mail me:                           #
#                                                     #
#   http://www.paterva.com/forum                      #
#                                                     #
#  Andrew MacPherson [ andrew <<at>> Paterva.com ]    #
#                                                     #
#######################################################


So here is a small python lib for creating your own transforms, just takes out some of the hassle Smiley

Basic Examples: (will create a Person Entity with a value of "Andrew MacPherson")

Hello World

This transform merely returns "hello world" as a phrase, it doesn't depend on the input entity at all
from MaltegoTransform import * 
me = MaltegoTransform()
me.addEntity("maltego.Phrase","hello world");
me.returnOutput()

Reading Input

This is simple transform to show reading input from an entity and returning it to the graph (in this case working with a domain and returning a phrase with that domain in it):
from MaltegoTransform import *
import sys

domain = sys.argv[1]

me = MaltegoTransform()
me.addEntity("maltego.Phrase","hello “ + domain)
me.returnOutput()

Reading Entity Properties

This example simply illustrates using the library to read the properties of an entity and printing them out *note* this is just a snippet, not a transform!
from MaltegoTransform import *
import sys

me = MaltegoTransform()
me.parseArguments(sys.argv);

longitude = me.getVar("longitude")
latitude = me.getVar("latitude")

print longitude
print latitude

Returning a complex entity

This transform example shows reading an entity in as well as setting properties, additional fields, a UI message and the weight of the entity (run on a domain):
from MaltegoTransform import *
import sys

me = MaltegoTransform()
domain = sys.argv[1]

thisent = me.addEntity("maltego.Domain","hello " + domain)

thisent.setType("maltego.Domain")
thisent.setValue("Complex." + domain)
thisent.setWeight(200)

thisent.setDisplayInformation("<h3>Heading</h3><p>content here about" + domain + "!</p>");
thisent.addAdditionalFields("variable","Display Value",True,domain)

me.addUIMessage("completed!")
me.returnOutput()


Available Functions:

Maltego Transform:
==============
addEntity(enType,enValue):
enType: Entity Type
enValue: Entity Value

addEntityToMessage(maltegoEntity):
maltegoEntity: MaltegoEntity Object to be added to the outputted "message"

addUIMessage(message,messageType="Inform"):
message: The Message to be displayed
messageType: FatalError/PartialError/Inform/Debug - note this defaults to "Inform" see documentation for additional information

addException(exceptionString):
exceptionString: Exception message to be thrown (eg "Error! Could not connect to 10.4.0.1")

throwExceptions():
Simply return exception XML to the application

returnOutput():
Function to return all the added entities as well as the UI Messages

writeSTDERR(msg):
Function to write msg to STDErr

heartbeat():
Function to produce a "heartbeat"

progress(percent):
Function to output progress, eg MaltegoTransform.progress(20); #20% done

debug(msg)
msg: Debug message to be sent out


Maltego Entity
===========

__init__(eT,v)
eT: Entity Type (eg. Person,IPAddress)
v: Value for this entity

setType(type)
Setter for the entity Type property

setValue(value)
Setter for the entity Value property

setWeight(weight)
Setter for the entity Weight property

setDisplayInformation(displayinformation)
Setter for the entity Display Information property

addAdditionalFields(fieldName=None,displayName=None,matchingRule=False,value=None)
Set additional fields for the entity
fieldName: Name used on the code side, eg displayName may be "Age of Person", but the app and your transform will see it as the fieldName variable
displayName: display name of the field shown within the entity properties
matchingRule: either "strict" for strict matching on this specific field or false
value: The additional fields value

setIconURL(iconURL)
Setter for the entity Icon URL (entity Icon) property

returnEntity()
Prints the entity with the correct XML formatting



UPDATE:
def parseArguments(self,argv):
*This function will parse the system arguments for you so that you dont have to!*
usage example: myMaltegoTransform.parseArguments(sys.argv);

These can then be called with the following:

def getValue(self):
*This function will return the value parameter, ie the value displayed on the graph*
usage example: theValue = myMaltegoTransform.getValue()

def getVar(self,varName):
*This function will return the entity property value for the variable given in varName*
usage example: entityValue = myMaltegoTransform.getVar("ESSID")


If you have any issues feel free to contact me -- andrewmohawk@gmail.com
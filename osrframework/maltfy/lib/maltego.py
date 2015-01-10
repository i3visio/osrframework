# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of OSRFramework. You can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################
import sys

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
		print "<Entity Type=\"" + str(self.entityType) + "\">";
		print "<Value>" + str(self.value) + "</Value>";
		print "<Weight>" + str(self.weight) + "</Weight>";
		if (self.displayInformation is not None):
			print "<DisplayInformation><Label Name=\"\" Type=\"text/html\"><![CDATA[" + str(self.displayInformation) + "]]></Label></DisplayInformation>";
		if (len(self.additionalFields) > 0):
			print "<AdditionalFields>";
			for i in range(len(self.additionalFields)):
				if (str(self.additionalFields[i][2]) <> "strict"):
					print "<Field Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
				else:
					print "<Field MatchingRule=\"" + str(self.additionalFields[i][2]) + "\" Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
			print "</AdditionalFields>";
		if (len(self.iconURL) > 0):
			print "<IconURL>" + self.iconURL + "</IconURL>";
		print "</Entity>";

	def getEntity(self):
		''' 
			Returning a Entity Type text.
		'''
		entityOutput = ""
		entityOutput +=	 "<Entity Type=\"" + str(self.entityType) + "\">";
		entityOutput +=	 "<Value>" + str(self.value) + "</Value>";
		entityOutput +=	 "<Weight>" + str(self.weight) + "</Weight>";
		if (self.displayInformation is not None):
			entityOutput +=	 "<DisplayInformation><Label Name=\"\" Type=\"text/html\"><![CDATA[" + str(self.displayInformation) + "]]></Label></DisplayInformation>";
		if (len(self.additionalFields) > 0):
			entityOutput +=	 "<AdditionalFields>";
			for i in range(len(self.additionalFields)):
				if (str(self.additionalFields[i][2]) <> "strict"):
					entityOutput +=	 "<Field Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
				else:
					entityOutput +=	 "<Field MatchingRule=\"" + str(self.additionalFields[i][2]) + "\" Name=\"" + str(self.additionalFields[i][0]) + "\" DisplayName=\"" + str(self.additionalFields[i][1]) + "\">" + str(self.additionalFields[i][3]) + "</Field>";
			entityOutput +=	 "</AdditionalFields>";
		if (len(self.iconURL) > 0):
			entityOutput +=	 "<IconURL>" + self.iconURL + "</IconURL>";
		entityOutput +=	 "</Entity>";


class MaltegoTransform(object):
	entities = []
	exceptions = []
	UIMessages = []
	values = {};
	
	def __init__(self):
		values = {};
		value = None;
	
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
		print "<MaltegoMessage>";
		print "<MaltegoTransformResponseMessage>";
						
		print "<Entities>"
		for i in range(len(self.entities)):
			self.entities[i].returnEntity();
		print "</Entities>"
						
		print "<UIMessages>"
		for i in range(len(self.UIMessages)):
			print "<UIMessage MessageType=\"" + self.UIMessages[i][0] + "\">" + self.UIMessages[i][1] + "</UIMessage>";
		print "</UIMessages>"
			
		print "</MaltegoTransformResponseMessage>";
		print "</MaltegoMessage>";
	
	def getOutput(self):
		''' 
			Returning a the Output text.
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
#   Version 0.2				              #
#                                                     #
# Local transform specification can be found at:      #
#    http://ctas.paterva.com/view/Specification	      #
#                                                     #
# For more help and other local transforms            #
# try the forum or mail me:                           #
#                                                     #
#   http://www.paterva.com/forum                      #
#                                                     #
#  Andrew MacPherson [ andrew <<at>> Paterva.com ]    #
#                                                     #
#######################################################


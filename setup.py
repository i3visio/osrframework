# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))

# Importing the local scrips for the setup and taking the new version number
import osrframework
NEW_VERSION = osrframework.__version__

import osrframework.utils.general as general

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
    raise Exception('Trying to load the markdown manually!')    
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
except Exception:
    read_md = lambda f: open(f, 'r').read()

# Reading the .md file    
try:
    long_description = read_md(os.path.join(HERE,"README.md"))
except:
    long_description = ""


# Creating the application path
applicationPath = general.getConfigPath()
applicationPathDefaults = os.path.join(applicationPath, "default")

if not os.path.exists(applicationPathDefaults):
    os.makedirs(applicationPathDefaults)

# Copying the default configuration files.


# verifying if the credential files have already been created
try:
    if not os.path.isfile("./osrframework/utils/config_api_keys.py"):
        # An empty api_keys file will be created
        with open("./osrframework/utils/config_api_keys.py", "w") as oF:
            with open("./osrframework/utils/config_api_keys.py.sample") as iF:
                cont = iF.read()
                oF.write(cont)
except:
    print "ERROR: something happened when reading the configuration files."
    print "The installation is aborting now."
    import sys
    sys.exit()
 
 
 
# Launching the setup
setup(    name="osrframework",
    version=NEW_VERSION,
    description="OSRFramework - A set of GPLv3+ OSINT tools developed by i3visio for online research.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/osrframework",
    license="COPYING",
    keywords = "python osint harvesting profiling maltego username socialmedia forums",
    scripts= [
        "osrframework/alias_generator.py",            
        "osrframework/entify.py",
        "osrframework/mailfy.py",              
        "osrframework/phonefy.py",             
        "osrframework/searchfy.py", 
        "osrframework/usufy.py",            
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',   
        'Intended Audience :: Information Technology',      
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'Topic :: Communications',   
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',  
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',  
        'Topic :: Text Processing :: Markup :: HTML'                                 
    ],    
    packages=[
        "osrframework", 
        "osrframework.api", 
        "osrframework.thirdparties", 
        "osrframework.thirdparties.blockchain_info", 
        "osrframework.thirdparties.haveibeenpwned_com", 
        "osrframework.thirdparties.infobel_com", 
        "osrframework.thirdparties.ip_api_com", 
        "osrframework.thirdparties.md5crack_com", 
        "osrframework.thirdparties.pipl_com",         
        "osrframework.thirdparties.pipl_com.lib",                 
        "osrframework.thirdparties.resolvethem_com",  
        "osrframework.thirdparties.skype",         
        "osrframework.utils",         
        "osrframework.transforms", 
        "osrframework.transforms.lib",         
        "osrframework.patterns", 
        "osrframework.wrappers", 
        "osrframework.searchengines",                                        
    ],
    long_description=long_description,
    install_requires=[
        "setuptools",
        "mechanize",
        "Skype4Py",
        "argparse",
        "requests",
        "python-emailahoy",
        "BeautifulSoup",
        "pyexcel",
        "pyexcel_ods",
        "pyexcel_xls",
        "pyexcel_xlsx",
        "pyexcel_io",
        "pyexcel_text",        
        "tweepy",
        "networkx",
        "decorator",
        "validate_email",
        "pyDNS",
        "tabulate",
        "oauthlib>=1.0.0"
    ],    
)

############################
### Creating other files ###
############################

general.changePermissionsRecursively(applicationPath, int(os.getenv('SUDO_UID')), int(os.getenv('SUDO_GID')))              
files_to_copy= {
    applicationPath :
    [
        "osrframework/transforms/lib/i3visio-transforms[linux].mtz",                                         
        "config/logo.png",       
    ],
    applicationPathDefaults :
    [
        "config/accounts.cfg",                                         
        "config/api_keys.cfg",                                         
        "config/browser.cfg",
    ],
}

# Iterating through all destinations to write the info
for destiny in files_to_copy.keys():

    # Grabbing each source file to be moved
    for sourceFile in files_to_copy[destiny]:
        fileToMove = os.path.join(HERE,sourceFile)

        # Choosing the command depending on the SO
        if sys.platform == 'win32':
            cmd = "copy \"" + fileToMove + "\" \"" + destiny + "\""
        elif sys.platform == 'linux2' or sys.platform == 'darwin':   
            cmd = "sudo cp \"" + fileToMove + "\" \"" + destiny + "\""

        output = os.popen(cmd).read()    
    
            

# Maltego transforms to be added as content scripts:
    """"/usr/share/osrframework/transforms" : 
        [                
            "osrframework/transforms/aliasToKnownEmails.py", 
            "osrframework/transforms/aliasToSkypeAccounts.py", 
            "osrframework/transforms/aliasToSkypeIP.py", 
            "osrframework/transforms/bitcoinAddressToBlockchainDetails.py", 
            "osrframework/transforms/coordinatesToGoogleMapsBrowser.py", 
            "osrframework/transforms/coordinatesToTwitterBrowser.py", 
            "osrframework/transforms/domainToGoogleSearchUriWithEmails.py", 
            "osrframework/transforms/domainToTld.py", 
            "osrframework/transforms/emailToAlias.py", 
            "osrframework/transforms/emailToBreachedAccounts.py", 
            "osrframework/transforms/emailToDomain.py", 
            "osrframework/transforms/emailToSkypeAccounts.py", 
            "osrframework/transforms/expandPropertiesFromI3visioEntity.py", 
            "osrframework/transforms/hashToMD5crackDotCom.py", 
            "osrframework/transforms/ipToIp_ApiInformation.py", 
            "osrframework/transforms/phoneToMoreInfo.py", 
            "osrframework/transforms/phoneToPerson.py", 
            "osrframework/transforms/textToEntities.py", 
            "osrframework/transforms/textToGoogleSearchUri.py", 
            "osrframework/transforms/textToPlatformSearch.py", 
            "osrframework/transforms/textToProfiles.py", 
            "osrframework/transforms/uriToBrowser.py", 
            "osrframework/transforms/uriToDomain.py", 
            "osrframework/transforms/uriToEntities.py", 
            "osrframework/transforms/uriToGoogleCacheUri.py", 
            "osrframework/transforms/uriToPort.py", 
            "osrframework/transforms/uriToProtocol.py",                
        ]        """            

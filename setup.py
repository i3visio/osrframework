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

__version__ = "v0.9.0b6"

#from distutils.core import setup
import os

# Ensuring that Setuptools is install
import ez_setup
ez_setup.use_setuptools()

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

    
# verifying if the credential files have already been created
import os
try:
    if not os.path.isfile("./osrframework/utils/config_credentials.py"):
        # An empty credentials file will be created
        with open("./osrframework/utils/config_credentials.py", "w") as oF:
            with open("./osrframework/utils/config_credentials.py.sample") as iF:
                cont = iF.read()
                oF.write(cont)
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
 
setup(    name="osrframework",
    version=__version__,
    description="OSRFramework - A set of GPLv3+ OSINT tools developed by i3visio for online research.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/osrframework",
    license="COPYING",
    packages=[
        "osrframework", 
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
        #"osrframework.darkfy",
        #"osrframework.darkfy.lib",
        #"osrframework.darkfy.lib.wrappers",                                 
    ],
#    scripts=[""],
    long_description=read_md("README.md"),
#    long_description=open('README.md').read(),
    install_requires=[
    "mechanize",
    "Skype4Py",
    "argparse",
    "requests",
    "python-emailahoy",
    "BeautifulSoup",
    #"validate_email",
    #"pypandoc",
    "pyexcel",
    "pyexcel_ods",    
    "pyexcel_xls",
    "pyexcel_xlsx",
    "pyexcel_text",
    ],
)


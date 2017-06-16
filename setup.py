# !/usr/bin/python2
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2016 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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
import sys
from setuptools import setup

# Checking if obsolete versions are installed in the machine
import shutil
import site

IS_VIRTUAL_ENV = False

# Get packagesPaths depending on whether the user launched it with sudo or not
if sys.platform == 'win32':
    # This will throw two folders, but we need the first one only. Typically:
    #   ['c:\\Users\\<a_user>\\AppData\\Roaming\\Python\\Python27\\site-packages']
    packagesPaths = site.getusersitepackages()[0]
    print "[*] The installation is going to be run as superuser."
else:
    # We need this verification because Windows does not have a wrapper ofr os.geteuid()
    if not os.geteuid() == 0:
        try:
            packagesPaths = site.getusersitepackages()
            # TODO: Check whether the packagesPaths is in the PATH, if not, add it
            print "[*] The installation has not been launched as superuser."
            user_bin_path = site.USER_BASE + "/bin"
            print "[*] We will verify is the '" + user_bin_path + "' folder is in the path so as to make the utils available anywhere in the system."
            bin_path = os.popen("echo $PATH").read()
            if user_bin_path in bin_path:
                print "[*] Great. '" + user_bin_path + "' is in the path. No further actions needed."
            else:
                print "[*] We are manually adding the '" + user_bin_path + "' folder to the ~/.bashrc file."
                # Building the commands to be added to .bashrc
                new_lines = """
                # Added by OSRFramework
                # ---------------------
                # Check this issue in Github for additional information about why these lines where added: <https://github.com/i3visio/osrframework/issues/187>

                export PY_USER_BIN= """ + user_bin_path + """
                export PATH=$PATH:$PY_USER_BIN
                """

                command = "echo '''" + new_lines + "''' >> ~/.bashrc"
                print "[*] As we want to be transparent, the command that is being run is the following:\n" + command
                a = os.popen(command).read()        
        except:
            IS_VIRTUAL_ENV = True
    else:
        # This will throw two folders, but we need the first one only:
        #   ['/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']
        packagesPaths = site.getsitepackages()[0]
        print "[*] The installation is going to be run as superuser."

if not IS_VIRTUAL_ENV:
    osrframeworkSystemPath = os.path.join(packagesPaths, "osrframework")

    print "[*] The chosen installation path is: " + osrframeworkSystemPath

    # Removing old installations first...
    if os.path.isdir(osrframeworkSystemPath):
        print "[!] Found an old installation at: " + osrframeworkSystemPath
        try:
            shutil.rmtree(osrframeworkSystemPath)
            print "[*] Successfully removed the old installation. Installation will resume now to upgrade it..."
        except Exception as e:
            print str(e)
            print "[E] The installed version of OSRFramework cannot be removed. Try to remove it manually in your python installation under 'local/lib/python2.7/dist-packages/'."
            print sys.exit()
    else:
        print "[*] No OSRFramework installation found in the system."
else:
    print "[*] OSRFramework seems to be installed using `virtualenv`."

HERE = os.path.abspath(os.path.dirname(__file__))

# Importing the temporal scripts for the setup and taking the new version number
import osrframework
NEW_VERSION = osrframework.__version__

import osrframework.utils.configuration as configuration

# Depending on the place in which the project is going to be upgraded
try:
    raise Exception('Trying to load the markdown manually!')
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("[!] pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
except Exception:
    read_md = lambda f: open(f, 'r').read()

# Reading the .md file
try:
    long_description = read_md(os.path.join(HERE,"README.md"))
except:
    long_description = ""

# Creating the application paths
paths = configuration.getConfigPath()

print "[*] Launching the installation of the osrframework module..."
# Launching the setup
setup(
    name="osrframework",
    version=NEW_VERSION,
    description="OSRFramework - A set of GPLv3+ OSINT tools developed by i3visio analysts for online research.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/osrframework",
    license="COPYING",
    keywords = "python osint harvesting profiling maltego username socialmedia forums",
    scripts= [
        "osrframework/alias_generator.py",
        "osrframework/domainfy.py",
        "osrframework/entify.py",
        "osrframework/mailfy.py",
        "osrframework/phonefy.py",
        "osrframework/searchfy.py",
        "osrframework/usufy.py",
        "osrframework/osrfconsole.py",
        "osrframework/osrframework_server.py",
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
        "osrframework.domains",
    ],
    long_description=long_description,
    install_requires=[
        "setuptools",
        "mechanize",
        "Skype4Py",
        "requests",
        "python-emailahoy",
        "BeautifulSoup",
        "pyexcel==0.2.1",
        "pyexcel_ods==0.1.1",
        "pyexcel_xls==0.1.0",
        "pyexcel_xlsx==0.1.0",
        "pyexcel_io==0.1.0",
        "pyexcel_text==0.2.0",
        "tweepy",
        "networkx",
        "decorator",
        "validate_email",
        "pydns",
        "tabulate",
        "oauthlib>=1.0.0",
        # Added to dinamically import wrappers:
        "importlib",
        #"inspect",
        #"pkgutil",
        # Adding dependencies to avoid the InsecurePlatformWarning when calling Twitter API dealing with SSL: <http://stackoverflow.com/a/29202163>. Other options would require the user to upgrade to Python 2.7.9.
        #"pyopenssl",
        #"ndg-httpsclient",
        #"pyasn1"
        "python-whois",
        "flask",
        "pyyaml"
    ],
)

############################
### Creating other files ###
############################
print "[*] Changing permissions of the user folders..."
try:
    configuration.changePermissionsRecursively(paths["appPath"], int(os.getenv('SUDO_UID')), int(os.getenv('SUDO_GID')))
except:
    # Something happened with the permissions... We omit this.
    pass

print "[*] Copying relevant files..."
files_to_copy= {
    paths["appPath"] : [
        os.path.join("config", "browser.cfg"),
        os.path.join("config", "general.cfg"),
    ],
    paths["appPathDefaults"] : [
        os.path.join("config", "accounts.cfg"),
        os.path.join("config", "api_keys.cfg"),
        os.path.join("config", "browser.cfg"),
        os.path.join("config", "general.cfg"),
    ],
    paths["appPathTransforms"] : [
        os.path.join("osrframework", "alias_generator.py"),
        os.path.join("osrframework", "entify.py"),
        os.path.join("osrframework", "phonefy.py"),
        os.path.join("osrframework", "searchfy.py"),
        os.path.join("osrframework", "mailfy.py"),
        os.path.join("osrframework", "usufy.py"),
        os.path.join("osrframework", "domainfy.py"),
        os.path.join("osrframework", "transforms", "aliasToKnownDomains.py"),
        os.path.join("osrframework", "transforms", "aliasToKnownEmails.py"),
        os.path.join("osrframework", "transforms", "aliasToSkypeAccounts.py"),
        os.path.join("osrframework", "transforms", "aliasToSkypeIP.py"),
        os.path.join("osrframework", "transforms", "bitcoinAddressToBlockchainDetails.py"),
        os.path.join("osrframework", "transforms", "coordinatesToGoogleMapsBrowser.py"),
        os.path.join("osrframework", "transforms", "coordinatesToTwitterBrowser.py"),
        os.path.join("osrframework", "transforms", "domainToGoogleSearchUriWithEmails.py"),
        os.path.join("osrframework", "transforms", "domainToTld.py"),
        os.path.join("osrframework", "transforms", "emailToAlias.py"),
        os.path.join("osrframework", "transforms", "emailToBreachedAccounts.py"),
        os.path.join("osrframework", "transforms", "emailToDomain.py"),
        os.path.join("osrframework", "transforms", "emailToSkypeAccounts.py"),
        os.path.join("osrframework", "transforms", "expandPropertiesFromI3visioEntity.py"),
        os.path.join("osrframework", "transforms", "hashToMD5crackDotCom.py"),
        os.path.join("osrframework", "transforms", "ipToIp_ApiInformation.py"),
        os.path.join("osrframework", "transforms", "phoneToMoreInfo.py"),
        os.path.join("osrframework", "transforms", "phoneToPerson.py"),
        os.path.join("osrframework", "transforms", "textToEntities.py"),
        os.path.join("osrframework", "transforms", "textToGoogleSearchUri.py"),
        os.path.join("osrframework", "transforms", "textToPlatformSearch.py"),
        os.path.join("osrframework", "transforms", "textToProfiles.py"),
        os.path.join("osrframework", "transforms", "uriToBrowser.py"),
        os.path.join("osrframework", "transforms", "uriToDomain.py"),
        os.path.join("osrframework", "transforms", "uriToEntities.py"),
        os.path.join("osrframework", "transforms", "uriToGoogleCacheUri.py"),
        os.path.join("osrframework", "transforms", "uriToPort.py"),
        os.path.join("osrframework", "transforms", "uriToProtocol.py"),
    ],
    paths["appPathWrappers"] : [
        os.path.join("config", "plugins", "wrapper.py.sample"),
    ],
    paths["appPathPatterns"] : [
        os.path.join("config", "plugins", "pattern.py.sample"),
    ],
    paths["appPathServer"] : [
        os.path.join("osrframework", "static"),
        os.path.join("osrframework", "templates"),
    ]
}

# Iterating through all destinations to write the info
for destiny in files_to_copy.keys():
    # Grabbing each source file to be moved
    for sourceFile in files_to_copy[destiny]:
        fileToMove = os.path.join(HERE,sourceFile)

        # Choosing the command depending on the SO
        if sys.platform == 'win32':
            if os.path.isdir(fileToMove):
                cmd = "echo d | xcopy \"" + fileToMove + "\" \"" + destiny + "\" /s /e"
            else:
                cmd = "copy \"" + fileToMove + "\" \"" + destiny + "\""
        elif sys.platform == 'linux2' or sys.platform == 'darwin':
            if not os.geteuid() == 0:
                cmd = "cp \"" + fileToMove + "\" \"" + destiny + "\" -r"
            else:
                cmd = "sudo cp \"" + fileToMove + "\" \"" + destiny + "\" -r"
        #print cmd
        output = os.popen(cmd).read()

print
print "[*] Last part: trying to configure Maltego Transforms..."
# Creating the configuration file
try:
    import osrframework.transforms.lib.configure_maltego as maltego
    maltego.configureMaltego(transformsConfigFolder=paths["appPathTransforms"], base=os.path.join(HERE,"osrframework/transforms/lib/osrframework-maltego-settings"), debug=False, backupPath=paths["appPathDefaults"])
except Exception, e:
    print "[!] The Maltego configuration file to use i3visio transforms could not be created and thus, cannot be used. Check the following error:"
    print str(e)
print

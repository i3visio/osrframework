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
    """if not os.path.isfile("./osrframework/utils/config_credentials.py"):
        # An empty credentials file will be created
        with open("./osrframework/utils/config_credentials.py", "w") as oF:
            with open("./osrframework/utils/config_credentials.py.sample") as iF:
                cont = iF.read()
                oF.write(cont)"""
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
    version="v0.4.0",
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
        "osrframework.thirdparties.ip_api_com", 
        "osrframework.thirdparties.md5crack_com", 
        "osrframework.thirdparties.skype",         
        "osrframework.utils",         
        "osrframework.maltfy", 
        "osrframework.maltfy.lib",         
        "osrframework.entify", 
        "osrframework.entify.patterns", 
        #"osrframework.darkfy",
        #"osrframework.darkfy.lib",
        #"osrframework.darkfy.lib.wrappers",
    ],
#    scripts=[""],
    long_description=read_md("README.md"),
#    long_description=open('README.md').read(),
    install_requires=[
#    "mechanize",
    "Skype4Py",
    "argparse",
    "requests",
#    "pypandoc",
    ],
)


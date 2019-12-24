################################################################################
#
#    Copyright 2015-2020 Felix Brezo and Yaiza Rubio
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
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


import os
import sys

from setuptools import setup, find_packages

try:
    print("[*] OSRFramework > Checking Python version...")
    assert sys.version_info >= (3, 6)
    print("OSRFramework > Python version Ok: {}.{}.{}.".format(sys.version_info.major,
                                                               sys.version_info.minor,
                                                               sys.version_info.micro))
except AssertionError:
    print("[*] OSRFramework > Installation aborted!")
    print("[*] OSRFramework > Since OSRFramework 0.20+, Python 3.6+ is required. Python 2.7 reached its end of life on 2019/12/31.")
    print("[*] OSRFramework > Try to install it using Python 3.6+.")
    sys.exit(1)


import osrframework
import osrframework.utils.configuration as configuration


HERE = os.path.abspath(os.path.dirname(__file__))

# Importing the temporal scripts for the setup and taking the new version number
NEW_VERSION = osrframework.__version__

print("[*] OSRFramework > Reading requirements...")
with open("requirements.txt") as file:
    requirements = file.read().splitlines()

# Depending on the place in which the project is going to be upgraded
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Creating the application paths
paths = configuration.get_config_path()

print("[*] OSRFramework > Launching the installation of the osrframework module...")
# Launching the setup
setup(
    name="osrframework",
    version=NEW_VERSION,
    description="OSRFramework - A set of AGPLv3+ OSINT tools developed by i3visio analysts for online research.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/osrframework",
    license="COPYING",
    keywords="python osint harvesting profiling username socialmedia forums",
    entry_points={
        'console_scripts': [
            'alias_generator = osrframework.alias_generator:main',
            'alias_generator.py = osrframework.alias_generator:main',
            'domainfy = osrframework.domainfy:main',
            'domainfy.py = osrframework.domainfy:main',
            'checkfy = osrframework.checkfy:main',
            'checkfy.py = osrframework.checkfy:main',
            'mailfy = osrframework.mailfy:main',
            'mailfy.py = osrframework.mailfy:main',
            'phonefy = osrframework.phonefy:main',
            'phonefy.py = osrframework.phonefy:main',
            'searchfy = osrframework.searchfy:main',
            'searchfy.py = osrframework.searchfy:main',
            'usufy = osrframework.usufy:main',
            'usufy.py = osrframework.usufy:main',
            'osrf = osrframework.launcher:main',
            'osrframework-cli = osrframework.launcher:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
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
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=requirements,
)

############################
### Creating other files ###
############################
print("[*] OSRFramework > Changing permissions of the user folders...")
try:
    configuration.change_permissions_recursively(paths["appPath"], int(os.getenv('SUDO_UID')), int(os.getenv('SUDO_GID')))
except:
    # Something happened with the permissions... We omit this.
    pass

print("[*] OSRFramework > Population OSRFramework's configuration folder...")
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
    paths["appPathWrappers"] : [
        os.path.join("config", "plugins", "wrapper.py.sample"),
        os.path.join("config", "plugins", "wrapper_v2.py.sample"),
    ]
}

# Iterating through all destinations to write the info
for destiny in files_to_copy.keys():
    # Grabbing each source file to be moved
    for source_file in files_to_copy[destiny]:
        file_to_move = os.path.join(HERE, source_file)
        cmd = ""
        # Choosing the command depending on the SO
        if sys.platform == 'win32':
            if os.path.isdir(file_to_move):
                cmd = "echo d | xcopy \"" + file_to_move + "\" \"" + destiny + "\" /s /e"
            else:
                cmd = "copy \"" + file_to_move + "\" \"" + destiny + "\""
        elif sys.platform == 'linux' or sys.platform == 'darwin':
            if not os.geteuid() == 0:
                cmd = "cp -r -- \"" + file_to_move + "\" \"" + destiny + "\""
            else:
                cmd = "sudo cp -r -- \"" + file_to_move + "\" \"" + destiny + "\""
        else:
            print("File '{file_to_move}' could not be copied in a {sys.platform.title()} system.")
            continue
        print(f"\t> {cmd}")
        output = os.popen(cmd).read()

print("[*] OSRFramework > Installation ended. If you don't know where to start, run `osrf` to start working on it.")

	================================================================
	OSRFramework  Copyright (C) 2016  F. Brezo and Y. Rubio, i3visio
	================================================================

[![Version in PyPI](https://img.shields.io/pypi/v/osrframework.svg)]()
[![Downloads/Month in PyPI](https://img.shields.io/pypi/dm/osrframework.svg)]()
[![License](https://img.shields.io/badge/license-GNU%20General%20Public%20License%20Version%203%20or%20Later-blue.svg)]()

1 - Description:
================
OSRFramework is a GPLv3+ set of libraries developed by i3visio to perform Open Source
Intelligence tasks. They include references to a bunch of different applications 
related to username checking, information leaks research, deep web search, regular
expressions extraction and many others. At the same time, by means of ad-hoc Maltego 
transforms, OSRFramework provides a way of making these queries graphically.


2 - License: GPLv3+
===================

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, check the COPYING file.

3 - Installation:
=================
The instructions may vary in the different OS but we encourage to run this program under Linux as some utilities may behave unstably.

3.1 - General install (all systems)
-----------------------------------

This installation is recommended for most users. This will use the official package uploaded to pip.

# 3.1.1 - Verifying the Python and pip installation

First of all, on any system we should verify that we have a Python 2.7 installation and a Pip installation setup properly. Opening the terminal or the powershell, we can try the following to check your python installation:
```
python --version
```

If you get errors at this point or the Python version is not appeating, your system is not yet prepared. You will need to install Python 2.7 from the official website:
```
https://www.python.org/downloads/
```
Follow the installation steps for your system. Note that in one step of the Windows installation process you WILL NEED to manually add c:\Python27 and C:\Python27\scripts to the system. Try again after completing this task.

Now it's the turn of the Package manager. Check that you have the pip version installed:
```
pip --version
```
If you get any errors at this point, you have several options:
* If your running Ubuntu or Debian-like systems, try sudo apt-get install python-pip
* In any case you can always download <https://bootstrap.pypa.io/get-pip.py> and install it manually.
```
# Going to the downloads folder
sudo python get-pip.py
```
In Windows-like systems, you do NOT need to type sudo. Try again and heck if the new pip version is installed.


# 3.1.2 - Installing OSRFramework from pip

Fast way to do it on any system
```
pip install osrframework
```
Under MacOS or Linux systems, you may need to do this as superuser:
```
sudo pip install osrframework
```
This will manage all the dependencies for you.

# 3.1.3 - Test the installation

If everything went correctly (we hope so!), it's time for trying usufy.py, mailfy.py and so on. But we are they? They are installed in your path meaning that you can open a terminal anywhere and typing the name of the program (seems to be an improvement from previous installations...). Examples:
```
usufy.py -n i3visio febrezo yrubiosec -p twitter facebook
searchfy.py -q "i3visio"
mailfy.py -m i3visio
```

3.2 - Manual install for developers
-----------------------------------

As Python is already installed, the rest of the installation under Python 2.7 is as 
follows:

1.- Download the repository. You have several options:
```
# Cloning the repository if you have git installed
git clone http://github.com/i3visio/osrframework osrframework-master
# Navigate to the destiny's folder
cd osrframework-master
```
or
```
# Download
wget http://github.com/i3visio/osrframework/archive/master.zip
# Unzip
unzip osrframework-master.zip
# Navigate to the destiny's folder
cd osrframework-master
```

2.- [Optional] Then, you might have to copy the sample files in the osrframework folder to add 
your own API Keys. You might edit them with your preferred text editor. The files are:
```
cp osrframework/utils/config_api_keys.py.sample osrframework/utils/config_api_keys.py
```
Then you can edit it with:
```
nano osrframework/utils/config_api_keys.py
```
If you skip this step, OSRFramework will create files without any credentials. This is not a major issue as you will be able to provide them as a parameter. Then you can resume the installation.

3.- [Optional] Then, you might have to copy the sample files in the osrframework folder to add 
your own credentials. You might edit them with your preferred text editor. The files are:
```
cp osrframework/utils/config_credentials.py.sample osrframework/utils/config_credentials.py
```
Then you can edit it with:
```
nano osrframework/utils/config_credentials.py
```
If you skip this step, OSRFramework will create files without any credentials. This is not a
major issue as you will be able to provide them as a parameter. Then you can resume the 
installation.

4.- Then you can resume the installation.
```
# Superuser privileges are required so as to complete the installation.
sudo python setup.py build
sudo python setup.py install	
# Installing other packages from PyPI that osrframework needs using the requirements.txt file
sudo pip install -r requirements.txt
```
Afterwards, the module will be importable from any python code. You can check this by typing:
```
python -c "import osrframework"
```
If no error is displayed, the installation would have been performed correctly.

4 - Maltego Installation
========================

However, to use our Maltego Transforms, you will have to download Maltego from 
Paterva's site: 
```
http://www.paterva.com/web6/products/download2.php
```
Follow the instructions there. Afterwards, you may launch the application and you you will have to import the recently created .mtz configuration file created by your Linux Installation.

Select all the groups and click next. You may use the new i3visio entities now.

### Tips for Windows users
To configure the Maltego entities and transforms we have developed, launch the built-in configurator in the project folder:
```
cd <DOWNLOAD_PATH>
cd osrframework-master
python configure_maltego.py
```

This will create a .mtz file under the following path, which is where you will find the entities to be configured: 
```
<DOWNLOAD_PATH>/osrframework-master/osrframework/transforms/lib/
```

5 - AUTHORS
===========

This software is a personal project leaded by Yaiza Rubio ([@yrubiosec](https://twitter.com/yrubiosec)) and Félix Brezo ([@febrezo](https://twitter.com/febrezo)), both of whom conform the [i3visio](http://i3visio.com) team.

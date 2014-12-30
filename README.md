	================================================================
	OSRFramework  Copyright (C) 2015  F. Brezo and Y. Rubio, i3visio
	================================================================

Description:
============
OSRFramework is a GPLv3+ set of libraries developed by i3visio to perform Open Source
Intelligence tasks. They include references to a bunch of different applications 
related to username checking, information leaks research, deep web search, regular
expressions extraction and many others. At the same time, by means of maltfy, several
Maltego transforms can be used to exploit these tools.


License: GPLv3+
===============

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

Installation:
=============
The instructions may vary in the different OS. 

Under Linux
-----------
We recommend you to create a folder under /var owned by the current user. For
instance:
```
# You will need superuser privileges to create this folder 
sudo mkdir /var/i3visio
# You will need to change the owner to your user to work with it safely
# If your user was alice
sudo chown alice:alice /var/i3visio
```

The rest of the installation under Python 2.7 is as follows:
```
# Navigate to the destiny's folder
cd /var/i3visio
# Cloning the repository
git clone http://github.com/i3visio/osrframework osrframework-master
cd osrframework-master
```
or
```
# Navigate to the destiny's folder
cd /var/i3visio
# Download
wget http://github.com/i3visio/osrframework/archive/master.zip
# Unzip
unzip osrframework-master.zip
cd osrframework-master
```

Then, you might have to copy the sample files in the osrframework folder to add your  
own credentials or API Keys. You might edit with your preferred text editor.
```
cp config_credentials.py.sample config_credentials.py
nano config_credentials.py
cp config_api_keys.py.sample config_api_keys.py
nano config_api_keys.py
cd ..
```
Then you can proceed to the installation.
```
# Superuser privileges are required so as to complete the installation.
sudo python setup.py build
sudo python setup.py install	
```
Afterwards, the module will be importable from any python code. You can check this by typing:
```
python -c "import osrframework"
```
If no error is displayed, the installation would have been performed correctly.

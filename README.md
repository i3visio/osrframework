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

Under Windows
-----------
First of all, you will have to download and install Python 2.7 from:
https://www.python.org/downloads/

The installation should be performed normally. However, you will need
to add c:\python27 to the system  path variable. You have a tutorial
here: http://earthwithsun.com/questions/441106/how-do-i-add-c-python27-to-systems-path

You can check how everything went by accessing the cmd. Type
```
python
```
If you have accessed the Python interpreter, those are good news.

The rest of the installation under Python 2.7 is as follows:

1.- Download the latest version of the osrframework found in:
```
http://github.com/i3visio/osrframework/archive/master.zip
```

2.- Unzip the master.zip file wherever you want.

3.- [Optional] Then, you might have to copy the sample files in the osrframework folder to add 
your own API Keys. You might edit them with your preferred text editor. The files are:
```
config_api_keys.py.sample 
```
which should be COPIED to 
```
config_api_keys.py
```
If you skip this step, OSRFramework will create files without any credentials. This is not a
major issue as you will be able to provide them as a parameter. Then you can resume the 
installation.

4.- Open the terminal (cmd) and navigate to the recently created folder. You know something like:
```
cd Downloads
cd osrframework-master
...
```

5.- In the osrframework-master folder, build and install the modules in your system:
```
python setup.py build
python setup.py install	
```
Afterwards, the module will be importable from any python code. You can check this by typing:
```
python -c "import osrframework"
```
If no error is displayed, the installation would have been performed correctly.

6.- To configure the Maltego Entities, launch the built-in configurator:
```
python configure_maltego.py
```
This will create a .mtz file under: 
```
<INSTALLATION_FOLDER>/osrframework/maltfy/
```

7.- However, to use our Maltego Transforms, you will have to download Maltego from 
Paterva's site: 
```
http://www.paterva.com
```
Follow the instructions there. Afterwards, you may launch the application.
8.- Finally, you will have to import the recently created .mtz configuration file. 
Select all the groups and click next. You may use the recently added i3visio 
entities now.

Under Linux
-----------
As Python is alrady installed, the rest of the installation under Python 2.7 is as 
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

2.- Then, you might have to COPY the sample files in the osrframework folder to add your  
own API Keys. You might edit them with your preferred text editor.
```
cp config_api_keys.py.sample config_api_keys.py
nano config_api_keys.py
cd ..
```
If you skip this step, OSRFramework will create files without any credentials. This is not a
major issue as you will be able to provide them as a parameter. 

3.- Then you can resume the installation.
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

4.- To configure the Maltego Entities, launch the built-in configurator:
```
python configure_maltego.py
```
This will create a .mtz file under: 
```
<INSTALLATION_FOLDER>/osrframework/maltfy/
```

5.- However, to use our Maltego Transforms, you will have to download Maltego from 
Paterva's site: 
```
http://www.paterva.com
```
Follow the instructions there. Afterwards, you may launch the application.

6.- You will have to import the recently created .mtz configuration file. Select 
all the groups and click next. You may use the recently added i3visio entities 
now.

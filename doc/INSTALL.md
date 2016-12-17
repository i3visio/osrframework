Installation instructions
=========================

More detailed installation instructions can be found in this file. This will use the official package uploaded to pip.

1.- Verifying the Python and pip installation
---------------------------------------------

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
* In any case you can always download <https://bootstrap.pypa.io/get-pip.py> and install it manually. In Windows-like systems, you do NOT need to type sudo. 
```
# Going to the downloads folder
python get-pip.py
```
You can do it at a time in Linux and MacOS systems:
```
# Downloading
wget https://bootstrap.pypa.io/get-pip.py
# Installing as root
sudo python get-pip.py
```
Try again and check if the new pip version is installed.


2 - Installing OSRFramework from pip
------------------------------------

Fast way to do it on any system:
```
pip install osrframework
```
Under MacOS or Linux systems, you may need to do this as superuser:
```
sudo pip install osrframework
```
This will manage all the dependencies for you.

3 - Testing the installation
-------------------------

If everything went correctly (we hope so!), it's time for trying usufy.py, mailfy.py and so on. But we are they? They are installed in your path meaning that you can open a terminal anywhere and typing the name of the program (seems to be an improvement from previous installations...). Examples:
```
usufy.py -n i3visio febrezo yrubiosec -p twitter facebook
searchfy.py -q "i3visio"
mailfy.py -n i3visio
```

4 - Updating the framework
--------------------------

OSRFramework is a tool in development mantained by its [authors](AUTHORS.md) and, thus, we will fix bugs and add new platforms from time to time. To upgrade your local osrframework installation you can type the following:
```
pip install osrframework --upgrade
```
Under MacOS or Linux systems, you may need to do this as superuser:
```
sudo pip install osrframework --upgrade
```
This will manage all the dependencies for you and will try to download the latest "stable" version. If you want to try a prerelease version, you can type:
```
sudo pip install osrframework --upgrade --pre
```
But please, do it under your responsibility. Strange things may take place!

5 - Maltego Installation
------------------------

However, to use our Maltego Transforms, you will have to download Maltego from Paterva's site: 
```
http://www.paterva.com/web6/products/download2.php
```
Follow the instructions there. Afterwards, you may launch the application and you you will have to import the recently created .mtz configuration file created by your Linux Installation.

Select all the groups and click next. You may use the new i3visio entities now.

The Maltego transforms and entities are generated automatically by the setup script.
This will create a .mtz file in the User's home (check the installation terminal output to find it) and under the default folder inside the application folder (just in case a disaster happends ;)).
```
# Under Linux...
~/osrframework-maltego-settings_<VERSION>.mtz
~/.config/OSRFramework/default/osrframework-maltego-settings_<VERSION>.mtz
```

You will then have to import this file in Maltego by clicking the Menu --> Import --> Import configuration. You might have to manually check all the types in the installer assistant.


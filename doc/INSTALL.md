Installation Instructions
=========================

More detailed installation instructions can be found in this file. This will use the official package uploaded to pip, but if you prefer to use this with Docker check (this file)[USAGE_WITH_DOCKER.md].

1.- Verifying the Python and Pip Installation
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

Now it's the turn of the package manager. Check that you have the pip version installed:
```
pip --version
```
If you get any errors at this point, you have several options:
* If your running Ubuntu or Debian-like systems, try `sudo apt-get install python-pip`.
* In any case you can always download <https://bootstrap.pypa.io/get-pip.py> and install it manually. In Windows-like systems, you do NOT need to type sudo.
```
# Going to the downloads folder
python get-pip.py
```
You can do it at a time in GNU/Linux and MacOS systems with a couple of commands:
```
# Downloading
wget https://bootstrap.pypa.io/get-pip.py
# Installing as root
sudo python get-pip.py
```
Try again and check if the new pip version is installed.


2 - Installing OSRFramework from Pip
------------------------------------
When installing OSRFramework you have to know that several packages and dependencies will be managed by the installer. The instuctions on how to install this may vary depending on the system.

### In (Most) GNU/Linux Systems and MacOS

The fast way to do it on almost any system is by installing it with:
```
pip install osrframework --user
```

You should be able to run `usufy.py`, `mailfy.py`, etc. from the terminal because these scripts have been added to the `~/.local/bin/` folder.

#### Known Possible Issues

If you are receiving an error saying that it cannot find `usufy.py: command not found`, check if the given folder is in the `PATH` with:
```
echo $PATH
```
If you cannot find the given folder in the previous output, you can always manually add this folder to your `PATH` by appending these two lines to your `.bashrc` as defined in <https://github.com/i3visio/osrframework/issues/187>.
```
export PY_USER_BIN=$(python -c 'import site; print(site.USER_BASE + "/bin")')
export PATH=$PY_USER_BIN:$PATH
```

You can also try to do it installing the framework as a superuser which would add the scripts to `/usr/local/bin/`.

```
```
However, note that both approaches may interfere with other libraries that you may have installed on your system. If you are worried about this issue, check the Virtual Environment section below.

### In Windows Systems

If you have already tested that Python 2.7.x and Pip are installed, this is easy too:
```
pip install osrframework
```

### Using VirtualEnv: Recommended for Devs and Advanced Users

The Python libraries we use in OSRFramework are all required to run different utils in the framework. However, and specially if you are a developer, the required packages may broke dependencies on your system. That's why we also recommend the installation using `virtualenv`, another Python package that tries to address this issue by downloading a copy of the needed packages in a virtualized environment.

To do so, you will need to install it with `virtualenv` so as to avoid problems with dependencies with other libraries. You can use Pip to do so:
```
pip install virtualenv --user
```
Afterwards, we are creating a virtual environment that we will arbitrarily call `osrframework-virtualenv`. Anyway, you can use the name you choose:
```
virtualenv osrframework-virtualenv
```
Now, if you want to enter the newly created virtual environment, you have to activate it. Note that this will change your prompt to indicate that you are now in a virtual environment:
```
source osrframework-virtualenv/bin/activate
(osrframework-virtualenv)$
```
Now in the new virtual environment you would be able to install osrframework easily and run the applications as usual:
```
(osrframework-virtualenv)$ pip install osrframework
(osrframework-virtualenv)$ usufy.py -h
```
Note that, we may have several virtual environments in the same system, but they should be activated before using them. Whenever we want to leave the virtual environment, we can type `deactivate`. This is useful to test different OSRFramework installations in the same system avoiding conflicts between them.
```
(osrframework-virtualenv)$ pip install osrframework
```

3 - Testing the installation
-------------------------

If everything went correctly (we hope so!), it's time for trying `usufy.py`, `mailfy.py` and so on. But we are they? They are installed in your path meaning that you can open a terminal anywhere and typing the name of the program (seems to be an improvement from previous installations...). Examples:
```
usufy.py -n i3visio febrezo yrubiosec -p twitter facebook
searchfy.py -q "i3visio"
mailfy.py -n i3visio
```

4 - Updating the framework
--------------------------

OSRFramework is a tool in development mantained by its [authors](AUTHORS.md) and, thus, we will fix bugs and add new platforms from time to time. To upgrade your local osrframework installation you can type the following:
```
pip install osrframework --upgrade --user
```
Depending on how you have installed the framework, you may need to do this as superuser:
```
sudo pip install osrframework --upgrade
```
This will manage all the dependencies for you and will try to download the latest *stable* version. If you want to try a prerelease version, you can  try to upgrade or install it by appending `--pre` tag:
```
sudo pip install osrframework --upgrade --pre
```
Please, things can be unstable and lead to problems so do it under your responsibility. To minimize the effect of those strange things that may take place, you may think about installing them using `virtualenv`.

### Known Possible Issues in OSRFramework <= 0.14.3 on Windows
If you had already installed 0.14.3 or earlier versions of the framework on Windows you may face some problems with `mailfy.py` and the libraries it uses. You *should* uninstall first `dnspython` and `pyDNS` before reinstalling `osrframework` again:
```
# Uninstalling dnspython
pip uninstall dnspython
# Uninstalling pydns
pip uninstall pydns
# Reinstalling osrframework, upgrading to most recent version
pip install osrframework --upgrade
```
Anyway, if you are facing any issues regarding the installation keep us posted at <https://github.com/i3visio/osrframework/issues/>.

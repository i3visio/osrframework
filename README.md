OSRFramework
============

OSRFramework: Open Sources Research Framework

Copyright (C) 2014-2017  F. Brezo and Y. Rubio, i3visio

[![Version in PyPI](https://img.shields.io/pypi/v/osrframework.svg)]()
[![License](https://img.shields.io/badge/license-GNU%20General%20Public%20License%20Version%203%20or%20Later-blue.svg)]()

1 - Description
---------------

OSRFramework is a GNU AGPLv3+ set of libraries developed by i3visio to perform
Open Source Intelligence tasks. They include references to a bunch of different
applications related to username checking, DNS lookups, information leaks
research, deep web search, regular expressions extraction and many others.
At the same time, by means of ad-hoc Maltego transforms, OSRFramework provides
a way of making these queries graphically as well as several interfaces to
interact with like OSRFConsole or a Web interface.

2 - License: GNU AGPLv3+
------------------------

This is free software, and you are welcome to redistribute it under certain
conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, check the [COPYING](COPYING) file.

3 - Installation
----------------

Fast way to do it on any system for a user with administration privileges:
```
pip install osrframework
```
You can upgrade to the latest release of the framework with:
```
pip install osrframework --upgrade
```
This will manage all the dependencies for you and install the latest version of
the framework.

If you needed further information on how to install OSRFramework on certain
systems, note that you may need to add `export PATH=$PATH:$HOME/.local/bin` to
your `~/.bashrc_profile`). This has been confirmed in some distributions,
including MacOS. In any case, we recommend you yo have a look at the
[INSTALL.md](doc/INSTALL.md) file where we provide additional details for these
cases.

4 - Basic usage
---------------

If everything went correctly (we hope so!), it's time for trying usufy.py,
mailfy.py and so on. But we are they? They are installed in your path meaning
that you can open a terminal anywhere and typing the name of the program (seems
to be an improvement from previous installations...). Examples:
```
usufy.py -n i3visio febrezo yrubiosec -p twitter facebook
searchfy.py -q "i3visio"
mailfy.py -n i3visio
osrfconsole.py
```

Type -h or --help to get more information about which are the parameters of each
application.

You can find the configuration files in a folder created in your user home to
define the default behaviour of the applications:
```
# Configuration files for Linux and MacOS
~/.config/OSRFramework/
# Configuration files for Windows
C:\Users\<User>\OSRFramework\
```

OSRFramework will look for the configuration settings stored there. You can add
new credentials there and if something goes wrong, you can always restore the
files stored in the `defaults` subfolder.

5 - HACKING
-----------

If you want to extend the functionalities of OSRFramework and you do not know
where to start from, check the [HACKING.md](doc/HACKING.md) file.

6 - AUTHORS
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.

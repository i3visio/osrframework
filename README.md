OSRFramework
============

OSRFramework: Open Sources Research Framework

Copyright (C) 2014-2020  F. Brezo and Y. Rubio, i3visio

[![Version in PyPI](https://img.shields.io/pypi/v/osrframework.svg)]()
[![License](https://img.shields.io/badge/license-GNU%20Affero%20General%20Public%20License%20Version%203%20or%20Later-blue.svg)]()

1 - Description
---------------

OSRFramework is a GNU AGPLv3+ set of libraries developed by i3visio to perform Open Source Intelligence collection tasks.
They include references to a bunch of different applications related to username checking, DNS lookups, information leaks research, deep web search, regular expressions extraction and many others.
At the same time, by means of ad-hoc Maltego transforms, OSRFramework provides a way of making these queries graphically as well as several interfaces to interact with like OSRFConsole or a Web interface.

2 - License: GNU AGPLv3+
------------------------

This is free software, and you are welcome to redistribute it under certain conditions.

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
pip3 install osrframework
```
You can upgrade to the latest release of the framework with:
```
pip3 install osrframework --upgrade
```
This will manage all the dependencies for you and install the latest version of the framework.

If you needed further information on how to install OSRFramework on certain systems, note that you may need to add `export PATH=$PATH:$HOME/.local/bin` to your `~/.bashrc_profile`). This has been confirmed in some distributions, including MacOS.
In any case, we recommend you yo have a look at the [INSTALL.md](doc/INSTALL.md) file where we provide additional details for these cases.

4 - Basic usage
---------------

If everything went correctly (we hope so!), it's time for trying usufy., mailfy and so on.
But we are they
? They are installed in your path meaning that you can open a terminal anywhere and typing the name of the program (seems to be an improvement from previous installations...). Examples:
```
osrf --help
usufy -n i3visio febrezo yrubiosec -p twitter facebook
searchfy -q "i3visio"
mailfy -n i3visio
```

Type -h or --help to get more information about which are the parameters of each application.

The tools installed in this package include:

- `alais_generator`. Generates candidate nicknames based on known info about the target. **Input**: information about the target. **Output**: list of possible nicknames.
- `checkfy`. Guesses possible emails based on a list of candidate nicknames and a pattern. **Input**: list of nicknames and an email pattern. **Output**. list of emails matching the pattern..
- `domainfy`. Finds domains that currently resolve using a given word or nickname. **Input**: liat of words. **Output**: domains using that word that currently resolve.
- `mailfy`. Find more information about emails taken as a reference either a nickname (to generate a  list of possible emails) or the email list. **Input**: list of nicknames or emails. **Output**: found information about the email.
- `osrf`. Shared wrapper for the rest of the applications. All commands can also be used as `osrf usufy…`, `osrf mailfy…`, etc.
- `phonefy`. Recovers information about mobile phones linked to known spam practices. **Inputs**: list of phones. **Outputs**: Phones linked to spam.
- `searchfy`. Finds profiles linked to a fullname. **Inputs**: list of phones. **Outputs**: Known profiles linked to the query.
- `usufy`. Identifies socialmedia profiles using a given nickname. **Inputs**: list of nicknames. **Outputs**: Known profiles in socialmedia using those nicknames.

You can find the configuration files in a folder created in your user home to define the default behaviour of the applications:
```
# Configuration files for Linux and MacOS
~/.config/OSRFramework/
# Configuration files for Windows
C:\Users\<User>\OSRFramework\
```

OSRFramework will look for the configuration settings for each application stored there.
You can add new credentials there and if something goes wrong, you can always restore the files stored in the `defaults` subfolder.

If you are experiencing problems, you might fight relevant information in the (FAQ Section)[doc/FAQ.md].

5 - HACKING
-----------

If you want to extend the functionalities of OSRFramework and you do not know where to start from, check the [HACKING.md](doc/HACKING.md) file.

6 - AUTHORS
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.

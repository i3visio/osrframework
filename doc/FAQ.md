Frequent Asked Questions
========================

In this section, we will try to address some of the most common questions we have heard about the platform.
Anyway, if the issue is not listed here, feel free to [report an issue](https://github.com/i3visio/osrframework/issues/new).

Table of Contents
------------------

1. [Installation and Deployment Issues](#installation-and-deployment-issues)
2. [General Usage Questions](#general-usage-questions)

Installation and Deployment Issues
----------------------------------

# Can I install OSRFramework in my Windows machine?

Yes, you can.
You still need to download [Python 3](https://www.python.org/downloads/release/python-2715/) from the official website.
Make sure that you click on `Add python.exe to the system path`.
Then, check that Python is reachable typing `python.exe --version` in a CMD.
The output should look like this:

```
Python 3.7.5
```

If this is not the case and Python is not recognised, you can follow [these steps](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path).

You can then proceed as follows installing OSRFramework:

```
pip install osrframework
```

After a while, `usufy`, `mailfy` and the rest of the tools will be reachable.


# Why there is no support to Python 2?

Moving to Python 3 was in our roadmap since the beginning of the development.
It required some important changes from the original source code and since 0.20.0, OSRFramework is only supported in Python 3.6+.

# Why it does not work in Python 3.5 and below?

Python 3 f-strings where introduced in Python 3.6 and they are required.
It is recommened to use them instead of spaghetti code and .format clauses.
More information about them can be found in [PEP498](https://www.python.org/dev/peps/pep-0498/).

# Why I receive a `command not found` error after installing and calling `usufy`?

This is a known issue in certain GNU/Linux systems such as some Ubuntu versions.
When installed with `--user`, `pip` installs the user entry points in `~/.local/bin/` folder.
This folder is generally in the System Path but in some systems that's not the case.

There are several workarounds to this:

- Installing it as root
- Adding `~/.local/bin` to the USER's path on each startup of the terminal:

```
PATH=$PATH:~/.local/bin
```

- Running the commands from that folder (note that you would need `./` before each command since you are running the local versions):
```
cd ~/.local/bin
./usufy
```

Check the [`INSTALL.md`](INSTALL.md) file for further details on the installation.

General Usage Questions
-----------------------

# What is the difference between `osrf usufy` and `usufy`?

Technically none.
`osrf` is just an entry point that provided an overview of the tools in the framework.
Thus, doing `osrf --help` can be used to list all the available commands.

```
$ osrf --help
usage: osrf [-h] [--license] [--version]
            <sub_command> <sub_command_options> ...

OSRFramework CLI. Collection of tools included in the framework.

SUBCOMMANDS:
  List of available commands that can be invoked using OSRFramework CLI.

  <sub_command> <sub_command_options>
    alias_generator     Generates a list of candidate usernames based on known
                        information.
    checkfy             Verifies if a given email address matches a pattern.
    domainfy            Checks whether domain names using words and nicknames
                        are available.
    mailfy              Gets information about email accounts.
    phonefy             Looks for information linked to spam practices by a
                        phone number.
    searchfy            Performs queries on several platforms.
    usufy               Looks for registered accounts with given nicknames.
    upgrade             Updates the module.

ABOUT ARGUMENTS:
  Showing additional information about this program.

  -h, --help            shows this help and exists.
  --license             shows the AGPLv3+ license and exists.
  --version             shows the version of the program and exists.

Use 'osrf <command> --help' to learn more about each command. Check
OSRFramework README.md file for further details on the usage of this program
or follow us on Twitter in <http://twitter.com/i3visio>.
```

Note that it also shows a `upgrade` subcommand that can be used to try to upgrade the current package.

# I see some false positives whenever I launch usufy -n my_nick -p all. What can I do to remove the non-working wrappers?

You have two options:

- **Excluding manually with each call**. You can do it by manually appending `-x facebook` or `--exclude facbeook` to exclude the Facebook wrapper.
- **Excluding them using the configuration file**. In the `general.cfg` file you can specify which platforms to exclude on each call. In GNU/Linux systems and MacOS machines the file can be found in `~/.config/OSRFramework`. In Windows systems, in the home folder of the user `<USER_HOME>/OSRFramework`. The file is a text file which can be edited with any text editor. The only lines to change are the last ones so as to set the  `exclude_platforms` to any list of space-separated list of wrappers. For instance, if you needed to exclude the Facebook and Instagram platforms you will have to set the `exclude_platforms` by typing `exclude_platforms = facebook instagram`. Remember that lines starting with a `#` are not interpreted and are provided as examples.

```
…
# Platforms to be manually excluded
exclude_platforms = facebook instagram
#exclude_platforms = twitter skype
```

# How can I export the results to an Excel file directly?

Although by default OSRFramework creates a `csv` file, you can always export the results to `xls`. `xlsx` or other formats. You can do it by launching it with the option `-e` or `--extension`:

```
usufy -n i3visio -p twitter -e xls gml csv
```

This command will create three different files in the current folder: `profiles.csv`, `profiles.gml` and `profiles.xls`.

# How can I open the results in the browser?

To open the found profiles in a web browser so as to perform a manual analysis, just use `-w` or `--web_browser`. For example:

```
usufy -n i3visio -p twitter -w
```

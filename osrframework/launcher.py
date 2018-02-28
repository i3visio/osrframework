#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2015-2018 Félix Brezo and Yaiza Rubio
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

import argparse
import sys

import osrframework
import osrframework.utils.general as general
import osrframework.alias_generator as alias_generator
import osrframework.domainfy as domainfy
import osrframework.entify as entify
import osrframework.mailfy as mailfy
import osrframework.phonefy as phonefy
import osrframework.searchfy as searchfy
import osrframework.usufy as usufy


EPILOG = """
  Use 'osrf <command> --help' to learn more about each command.\n\n

  Check OSRFramework README.md file for further details on the usage of this
  program or follow us on Twitter in <http://twitter.com/i3visio>.
"""


class OSRFParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("The following error was thrown by '%s' when parsing the provided parameters:\n\t%s\n\n" % (self.prog, message))
        self.print_help()
        sys.exit(2)

def getParser():
    parser = OSRFParser(
        description='OSRFramework CLI',
        prog='osrf',
        epilog=EPILOG,
        conflict_handler='resolve'
    )

    # Add subcommands as subparsers
    subcommands = parser.add_subparsers(
        title="SUBCOMMANDS",
        description="List of available commands that can be invoked using OSRFramework CLI.",
        metavar="<sub_command> <sub_command_options>",
        dest='command_name'
    )

    subparser_alias_generator = subcommands.add_parser(
        "alias_generator",
        help="Generates a list of candidate usernames based on known information.",
        parents=[alias_generator.getParser()]
    )
    subparser_domainfy = subcommands.add_parser(
        "domainfy",
        help="Checks whether domain names using words and nicknames are available.",
        parents=[domainfy.getParser()]
    )
    subparser_entify = subcommands.add_parser(
        "entify",
        help="Extracts entities using regular expressions from provided URIs.",
        parents=[entify.getParser()]
    )
    subparser_mailfy = subcommands.add_parser(
        "mailfy",
        help="Gets information about email accounts. ",
        parents=[mailfy.getParser()]
    )
    subparser_phonefy = subcommands.add_parser(
        "phonefy",
        help="Looks for information linked to spam practices by a phone number.",
        parents=[phonefy.getParser()]
    )
    subparser_searchfy = subcommands.add_parser(
        "searchfy",
        help="Performs queries on several platforms",
        parents=[searchfy.getParser()]
    )
    subparser_usufy = subcommands.add_parser(
        "usufy",
        help="Looks for registered accounts with given nicknames",
        parents=[usufy.getParser()]
    )

    # About options
    groupAbout = parser.add_argument_group('ABOUT ARGUMENTS', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--license', action='store_true', default=False, help='shows the AGPLv3+ license and exists.')
    groupAbout.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(params=None):
    """
    Main function to launch OSRFramework CLI

    The function is created in this way so as to let other applications make
    use of the full configuration capabilities of the application. The
    parameters received are used as parsed by this modules `getParser()`.

    Args:
    -----
        params: A list with the parameters as grabbed by the terminal. It is
            None when this is called by an entry_point.

    Returns:
    --------
        Returns 0 if execution was successful and 1 for failed executions.
    """
    parser = getParser()

    try:
        if params != None:
            args = parser.parse_args(params)
        else:
            args = parser.parse_args()
    except:
        sys.exit(0)

    if args.license:
        general.showLicense()

    # Launch the appropiate util
    module = __import__(args.command_name)
    module.main(params[1:])
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])

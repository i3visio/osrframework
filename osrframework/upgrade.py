################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
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
import datetime as dt
import json
import os
from subprocess import call
import sys

import osrframework
import osrframework.utils.general as general
from osrframework.utils.updates import UpgradablePackage
import osrframework.utils.banner as banner

def get_parser():
    parser = argparse.ArgumentParser(description='OSRFramework upgrade script.', prog='upgrade', epilog='Check the README.md file for further details on the usage of this program or follow us on Twitter in <http://twitter.com/i3visio>.', add_help=False, conflict_handler='resolve')

    # Configuring the processing options
    group_processing = parser.add_argument_group('Processing arguments', 'For the wrapper')
    group_processing.add_argument('--only-check', action='store_true', default=False, help='prevents the script from upgradeing OSRFramework')
    group_processing.add_argument('--use-development', action='store_true', default=False, help='looks for development versions')


    # About options
    group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    group_about.add_argument('--version', action='version', version='[%(prog)s] OSRFramework ' + osrframework.__version__, help='shows the version of the program and exists.')

    return parser


def main(args=None):
    print(general.title(banner.text))

    saying_hello = f"""
      OSRFramework Upgrade Tool | Copyright (C) Yaiza Rubio & Félix Brezo (i3visio) 2014-2020

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit <{general.LICENSE_URL}>.
"""
    print(general.info(saying_hello))

    startTime = dt.datetime.now()
    print(f"{startTime}\tGrabbing information about local and upstream versions of OSRFramework…\n")
    package = UpgradablePackage(package_name="osrframework")
    print(f"Details:\n{general.emphasis(json.dumps(package.get_dict(), indent=2))}\n")

    now = dt.datetime.now()
    if package.is_upgradable():
        print(f"{now}\tLocal version of OSRFramework {general.warning('can be upgraded')} to version {package.get_dict()['remote_version']}.\n")
        if not args.only_check:
            now = dt.datetime.now()
            cmd = ["pip3", "install", "osrframework", "--upgrade"]

            # Installing development versions
            if args.use_development:
                cmd.append("--pre")

            # Make installation for the user
            if not sys.platform == 'win32' or os.geteuid() != 0:
                cmd.append("--user")
            print(f"{now}\tTrying to upgrade the package running '{' '.join(cmd)}'...")

            status = call(cmd)
            if status:
                # Displaying a warning if this is being run in a windows system
                if sys.platform == 'win32':
                    print(f"{now}\t{general.error('Installation failed')}.")
                else:
                    print(f"{now}\t{general.error('Installation failed')}. Retry the installation as a superuser: '{' '.join(['sudo'] + cmd)}'")
                sys.exit(1)
            else:
                print(f"{now}\t{general.error('Installation sucessful')}. Upgraded to '{general.success(package.get_dict()['remote_version'])}'.")

    else:
        print(f"{now}\tLocal version of OSRFramework ({package.get_dict()['local_version']}) {general.success('is up to date')} with the remote version ({package.get_dict()['remote_version']}).\n")


if __name__ == "__main__":
    main(sys.argv[1:])

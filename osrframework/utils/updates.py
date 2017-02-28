# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2014-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero  General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import xmlrpclib
import pip


def hasUpdatesOnPypi(packageName="osrframework"):
    installedPackage = None
    for dist in pip.get_installed_distributions():
        if dist.project_name == packageName:
            installedPackage = dist
            break

    pypi = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    # This is an array
    version_available = pypi.package_releases(packageName)
    try:
        if version_available[0] == installedPackage.version:
            # No updates available
            return False, installedPackage.version
        else:
            # There are updates available!
            return True, version_available[0]
    except IndexError as e:
        if not installedPackage:
            # Yes, the package has no version on Pypi
            return False, "No version found"


if __name__ == "__main__":
    print hasUpdatesOnPypi()

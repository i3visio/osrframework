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

import xmlrpc.client
try:
    from pip._internal.utils.misc import get_installed_distributions
except ImportError:  # pip<10
    from pip import get_installed_distributions


class UpgradablePackage(object):
    def __init__(self, package_name="osrframework",
                 repository='https://pypi.python.org/pypi'):
        """Checks if a locally installed package has an update

        Args:
            packake_name (str): The name of the package.
            repository (str): Defines the repository. By default, the official
                one.
        """
        installed_package = None
        self.local_version = None
        self.remote_version = None
        self.repository = repository

        for dist in get_installed_distributions():
            if dist.project_name == package_name:
                installed_package = dist
                try:
                    self.local_version = installed_package.version
                except AttributeError:
                    pass
                break

        pypi = xmlrpc.client .ServerProxy(repository)
        # This is an array
        version_available = pypi.package_releases(package_name)

        try:
            self.remote_version = version_available[0]
            if version_available[0] < installed_package.version:
                # No updates available
                self.status = "unstable"
            elif version_available[0] == installed_package.version:
                # No updates available
                self.status = "up-to-date"
            else:
                # There are updates available!
                self.status = "outdated"
        except IndexError:
            self.status = "unknown"

    def get_dict(self):
        """Returns a dict representing the object representation

        Returns:
            A dict representing the information stored.
        """
        return {
            "status": self.status,
            "local_version": self.local_version,
            "remote_version": self.remote_version,
            "repository": self.repository,
        }

    def is_upgradable(self):
        """Checks if a locally stored version of a file is outdated

        Returns:
            Bool if the local version is smaller than the remote one.
        """
        return self.local_version < self.remote_version


if __name__ == "__main__":
    print(UpgradablePackage(package_name="osrframework").get_dict())

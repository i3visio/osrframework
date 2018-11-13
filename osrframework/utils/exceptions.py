# -*- coding: utf-8 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


import os

import osrframework.utils.configuration as configuration
import osrframework.utils.general as general


class OSRFrameworkException(Exception):
    """
    Generic OSrframework Exception

    It will be used to show warnings, i. e., any operation which throws an
    exception but which does not stop OSRFramework from running.

    Messages will be printed as warnings, in orange.
    """
    def __init__(self, msg, *args, **kwargs):
        Exception.__init__(self, general.warning(msg))
        self.generic = "Generic OSRFramework exception."


class NoCredentialsException(OSRFrameworkException):
    def __init__(self, platform, *args, **kwargs):
        msg = """
        [*] Warning:\t{}. Details:
            No valid credentials provided for '{}'.
            Update the configuration file at: '{}'.
            """.format(
            self.__class__.__name__,
            platform,
            os.path.join(configuration.getConfigPath()["appPath"], "accounts.cfg"),
            general.emphasis("-x " + platform)
        )
        OSRFrameworkException.__init__(self, general.warning(msg))
        self.generic = "The credentials for some platforms where NOT provided."


class OSRFrameworkError(Exception):
    """
    Generic OSrframework Error

    It will be used to show errors, i. e., any operation which throws an error
    from which OSRFramework cannot get recovered.

    Messages will be printed as errors, in red.
    """
    def __init__(self, msg, *args, **kwargs):
        Exception.__init__(self, "{}".format(general.error(msg)))
        self.generic = "Generic OSRFramework error."


class NotImplementedModeError(OSRFrameworkError):
    def __init__(self, platform, mode, *args, **kwargs):
        msg = """
        [*] Error:\t{}. Details:
            The  '{}' wrapper has tried to call 'self.do_{}(...)'.
            The method seems be implemented wrongly or not implemented.""".format(
            self.__class__.__name__,
            platform,
            mode
        )
        OSRFrameworkError.__init__(self, msg)
        self.generic = "A wrapper has tried to launch a mode which is not yet implemented. This error should not be happening unless you have added a new method out of the standard ones for mailfy, phonefy, searchfy or usufy."

class BadImplementationError(OSRFrameworkError):
    def __init__(self, original_message, *args, **kwargs):
        msg = """
        [*] Error:\t{}. Details:
            {}.
            {}""".format(
            self.__class__.__name__,
            original_message,
            "The wrapper may be missing an attribute like self.creds empty list in its constructor."
        )
        OSRFrameworkError.__init__(self, msg)
        self.generic = "A wrapper has launched an unexpected implementation error."

################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#   This program is part of OSRFramework. You can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import textwrap
import random

import osrframework
import osrframework.utils.general as general
import osrframework.utils.fortunes as fortunes

release = "OSRFramework " + osrframework.__version__

logo = """
        .===========================================================.
        |...........................................................|
        |...........................................................|
        |...........................................................|
        |.......................              ......................|
        |...................                    ....................|
        |...................                      ..................|
        |..................                       ..................|
        |..................                        .................|
        |..................                       ..................|
        |..................                      ...................|
        |..................                      ...................|
        |..................                      ...................|
        |.................                         .................|
        |.................                        ..................|
        |..................                       ..................|
        |...................                    ....................|
        |....................                   ....................|
        |....................                  .....................|
        |......................               ......................|
        |......................               ......................|
        |.....................                 .....................|
        |.....................                 .....................|
        |....................                   ....................|
        |..................                       ..................|
        |..............                               ..............|
        |..........                                       ..........|
        |......                                               ......|
        |....{}....|
        |..                                                       ..|
        '==========================================================='
    """.format(release.center(51))


title = """
     ___  ____  ____  _____                                            _
    / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
   | | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
   | |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
    \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\\
"""

header = """
    {}

    {}

                   Coded with {} by {} & {}


{}
    """

text = textwrap.dedent(
    header.format(
        general.colorize(logo, "INFO BOLD"),
        general.colorize(title, "BOLD"),
        general.colorize("♥", "ERROR BOLD"),
        general.colorize("Yaiza Rubio", "SUCCESS BOLD"),
        general.colorize("Félix Brezo", "SUCCESS BOLD"),
        general.colorize(random.choice(fortunes.messages).center(80), "WARNING")
    )
)



footer = """
Did something go wrong? Is a platform reporting false positives? Do you need to
integrate a new one and you don't know how to start? Then, you can always place
an issue in the Github project:
    https://github.com/i3visio/osrframework/issues
Note that otherwise, we won't know about it!
"""

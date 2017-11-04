# -*- coding: utf-8 -*-
#
##################################################################################
#
#    Copyright 2015-2017 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
#
#    This file is part of OSRFramework. You can redistribute it and/or modify
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
##################################################################################

import colorama

import osrframework

colorama.init(autoreset=True)

text = colorama.Fore.BLUE + colorama.Style.BRIGHT + """
     ___  ____  ____  _____                                            _
    / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
   | | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
   | |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
    \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\\


                Version:      OSRFramework """ + osrframework.__version__ + """
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)

"""

footer = """
Did something go wrong? Is a platform reporting false positives? Do you need to
integrate a new one and you don't know how to start? Then, you can always place
an issue in the Github project:
    https://github.com/i3visio/osrframework/issues
Note that otherwise, we won't know about it!
"""

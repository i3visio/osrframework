# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    Copyright 2015 Félix Brezo and Yaiza Rubio (i3visio, contacto@i3visio.com)
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

import webbrowser as wb

from osrframework.transforms.lib.maltego import *

def coordinatesToTwitterBrowser(coord=None, proximity="20km"):
    ''' 
        Method that launches the URI in the default browser of the system with all the tweets in a given location. This returns no new entity.

        :param coord:    coordinates in which the lookup will be done.
    '''
    me = MaltegoTransform()

    # Building Google Maps coordinates
    coord = coord.replace(' ','')
    coord = coord.replace(',','%2C')
    uri = "https://twitter.com/search?q=geocode%3A"+coord+"%2C"+proximity+"&src=typd"

    wb.open(uri, new=2)    

    me.returnOutput()


if __name__ == "__main__":
    coordinatesToTwitterBrowser(coord=sys.argv[1], proximity="20km")



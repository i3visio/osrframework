# !/usr/bin/python
# -*- coding: cp1252 -*-
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

__all__ = ['search']

import argparse
import json
import os
import sys
import time

if sys.version_info[0] > 2:
    from http.cookiejar import LWPCookieJar
    from urllib.request import Request, urlopen
    from urllib.parse import quote_plus, urlparse, parse_qs
else:
    from cookielib import LWPCookieJar
    from urllib import quote_plus
    from urllib2 import Request, urlopen
    from urlparse import urlparse, parse_qs

# Lazy import of BeautifulSoup.
BeautifulSoup = None

# URL templates to make Google searches.
url_home          = "http://www.google.%(tld)s/"
url_search        = "http://www.google.%(tld)s/search?hl=%(lang)s&q=%(query)s&btnG=Google+Search&inurl=https"
url_next_page     = "http://www.google.%(tld)s/search?hl=%(lang)s&q=%(query)s&start=%(start)d&inurl=https"
url_search_num    = "http://www.google.%(tld)s/search?hl=%(lang)s&q=%(query)s&num=%(num)d&btnG=Google+Search&inurl=https"
url_next_page_num = "http://www.google.%(tld)s/search?hl=%(lang)s&q=%(query)s&num=%(num)d&start=%(start)d&inurl=https"

# Cookie jar. Stored at the user's home folder.
home_folder = os.getenv('HOME')
if not home_folder:
    home_folder = os.getenv('USERHOME')
    if not home_folder:
        home_folder = '.'   # Use the current folder on error.
cookie_jar = LWPCookieJar(os.path.join(home_folder, '.google-cookie'))
try:
    cookie_jar.load()
except Exception:
    pass

# Request the given URL and return the response page, using the cookie jar.
def get_page(url):
    """
    Request the given URL and return the response page, using the cookie jar.

    @type  url: str
    @param url: URL to retrieve.

    @rtype:  str
    @return: Web page retrieved for the given URL.

    @raise IOError: An exception is raised on error.
    @raise urllib2.URLError: An exception is raised on error.
    @raise urllib2.HTTPError: An exception is raised on error.
    """
    request = Request(url)
    request.add_header('User-Agent',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
    cookie_jar.add_cookie_header(request)
    response = urlopen(request)
    cookie_jar.extract_cookies(response, request)
    html = response.read()
    response.close()
    cookie_jar.save()
    return html

# Filter links found in the Google result pages HTML code.
# Returns None if the link doesn't yield a valid result.
def filter_result(link):
    try:

        # Valid results are absolute URLs not pointing to a Google domain
        # like images.google.com or googleusercontent.com
        o = urlparse(link, 'http')
        if o.netloc and 'google' not in o.netloc:
            return link

        # Decode hidden URLs.
        if link.startswith('/url?'):
            link = parse_qs(o.query)['q'][0]

            # Valid results are absolute URLs not pointing to a Google domain
            # like images.google.com or googleusercontent.com
            o = urlparse(link, 'http')
            if o.netloc and 'google' not in o.netloc:
                return link

    # Otherwise, or on error, return None.
    except Exception:
        pass
    return None

# Returns a generator that yields URLs.
def search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0,
           only_standard=False):
    """
    Search the given query string using Google.

    @type  query: str
    @param query: Query string. Must NOT be url-encoded.

    @type  tld: str
    @param tld: Top level domain.

    @type  lang: str
    @param lang: Languaje.

    @type  num: int
    @param num: Number of results per page.

    @type  start: int
    @param start: First result to retrieve.

    @type  stop: int
    @param stop: Last result to retrieve.
        Use C{None} to keep searching forever.

    @type  pause: float
    @param pause: Lapse to wait between HTTP requests.
        A lapse too long will make the search slow, but a lapse too short may
        cause Google to block your IP. Your mileage may vary!

    @type  only_standard: bool
    @param only_standard: If C{True}, only returns the standard results from
        each page. If C{False}, it returns every possible link from each page,
        except for those that point back to Google itself. Defaults to C{False}
        for backwards compatibility with older versions of this module.

    @rtype:  generator
    @return: Generator (iterator) that yields found URLs. If the C{stop}
        parameter is C{None} the iterator will loop forever.
    """

    # Lazy import of BeautifulSoup.
    # Try to use BeautifulSoup 4 if available, fall back to 3 otherwise.
    global BeautifulSoup
    if BeautifulSoup is None:
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            from BeautifulSoup import BeautifulSoup

    # Set of hashes for the results found.
    # This is used to avoid repeated results.
    hashes = set()

    # Prepare the search string.
    query = quote_plus(query)

    # Grab the cookie from the home page.
    get_page(url_home % vars())

    # Prepare the URL of the first request.
    if start:
        if num == 10:
            url = url_next_page % vars()
        else:
            url = url_next_page_num % vars()
    else:
        if num == 10:
            url = url_search % vars()
        else:
            url = url_search_num % vars()

    # Loop until we reach the maximum result, if any (otherwise, loop forever).
    while not stop or start < stop:

        # Sleep between requests.
        time.sleep(pause)

        # Request the Google Search results page.
        html = get_page(url)

        # Parse the response and process every anchored URL.
        soup = BeautifulSoup(html)
        anchors = soup.find(id='search').findAll('a')
        for a in anchors:

            # Leave only the "standard" results if requested.
            # Otherwise grab all possible links.
            if only_standard and (
                        not a.parent or a.parent.name.lower() != "h3"):
                continue

            # Get the URL from the anchor tag.
            try:
                link = a['href']
            except KeyError:
                continue

            # Filter invalid links and links pointing to Google itself.
            link = filter_result(link)
            if not link:
                continue

            # Discard repeated results.
            h = hash(link)
            if h in hashes:
                continue
            hashes.add(h)

            # Yield the result.
            yield link

        # End if there are no more results.
        if not soup.find(id='nav'):
            break

        # Prepare the URL for the next request.
        start += num
        if num == 10:
            url = url_next_page % vars()
        else:
            url = url_next_page_num % vars()

# Returns a generator that yields URLs.
def processSearch(query, tld='com', lang='en', num=10, start=0, stop=50, pause=2.0, only_standard=False):
    ''' 
        Method that recovers the URI for a search returning an i3visio-compliant json object.
        
        :return:    A json-like object.

    '''
    uriList = search(query, tld=tld, lang=lang, num=int(num), start=int(start), stop=int(stop), pause=float(pause),only_standard=only_standard)       
    
    # Dictionary containing the URI objects
    results = []
    
    # Building the objects
    for uri in uriList:
        aux = {}
        aux["type"] = "i3visio.uri"
        aux["value"] = uri        
        aux["attributes"] = []
        results.append(aux)

    return results
    
# When run as a script...
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A package that allows the execution of searches in Google.', prog='google.py', add_help=False)
    parser.add_argument("-q", "--query", metavar="<QUERY>", required = True, help="Query to be performed.")
    parser.add_argument("--tld", metavar="TLD", default="com", help="top level domain to use [default: com]")
    parser.add_argument("--lang", metavar="LANGUAGE", default="en",help="produce results in the given language [default: en]")
    parser.add_argument("--num", metavar="NUMBER", type=int, default=10,help="number of results per page [default: 10]")
    parser.add_argument("--start", metavar="NUMBER", type=int, default=0, help="first result to retrieve [default: 0]")
    parser.add_argument("--stop", metavar="NUMBER", type=int, default=50, help="last result to retrieve [default: 100]")
    parser.add_argument("--pause", metavar="SECONDS", type=float, default=2.0, help="pause between HTTP requests [default: 2.0]")
    parser.add_argument("--all", dest="only_standard", action="store_false", default=True, help="grab all possible links from result pages")

    groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')
    args = parser.parse_args()

    print "Searching..." 
    
    results = processSearch(args.query, tld=args.tld, lang=args.lang, num=int(args.num), start=int(args.start), stop=int(args.stop), pause=float(args.pause),only_standard=args.only_standard)

    print json.dumps(results, indent=2)
                    

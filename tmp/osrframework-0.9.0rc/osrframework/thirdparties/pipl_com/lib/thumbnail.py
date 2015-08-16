"""Python wrapper for Pipl's Thumbnail API.

Pipl's thumbnail API provides a thumbnailing service for presenting images in 
your application. The images can be from the results you got from our Search
API but it can also be any web URI of an image.

The thumbnails returned by the API are in the height/width defined in the 
request. Additional features of the API are:
- Detect and Zoom-in on human faces (in case there's a human face in the image).
- Optionally adding to the thumbnail the favicon of the website where the image 
  is from (for attribution, recommended for copyright reasons).

This module contains only one function - generate_thumbnail_url() that can be 
used for transforming an image URL into a thumbnail API URL.

"""
import urllib

from osrframework.thirdparties.pipl_com.lib import Image
from osrframework.thirdparties.pipl_com.lib.utils import to_utf8


BASE_URL = 'http://api.pipl.com/thumbnail/v2/?'
# HTTPS is also supported:
#BASE_URL = 'https://api.pipl.com/thumbnail/v2/?'

MAX_PIXELS = 500


# Default API key value, you can set your key globally in this variable instead 
# of passing it in each call to generate_thumbnail_url().
# >>> import osrframework.thirdparties.pipl_com.lib.thumbnail
# >>> osrframework.thirdparties.pipl_com.lib.thumbnail.default_api_key = '<your_key>'
default_api_key = None


def generate_thumbnail_url(image_url, height, width, favicon_domain=None, 
                           zoom_face=True, api_key=None):
    """Take an image URL and generate a thumbnail URL for that image.
    
    Args:
    
    image_url -- unicode (or utf8 encoded str), URL of the image you want to 
                 thumbnail.   
    height -- int, requested thumbnail height in pixels, maximum 500.
    width -- int, requested thumbnail width in pixels, maximum 500.
    favicon_domain -- unicode (or utf8 encoded str), optional, the domain of 
                      the website where the image came from, the favicon will 
                      be added to the corner of the thumbnail, recommended for 
                      copyright reasones.
                      IMPORTANT: Don't assume that the domain of the website is
                      the domain from `image_url`, it's possible that 
                      domain1.com hosts its images on domain2.com.
    zoom_face -- bool, indicates whether you want the thumbnail to zoom on the 
                 face in the image (in case there is a face) or not.
    api_key -- str, a valid API key (use "samplekey" for experimenting).
               Note that you can set a default API key
               (osrframework.thirdparties.pipl_com.lib.thumbnail.default_api_key = '<your_key>') instead of 
               passing your key in each call.
    
    ValueError is raised in case of illegal parameters.
    
    Example (thumbnail URL from an image URL):
    
    >>> from osrframework.thirdparties.pipl_com.lib.thumbnail import generate_thumbnail_url
    >>> image_url = 'http://a7.twimg.com/a/ab76f.jpg'
    >>> generate_thumbnail_url(image_url, 100, 100, 
                               favicon_domain='twitter.com',
                               api_key='samplekey')
    'http://api.pipl.com/thumbnail/v2/?key=samplekey&
    favicon_domain=twitter.com&height=100&width=100&zoom_face=True&
    image_url=http%3A%2F%2Fa7.twimg.com%2Fa%2Fab76f.jpg'
    
    Example (thumbnail URL from a record that came in the response of our 
    Search API):
    
    >>> from osrframework.thirdparties.pipl_com.lib.thumbnail import generate_thumbnail_url
    >>> generate_thumbnail_url(record.images[0].url, 100, 100, 
                               favicon_domain=record.source.domain,
                               api_key='samplekey')
    'http://api.pipl.com/thumbnail/v2/?key=samplekey&
    favicon_domain=twitter.com&height=100&width=100&zoom_face=True&
    image_url=http%3A%2F%2Fa7.twimg.com%2Fa%2Fab76f.jpg'
    
    """
    if not (api_key or default_api_key):
        raise ValueError('A valid API key is required')
    if not Image(url=image_url).is_valid_url:
        raise ValueError('image_url is not a valid URL')
    if not (0 < height <= MAX_PIXELS and 0 < width <= MAX_PIXELS):
        raise ValueError('height/width must be between 0 and %d' % MAX_PIXELS)
    query = {
        'key': to_utf8(api_key or default_api_key),
        'image_url': urllib.unquote(to_utf8(image_url)),
        'height': height,
        'width': width,
        'favicon_domain': to_utf8(favicon_domain or ''),
        'zoom_face': zoom_face,
    }
    return BASE_URL + urllib.urlencode(query)

from osrframework.thirdparties.pipl_com.lib.fields import Field
from osrframework.thirdparties.pipl_com.lib.utils import is_valid_url


class Source(Field):
    
    """A source of data that's available in a Record/Person object.
    
    The source is simply the URL of the page where the data was found, for 
    convenience it also contains some meta-data about the data-source (like
    its full name and the category it belongs to).
    
    Note that this class is a subclass of Field even though a source is not 
    exactly a data field, it's just because the functionality implemented in 
    Field is usefull here too.
    
    """
    
    attributes = ('is_sponsored',)
    children = ('name', 'category', 'url', 'domain')
    categories = set(['background_reports', 'contact_details', 
                      'email_address', 'media', 'personal_profiles', 
                      'professional_and_business', 'public_records', 
                      'publications', 'school_and_classmates', 'web_pages'])
    
    def __init__(self, name=None, category=None, url=None, domain=None,  
                 is_sponsored=None):
        """`name`, `category`, `url` and `domain` should all be unicode or utf8 
        encoded strs (will be decoded automatically).
        
        `is_sponsored` is a bool value that indicates whether the source is from 
        one of Pipl's sponsored sources.
        
        `category` is one of Source.categories.
        
        """
        Field.__init__(self)
        self.name = name
        self.category = category
        self.url = url
        self.domain = domain
        self.is_sponsored = is_sponsored
    
    @property
    def is_valid_url(self):
        """A bool that indicates whether the URL is valid."""
        return bool(self.url and is_valid_url(self.url))
    
    @staticmethod
    def validate_categories(categories):
        """Take an iterable of source categories and raise ValueError if some 
        of them are invalid."""
        if not set(categories) <= Source.categories:
            invalid = list(set(categories) - Source.categories)
            raise ValueError('Invalid categories: %s' % invalid)
        

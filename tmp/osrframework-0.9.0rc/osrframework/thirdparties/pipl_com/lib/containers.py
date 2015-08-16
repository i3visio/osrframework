from osrframework.thirdparties.pipl_com.lib.fields import *
from osrframework.thirdparties.pipl_com.lib.source import Source
from osrframework.thirdparties.pipl_com.lib.utils import *


__all__ = ['Record', 'Person']


class FieldsContainer(object):
    
    """The base class of Record and Person, made only for inheritance."""
    
    class_container = {
        Name: 'names', 
        Address: 'addresses', 
        Phone: 'phones', 
        Email: 'emails', 
        Job: 'jobs', 
        Education: 'educations', 
        Image: 'images', 
        Username: 'usernames', 
        UserID: 'user_ids', 
        DOB: 'dobs', 
        RelatedURL: 'related_urls', 
        Relationship: 'relationships', 
        Tag: 'tags', 
    }
    
    def __init__(self, fields=None):
        """`fields` is an iterable of field objects from 
        osrframework.thirdparties.pipl_com.lib.fields."""
        self.names = []
        self.addresses = []
        self.phones = []
        self.emails = []
        self.jobs = []
        self.educations = []
        self.images = []
        self.usernames = []
        self.user_ids = []
        self.dobs = []
        self.related_urls = []
        self.relationships = []
        self.tags = []
        
        self.add_fields(fields or [])
    
    def add_fields(self, fields):
        """Add the fields to their corresponding container.
        
        `fields` is an iterable of field objects from osrframework.thirdparties.pipl_com.lib.fields.
        
        """
        for field in fields:
            cls = field.__class__
            try:
                container = FieldsContainer.class_container[cls]
            except KeyError:
                raise ValueError('Object of type %s is an invalid field' % cls)
            getattr(self, container).append(field)
    
    @property
    def all_fields(self):
        """A list with all the fields contained in this object."""
        return [field 
                for container in FieldsContainer.class_container.values()
                for field in getattr(self, container)]
        
    @staticmethod
    def fields_from_dict(d):
        """Load the fields from the dict, return a list with all the fields."""
        class_container = FieldsContainer.class_container
        fields = [field_cls.from_dict(field_dict) 
                  for field_cls, container in class_container.iteritems()
                  for field_dict in d.get(container, [])]
        return fields
        
    def fields_to_dict(self):
        """Transform the object to a dict and return the dict."""
        d = {}
        for container in FieldsContainer.class_container.values():
            fields = getattr(self, container)
            if fields:
                d[container] = [field.to_dict() for field in fields]
        return d
    
    
class Record(Serializable, FieldsContainer):
    
    """A record is all the data available in a specific source. 
    
    Every record object is based on a source which is basically the URL of the 
    page where the data is available, and the data itself that comes as field
    objects (Name, Address, Email etc. see osrframework.thirdparties.pipl_com.lib.fields).
    
    Each type of field has its own container (note that Record is a subclass 
    of FieldsContainer).
    For example:
    
    >>> from osrframework.thirdparties.pipl_com.lib import Record, Email, Phone
    >>> fields = [Email(address='eric@cartman.com'), Phone(number=999888777)]
    >>> record = Record(fields=fields)
    >>> record.emails
    [Email(address=u'eric@cartman.com')]
    >>> record.phones
    [Phone(number=999888777)]
    
    Records come as results for a query and therefore they have attributes that 
    indicate if and how much they match the query. They also have a validity 
    timestamp available as an attribute.
    
    """
    
    def __init__(self, fields=None, source=None, query_params_match=None, 
                 query_person_match=None, valid_since=None):
        """Extend FieldsContainer.__init__ and set the record's source
        and attributes.
        
        Args:
        
        fields -- An iterable of fields (from osrframework.thirdparties.pipl_com.lib.fields).
        source -- A Source object (osrframework.thirdparties.pipl_com.lib.source.Source).
        query_params_match -- A bool value that indicates whether the record 
                              contains all the params from the query or not.
        query_person_match -- A float between 0.0 and 1.0 that indicates how 
                              likely it is that this record holds data about 
                              the person from the query.
                              Higher value means higher likelihood, value 
                              of 1.0 means "this is definitely him".
                              This value is based on Pipl's statistical 
                              algorithm that takes into account many parameters
                              like the popularity of the name/address (if there 
                              was a name/address in the query) etc.
        valid_since -- A datetime.datetime object, this is the first time 
                       Pipl's crawlers saw this record.
        
        """
        FieldsContainer.__init__(self, fields)
        self.source = source or Source()
        self.query_params_match = query_params_match
        self.query_person_match = query_person_match
        self.valid_since = valid_since
        
    @staticmethod
    def from_dict(d):
        """Transform the dict to a record object and return the record."""
        query_params_match = d.get('@query_params_match')
        query_person_match = d.get('@query_person_match')
        valid_since = d.get('@valid_since')
        if valid_since:
            valid_since = str_to_datetime(valid_since)
        source = Source.from_dict(d.get('source', {}))
        fields = Record.fields_from_dict(d)
        return Record(source=source, fields=fields, 
                      query_params_match=query_params_match, 
                      query_person_match=query_person_match, 
                      valid_since=valid_since)
        
    def to_dict(self):
        """Return a dict representation of the record."""
        d = {}
        if self.query_params_match is not None:
            d['@query_params_match'] = self.query_params_match
        if self.query_person_match is not None:
            d['@query_person_match'] = self.query_person_match
        if self.valid_since is not None:
            d['@valid_since'] = datetime_to_str(self.valid_since)
        if self.source is not None:
            d['source'] = self.source.to_dict()
        d.update(self.fields_to_dict())
        return d


class Person(Serializable, FieldsContainer):
    
    """A Person object is all the data available on an individual.
    
    The Person object is essentially very similar in its structure to the 
    Record object, the main difference is that data about an individual can 
    come from multiple sources while a record is data from one source.
    
    The person's data comes as field objects (Name, Address, Email etc. see 
    osrframework.thirdparties.pipl_com.lib.fields).
    Each type of field has its on container (note that Person is a subclass 
    of FieldsContainer).
    For example:
    
    >>> from osrframework.thirdparties.pipl_com.lib import Person, Email, Phone
    >>> fields = [Email(address='eric@cartman.com'), Phone(number=999888777)]
    >>> person = Person(fields=fields)
    >>> person.emails
    [Email(address=u'eric@cartman.com')]
    >>> person.phones
    [Phone(number=999888777)]
    
    Note that a person object is used in the Search API in two ways:
    - It might come back as a result for a query (see SearchResponse).
    - It's possible to build a person object with all the information you 
      already have about the person you're looking for and send this object as 
      the query (see SearchRequest).
     
    """
    
    def __init__(self, fields=None, sources=None, query_params_match=None):
        """Extend FieldsContainer.__init__ and set the record's sources
        and query_params_match attribute.
        
        Args:
        
        fields -- An iterable of fields (from osrframework.thirdparties.pipl_com.lib.fields).
        sources -- A list of Source objects (osrframework.thirdparties.pipl_com.lib.source.Source).
        query_params_match -- A bool value that indicates whether the record 
                              contains all the params from the query or not.
        
        """
        
        FieldsContainer.__init__(self, fields)
        self.sources = sources or []
        self.query_params_match = query_params_match
    
    @property
    def is_searchable(self):
        """A bool value that indicates whether the person has enough data and
        can be sent as a query to the API."""
        filter_func = lambda field: field.is_searchable
        return bool(filter(filter_func, self.names) or 
                    filter(filter_func, self.emails) or
                    filter(filter_func, self.phones) or
                    filter(filter_func, self.usernames))
    
    @property
    def unsearchable_fields(self):
        """A list of all the fields that can't be searched by.
        
        For example: names/usernames that are too short, emails that are 
        invalid etc.
        
        """
        filter_func = lambda field: not field.is_searchable
        return filter(filter_func, self.names) + \
               filter(filter_func, self.emails) + \
               filter(filter_func, self.phones) + \
               filter(filter_func, self.usernames) + \
               filter(filter_func, self.addresses) + \
               filter(filter_func, self.dobs)
        
    @staticmethod
    def from_dict(d):
        """Transform the dict to a person object and return the person."""
        query_params_match = d.get('@query_params_match')
        sources = [Source.from_dict(source) for source in d.get('sources', [])]
        fields = Person.fields_from_dict(d)
        return Person(fields=fields, sources=sources,
                      query_params_match=query_params_match)
        
    def to_dict(self):
        """Return a dict representation of the person."""
        d = {}
        if self.query_params_match is not None:
            d['@query_params_match'] = self.query_params_match
        if self.sources:
            d['sources'] = [source.to_dict() for source in self.sources]
        d.update(self.fields_to_dict())
        return d

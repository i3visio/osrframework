"""Python wrapper for easily making calls to Pipl's Search API.

Pipl's Search API allows you to query with the information you have about
a person (his name, address, email, phone, username and more) and in response 
get all the data available on him on the web.

The classes contained in this module are:
- SearchAPIRequest -- Build your request and send it.
- SearchAPIResponse -- Holds the response from the API in case it contains data.
- SearchAPIError -- An exception raised when the API response is an error.

The classes are based on the person data-model that's implemented here in the
sub-package osrframework.thirdparties.pipl_com.lib.

"""
import urllib
import urllib2
import itertools
import threading

import osrframework.thirdparties.pipl_com
from osrframework.thirdparties.pipl_com.lib.error import APIError
from osrframework.thirdparties.pipl_com.lib import *
from osrframework.thirdparties.pipl_com.lib.utils import Serializable


# Default API key value, you can set your key globally in this variable instead 
# of passing it to each request object.
# >>> import osrframework.thirdparties.pipl_com.lib.search
# >>> osrframework.thirdparties.pipl_com.lib.search.default_api_key = '<your_key>'
default_api_key = None


class SearchAPIRequest(object):
    
    """A request to Pipl's Search API.
    
    Building the request from the query parameters can be done in two ways:
    
    Option 1 - directly and quickly (for simple requests with only few 
               parameters):
            
    >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest
    >>> request = SearchAPIRequest(api_key='samplekey', 
                                   email='eric@cartman.com')
    >>> response = request.send()
    
    Option 2 - using the data-model (useful for more complex queries; for 
               example, when there are multiple parameters of the same type 
               such as few phones or a few addresses or when you'd like to use 
               information beyond the usual identifiers such as name or email, 
               information like education, job, relationships etc):
            
    >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest
    >>> from osrframework.thirdparties.pipl_com.lib import Person, Name, Address, Job
    >>> fields = [Name(first='Eric', last='Cartman'),
                  Address(country='US', state='CO', city='South Park'),
                  Address(country='US', state='NY'),
                  Job(title='Actor')]
    >>> request = SearchAPIRequest(api_key='samplekey', 
                                   person=Person(fields=fields))
    >>> response = request.send()

    The request also supports prioritizing/filtering the type of records you
    prefer to get in the response (see the append_priority_rule and 
    add_records_filter methods).
    
    Sending the request and getting the response is very simple and can be done
    by either making a blocking call to request.send() or by making 
    a non-blocking call to request.send_async(callback) which sends the request 
    asynchronously.
    
    """
    
    HEADERS = {'User-Agent': 'osrframework.thirdparties.pipl_com/python/%s' % osrframework.thirdparties.pipl_com.lib.__version__}
    BASE_URL = 'http://api.pipl.com/search/v3/json/?'
    # HTTPS is also supported:
    #BASE_URL = 'https://api.pipl.com/search/v3/json/?'
    
    def __init__(self, api_key=None, first_name=None, middle_name=None, 
                 last_name=None, raw_name=None, email=None, phone=None, 
                 username=None, country=None, state=None, city=None, 
                 raw_address=None, from_age=None, to_age=None, person=None,
                 query_params_mode='and', exact_name=False):
        """Initiate a new request object with given query params.
        
        Each request must have at least one searchable parameter, meaning 
        a name (at least first and last name), email, phone or username. 
        Multiple query params are possible (for example querying by both email 
        and phone of the person).
        
        Args:
        
        api_key -- str, a valid API key (use "samplekey" for experimenting).
                   Note that you can set a default API key 
                   (osrframework.thirdparties.pipl_com.lib.search.default_api_key = '<your_key>') instead of 
                   passing it to each request object. 
        first_name -- unicode, minimum 2 chars.
        middle_name -- unicode. 
        last_name -- unicode, minimum 2 chars.
        raw_name -- unicode, an unparsed name containing at least a first name 
                    and a last name.
        email -- unicode.
        phone -- int/long. If a unicode/str is passed instead then it'll be 
                 striped from all non-digit characters and converted to int.
                 IMPORTANT: Currently only US/Canada phones can be searched by
                 so country code is assumed to be 1, phones with different 
                 country codes are considered invalid and will be ignored.
        username -- unicode, minimum 4 chars.
        country -- unicode, a 2 letter country code from:
                   http://en.wikipedia.org/wiki/ISO_3166-2
        state -- unicode, a state code from:
                 http://en.wikipedia.org/wiki/ISO_3166-2%3AUS
                 http://en.wikipedia.org/wiki/ISO_3166-2%3ACA
        city -- unicode.
        raw_address -- unicode, an unparsed address.
        from_age -- int.
        to_age -- int.
        person -- A Person object (available at osrframework.thirdparties.pipl_com.lib.Person).
                  The person can contain every field allowed by the data-model
                  (see osrframework.thirdparties.pipl_com.lib.fields) and can hold multiple fields of 
                  the same type (for example: two emails, three addresses etc.)
        query_params_mode -- str, one of "and"/"or" (default "and").
                             Advanced parameter, use only if you care about the 
                             value of record.query_params_match in the response 
                             records.
                             Each record in the response has an attribute 
                             "query_params_match" which indicates whether the 
                             record has the all fields from the query or not.
                             When set to "and" all query params are required in 
                             order to get query_params_match=True, when set to 
                             "or" it's enough that the record has at least one
                             of each field type (so if you search with a name 
                             and two addresses, a record with the name and one 
                             of the addresses will have query_params_match=True)
        exact_name -- bool (default False).
                      If set to True the names in the query will be matched 
                      "as is" without compensating for nicknames or multiple
                      family names. For example "Jane Brown-Smith" won't return 
                      results for "Jane Brown" in the same way "Alexandra Pitt"
                      won't return results for "Alex Pitt".
        
        Each of the arguments that should have a unicode value accepts both 
        unicode objects and utf8 encoded str (will be decoded automatically).
        
        """
        if person is None:
            person = Person()
        if first_name or middle_name or last_name:
            name = Name(first=first_name, middle=middle_name, last=last_name)
            person.add_fields([name])
        if raw_name:
            person.add_fields([Name(raw=raw_name)])
        if email:
            person.add_fields([Email(address=email)])
        if phone:
            if isinstance(phone, basestring):
                person.add_fields([Phone.from_text(phone)])
            else:
                person.add_fields([Phone(number=phone)])
        if username:
            person.add_fields([Username(content=username)])
        if country or state or city:
            address = Address(country=country, state=state, city=city)
            person.add_fields([address])
        if raw_address:
            person.add_fields([Address(raw=raw_address)])
        if from_age is not None or to_age is not None:
            dob = DOB.from_age_range(from_age or 0, to_age or 1000)
            person.add_fields([dob])
        
        self.api_key = api_key
        self.person = person
        self.query_params_mode = query_params_mode
        self.exact_name = exact_name
        self._filter_records_by = []
        self._prioritize_records_by = []
    
    @staticmethod
    def _prepare_filtering_params(domain=None, category=None, 
                                  sponsored_source=None, has_field=None,
                                  has_fields=None, query_params_match=None, 
                                  query_person_match=None, **kwargs):
        """Transform the params to the API format, return a list of params."""
        if query_params_match not in (None, True):
            raise ValueError('query_params_match can only be `True`')
        if query_person_match not in (None, True):
            raise ValueError('query_person_match can only be `True`')
        
        params = []
        if domain is not None:
            params.append('domain:%s' % domain)
        if category is not None:
            Source.validate_categories([category])
            params.append('category:%s' % category)
        if sponsored_source is not None:
            params.append('sponsored_source:%s' % sponsored_source)
        if query_params_match is not None:
            params.append('query_params_match')
        if query_person_match is not None:
            params.append('query_person_match')
        has_fields = has_fields or []
        if has_field is not None:
            has_fields.append(has_field)
        for has_field in has_fields:
            params.append('has_field:%s' % has_field.__name__)
        return params
        
    def add_records_filter(self, domain=None, category=None, 
                           sponsored_source=None, has_fields=None, 
                           query_params_match=None, query_person_match=None):
        """Add a new "and" filter for the records returned in the response.
        
        IMPORTANT: This method can be called multiple times per request for 
        adding multiple "and" filters, each of these "and" filters is 
        interpreted as "or" with the other filters.
        For example:
        
        >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest
        >>> from osrframework.thirdparties.pipl_com.lib import Phone, Job
        >>> request = SearchAPIRequest('samplekey', username='eric123')
        >>> request.add_records_filter(domain='linkedin', has_fields=[Phone])
        >>> request.add_records_filter(has_fields=[Phone, Job])
        
        The above request is only for records that are:
        (from LinkedIn AND has a phone) OR (has a phone AND has a job).
        Records that don't match this rule will not come back in the response.
        
        Please note that in case there are too many results for the query, 
        adding filters to the request can significantly improve the number of
        useful results; when you define which records interest you, you'll
        get records that would have otherwise be cut-off by the limit on the
        number of records per query.
        
        Args:
        
        domain -- str, for example "linkedin.com", you may also use "linkedin"
                  but note that it'll match "linkedin.*" and "*.linkedin.*" 
                  (any sub-domain and any TLD).
        category -- str, any one of the categories defined in
                    osrframework.thirdparties.pipl_com.lib.source.Source.categories.
        sponsored_source -- bool, True means you want just the records that 
                            come from a sponsored source and False means you 
                            don't want these records.
        has_fields -- A list of fields classes from osrframework.thirdparties.pipl_com.lib.fields, 
                      records must have content in all these fields.
                      For example: [Name, Phone] means you only want records 
                      that has at least one name and at least one phone.
        query_params_match -- True is the only possible value and it means you 
                              want records that match all the params you passed 
                              in the query.
        query_person_match -- True is the only possible value and it means you
                              want records that are the same person you 
                              queried by (only records with 
                              query_person_match == 1.0, see the documentation 
                              of record.query_person_match for more details).
        
        ValueError is raised in any case of an invalid parameter.
        
        """
        params = SearchAPIRequest._prepare_filtering_params(**locals())
        if params:
            self._filter_records_by.append(' AND '.join(params))
    
    def append_priority_rule(self, domain=None, category=None, 
                             sponsored_source=None, has_field=None, 
                             query_params_match=None, query_person_match=None):
        """Append a new priority rule for the records returned in the response.
        
        IMPORTANT: This method can be called multiple times per request for 
        adding multiple priority rules, each call can be with only one argument
        and the order of the calls matter (the first rule added is the highest 
        priority, the second is second priority etc).
        For example:
        
        >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest
        >>> from osrframework.thirdparties.pipl_com.lib import Phone
        >>> request = SearchAPIRequest('samplekey', username='eric123')
        >>> request.append_priority_rule(domain='linkedin')
        >>> request.append_priority_rule(has_field=Phone)
        
        In the response to the above request records from LinkedIn will be 
        returned before records that aren't from LinkedIn and records with 
        phone will be returned before records without phone. 
        
        Please note that in case there are too many results for the query,
        adding priority rules to the request does not only affect the order 
        of the records but can significantly improve the number of useful 
        results; when you define which records interest you, you'll get records
        that would have otherwise be cut-off by the limit on the number
        of records per query.  

        Args:
        
        domain -- str, for example "linkedin.com", "linkedin" is also possible 
                  and it'll match "linkedin.*".
        category -- str, any one of the categories defined in
                    osrframework.thirdparties.pipl_com.lib.source.Source.categories.
        sponsored_source -- bool, True will bring the records that 
                            come from a sponsored source first and False 
                            will bring the non-sponsored records first.
        has_fields -- A field class from osrframework.thirdparties.pipl_com.lib.fields.
                      For example: has_field=Phone means you want to give 
                      a priority to records that has at least one phone.
        query_params_match -- True is the only possible value and it means you 
                              want to give a priority to records that match all 
                              the params you passed in the query.
        query_person_match -- True is the only possible value and it means you
                              want to give a priority to records with higher
                              query_person_match (see the documentation of 
                              record.query_person_match for more details).
                     
        ValueError is raised in any case of an invalid parameter.
        
        """
        params = SearchAPIRequest._prepare_filtering_params(**locals())
        if len(params) > 1:
            raise ValueError('The function should be called with one argument')
        if params:
            self._prioritize_records_by.append(params[0])
        
    def validate_query_params(self, strict=True):
        """Check if the request is valid and can be sent, raise ValueError if 
        not.
        
        `strict` is a boolean argument that defaults to True which means an 
        exception is raised on every invalid query parameter, if set to False
        an exception is raised only when the search request cannot be performed
        because required query params are missing.
        
        """
        if not (self.api_key or default_api_key):
            raise ValueError('API key is missing')
        if strict and self.query_params_mode not in (None, 'and', 'or'):
            raise ValueError('query_params_match should be one of "and"/"or"')
        if not self.person.is_searchable:
            raise ValueError('No valid name/username/phone/email in request')
        if strict and self.person.unsearchable_fields:
            raise ValueError('Some fields are unsearchable: %s' 
                             % self.person.unsearchable_fields)
        
    @property
    def url(self):
        """The URL of the request (str)."""
        query = {
            'key': self.api_key or default_api_key,
            'person': self.person.to_json(),
            'query_params_mode': self.query_params_mode,
            'exact_name': self.exact_name,
            'prioritize_records_by': ','.join(self._prioritize_records_by),
            'filter_records_by': self._filter_records_by,
        }
        return SearchAPIRequest.BASE_URL + urllib.urlencode(query, doseq=True)
    
    def send(self, strict_validation=True):
        """Send the request and return the response or raise SearchAPIError.
        
        Calling this method blocks the program until the response is returned,
        if you want the request to be sent asynchronously please refer to the 
        send_async method. 
        
        The response is returned as a SearchAPIResponse object.
        
        `strict_vailidation` is a bool argument that's passed to the 
        validate_query_params method.
        
        Raises ValueError (raised from validate_query_params), 
        HttpError/URLError and SearchAPIError (when the response is returned 
        but contains an error).
        
        Example:
        
        >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest, SearchAPIError
        >>> request = SearchAPIRequest('samplekey', email='eric@cartman.com')
        >>> try:
        ...     response = request.send()
        ... except SearchAPIError as e:
        ...     print e.http_status_code, e
        
        """
        self.validate_query_params(strict=strict_validation)
        query = {
            'key': self.api_key or default_api_key,
            'person': self.person.to_json(),
            'query_params_mode': self.query_params_mode,
            'exact_name': self.exact_name,
            'prioritize_records_by': ','.join(self._prioritize_records_by),
            'filter_records_by': self._filter_records_by,
        }
        request = urllib2.Request(url=SearchAPIRequest.BASE_URL, data=urllib.urlencode(query, True), headers=SearchAPIRequest.HEADERS)
        try:
            json_response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            json_error = e.read()
            if not json_error:
                raise e
            try:
                raise SearchAPIError.from_json(json_error)
            except ValueError:
                raise e
        return SearchAPIResponse.from_json(json_response)
    
    def send_async(self, callback, strict_validation=True):
        """Same as send() but in a non-blocking way.
        
        Use this method if you want to send the request asynchronously so your 
        program can do other things while waiting for the response.
        
        `callback` is a function (or other callable) with the following 
        signature:
        callback(response=None, error=None)
        
        Example:
        
        >>> from osrframework.thirdparties.pipl_com.lib.search import SearchAPIRequest
        >>>
        >>> def my_callback(response=None, error=None):
        ...     print response or error
        ...
        >>> request = SearchAPIRequest('samplekey', email='eric@cartman.com')
        >>> request.send_async(my_callback)
        >>> do_other_things()
        
        """
        def target():
            try:
                response = self.send(strict_validation)
                callback(response=response)
            except Exception as e:
                callback(error=e)
        threading.Thread(target=target).start()


class SearchAPIResponse(Serializable):
    
    """A response from Pipl's Search API.
    
    A response comprises the two things returned as a result to your query:
    
    - A person (osrframework.thirdparties.pipl_com.lib.containers.Person) that is the deta object 
      representing all the information available for the person you were 
      looking for.
      This object will only be returned when our identity-resolution engine is
      convinced that the information is of the person represented by your query.
      Obviously, if the query was for "John Smith" there's no way for our
      identity-resolution engine to know which of the hundreds of thousands of
      people named John Smith you were referring to, therefore you can expect
      that the response will not contain a person object.
      On the other hand, if you search by a unique identifier such as email or
      a combination of identifiers that only lead to one person, such as
      "Eric Cartman, Age 22, From South Park, CO, US", you can expect to get 
      a response containing a single person object.
    
    - A list of records (osrframework.thirdparties.pipl_com.lib.containers.Record) that fully/partially 
      match the person from your query, if the query was for "Eric Cartman from 
      Colorado US" the response might also contain records of "Eric Cartman 
      from US" (without Colorado), if you need to differentiate between records 
      with full match to the query and partial match or if you want to get a
      score on how likely is that record to be related to the person you are
      searching please refer to the record's attributes 
      record.query_params_match and record.query_person_match.
    
    The response also contains the query as it was interpreted by Pipl. This 
    part is useful for verification and debugging, if some query parameters 
    were invalid you can see in response.query that they were ignored, you can 
    also see how the name/address from your query were parsed in case you 
    passed raw_name/raw_address in the query.
    
    In some cases when the query isn't focused enough and can't be matched to 
    a specific person, such as "John Smith from US", the response also contains 
    a list of suggested searches. This is a list of Record objects, each of 
    these is an expansion of the original query, giving additional query 
    parameters so the you can zoom in on the right person.
    
    """
    
    def __init__(self, query=None, person=None, records=None, 
                 suggested_searches=None, warnings_=None):
        """Args:
        
        query -- A Person object with the query as interpreted by Pipl.
        person -- A Person object with data about the person in the query.
        records -- A list of Record objects with full/partial match to the 
                   query.
        suggested_searches -- A list of Record objects, each of these is an 
                              expansion of the original query, giving additional
                              query parameters to zoom in on the right person.
        warnings_ -- A list of unicodes. A warning is returned when the query 
                    contains a non-critical error and the search can still run.
                    
        """
        self.query = query
        self.person = person
        self.records = records or []
        self.suggested_searches = suggested_searches or []
        self.warnings = warnings_ or []
        
    @property
    def query_params_matched_records(self):
        """Records that match all the params in the query."""
        return [rec for rec in self.records if rec.query_params_match]
    
    @property
    def query_person_matched_records(self):
        """Records that match the person from the query.
        
        Note that the meaning of "match the person from the query" means "Pipl 
        is convinced that these records hold data about the person you're 
        looking for". 
        Remember that when Pipl is convinced about which person you're looking 
        for, the response also contains a Person object. This person is 
        created by merging all the fields and sources of these records. 
        
        """
        return [rec for rec in self.records if rec.query_person_match == 1.]
        
    def group_records(self, key_function):
        """Return a dict with the records grouped by the key returned by 
        `key_function`.
        
        `key_function` takes a record and returns the value from the record to
        group by (see examples in the group_records_by_* methods below).
        
        The return value is a dict, a key in this dict is a key returned by
        `key_function` and the value is a list of all the records with this key.
        
        """
        sorted_records = sorted(self.records, key=key_function)
        grouped_records = itertools.groupby(sorted_records, key=key_function)
        return dict([(key, list(group)) for key, group in grouped_records])
    
    def group_records_by_domain(self):
        """Return the records grouped by the domain they came from.
        
        The return value is a dict, a key in this dict is a domain
        and the value is a list of all the records with this domain.
        
        """
        key_function = lambda record: record.source.domain
        return self.group_records(key_function)
    
    def group_records_by_category(self):
        """Return the records grouped by the category of their source.
        
        The return value is a dict, a key in this dict is a category
        and the value is a list of all the records with this category.
        
        """
        Source.validate_categories(categories)
        key_function = lambda record: record.source.category
        return self.group_records(key_function)
    
    def group_records_by_query_params_match(self):
        """Return the records grouped by their query_params_match attribute.
        
        The return value is a dict, a key in this dict is a query_params_match
        bool (so the keys can be just True or False) and the value is a list 
        of all the records with this query_params_match value.
        
        """
        key_function = lambda record: record.query_params_match
        return self.group_records(key_function)
    
    def group_records_by_query_person_match(self):
        """Return the records grouped by their query_person_match attribute.
        
        The return value is a dict, a key in this dict is a query_person_match
        float and the value is a list of all the records with this 
        query_person_match value.
        
        """
        key_function = lambda record: record.query_person_match
        return self.group_records(key_function)
    
    @staticmethod
    def from_dict(d):
        """Transform the dict to a response object and return the response."""
        warnings_ = d.get('warnings', [])
        query = d.get('query') or None
        if query:
            query = Person.from_dict(query)
        person = d.get('person') or None
        if person:
            person = Person.from_dict(person)
        records = d.get('records')
        if records:
            records = [Record.from_dict(record) for record in records]
        suggested_searches = d.get('suggested_searches')
        if suggested_searches:
            suggested_searches = [Record.from_dict(record) 
                                  for record in suggested_searches]
        return SearchAPIResponse(query=query, person=person, records=records, 
                                 suggested_searches=suggested_searches,
                                 warnings_=warnings_)
    
    def to_dict(self):
        """Return a dict representation of the response."""
        d = {}
        if self.warnings:
            d['warnings'] = self.warnings
        if self.query is not None:
            d['query'] = self.query.to_dict()
        if self.person is not None:
            d['person'] = self.person.to_dict()
        if self.records:
            d['records'] = [record.to_dict() for record in self.records]
        if self.suggested_searches:
            d['suggested_searches'] = [record.to_dict() 
                                       for record in self.suggested_searches]
        return d
        

class SearchAPIError(APIError):
    
    """An exception raised when the response from the search API contains an 
    error."""
    
    pass

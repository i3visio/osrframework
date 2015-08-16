import re
import datetime

from osrframework.thirdparties.pipl_com.lib.utils import *


__all__ = ['Name', 'Address', 'Phone', 'Email', 'Job', 'Education', 'Image', 
           'Username', 'UserID', 'DOB', 'RelatedURL', 'Relationship', 'Tag',
           'DateRange']


class Field(Serializable):
    
    """Base class of all data fields, made only for inheritance."""
    
    attributes = ()
    children = ('content',)
    
    def __init__(self, valid_since=None):
        self.valid_since = valid_since
    
    def __setattr__(self, attr, value):
        """Extend the default object.__setattr___ and make sure that str values 
        are converted to unicode and that assigning to the `type` attribute is 
        only from the allowed values.
        
        Setting an str value for an attribute is impossible, if an str is 
        provided then it must be in utf8 encoding and it will be automatically
        converted to a unicode object.
        
        Example:
        >>> from osrframework.thirdparties.pipl_com.lib.data import Name
        >>> name = Name(first='eric')
        >>> name.first
        u'eric'
        
        """
        if isinstance(value, str):
            try:
                value = value.decode('utf8')
            except UnicodeDecodeError:
                raise ValueError('Tried to assign a non utf8 string to ' + attr)
        if attr == 'type':
            self.validate_type(value)
        object.__setattr__(self, attr, value)
    
    def __unicode__(self):
        """Return the unicode representation of the object."""
        children = list(self.children)
        if 'raw' in children:
            children.remove('raw')
        values = [getattr(self, child) for child in children]
        return u' '.join([unicode(val) for val in values if val is not None])
    
    def __str__(self):
        """Return the str representation of the object (encoded with utf8)."""
        return unicode(self).encode('utf8')
    
    def __repr__(self):
        """Return a representation of the object (a valid value for eval())."""
        attrs = list(self.attributes + self.children)
        attrs.append('valid_since')
        attrs_values = [(attr, getattr(self, attr)) for attr in attrs]
        attrs_values = [(attr, value) if attr != 'type' else ('type_', value)
                        for attr, value in attrs_values]
        args = ['%s=%s' % (attr, repr(value)) 
                for attr, value in attrs_values if value is not None]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(args))
    
    def __eq__(self, other):
        """Bool, indicates whether `self` and `other` have exactly the same 
        data."""
        return repr(self) == repr(other)
        
    def validate_type(self, type_):
        """Take an str/unicode `type_` and raise a ValueError if it's not 
        a valid type for the object.
        
        A valid type for a field is a value from the types_set attribute of 
        that field's class. 
        
        """
        if type_ is not None and type_ not in self.types_set:
            raise ValueError('Invalid type for %s:%s' % (self.__class__, type_))
    
    @classmethod
    def from_dict(cls, d):
        """Transform the dict to a field object and return the field."""
        kwargs = {}
        for key, val in d.iteritems():
            if key.startswith('display'): # includes phone.display_international
                continue
            if key.startswith('@'):
                key = key[1:]
            if key == 'type':
                key = 'type_'
            elif key == 'valid_since':
                val = str_to_datetime(val)
            elif key == 'date_range':
                val = DateRange.from_dict(val)
            kwargs[key.encode('ascii')] = val
        return cls(**kwargs)
        
    def to_dict(self):
        """Return a dict representation of the field."""
        d = {}
        if self.valid_since is not None:
            d['@valid_since'] = datetime_to_str(self.valid_since)
        for attr_list, prefix in [(self.attributes, '@'), (self.children, '')]:
            for attr in attr_list:
                value = getattr(self, attr)
                if isinstance(value, Serializable):
                    value = value.to_dict()
                if value or isinstance(value, (bool, int, long)):
                    d[prefix + attr] = value
        if hasattr(self, 'display') and self.display:
            d['display'] = self.display
        return d
        
    
class Name(Field):
    
    """A name of a person."""
    
    attributes = ('type',)
    children = ('prefix', 'first', 'middle', 'last', 'suffix', 'raw')
    types_set = set(['present', 'maiden', 'former', 'alias'])
    
    def __init__(self, prefix=None, first=None, middle=None, last=None, 
                 suffix=None, raw=None, type_=None, valid_since=None):
        """`prefix`, `first`, `middle`, `last`, `suffix`, `raw`, `type_`, 
        should all be unicode objects or utf8 encoded strs (will be decoded 
        automatically).
        
        `raw` is an unparsed name like "Eric T Van Cartman", usefull when you 
        want to search by name and don't want to work hard to parse it.
        Note that in response data there's never name.raw, the names in 
        the response are always parsed, this is only for querying with 
        an unparsed name.
        
        `type_` is one of Name.types_set.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.prefix = prefix
        self.first = first
        self.middle = middle
        self.last = last    
        self.suffix = suffix
        self.raw = raw
        self.type = type_
    
    @property
    def display(self):
        """A unicode value with the object's data, to be used for displaying 
        the object in your application."""
        return unicode(self)
    
    @property
    def is_searchable(self):
        """A bool value that indicates whether the name is a valid name to 
        search by."""
        first = alpha_chars(self.first or u'')
        last = alpha_chars(self.last or u'')
        raw = alpha_chars(self.raw or u'')
        return (len(first) >= 2 and len(last) >= 2) or len(raw) >= 4
    

class Address(Field):
    
    """An address of a person."""
    
    attributes = ('type',)
    children = ('country', 'state', 'city', 'po_box', 
                'street', 'house', 'apartment', 'raw')
    types_set = set(['home', 'work', 'old'])
    
    def __init__(self, country=None, state=None, city=None, po_box=None, 
                 street=None, house=None, apartment=None, raw=None, type_=None, 
                 valid_since=None):
        """`country`, `state`, `city`, `po_box`, `street`, `house`, `apartment`, 
        `raw`, `type_`, should all be unicode objects or utf8 encoded strs 
        (will be decoded automatically).
        
        `country` and `state` are country code (like "US") and state code 
        (like "NY"), note that the full value is available as 
        address.country_full and address.state_full.
        
        `raw` is an unparsed address like "123 Marina Blvd, San Francisco, 
        California, US", usefull when you want to search by address and don't 
        want to work hard to parse it.
        Note that in response data there's never address.raw, the addresses in 
        the response are always parsed, this is only for querying with 
        an unparsed address.
        
        `type_` is one of Address.types_set.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.country = country
        self.state = state
        self.city = city
        self.po_box = po_box
        self.street = street
        self.house = house
        self.apartment = apartment
        self.raw = raw
        self.type = type_
    
    @property
    def display(self):
        """A unicode value with the object's data, to be used for displaying 
        the object in your application."""
        country = self.country if self.state else self.country_full
        state = self.state if self.city else self.state_full
        vals = (self.street, self.city, state, country)
        disp = u', '.join(filter(None, vals))
        if self.street and (self.house or self.apartment):
            prefix = u'-'.join([val for val in (self.house, self.apartment) 
                                if val])
            disp = prefix + u' ' + (disp or u'')
        if self.po_box and not self.street:
            disp = u' '.join([u'P.O. Box', self.po_box, (disp or u'')])
        return disp
            
    @property
    def is_searchable(self):
        """A bool value that indicates whether the address is a valid address 
        to search by."""
        return self.raw or (self.is_valid_country and 
                            (not self.state or self.is_valid_state))
    
    @property
    def is_valid_country(self):
        """A bool value that indicates whether the object's country is a valid 
        country code."""
        return self.country is not None and self.country.upper() in COUNTRIES
    
    @property
    def is_valid_state(self):
        """A bool value that indicates whether the object's state is a valid 
        state code."""
        return self.is_valid_country and self.country.upper() in STATES and \
               self.state is not None and \
               self.state.upper() in STATES[self.country.upper()]
    
    @property
    def country_full(self):
        """unicode, the full name of the object's country.
        
        >>> address = Address(country='FR')
        >>> address.country
        u'FR'
        >>> address.country_full
        u'France'
        
        """
        if self.country:
            return COUNTRIES.get(self.country.upper())
    
    @property
    def state_full(self):
        """unicode, the full name of the object's state.
        
        >>> address = Address(country='US', state='CO')
        >>> address.state
        u'CO'
        >>> address.state_full
        u'Colorado'
        
        """
    
        if self.is_valid_state:
            return STATES[self.country.upper()].get(self.state.upper())
    

class Phone(Field):
    
    """A phone number of a person."""
    
    attributes = ('type',)
    children = ('country_code', 'number', 'extension')
    types_set = set(['mobile', 'home_phone', 'home_fax', 'work_phone', 
                     'work_fax', 'pager'])
    
    def __init__(self, country_code=None, number=None, extension=None,
                 type_=None, valid_since=None):
        """`country_code`, `number` and `extension` should all be int/long.
        
        `type_` is one of Phone.types_set.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.country_code = country_code
        self.number = number
        self.extension = extension
        self.type = type_
        # The two following display attributes are available when working with 
        # a response from the API, both hold unicode values that can be used to 
        # display the phone in your application.
        # Note that in other fields the display attribute is a property, this 
        # is not the case here since generating the display for a phone is 
        # country specific and requires a special library.
        self.display = u''
        self.display_international = u''
        
    @property
    def is_searchable(self):
        """A bool value that indicates whether the phone is a valid phone 
        to search by."""
        return self.number is not None and \
               (not self.country_code or self.country_code == 1)
    
    @staticmethod
    def from_text(text):
        """Strip `text` (unicode/str) from all non-digit chars and return a new
        Phone object with the number from text.
        
        >>> phone = Phone.from_text('(888) 777-666')
        >>> phone.number
        888777666
        
        """
        number = int(filter(unicode.isdigit, unicode(text)))
        return Phone(number=number)
        
    @classmethod
    def from_dict(cls, d):
        """Extend Field.from_dict, set display/display_international 
        attributes."""
        phone = super(cls, cls).from_dict(d)
        phone.display = d.get('display', u'')
        phone.display_international = d.get('display_international', u'')
        return phone
        
    def to_dict(self):
        """Extend Field.to_dict, take the display_international attribute."""
        d = Field.to_dict(self)
        if self.display_international:
            d['display_international'] = self.display_international
        return d
    
        
class Email(Field):
    
    """An email address of a person with the md5 of the address, might come
    in some cases without the address itself and just the md5 (for privacy 
    reasons).
    
    """
    
    attributes = ('type',)
    children = ('address', 'address_md5')
    types_set = set(['personal', 'work'])
    re_email = re.compile('^[\w.%\-+]+@[\w.%\-]+\.[a-zA-Z]{2,6}$')
    
    def __init__(self, address=None, address_md5=None, type_=None, 
                 valid_since=None):
        """`address`, `address_md5`, `type_` should be unicode objects or utf8 
        encoded strs (will be decoded automatically).
        
        `type_` is one of Email.types_set.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.address = address
        self.address_md5 = address_md5
        self.type = type_
    
    @property
    def is_valid_email(self):
        """A bool value that indicates whether the address is a valid 
        email address.
        
        Note that the check is done be matching to the regular expression 
        at Email.re_email which is very basic and far from covering end-cases...
        
        """
        return bool(self.address and Email.re_email.match(self.address))
    
    @property
    def is_searchable(self):
        """A bool value that indicates whether the email is a valid email 
        to search by."""
        return self.is_valid_email
    
    @property
    def username(self):
        """unicode, the username part of the email or None if the email is 
        invalid.
        
        >>> email = Email(address='eric@cartman.com')
        >>> email.username
        u'eric'
        
        """
        if not self.is_valid_email:
            return
        return self.address.split('@')[0]
    
    @property
    def domain(self):
        """unicode, the domain part of the email or None if the email is 
        invalid.
        
        >>> email = Email(address='eric@cartman.com')
        >>> email.domain
        u'cartman.com'
        
        """
        if not self.is_valid_email:
            return
        return self.address.split('@')[1]    
        
        
class Job(Field):
    
    """Job information of a person."""
    
    children = ('title', 'organization', 'industry', 'date_range')

    def __init__(self, title=None, organization=None, industry=None,
                 date_range=None, valid_since=None):
        """`title`, `organization`, `industry`, should all be unicode objects 
        or utf8 encoded strs (will be decoded automatically).
        
        `date_range` is A DateRange object (osrframework.thirdparties.pipl_com.lib.fields.DateRange), 
        that's the time the person held this job.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.title = title
        self.organization = organization
        self.industry = industry
        self.date_range = date_range
    
    @property
    def display(self):
        """A unicode value with the object's data, to be used for displaying 
        the object in your application."""
        if self.title and self.organization:
            disp = self.title + u' at ' + self.organization
        else:
            disp = self.title or self.organization or None
        if disp and self.industry:
            if self.date_range is not None:
                disp += u' (%s, %d-%d)' % ((self.industry,) + \
                                           self.date_range.years_range)
            else:
                disp += u' (%s)' % self.industry
        else:
            disp = ((disp or u'') + u' ' + (self.industry or u'')).strip()
            if disp and self.date_range is not None:
                disp += u' (%d-%d)' % self.date_range.years_range
        return disp 
    

class Education(Field):
    
    """Education information of a person."""
    
    children = ('degree', 'school', 'date_range')
    
    def __init__(self, degree=None, school=None, date_range=None,
                 valid_since=None):
        """`degree` and `school` should both be unicode objects or utf8 encoded 
        strs (will be decoded automatically).
        
        `date_range` is A DateRange object (osrframework.thirdparties.pipl_com.lib.fields.DateRange), 
        that's the time the person was studying.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.degree = degree
        self.school = school
        self.date_range = date_range
    
    @property
    def display(self):
        """A unicode value with the object's data, to be used for displaying 
        the object in your application."""
        if self.degree and self.school:
            disp = self.degree + u' from ' + self.school
        else:
            disp = self.degree or self.school or None
        if disp is not None and self.date_range is not None:
            disp += u' (%d-%d)' % self.date_range.years_range
        return disp or u''
    

class Image(Field):
    
    """A URL of an image of a person."""
    
    children = ('url',)
    
    def __init__(self, url=None, valid_since=None):
        """`url` should be a unicode object or utf8 encoded str (will be decoded 
        automatically).
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.url = url
    
    @property
    def is_valid_url(self):
        """A bool value that indicates whether the image URL is a valid URL."""
        return bool(self.url and is_valid_url(self.url))
    

class Username(Field):
    
    """A username/screen-name associated with the person.
    
    Note that even though in many sites the username uniquely identifies one 
    person it's not guarenteed, some sites allow different people to use the 
    same username.
    
    """
    
    def __init__(self, content=None, valid_since=None):
        """`content` is the username itself, it should be a unicode object or 
        a utf8 encoded str (will be decoded automatically).
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.content = content
    
    @property
    def is_searchable(self):
        """A bool value that indicates whether the username is a valid username 
        to search by."""
        return len(alnum_chars(self.content or u'')) >= 4


class UserID(Field):
    
    """An ID associated with a person.
    
    The ID is a string that's used by the site to uniquely identify a person, 
    it's guaranteed that in the site this string identifies exactly one person.
    
    """
    
    def __init__(self, content=None, valid_since=None):
        """`content` is the ID itself, it should be a unicode object or a utf8 
        encoded str (will be decoded automatically).
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.content = content
      

class DOB(Field):
    
    """Date-of-birth of A person.
    Comes as a date-range (the exact date is within the range, if the exact 
    date is known the range will simply be with start=end).
    
    """
    
    children = ('date_range',)

    def __init__(self, date_range=None, valid_since=None):
        """`date_range` is A DateRange object (osrframework.thirdparties.pipl_com.lib.fields.DateRange), 
        the date-of-birth is within this range.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.date_range = date_range
    
    @property
    def display(self):
        """A unicode value with the object's data, to be used for displaying 
        the object in your application.
        
        Note: in a DOB object the display is the estimated age.
        
        """
        if self.age is None:
            return u''
        return unicode(self.age)
    
    @property
    def is_searchable(self):
        return self.date_range is not None
    
    @property
    def age(self):
        """int, the estimated age of the person.
        
        Note that A DOB object is based on a date-range and the exact date is 
        usually unknown so for age calculation the the middle of the range is 
        assumed to be the real date-of-birth. 
        
        """
        if self.date_range is None:
            return
        dob = self.date_range.middle
        today = datetime.date.today()
        if (today.month, today.day) < (dob.month, dob.day):
            return today.year - dob.year - 1
        else:
            return today.year - dob.year
    
    @property
    def age_range(self):
        """A tuple of two ints - the minimum and maximum age of the person."""
        if self.date_range is None:
            return None, None
        start_date = DateRange(self.date_range.start, self.date_range.start)
        end_date = DateRange(self.date_range.end, self.date_range.end)
        start_age = DOB(date_range=end_date).age
        end_age = DOB(date_range=start_date).age
        return start_age, end_age
        
    @staticmethod
    def from_birth_year(birth_year):
        """Take a person's birth year (int) and return a new DOB object 
        suitable for him."""
        if birth_year <= 0:
            raise ValueError('birth_year must be positive')
        date_range = DateRange.from_years_range(birth_year, birth_year)
        return DOB(date_range=date_range)
    
    @staticmethod
    def from_birth_date(birth_date):
        """Take a person's birth date (datetime.date) and return a new DOB 
        object suitable for him."""
        if birth_date > datetime.date.today():
            raise ValueError('birth_date can\'t be in the future')
        date_range = DateRange(birth_date, birth_date)
        return DOB(date_range=date_range)
    
    @staticmethod
    def from_age(age):
        """Take a person's age (int) and return a new DOB object 
        suitable for him."""
        return DOB.from_age_range(age, age)
    
    @staticmethod
    def from_age_range(start_age, end_age):
        """Take a person's minimal and maximal age and return a new DOB object 
        suitable for him."""
        if start_age < 0 or end_age < 0:
            raise ValueError('start_age and end_age can\'t be negative')
        
        if start_age > end_age:
            start_age, end_age = end_age, start_age
            
        today = datetime.date.today()
        
        try:
            start_date = today.replace(year=today.year - end_age - 1)
        except ValueError:  # February 29
            start_date = today.replace(year=today.year - end_age - 1, day=28)
        start_date += datetime.timedelta(days=1)
        
        try:
            end_date = today.replace(year=today.year - start_age)
        except ValueError:  # February 29
            end_date = today.replace(year=today.year - start_age, day=28)
        
        date_range = DateRange(start_date, end_date)
        return DOB(date_range=date_range) 
    

class RelatedURL(Field):
    
    """A URL that's related to a person (blog, personal page in the work 
    website, profile in some other website).
    
    IMPORTANT: This URL is NOT the origin of the data about the person, it's 
    just an extra piece of information available on him.
    
    """
    
    attributes = ('type',)
    types_set = set(['personal', 'work', 'blog'])
    
    def __init__(self, content=None, type_=None, valid_since=None):
        """`content` is the URL address itself, both content and type_ should 
        be unicode objects or utf8 encoded strs (will be decoded automatically).
        
        `type_` is one of RelatedURL.types_set.
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.content = content
        self.type = type_
    
    @property
    def is_valid_url(self):
        """A bool value that indicates whether the URL is a valid URL."""
        return bool(self.content and is_valid_url(self.content))
        

class Relationship(Field):
    
    """Name of another person related to this person."""
    
    attributes = ('type', 'subtype')
    children = ('name',)
    types_set = set(['friend', 'family', 'work', 'other'])
    
    def __init__(self, name=None, type_=None, subtype=None, 
                 valid_since=None):
        """`name` is a Name object (osrframework.thirdparties.pipl_com.lib.fields.Name).
        
        `type_` and `subtype` should both be unicode objects or utf8 encoded 
        strs (will be decoded automatically).
        
        `type_` is one of RelatedURL.types_set.
        
        `subtype` is not restricted to a specific list of possible values (for 
        example, if type_ is "family" then subtype can be "Father", "Mother", 
        "Son" and many other things).
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.name = name
        self.type = type_
        self.subtype = subtype
    
    @classmethod
    def from_dict(cls, d):
        """Extend Field.from_dict and also load the name from the dict."""
        relationship = super(cls, cls).from_dict(d)
        if relationship.name is not None:
            relationship.name = Name.from_dict(relationship.name)
        return relationship


class Tag(Field):
    
    """A general purpose element that holds any meaningful string that's 
    related to the person.
    Used for holding data about the person that either couldn't be clearly 
    classified or was classified as something different than the available
    data fields.
    
    """
    
    attributes = ('classification',)
    
    def __init__(self, content=None, classification=None, valid_since=None):
        """`content` is the tag itself, both `content` and `classification` 
        should be unicode objects or utf8 encoded strs (will be decoded 
        automatically).
        
        `valid_since` is a datetime.datetime object, it's the first time Pipl's
        crawlers found this data on the page.
        
        """
        Field.__init__(self, valid_since)
        self.content = content
        self.classification = classification
    

class DateRange(Serializable):
    
    """A time intervel represented as a range of two dates.
    
    DateRange objects are used inside DOB, Job and Education objects.
    
    """
    
    def __init__(self, start, end):
        """`start` and `end` are datetime.date objects, both are required.
        
        For creating a DateRange object for an exact date (like if exact 
        date-of-birth is known) just pass the same value for `start` and `end`.
        
        """
        if start > end:
            start, end = end, start
        self.start = start
        self.end = end
    
    def __unicode__(self):
        """Return the unicode representation of the object."""
        return u' - '.join([unicode(self.start), unicode(self.end)])
    
    def __repr__(self):
        """Return a representation of the object (a valid value for eval())."""
        return 'DateRange(%s, %s)' % (repr(self.start), repr(self.end))
    
    def __eq__(self, other):
        """Bool, indicates whether `self` and `other` have exactly the same 
        start date and end date."""
        return repr(self) == repr(other)
    
    @property
    def is_exact(self):
        """True if the object holds an exact date (start=end), 
        False otherwise."""
        return self.start == self.end
    
    @property
    def middle(self):
        """The middle of the date range (a datetime.date object)."""
        return self.start + (self.end - self.start) / 2 
    
    @property
    def years_range(self):
        """A tuple of two ints - the year of the start date and the year of the 
        end date."""
        return self.start.year, self.end.year
    
    @staticmethod
    def from_years_range(start_year, end_year):
        """Transform a range of years (two ints) to a DateRange object."""
        start = datetime.date(start_year, 1 , 1)
        end = datetime.date(end_year, 12 , 31)
        return DateRange(start, end)
    
    @staticmethod
    def from_dict(d):
        """Transform the dict to a DateRange object."""
        start = d.get('start')
        end = d.get('end')
        if not (start and end):
            raise ValueError('DateRange must have both start and end')
        start = str_to_date(start)
        end = str_to_date(end)
        return DateRange(start, end)
    
    def to_dict(self):
        """Transform the date-range to a dict."""
        d = {}
        d['start'] = date_to_str(self.start)
        d['end'] = date_to_str(self.end)
        return d
    

import re
import json
import datetime


STATES = {
    u'US': {u'WA': u'Washington', u'VA': u'Virginia', u'DE': u'Delaware', u'DC': u'District Of Columbia', u'WI': u'Wisconsin', u'WV': u'West Virginia', u'HI': u'Hawaii', u'FL': u'Florida', u'YT': u'Yukon', u'WY': u'Wyoming', u'PR': u'Puerto Rico', u'NJ': u'New Jersey', u'NM': u'New Mexico', u'TX': u'Texas', u'LA': u'Louisiana', u'NC': u'North Carolina', u'ND': u'North Dakota', u'NE': u'Nebraska', u'FM': u'Federated States Of Micronesia', u'TN': u'Tennessee', u'NY': u'New York', u'PA': u'Pennsylvania', u'CT': u'Connecticut', u'RI': u'Rhode Island', u'NV': u'Nevada', u'NH': u'New Hampshire', u'GU': u'Guam', u'CO': u'Colorado', u'VI': u'Virgin Islands', u'AK': u'Alaska', u'AL': u'Alabama', u'AS': u'American Samoa', u'AR': u'Arkansas', u'VT': u'Vermont', u'IL': u'Illinois', u'GA': u'Georgia', u'IN': u'Indiana', u'IA': u'Iowa', u'MA': u'Massachusetts', u'AZ': u'Arizona', u'CA': u'California', u'ID': u'Idaho', u'PW': u'Palau', u'ME': u'Maine', u'MD': u'Maryland', u'OK': u'Oklahoma', u'OH': u'Ohio', u'UT': u'Utah', u'MO': u'Missouri', u'MN': u'Minnesota', u'MI': u'Michigan', u'MH': u'Marshall Islands', u'KS': u'Kansas', u'MT': u'Montana', u'MP': u'Northern Mariana Islands', u'MS': u'Mississippi', u'SC': u'South Carolina', u'KY': u'Kentucky', u'OR': u'Oregon', u'SD': u'South Dakota'},
    u'CA': {u'AB': u'Alberta', u'BC': u'British Columbia', u'MB': u'Manitoba', u'NB': u'New Brunswick', u'NT': u'Northwest Territories', u'NS': u'Nova Scotia', u'NU': u'Nunavut', u'ON': u'Ontario', u'PE': u'Prince Edward Island', u'QC': u'Quebec', u'SK': u'Saskatchewan', u'YU': u'Yukon', u'NL': u'Newfoundland and Labrador'},
    u'AU': {u'WA': u'State of Western Australia', u'SA': u'State of South Australia', u'NT': u'Northern Territory', u'VIC': u'State of Victoria', u'TAS': u'State of Tasmania', u'QLD': u'State of Queensland', u'NSW': u'State of New South Wales', u'ACT': u'Australian Capital Territory'},
    u'GB': {u'WLS': u'Wales', u'SCT': u'Scotland', u'NIR': u'Northern Ireland', u'ENG': u'England'},
}
COUNTRIES = {u'BD': u'Bangladesh', u'WF': u'Wallis And Futuna Islands', u'BF': u'Burkina Faso', u'PY': u'Paraguay', u'BA': u'Bosnia And Herzegovina', u'BB': u'Barbados', u'BE': u'Belgium', u'BM': u'Bermuda', u'BN': u'Brunei Darussalam', u'BO': u'Bolivia', u'BH': u'Bahrain', u'BI': u'Burundi', u'BJ': u'Benin', u'BT': u'Bhutan', u'JM': u'Jamaica', u'BV': u'Bouvet Island', u'BW': u'Botswana', u'WS': u'Samoa', u'BR': u'Brazil', u'BS': u'Bahamas', u'JE': u'Jersey', u'BY': u'Belarus', u'BZ': u'Belize', u'RU': u'Russian Federation', u'RW': u'Rwanda', u'LT': u'Lithuania', u'RE': u'Reunion', u'TM': u'Turkmenistan', u'TJ': u'Tajikistan', u'RO': u'Romania', u'LS': u'Lesotho', u'GW': u'Guinea-bissau', u'GU': u'Guam', u'GT': u'Guatemala', u'GS': u'South Georgia And South Sandwich Islands', u'GR': u'Greece', u'GQ': u'Equatorial Guinea', u'GP': u'Guadeloupe', u'JP': u'Japan', u'GY': u'Guyana', u'GG': u'Guernsey', u'GF': u'French Guiana', u'GE': u'Georgia', u'GD': u'Grenada', u'GB': u'Great Britain', u'GA': u'Gabon', u'GN': u'Guinea', u'GM': u'Gambia', u'GL': u'Greenland', u'GI': u'Gibraltar', u'GH': u'Ghana', u'OM': u'Oman', u'TN': u'Tunisia', u'JO': u'Jordan', u'HR': u'Croatia', u'HT': u'Haiti', u'SV': u'El Salvador', u'HK': u'Hong Kong', u'HN': u'Honduras', u'HM': u'Heard And Mcdonald Islands', u'AD': u'Andorra', u'PR': u'Puerto Rico', u'PS': u'Palestine', u'PW': u'Palau', u'PT': u'Portugal', u'SJ': u'Svalbard And Jan Mayen Islands', u'VG': u'Virgin Islands, British', u'AI': u'Anguilla', u'KP': u'North Korea', u'PF': u'French Polynesia', u'PG': u'Papua New Guinea', u'PE': u'Peru', u'PK': u'Pakistan', u'PH': u'Philippines', u'PN': u'Pitcairn', u'PL': u'Poland', u'PM': u'Saint Pierre And Miquelon', u'ZM': u'Zambia', u'EH': u'Western Sahara', u'EE': u'Estonia', u'EG': u'Egypt', u'ZA': u'South Africa', u'EC': u'Ecuador', u'IT': u'Italy', u'AO': u'Angola', u'KZ': u'Kazakhstan', u'ET': u'Ethiopia', u'ZW': u'Zimbabwe', u'SA': u'Saudi Arabia', u'ES': u'Spain', u'ER': u'Eritrea', u'ME': u'Montenegro', u'MD': u'Moldova', u'MG': u'Madagascar', u'MA': u'Morocco', u'MC': u'Monaco', u'UZ': u'Uzbekistan', u'MM': u'Myanmar', u'ML': u'Mali', u'MO': u'Macau', u'MN': u'Mongolia', u'MH': u'Marshall Islands', u'US': u'United States', u'UM': u'United States Minor Outlying Islands', u'MT': u'Malta', u'MW': u'Malawi', u'MV': u'Maldives', u'MQ': u'Martinique', u'MP': u'Northern Mariana Islands', u'MS': u'Montserrat', u'NA': u'Namibia', u'IM': u'Isle Of Man', u'UG': u'Uganda', u'MY': u'Malaysia', u'MX': u'Mexico', u'IL': u'Israel', u'BG': u'Bulgaria', u'FR': u'France', u'AW': u'Aruba', u'AX': u'\xc3\x85land', u'FI': u'Finland', u'FJ': u'Fiji', u'FK': u'Falkland Islands', u'FM': u'Micronesia', u'FO': u'Faroe Islands', u'NI': u'Nicaragua', u'NL': u'Netherlands', u'NO': u'Norway', u'SO': u'Somalia', u'NC': u'New Caledonia', u'NE': u'Niger', u'NF': u'Norfolk Island', u'NG': u'Nigeria', u'NZ': u'New Zealand', u'NP': u'Nepal', u'NR': u'Nauru', u'NU': u'Niue', u'MR': u'Mauritania', u'CK': u'Cook Islands', u'CI': "C\xc3\xb4te D'ivoire", 'CH': u'Switzerland', u'CO': u'Colombia', u'CN': u'China', u'CM': u'Cameroon', u'CL': u'Chile', u'CC': u'Cocos (keeling) Islands', u'CA': u'Canada', u'CG': u'Congo (brazzaville)', u'CF': u'Central African Republic', u'CD': u'Congo (kinshasa)', u'CZ': u'Czech Republic', u'CY': u'Cyprus', u'CX': u'Christmas Island', u'CS': u'Serbia', u'CR': u'Costa Rica', u'HU': u'Hungary', u'CV': u'Cape Verde', u'CU': u'Cuba', u'SZ': u'Swaziland', u'SY': u'Syria', u'KG': u'Kyrgyzstan', u'KE': u'Kenya', u'SR': u'Suriname', u'KI': u'Kiribati', u'KH': u'Cambodia', u'KN': u'Saint Kitts And Nevis', u'KM': u'Comoros', u'ST': u'Sao Tome And Principe', u'SK': u'Slovakia', u'KR': u'South Korea', u'SI': u'Slovenia', u'SH': u'Saint Helena', u'KW': u'Kuwait', u'SN': u'Senegal', u'SM': u'San Marino', u'SL': u'Sierra Leone', u'SC': u'Seychelles', u'SB': u'Solomon Islands', u'KY': u'Cayman Islands', u'SG': u'Singapore', u'SE': u'Sweden', u'SD': u'Sudan', u'DO': u'Dominican Republic', u'DM': u'Dominica', u'DJ': u'Djibouti', u'DK': u'Denmark', u'DE': u'Germany', u'YE': u'Yemen', u'AT': u'Austria', u'DZ': u'Algeria', u'MK': u'Macedonia', u'UY': u'Uruguay', u'YT': u'Mayotte', u'MU': u'Mauritius', u'TZ': u'Tanzania', u'LC': u'Saint Lucia', u'LA': u'Laos', u'TV': u'Tuvalu', u'TW': u'Taiwan', u'TT': u'Trinidad And Tobago', u'TR': u'Turkey', u'LK': u'Sri Lanka', u'LI': u'Liechtenstein', u'LV': u'Latvia', u'TO': u'Tonga', u'TL': u'Timor-leste', u'LU': u'Luxembourg', u'LR': u'Liberia', u'TK': u'Tokelau', u'TH': u'Thailand', u'TF': u'French Southern Lands', u'TG': u'Togo', u'TD': u'Chad', u'TC': u'Turks And Caicos Islands', u'LY': u'Libya', u'VA': u'Vatican City', u'AC': u'Ascension Island', u'VC': u'Saint Vincent And The Grenadines', u'AE': u'United Arab Emirates', u'VE': u'Venezuela', u'AG': u'Antigua And Barbuda', u'AF': u'Afghanistan', u'IQ': u'Iraq', u'VI': u'Virgin Islands, U.s.', u'IS': u'Iceland', u'IR': u'Iran', u'AM': u'Armenia', u'AL': u'Albania', u'VN': u'Vietnam', u'AN': u'Netherlands Antilles', u'AQ': u'Antarctica', u'AS': u'American Samoa', u'AR': u'Argentina', u'AU': u'Australia', u'VU': u'Vanuatu', u'IO': u'British Indian Ocean Territory', u'IN': u'India', u'LB': u'Lebanon', u'AZ': u'Azerbaijan', u'IE': u'Ireland', u'ID': u'Indonesia', u'PA': u'Panama', u'UA': u'Ukraine', u'QA': u'Qatar', u'MZ': u'Mozambique'}

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'

VALID_URL_REGEX = re.compile('^(?#Protocol)(?:(?:ht|f)tp(?:s?)\:\/\/|~\/|\/)?(?#Username:Password)(?:\w+:\w+@)?(?#Subdomains)(?:(?:[-\w]+\.)+(?#TopLevel Domains)(?:com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum|travel|[a-z]{2}))(?#Port)(?::[\d]{1,5})?(?#Directories)(?:(?:(?:\/(?:[-\w~!$+|.,=]|%[a-f\d]{2})+)+|\/)+|\?|#)?(?#Query)(?:(?:\?(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=?(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)(?:&(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=?(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)*)*(?#Anchor)(?:#(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?$')



class Serializable(object):
    
    """The base class of every class in the library that needs the ability to
    be serialized/deserialized to/from a JSON string.
    
    Every inherited class must implement its own to_dict method that transforms
    an object to a dict and from_dict method that transforms a dict to 
    an object.
    
    """
    
    @classmethod
    def from_json(cls, json_str):
        """Deserialize the object from a JSON string."""
        d = json.loads(json_str)
        return cls.from_dict(d)
        
    def to_json(self):
        """Serialize the object to a JSON string."""
        d = self.to_dict()
        return json.dumps(d)


def str_to_datetime(s):
    """Transform an str object to a datetime object."""
    return datetime.datetime.strptime(s, TIMESTAMP_FORMAT)


def datetime_to_str(dt):
    """Transform a datetime object to an str object."""
    return dt.isoformat()


def str_to_date(s):
    """Transform an str object to a date object."""
    return datetime.datetime.strptime(s, DATE_FORMAT).date()


def date_to_str(d):
    """Transform a date object to an str object."""
    return d.isoformat()


def is_valid_url(url):
    """Return True if `url` (str/unicode) is a valid URL, False otherwise."""
    return bool(VALID_URL_REGEX.search(url))


def alpha_chars(s):
    """Strip all non alphabetic characters from the str/unicode `s`."""
    return ''.join([c for c in s if c.isalpha()])
    
    
def alnum_chars(s):
    """Strip all non alphanumeric characters from the str/unicode `s`."""
    return ''.join([c for c in s if c.isalnum()])


def to_utf8(obj):
    """Return str representation of obj, if s is a unicode object it's encoded
    with utf8."""
    if isinstance(obj, unicode):
        return obj.encode('utf8')
    return str(obj)


def to_unicode(obj):
    """Return unicode representation of obj, if s is an str object it's decoded
    with utf8."""
    if isinstance(obj, str):
        return obj.decode('utf8')
    return unicode(obj)

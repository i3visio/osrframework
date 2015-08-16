from osrframework.thirdparties.pipl_com.lib.utils import Serializable


class APIError(Exception, Serializable):
    
    """An exception raised when the response from the API contains an error."""
    
    def __init__(self, error, http_status_code):
        """Extend Exception.__init___ and set two extra attributes - 
        error (unicode) and http_status_code (int)."""
        Exception.__init__(self, error)
        self.error = error
        self.http_status_code = http_status_code
    
    @property
    def is_user_error(self):
        """A bool that indicates whether the error is on the user's side."""
        return 400 <= self.http_status_code < 500
    
    @property
    def is_pipl_error(self):
        """A bool that indicates whether the error is on Pipl's side."""
        return not self.is_user_error
    
    @classmethod
    def from_dict(cls, d):
        """Transform the dict to a error object and return the error."""
        return cls(d.get('error'), d.get('@http_status_code'))
    
    def to_dict(self):
        """Return a dict representation of the error."""
        return {'error': self.error, '@http_status_code': self.http_status_code}
        

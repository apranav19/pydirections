from .exceptions import InvalidModeError, InvalidAPIKeyError
ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])

class DirectionsRequest(object):
	"""
		This class holds all the necessary information required for a proposed route
	"""
	def __init__(self, **kwargs):
		"""
			The constructor will set values for the required params i.e. origin & destination
			Addtionally, it will set the default mode of transportation as driving
		"""
		self.__mode = "driving"
		self.__origin = kwargs['origin']
		self.__destination = kwargs['destination']

	@property
	def api_key(self):
		return self.__api_key

	def set_api_key(self, api_key):
		if type(api_key) != str:
			raise InvalidAPIKeyError
		self.__api_key = api_key
		return self
	
	@property
	def mode(self):
	    return self.__mode

	def set_mode(self, mode):
		if mode not in ACCEPTABLE_MODES:
			raise InvalidModeError(mode)
		self.__mode = mode
		return self

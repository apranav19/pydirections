from .exceptions import InvalidModeError, InvalidAPIKeyError, InvalidAlternativeError

class ModeContainer(object):
	"""
		The purpose of this class is to simply validate modes
	"""
	__ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])

	@classmethod
	def validate_mode(cls, mode):
		""" 
			This function simply checks if a given mode exists in the
			set of acceptable modes
		"""
		return mode in cls.__ACCEPTABLE_MODES

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
		self.__alternatives = False

	@property
	def api_key(self):
		""" Returns the currently configured api key """
		return self.__api_key

	def set_api_key(self, api_key):
		"""
			This function sets the API key for an instance of a DirectionsRequest class.
			Raises an InvalidAPIKeyError if the provided key is not a string.
		"""
		if type(api_key) != str:
			raise InvalidAPIKeyError
		self.__api_key = api_key
		return self
	
	@property
	def mode(self):
		""" Returns the currently configured mode of transportation """
		return self.__mode

	def set_mode(self, mode):
		"""
			This function configures the mode of transportation.
			Raises an InvalidModeError if the mode provided does not exist.
		"""
		if not ModeContainer.validate_mode(mode):
			raise InvalidModeError(mode)
		self.__mode = mode
		return self

	def set_alternatives(self, alternative):
		""" Toggles the alternative param if user wants alternative routes """
		if type(alternative) != bool:
			raise InvalidAlternativeError
		
		self.__alternatives = alternative
		return self

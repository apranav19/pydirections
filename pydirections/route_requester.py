from .exceptions import MissingParameterError, InvalidModeError, InvalidAPIKeyError
from .exceptions import InvalidAlternativeError, MissingAPIKeyError, InvalidRouteRestrictionError
import re
import json


class ParameterValidationContainer(object):
	"""
		The purpose of this class is to simply validate any pre-defined parameters
		such as: possible modes, route restriction params
	"""
	ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])
	ACCEPTABLE_RESTRICTIONS = set(["tolls", "highways", "ferries"])

	@classmethod
	def validate_mode(cls, mode):
		"""
			This function simply checks if a given mode exists in the
			set of acceptable modes
		"""
		return mode in cls.ACCEPTABLE_MODES

	@classmethod
	def validate_restrictions(cls, restrictions):
		"""
			This function applies validation on the restrictions provided
		"""
		for restriction in restrictions:
			if not restriction in cls.ACCEPTABLE_RESTRICTIONS:
				return False

		return True

class DirectionsRequest(object):
	"""
		This class holds all the necessary information required for a proposed route
	"""
	REQUEST_ERROR_MESSSAGES = {
		'missing_params': "Missing the {0} parameter",
		'invalid_route_restrictions': "Invalid route restrictions provided",
		'invalid_mode': "{0} is not a valid mode"
	}

	def __init__(self, **kwargs):
		"""
			The constructor will set values for the required params i.e. origin & destination
			Addtionally, it will set the default mode of transportation as driving
		"""

		try: # Check for required params
			self._origin = kwargs['origin']
			self._destination = kwargs['destination']
			self._key = kwargs['key']
			self._mode = "driving"
		except KeyError as key_err:
			raise MissingParameterError(DirectionsRequest.REQUEST_ERROR_MESSSAGES['missing_params'].format(key_err))

	@property
	def key(self):
		""" Returns the currently configured api key """
		return self._key

	@key.setter
	def key(self, api_key):
		"""
			This function sets the API key for an instance of a DirectionsRequest class.
			Raises an InvalidAPIKeyError if the provided key is not a string.
		"""
		if type(api_key) != str:
			raise InvalidAPIKeyError
		self._key = api_key
		return self

	@property
	def mode(self):
		""" Returns the currently configured mode of transportation """
		return self._mode

	@mode.setter
	def mode(self, mode):
		"""
			This function configures the mode of transportation.
			Raises an InvalidModeError if the mode provided does not exist.
		"""
		if not ParameterValidationContainer.validate_mode(mode):
			raise InvalidModeError(self.REQUEST_ERROR_MESSSAGES['invalid_mode'].format(mode))
		self._mode = mode
		return self

	def set_alternatives(self, alternative):
		""" Toggles the alternative param if user wants alternative routes """
		if type(alternative) != bool:
			raise InvalidAlternativeError

		self.alternatives = alternative
		return self

	def set_route_restrictions(self, *args):
		"""
			This function configures the supplied restrictions for a route
		"""
		normalized_args = set(args)
		if len(normalized_args) > 3:
			raise ValueError("There are only 3 route restrictions")

		if not ParameterValidationContainer.validate_restrictions(normalized_args):
			raise InvalidRouteRestrictionError(self.REQUEST_ERROR_MESSSAGES['invalid_route_restrictions'])

		self.avoid = list(normalized_args)
		return self

	def get_payload(self):
		"""
			This function converts an instance of DirectionsRequest to a dictionary
		"""
		res_payload, current_payload, REGEX_PATTERN = {}, self.__dict__, '_'
		for param in current_payload:
			clean_param = re.split(REGEX_PATTERN, param)[1]
			current_value = current_payload[param]
			if clean_param == 'avoid':
				res_payload[clean_param] = self.__format_route_restrictions(current_value)
			else:
				res_payload[clean_param] = current_payload[param]
		return res_payload

	def __format_route_restrictions(self, restrictions):
		"""
			This private function formats the route restrictions parameters accordingly
		"""
		return ('|').join(restrictions)

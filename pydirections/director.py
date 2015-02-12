from __future__ import absolute_import
from builtins import object
import requests
from .exceptions import MissingParameterError, InvalidModeError, InvalidAPIKeyError, MissingAPIKeyError
from .route_request import DirectionsRequest

class Director(object):
	"""
        The Director class is responsible for handling a user's requests and processing the
        HTTP responses from Google's Directions API.
	"""
	__ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])
	__BASE_URL = "https://maps.googleapis.com/maps/api/directions/json?"
	__REQUEST_URL = None
	__CURRENT_API_KEY = None

	@classmethod
	def configure_api_key(cls, api_key):
		"""
		    This function configures the API Key for the current application/consumer
		"""
		if type(api_key) != str:
			raise InvalidAPIKeyError

		cls.__CURRENT_API_KEY = api_key
		return cls

	@classmethod
	def has_configured_key(cls):
		""" Checks whether an api key has been configured """
		return cls.__CURRENT_API_KEY != None

	@classmethod
	def is_valid_mode(cls, mode):
		"""
		   Checks if a given mode of transport is valid
		"""
		return mode in cls.__ACCEPTABLE_MODES

	@classmethod
	def get_base_url(cls):
		"""
			Returns the base uri
		"""
		return cls.__BASE_URL

	@classmethod
	def get_request_url(cls):
		"""
			Returns the complete url of the request that has been made
		"""
		return cls.__REQUEST_URL

	@classmethod
	def fetch_directions(cls, request_object):
		"""
		   Given the origin and destination (addresses or points of interests),
		   this function will make a request to Google and fetch the possible routes
		"""
		return None
		
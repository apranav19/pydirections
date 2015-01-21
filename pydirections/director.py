from __future__ import absolute_import
from builtins import object
import requests
from .exceptions import MissingParameterError, InvalidModeError

class Director(object):
	"""
        The Director class is responsible for handling a user's requests and processing the
        HTTP responses from Google's Directions API.
	"""
	__ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])
	__BASE_URL = "https://maps.googleapis.com/maps/api/directions/{0}?"
	__REQUEST_URL = None
	__CURRENT_OUTPUT_FORMAT = "json"

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
	def fetch_directions(cls, mode="driving", **kwargs):
		"""
		   Given the origin and destination (addresses or points of interests),
		   this function will make a request to Google and fetch the possible routes
		"""
		if 'origin' not in kwargs or 'destination' not in kwargs:
			raise MissingParameterError("Missing either an origin or a destination")

		mode = mode.lower() # Ensure consistency

		# Ensure mode is valid
		if not cls.is_valid_mode(mode):
			raise InvalidModeError(mode)

		origin, destination = kwargs['origin'], kwargs['destination']

		# Prepare the actual request uri
		request_url = cls.__BASE_URL.format(cls.__CURRENT_OUTPUT_FORMAT)
		resp = requests.get(request_url, params={'origin':origin, 'destination':destination, 'mode':mode})
		cls.__REQUEST_URL = resp.url

		# Return data
		data = resp.json()

		if data['status'] != "OK":
			raise ValueError("Here's what went wrong: " + data['status'])

		return data

from __future__ import absolute_import
from builtins import object
import requests
from .exceptions import MissingParameterError, InvalidModeError, InvalidAPIKeyError, MissingAPIKeyError, InvalidRequestObjectError
from .route_requester import DirectionsRequest
from .route_responses import DirectionsResponse

class Director(object):
	"""
        The Director class is responsible for handling a user's requests and processing the
        HTTP responses from Google's Directions API.
	"""
	__BASE_URL = "https://maps.googleapis.com/maps/api/directions/json?"
	__REQUEST_URL = None

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
		if not isinstance(request_object, DirectionsRequest):
			raise InvalidRequestObjectError()

		resp = requests.get(cls.__BASE_URL, params=request_object.get_payload())
		cls.__REQUEST_URL = resp.url

		return cls.__serialize_response(resp.json())

	@classmethod
	def __serialize_response(cls, stream):
		return DirectionsResponse(stream['status'], stream['routes'])
		
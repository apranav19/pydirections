from schematics.models import Model
from schematics.types import StringType

from .models import Route

class DirectionsResponse(object):
	"""
		The Directions Response class represents a response.
		The two attributes include:
		1. Status - Represents the status of the request
		2. Routes - Represents an array of routes from origin to destination
	"""
	def __init__(self, status, routes):
		self._status = status
		self._routes = routes

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

	@property
	def routes(self):
	    return self._routes

	@routes.setter
	def routes(self, routes):
		self._routes = routes

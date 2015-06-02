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
		self.status = status
		self.routes = routes

	@property
	def status(self):
		return self.status

	@property
	def routes(self):
	    return self.routes

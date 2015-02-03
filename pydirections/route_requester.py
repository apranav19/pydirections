"""
    This class holds all the necessary information required for a proposed route
"""
ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])

class DirectionsRequest(object):

	def __init__(self, **kwargs):
		self.mode = "driving"
		self.origin = kwargs['origin']
		self.destination = kwargs['destination']

	
	def set_api_key(self, key):
		self.api_key = key
		return self

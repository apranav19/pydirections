import requests

class Director(object):
	"""
        The Director class is responsible for handling a user's requests and processing the
        HTTP responses from Google's Directions API.
	"""
	def __init__(self):
		"""
			The constructor builds the base uri
		"""
		self.__base_uri = "https://maps.googleapis.com/maps/api/directions/{0}?"
		self.__output_format = "json"

	@property
	def base_uri(self):
		"""
			Returns the base uri
		"""
		return self.__base_uri

	@property
	def output_format(self):
	 	"""
	 		Returns the current output format
	 	"""
		return self.__output_format

	@output_format.setter
	def change_output_format(self, output_format):
		"""
			Changes the current output format to the one provided
		""" 
		self.__output_format = output_format

	def fetch_directions(self, mode="driving", **kwargs):
		origin, destination = kwargs['origin'], kwargs['dest']
		request_uri = self.__base_uri.format(self.__output_format)
		resp = requests.get(request_uri, params={'origin':origin, 'destination':destination, 'mode':mode})
		return resp

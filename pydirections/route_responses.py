from future.utils import with_metaclass
from abc import ABCMeta, abstractmethod

class BaseResponse(with_metaclass(ABCMeta, object)):
	"""
		The Base Response class
	"""
	def __init__(self, stream):
		self.__status = stream

	@property
	def status(self):
		""" Returns the status code of the request made """
		return self.__status

class DirectionsResponse(BaseResponse):
	"""
		The Directions Response class represents a response which was obtained due to a successful request
	"""
	def __init__(self, status, routes):
		self.__status = status
		self.__routes = routes

	@property
	def status(self):
		return self.__status

	@property
	def routes(self):
	    return self.__routes

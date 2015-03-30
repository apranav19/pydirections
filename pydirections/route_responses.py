from future.utils import with_metaclass
from abc import ABCMeta, abstractmethod

class BaseResponse(with_metaclass(ABCMeta, object)):
	"""
		The Base Response class
	"""
	def __init__(self, status):
		self.__status = status
		self.__routes = []

	@property
	def status(self):
		""" Returns the status code of the request made """
		return self.__status

	@property
	def routes(self):
		return self.__routes

class DirectionsResponse(BaseResponse):
	"""
		The Directions Response class represents a response which was obtained due to a successful request
	"""
	pass
	
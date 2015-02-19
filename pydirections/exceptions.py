"""
	This file is comprised of all the custom Exceptions that will be utilized elsewhere
"""

class ParameterError(Exception):
	def __init__(self):
		self.error_msg = "Parameter Error: {0}"

	def __str__(self):
		return repr(self.error_msg)

class InvalidModeError(ParameterError):
	"""
		This particular exception handles cases where an invalid mode is provided
	"""
	def __init__(self, mode):
		super(InvalidModeError, self).__init__()
		self.error_msg = self.error_msg.format("{0} is not a valid mode".format(mode))

class MissingParameterError(ParameterError):
	"""
	    This particular exception handles cases when either an origin or a destination
	    parameter is incorrectly passed or is missing
	"""
	def __init__(self, msg):
		super(MissingParameterError, self).__init__()
		self.error_msg = self.error_msg.format(msg)

class InvalidAPIKeyError(Exception):
	"""
		This particular exception handles a scenario if a non-string value was provided as the api key
	"""
	def __init__(self):
		self.error_msg = "The API Key provided must be a string data type"

	def __str__(self):
		return repr(self.error_msg)

class MissingAPIKeyError(Exception):
	"""
		This exception is raised when a user has not configured an API Key
	"""
	def __init__(self):
		self.error_msg = "An API Key must be configured before requesting directions"

	def __str__(self):
		return repr(self.error_msg)

class InvalidAlternativeError(Exception):
	"""
		This exception is raised when a user provides a non-boolean value
	"""
	def __init__(self):
		self.error_msg = "The Alternative parameter must be set to either True or False"

	def __str__(self):
		return repr(self.error_msg)

class InvalidRequestObjectError(Exception):
	"""
		This exception is raised when a user provides an object (that is not an instance of
		the DirectionsRequest class) to Director's fetch_directions()
	"""
	def __init__(self):
		self.error_msg = "The request_object must be an instance of the DirectionsRequest class"

	def __str__(self):
		return repr(self.error_msg)
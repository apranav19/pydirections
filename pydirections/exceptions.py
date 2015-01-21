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
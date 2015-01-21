from pydirections.director import Director
from unittest import TestCase

class TestModeValidity(TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		default_error_message = "The mode: {0} is invalid"
		invalid_mode = "flying"
		self.assertFalse(Director.is_valid_mode(invalid_mode), msg=default_error_message.format(invalid_mode))

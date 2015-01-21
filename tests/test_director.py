from pydirections.director import Director
from unittest import TestCase
import re

class TestModeValidity(TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		default_error_message = "The mode: {0} is invalid"
		invalid_mode = "flying"
		self.assertFalse(Director.is_valid_mode(invalid_mode), msg=default_error_message.format(invalid_mode))

class TestDirectionFetching(TestCase):
	"""
	    This class has test cases to cover the functionality of the fetch_directions function.
	"""	
	def test_invalid_or_missing_params(self):
		"""
			Tests if the required key-word args are missing or are invalid
		"""
		with self.assertRaises(ValueError):
			Director.fetch_directions()

		with self.assertRaises(ValueError):
			Director.fetch_directions(origin="123 Fake Street Springfield, MA", dest="End")

	def test_invalid_mode(self):
		"""
			Tests if an exception was raised if an invalid mode was provided
		"""
		with self.assertRaises(ValueError):
			Director.fetch_directions(origin="San Francisco, CA", destination="Mountain View, CA", mode="flying")

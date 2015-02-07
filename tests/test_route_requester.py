import unittest
from pydirections.route_requester import DirectionsRequest
from pydirections.exceptions import InvalidModeError, InvalidAPIKeyError, InvalidAlternativeError

requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA")

class TestOptionalParameters(unittest.TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		with self.assertRaises(InvalidModeError):
			requester.set_mode("flying")

	def test_invalid_alternative(self):
		"""
			Tests for error handling when an invalid value is provided to
			the set_alternative function
		"""
		with self.assertRaises(InvalidAlternativeError):
			requester.set_alternatives('False')

class TestAPIKey(unittest.TestCase):
	
	def test_invalid_api_key(self):
		invalid_key = 123456
		with self.assertRaises(InvalidAPIKeyError):
			requester.set_api_key(invalid_key)

if __name__ == '__main__':
	unittest.main()
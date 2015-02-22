import unittest
from pydirections.route_requester import DirectionsRequest
from pydirections.exceptions import InvalidModeError, InvalidAPIKeyError, InvalidAlternativeError
from pydirections.exceptions import InvalidRouteRestrictionError
import os

MAPS_API_KEY = os.environ['MAPS_API_KEY']

class TestOptionalParameters(unittest.TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA", key=MAPS_API_KEY)
		with self.assertRaises(InvalidModeError):
			requester.set_mode("flying")

	def test_invalid_alternative(self):
		"""
			Tests for error handling when an invalid value is provided to
			the set_alternative function
		"""
		requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA", key=MAPS_API_KEY)
		with self.assertRaises(InvalidAlternativeError):
			requester.set_alternatives('False')

	def test_invalid_restrictions(self):
		"""
			Tests for invalid route restrictions
		"""
		requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA", key=MAPS_API_KEY)
		with self.assertRaises(InvalidRouteRestrictionError):
			requester.set_route_restrictions("freeways", "railways")

class TestAPIKey(unittest.TestCase):
	def test_invalid_api_key(self):
		requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA", key=MAPS_API_KEY)
		invalid_key = 123456
		with self.assertRaises(InvalidAPIKeyError):
			requester.set_api_key(invalid_key)

if __name__ == '__main__':
	unittest.main()
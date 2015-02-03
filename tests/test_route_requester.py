import unittest
from pydirections.route_requester import DirectionsRequest

class TestModeValidity(unittest.TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		with self.assertRaises(ValueError):
			requester = DirectionsRequest(origin="San Francisco, CA", destination="Palo Alto, CA")
			requester.set_mode("flying")

if __name__ == '__main__':
	unittest.main()
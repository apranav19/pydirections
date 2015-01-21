import unittest
from pydirections.director import Director

class TestModeValidity(unittest.TestCase):
	def test_invalid_mode(self):
		"""
		    Tests the is_valid_mode function for an invalid input
		"""
		default_error_message = "The mode: {0} is invalid"
		invalid_mode = "flying"
		self.assertFalse(Director.is_valid_mode(invalid_mode), msg=default_error_message.format(invalid_mode))

class TestDirectionFetching(unittest.TestCase):
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

	def test_unimagineable_route(self):
		"""
			Tests if a route cannot be obtained if there are no ways to make a journey between 2
			points based on the provided mode of travel
		"""
		modes = ["driving", "walking", "bicycling", "transit"]
		extreme_end_points = ("San Francisco, CA", "Tokyo, Japan")
		for m in modes:
			with self.assertRaises(ValueError):
				Director.fetch_directions(origin=extreme_end_points[0], destination=extreme_end_points[1], mode=m)



if __name__ == '__main__':
	unittest.main()
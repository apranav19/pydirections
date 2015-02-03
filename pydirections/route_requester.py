
ACCEPTABLE_MODES = set(["driving", "walking", "bicycling", "transit"])

class DirectionsRequest(object):
    """
        This class holds all the necessary information required for a proposed route
    """
    def __init__(self, **kwargs):
		self.mode = "driving"
		self.origin = kwargs['origin']
		self.destination = kwargs['destination']

    def set_api_key(self, key):
        self.api_key = key
        return self

    def set_mode(self, mode):
    	if mode not in ACCEPTABLE_MODES:
    		raise ValueError("Invalid mode")
    	self.mode = mode
    	return self

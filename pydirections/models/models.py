from schematics.models import Model
from schematics.types import StringType

class Step(Model):
	"""
		Represents an individual step
	"""
	html_instructions = StringType()

class Leg(Model):
	"""
		Represents an individual leg
	"""
	start_address = StringType()
	end_address = StringType()
	

class Route(Model):
	"""
		Represents an individual route whose attributes include
	"""
	summary = StringType(required=True)
	copyrights = StringType()

	@property
	def summary():
		return summary
from schematics.models import Model
from schematics.types import StringType, DecimalType
from schematics.types.compound import ListType, ModelType

class Distance(Model):
	"""
		Represents the duration of a leg/step
	"""
	value = DecimalType()
	text = StringType()

class Duration(Model):
	"""
		Represents the duration of a leg/step
	"""
	value = DecimalType()
	text = StringType()


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
	steps = ListType(ModelType(Step))


class Route(Model):
	"""
		Represents an individual route whose attributes include
	"""
	summary = StringType(required=True)
	legs = ListType(ModelType(Leg))
	copyrights = StringType()

	@property
	def summary():
		return summary

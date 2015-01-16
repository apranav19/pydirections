# pydirections #

PyDirections is an easy to use Python client for Google's [Directions](https://developers.google.com/maps/documentation/directions/) API.
Through this client you can request directions between any two points for the following modes of transport:
* Driving
* Walking
* Bicycling
* Public Transit

## Quick Start ##
### Installing PyDirections ###
You can install PyDirections through pip by running the command:
	`pip install pydirections`

### Requesting Driving Directions ###
To request driving directions between two addresses, create a Director object and supply the two addresses.

	import pydirections
	director = pydirections.Director(origin="123 Fake St Springfield, MA", dest="5th Avenue Springfield, MA")
	directions = director.fetch_directions()

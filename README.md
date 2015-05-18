# pydirections #

[![Build Status](https://magnum.travis-ci.com/apranav19/pydirections.svg?token=1SB6Uw5qyBVN5BUSihPq&branch=basic_test_coverage)](https://magnum.travis-ci.com/apranav19/pydirections)

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
```
import pydirections

director = pydirections.Director.configure_api_key(<YOUR API KEY>)
routes = director.fetch_directions(origin="123 Fake St Springfield, MA", dest="456 Fake St Springfield, MA", mode="driving")
```

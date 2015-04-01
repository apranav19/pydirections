from pydirections import DirectionsRequest, Director
import os
import json

output_file = open('test_data.json', 'r+')
req = DirectionsRequest(origin="San Francisco, CA", destination="Mountain View, CA", key=os.environ['MAPS_API_KEY'])
resp = Director.fetch_directions(req)
json.dump(resp, output_file)
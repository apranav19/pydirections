from pydirections import DirectionsRequest, Director
import os

req = DirectionsRequest(origin="San Francisco, CA", destination="Mountain View, CA", key=os.environ['MAPS_API_KEY'])
resp = Director.fetch_directions(req)
print(resp.status)
print("===============")
print(resp.routes)
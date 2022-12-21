import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];area[name="India"];(node[place="city"](area););out;
"""

response = requests.get(
    overpass_url,
    params={'data': overpass_query}
)
count = 100
coords = []
if response.status_code == 200:
    data = response.json()
    places = data.get('elements', [])
    for place in places:
        coords.append((place['lat'], place['lon']))
        count -=1
        if count==0:
            break
    print ("Got %s village coordinates!" % len(coords))
    print (coords[0])
else:
     print("Error")
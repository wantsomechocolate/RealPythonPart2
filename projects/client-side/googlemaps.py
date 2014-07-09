# googlemaps.py

import requests

lang='json'
url='http://maps.googleapis.com/maps/api/directions/'

origin='Central+Park'
destination='Times+Square'
sensor='false'
mode='walking'

request=url+lang+'?'+'origin='+origin+'&'+'destination='+destination+\
'&'+'sensor='+sensor+'&'+'mode='+mode


response=requests.get(request)

output=response.json()

for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print step['html_instructions'], step['distance']['text']

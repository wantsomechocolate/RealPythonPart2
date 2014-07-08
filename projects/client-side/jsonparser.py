# jsonparser.py

import json
import requests


##output = json.load(open('cars.json'))
##
##print (json.dumps(output, indent=4, sort_keys=True))
##print(output[0]['CAR'][0]['MODEL'])

url = 'http://httpbin.org/post'

payload={'colors':[
    {'color':'red','hex':'#f00'},
    {'color':'green','hex':'#0f0'},
    {'color':'blue','hex':'#00f'},
    {'color':'cyan','hex':'#0ff'},
    {'color':'magenta','hex':'#f0f'},
    {'color':'yellow','hex':'#ff0'},
    {'color':'yellow','hex':'#000'}
    ]}

headers = {'content-type':'application/json'}

response=requests.post(url, data=json.dumps(payload), headers=headers)

print response.status_code

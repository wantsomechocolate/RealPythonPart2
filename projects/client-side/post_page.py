# retrieving a web page

import requests

url='http://httpbin.org/post'
data={'fname':'Michael','lname':'Herman'}



# retrieve the web page
r=requests.post(url, data=data)


print r

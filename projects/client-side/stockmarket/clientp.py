import requests
import time

#i=0

while(True):

	base_url = 'http://download.finance.yahoo.com/d/quotes.csv'

	data = requests.get(base_url,
		params={'s':'GOOG', 'f':'sl1d1t1c1ohgv','e':'.csv'})

	with open('stocks.csv','a') as code:
		code.write(data.content)
	#i+=1

	time.sleep(60)
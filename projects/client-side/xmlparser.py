# xml parsing 1

from xml.etree import ElementTree as et

### parses the file
##
##doc = et.parse("cars.xml")
##
###outputs the first Model in the file
##
###print(doc.find("CAR[2]/MODEL").text)
##
##for element in doc.findall("CAR"):
##    print(element.find("MAKE").text + " " +
##          element.find("MODEL").text + ", $" +
##          element.find("COST").text)


import requests
xml = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')

with open('test.xml','wb') as code:
    code.write(xml.content)

doc = et.parse('test.xml')

for element in doc.findall("CD"):
    print ("Album: ", element.find("TITLE").text)
    print ("Artist: ", element.find("ARTIST").text)
    print ("Year: ", element.find("YEAR").text)
    print ("")
    

import urllib2
response = urllib2.urlopen('http://web2py.com')
html = response.read()

from bs4 import BeautifulSoup as bs
soup = bs(html)

urls=[]
base_url="http://web2py.com/"

for link in soup.find_all('a'):
        url = link.get('href')
        if url[:3]!="http":
                url = urllib2.urlparse.urljoin(base_url,url)
        else:
                pass
        
        urls.append(url)
        print url



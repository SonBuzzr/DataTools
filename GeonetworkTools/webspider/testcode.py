import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin


url = 'http://www.dr-chuck.com/'

req = requests.get(url)
print(dir(req))
print(req.headers['Content-Type'])
if 'text/html; charset=UTF-8' != req.headers['Content-Type']:
    print("Ignore non text/html page")
else:
    print("nt")


soup = BeautifulSoup(req.text, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    href = tag.get('href', None)
    if href is None:
        continue
    # print(href)
    up = urlparse(href)
    # print(up)
    if len(up.scheme) < 1:
        href = urljoin(url, href)
        # print(href)
    ipos = href.find('#')
    if(ipos > 1) :
        href = href[:ipos]
        # print(href)

    if(href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif')):
        continue
    if (href.endswith('/')):
        href = href[:-1]
        # print(href)
    if(len(href)<1):
        continue

    # print(href)

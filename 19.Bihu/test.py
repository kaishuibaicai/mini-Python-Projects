import urllib
from bs4 import BeautifulSoup

import time



response = urllib.request.urlopen('https://www.bihu.com/article/404')
print (response.getcode())
html = response.read()

soup = BeautifulSoup(html, "lxml")

print (soup)


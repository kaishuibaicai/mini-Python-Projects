#-*-coding:utf-8-*-
import urllib
import nltk
from bs4 import BeautifulSoup

response = urllib.urlopen('http://www.kekenet.com/read/201709/526460.shtml')
html = response.read()
soup = BeautifulSoup(html, "lxml")
for i in soup.select(".qh_zg"):
	print (i.encode('utf-8'))
print (soup.select(".qh_en"))
#text = soup.get_text(strip=True)
#print (text)
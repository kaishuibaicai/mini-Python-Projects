#-- coding:utf-8 --
import urllib
import nltk
from bs4 import BeautifulSoup
import time

response = urllib.urlopen('http://www.kekenet.com/read/201709/526460.shtml')
html = response.read()
soup = BeautifulSoup(html, "lxml")
a = 1
zg_text = soup.select(".qh_zg")
zg_Post = ''
#print (zg_text) 
en_text = soup.select(".qh_en")
en_Post = ' '
#print (en_text)
for i in zg_text:
	zg_Post += i.get_text().encode('utf-8')
for m in en_text: 
	en_Post += m.get_text().encode('utf-8')
print zg_Post

print en_Post
#text = soup.get_text(strip=True)
#print (text)
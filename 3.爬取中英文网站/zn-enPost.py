#-*-coding:utf-8-*-
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
en_Post = ''
#print (en_text)
for i in zg_text:
	#print (i.encode('utf-8'))
	#print a
	#time.sleep(0.1)
	#print (i.get_text())
	#a += 1
	zg_Post += i.get_text()
for m in en_text: 
	print (m.get_text())
	en_Post += m.get_text()
print zg_Post
print en_Post
#text = soup.get_text(strip=True)
#print (text)
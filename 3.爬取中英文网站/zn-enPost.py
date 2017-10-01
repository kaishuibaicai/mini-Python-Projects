#-- coding:utf-8 --
import urllib
import re
from nltk.tokenize import sent_tokenize
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
#print en_Post
En_Post = en_Post.decode("utf-8")
filtrate = re.compile(u'[^\u4E00-\u9FA5]')#非中文
nEn_Post = filtrate.sub(r'', En_Post)#replace
print nEn_Post.encode('utf-8')
#print sent_tokenize(en_Post,"english")
#text = soup.get_text(strip=True)
#print (text)
#-- coding:utf-8 --
import urllib
import re
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import pymysql

response = urllib.urlopen('http://www.kekenet.com/read/201709/526460.shtml')
html = response.read()
soup = BeautifulSoup(html, "lxml")

postTitle = soup.select("#nrtitle")[0].get_text().encode('utf-8')
print postTitle

zg_text = soup.select(".qh_zg")
zg_Post = ''

en_text = soup.select(".qh_en")
en_Post = ' '

for i in zg_text:
	zg_Post += i.get_text().encode('utf-8')
for m in en_text: 
	en_Post += m.get_text().encode('utf-8')

print zg_Post
print en_Post

En_Post = en_Post.decode("utf-8")
filtrate = re.compile(u'[^\u4E00-\u9FA5]')#非中文
nEn_Post = filtrate.sub(r'', En_Post)#replace
print nEn_Post.encode('utf-8')

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost')
cur = conn.cursor()

conn.commit()
cur.close()
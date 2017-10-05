#-- coding:utf-8 --
import urllib
import re
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import pymysql

response = urllib.urlopen('http://www.kekenet.com/read/201709/526460.shtml')
html = response.read()
soup = BeautifulSoup(html, "lxml")

postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk').encode('utf-8')
print postTitle

zn_text = soup.select(".qh_zg")
zn_Post = ''

en_text = soup.select(".qh_en")
en_Post = ' '

for i in zn_text:
	zn_Post += i.get_text()
for m in en_text: 
	en_Post += m.get_text()

print type(zn_Post)
print type(en_Post)
print zn_Post
print en_Post

zn_Post = zn_Post.decode('gbk').encode('utf-8')
en_Post = en_Post.decode('gbk').encode('utf-8')

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost',charset='utf8')
cur = conn.cursor()
cur.execute('insert ignore into znenpost (postTitle, EnText, ZnText) values (%s, %s, %s)', [postTitle, en_Post, zn_Post])
conn.commit()
cur.close()
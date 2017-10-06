#-- coding:utf-8 --
import urllib
import re
from bs4 import BeautifulSoup
import pymysql

base = 'http://www.kekenet.com'
task = '/read/201710/526886.shtml'

def spider(url):
	response = urllib.urlopen(base+task)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")

	postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk').encode('utf-8')
	print '[爬取成功:]  '+postTitle

	zn_text = soup.select(".qh_zg")
	zn_Post = ''

	en_text = soup.select(".qh_en")
	en_Post = ' '

	for i in zn_text:
		zn_Post += i.get_text()
	for m in en_text: 
		en_Post += m.get_text()

	zn_Post = zn_Post.decode('gbk').encode('utf-8')
	en_Post = en_Post[:-25].decode('gbk').encode('utf-8')
	result = [postTitle, en_Post, zn_Post]
	return result
##############################################################################
# response = urllib.urlopen(base+task)
# html = response.read()
# soup = BeautifulSoup(html, "lxml")

# postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk').encode('utf-8')
# print '[爬取成功:]  '+postTitle

# zn_text = soup.select(".qh_zg")
# zn_Post = ''

# en_text = soup.select(".qh_en")
# en_Post = ' '

# for i in zn_text:
# 	zn_Post += i.get_text()
# for m in en_text: 
# 	en_Post += m.get_text()


# zn_Post = zn_Post.decode('gbk').encode('utf-8')
# en_Post = en_Post[:-25].decode('gbk').encode('utf-8')


Result = spider(base+task)

conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost',charset='utf8')
cur = conn.cursor()
cur.execute('insert ignore into znenpost (postTitle, EnText, ZnText) values (%s, %s, %s)', [Result[0], Result[1], Result[2]])
conn.commit()
cur.close()
#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import pymysql
import time


base = 'http://www.kekenet.com'
task = '/read/201709/526085.shtml'
n = 1
def spider(url):
	global n
	response = urllib.urlopen(base+task)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")

	postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk', 'ignore').encode('utf-8')
	print '[第%d篇文章数据获取成功:]  %s' % (n, postTitle)

	zn_text = soup.select(".qh_zg")
	zn_Post = ''

	en_text = soup.select(".qh_en")
	en_Post = ' '

	for i in zn_text:
		zn_Post += i.get_text()
	for m in en_text: 
		en_Post += m.get_text()

	newtask = soup.select(".fl")[0].a['href']

	zn_Post = zn_Post.decode('gbk', 'ignore').encode('utf-8')
	en_Post = en_Post[:-25].decode('gbk', 'ignore').encode('utf-8')

	result = [postTitle, en_Post, zn_Post, newtask]
	n += 1

	return result


conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost', charset='utf8')
cur = conn.cursor()


try:
	while 1:
		Result = spider(base+task)
		cur.execute('insert ignore into znenpost (postTitle, EnText, ZnText) values (%s, %s, %s)', [Result[0], Result[1], Result[2]])
		print ('已经保存到数据库')
		task = Result[3]
		#time.sleep(0.5)
finally:
	conn.commit()
	cur.close()

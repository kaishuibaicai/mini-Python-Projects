#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import pymysql
import time

#初始链接
base = 'http://www.kekenet.com'
task = '/read/201709/526085.shtml'
n = 1

#数据爬取函数
def spider(url):
	global n
	response = urllib.urlopen(base+task)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")

	#获取文章标题
	postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk', 'ignore').encode('utf-8')
	print '[第%d篇文章数据获取成功:]  %s' % (n, postTitle)
	
	#获取中文文本
	zn_text = soup.select(".qh_zg")
	zn_Post = ''
	for i in zn_text:
		zn_Post += i.get_text()
	zn_Post = zn_Post.decode('gbk', 'ignore').encode('utf-8')

	#获取英文文本
	en_text = soup.select(".qh_en")
	en_Post = ' '
	for m in en_text: 
		en_Post += m.get_text()
	en_Post = en_Post[:-25].decode('gbk', 'ignore').encode('utf-8')

	#获取下一篇文章的连接
	newtask = soup.select(".fl")[0].a['href']

	result = [postTitle, en_Post, zn_Post, newtask]
	n += 1

	return result

#数据库连接
conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost', charset='utf8')
cur = conn.cursor()


#数据爬取，并且保存到数据库
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

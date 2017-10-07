## 中英文网站文章爬取

#### 一、概述

​	该程序主要是爬取http://www.kekenet.com网站的文章。文章分别有中英两种语言，程序能够自动按顺序爬取每篇文章数据并且将中英文文本存入MySQL数据库中。程序是在Python2.7.13版本下开发，数据库版本是MySql5.7。

**程序运行如下图所示：**

![运行效果](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E8%BF%90%E8%A1%8C%E6%95%88%E6%9E%9C.JPG?raw=true)

**保存到数据库中的数据：**

![数据效果](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)

**英文文本：**

![英文文本](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E8%8B%B1%E6%96%87%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)

**中文文本：**

![中文文本](https://github.com/kaishuibaicai/mini-Python-Projects/blob/master/3.%E7%88%AC%E5%8F%96%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BD%91%E7%AB%99/img/%E4%B8%AD%E6%96%87%E6%95%B0%E6%8D%AE%E6%95%88%E6%9E%9C.JPG?raw=true)



#### 二、运行说明

1. 首先在cmd中登录MySql，创建`zn-enpost`数据库。

2. 运行`CreateTable.py`文件来创建`znenpost`表。

   ```python
   import pymysql

   conn = pymysql.connect(host="127.0.0.1", user='root', passwd='root', db='zn-enpost',charset='utf8')
   cur = conn.cursor()

   #cur.execute('drop znenpost table if exists')

   createTable = """CREATE TABLE znenpost (
   		 id INT UNSIGNED AUTO_INCREMENT NOT NULL,
   		 postTitle VARCHAR(50) NOT NULL, 
   		 EnText TEXT,
   		 ZnText TEXT,
   		 UNIQUE (id, postTitle))"""

   cur.execute(createTable)

   conn.commit()
   cur.close()
   ```

3. 再运行`zn-enPost.py`文件进行文章的爬取。

   ```python
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
   ```



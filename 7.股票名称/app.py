#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup

try:
	f = open("numList.txt")             # 返回一个文件对象
	nums = f.readlines()            # 调用文件的 readline()方法
	 
	for num in nums:
		num = num.strip()
		print num
		#url = 'https://gupiao.baidu.com/stock/sz' + num + '.html?from=aladingpc'  # 深市查询地址
		url = 'https://gupiao.baidu.com/stock/sh' + num + '.html'                  # 沪市查询地址
		response = urllib.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, "lxml")
		name = soup.select(".bets-name")[0].get_text().decode('gbk', 'ignore').encode('utf-8').strip()[:-8]
		print name
		with open("nameList.txt", 'a+') as s:
			s.write(name + '\n')
	
finally:
	if f:
		f.close()ai
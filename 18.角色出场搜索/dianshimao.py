#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = 'http://www.tvmao.com/drama/WVA0bQ==/episode/0-1'

response = urllib.request.urlopen(url, headers=header)
html = response.read()
soup = BeautifulSoup(html, "lxml")

#获取文章标题
#postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk', 'ignore').encode('utf-8')
#print '[第%d篇文章数据获取成功:]  %s' % (n, postTitle)
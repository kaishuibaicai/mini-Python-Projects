#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import time

headers = {'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
url = 'http://www.tvmao.com/drama/WVA0bQ==/episode/0-1'

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request).read
print (response)
soup = BeautifulSoup(response, "lxml")

#获取文章标题
#postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk', 'ignore').encode('utf-8')
#print '[第%d篇文章数据获取成功:]  %s' % (n, postTitle)
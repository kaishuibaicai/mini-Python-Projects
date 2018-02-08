#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import time

headers = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url = 'http://www.tvmao.com/drama/WVA0bQ==/episode/0-1'

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request).read
print (response)
soup = BeautifulSoup(response, "html")

#获取文章标题
#postTitle = soup.select("#nrtitle")[0].get_text().decode('gbk', 'ignore').encode('utf-8')
#print '[第%d篇文章数据获取成功:]  %s' % (n, postTitle)
#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup


word = urllib.parse.quote('钢之炼金术师FA')
#url = 'https://baike.baidu.com/item/' + word + urllib.parse.quote('#分集剧情')
url = 'https://baike.baidu.com/item/%E9%92%A2%E4%B9%8B%E7%82%BC%E9%87%91%E6%9C%AF%E5%B8%88%20FULLMETAL%20ALCHEMIST/4934836?fromtitle=%E9%92%A2%E4%B9%8B%E7%82%BC%E9%87%91%E6%9C%AF%E5%B8%88FA&fromid=3585525#分集剧情'

response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "lxml")


print (soup)
#-*- coding: utf-8 -*-
from collections import namedtuple

websites = [
	('Souhu', 'http://www.souhu.com/', u'张朝阳'),
	('Sina', 'http://www.sina.com.cn/', u'王志东'),
	('163', 'http://www.163.com/', u'丁磊')
	]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
	website = Website._make(website)
	print type(website)
	
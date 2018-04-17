import urllib.request
import requests
import re
import os

headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Host': 'p1.pstatp.com',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
saveImgPath = 'H:\\face\闭眼图片\\'

def getID(pageurl):
	f = urllib.request.urlopen(pageurl)
	result = f.read().decode('utf-8')
	#print (result)
	#print (type(result))
	rg = re.compile(r'imageId":"(\d+)')
	result = rg.findall(result)
	if result:
		for i in result:
			saveImg(i)

def saveImg(id):

	url = 'https://p1.pstatp.com/weili/l/' + id + '.webp'
	
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		filepath = saveImgPath + id + '.jpg'
		with open(filepath, 'wb')as f:
			f.write(response.content)
		print (id, 'Downloaded')
	else:
		print (id, '404')
	
	


if __name__ == '__main__':
	p = 1
	while 1:
		#pageurl = 'https://stock.tuchong.com/search?use=0&type=&layout=&sort=0&category=146%2C209%2C2016&page={0}&size=100&search_from=&exact=0&platform=weili&tp=&abtest=&royalty_free=0&option=&has_person=2&face_num=&gender=0&age=&racial=3'.format(str(p))
		pageurl = 'https://stock.tuchong.com/search?term=%E9%97%AD%E7%9C%BC&use=0&type=&layout=&sort=0&category=0&page={0}&size=100&search_from=head&exact=0&platform=weili&tp=&abtest=&royalty_free=0&option=&has_person=0&face_num=&gender=0&age=&racial='.format(str(p))
		print ('【page: %d】' % p)
		getID(pageurl)
		p += 1
		if p > 50:
			break
import urllib.request
import re

def getID(pageurl)
	f = urllib.request.urlopen(pageurl)
	result = f.read().decode('utf-8')
	print (result)
	print (type(result))
	rg = re.compile(r'imageId":"(\d+)')
	re = rg.findall(result)
	if re:
		for i in re:
			saveImg(i)

def saveImg(id):
	url = 'https//p1.pstatp.com/weili/ms/' + id + '.webp'
	response = requests.get(url)
	if response.status_code == 200:
		file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
		if not os.path.exists(file_path):
			with open(file_path, 'wb')as f:
			f.write(response.content)


'https://stock.tuchong.com/search?use=0&type=&layout=&sort=0&category=146%2C209%2C2016&page=1&size=100&search_from=&exact=0&platform=weili&tp=&abtest=&royalty_free=0&option=&has_person=2&face_num=&gender=0&age=&racial=3'
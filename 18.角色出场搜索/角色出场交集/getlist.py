#-- coding:utf-8 --

def getlist(url):
	f = open(url)
	L = []
	for line in f.readlines():
		if line is not '\n':
			print (line.lstrip()[:4])	#这里的.lstrip()是去除字符串开头的空格，.rstrip()是去除字符串末尾的空格



if __name__ == '__main__':
	getlist('C:\\Users\\Administrator\\Desktop\\mini-Python-Projects\\18.角色出场搜索\\角色出场交集\\2.txt')

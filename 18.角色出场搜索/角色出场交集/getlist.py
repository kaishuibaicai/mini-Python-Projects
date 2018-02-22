#-- coding:utf-8 --
import re


def getlist(url):
	f = open(url)
	L = []
	for line in f.readlines():
		if line is not '\n':
			line = line.lstrip().lstrip('0')[:4]	#这里的.lstrip()是去除字符串开头的空格，.rstrip()是去除字符串末尾的空格
			Line = re.findall(r"\d+",line)
			if Line:
				#print (Line[0])
				L.append(Line[0])
	return L


if __name__ == '__main__':
	getlist('C:\\Users\\Administrator\\Desktop\\mini-Python-Projects\\18.角色出场搜索\\角色出场交集\\3.txt')

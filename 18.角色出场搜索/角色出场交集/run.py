from getlist import *
import os

def getInter(url):
	I = []
	for file in os.listdir(url):
		L = getlist(url + '\\' + file)
		if I:
			I = [x for x in I if x in L]
		else:
			I = L

	return I

if __name__ == '__main__':
	url = 'C:\\Users\\Administrator\\Desktop\\mini-Python-Projects\\18.角色出场搜索\\角色出场交集\\files'
	print (getInter(url))
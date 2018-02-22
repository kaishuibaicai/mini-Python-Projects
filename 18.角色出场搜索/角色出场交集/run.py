from getlist import *


def getInter(url):
	I = []
	for file in os.listdir(url):
		L = getlist(url + '\\' + file)
		if I:
			I = []

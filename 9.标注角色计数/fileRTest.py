# coding:utf-8
import os
path = "C:\Users\Administrator\Desktop\huoying-zl"
dirs = os.listdir(path)


for Dir in dirs:
	if not os.path.isdir(Dir):
		print '[' + Dir + ']'
		files = os.listdir(path + '/' + Dir)
		#print (type(files))
		for file in files:
			print file
	#if not os.path.isdir(file):
	#	f = open(path + '/' + file)
# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\cosplay-筛选"
dirs = os.listdir(path)

for dir in dirs:
	print dir
	n = 1
	for file in os.listdir(path + '\\' + dir):
	    if file.endswith('.jpg'):
	    	newname = dir + '_Preprocessing_%08d_00.jpg' % n
	        os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + newname)
	        n = n + 1
	        print newname, 'Done'
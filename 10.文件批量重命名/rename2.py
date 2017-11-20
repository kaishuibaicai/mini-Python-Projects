# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\cosplayData\cosplay-all"
dirs = os.listdir(path)
n = 1
for dir in dirs:
	
	for file in os.listdir(path + '\\' + dir):
	    
	    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
	    newname = file[0:84] + '_%02d' % n + '_label_20171117_00_00' + '.xml'
	    os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + newname)
	    
	    print newname, 'Done'

	n = n + 1 
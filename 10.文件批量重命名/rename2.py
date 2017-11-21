# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\cosplay"
dirs = os.listdir(path)
n = 1
for dir in dirs:
	with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
				s.write(str(n) + "    " + dir + '\n')
	for file in os.listdir(path + '\\' + dir):
	    
	    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
	    #newname = file[0:84] + '_%02d' % n + '_label_20171117_00_00' + '.xml'
	    newname = '%02d_' % n +  file
	    os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + newname)
	    
	    print newname, 'Done'

	n = n + 1 
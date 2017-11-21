# -*- coding: utf-8 -*-
import os
import shutil

path = "C:\Users\Administrator\Desktop\missions\cosplay"
dirs = os.listdir(path)

for dir in dirs:
	#with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
	#			s.write(str(n) + "    " + dir + '\n')
	for file in os.listdir(path + '\\' + dir):
	    
	    if file.endswith('.jpg'):
		    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
		shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\rich_text\\" + file)
		print file, 'Done'
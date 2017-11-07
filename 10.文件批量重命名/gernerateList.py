# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\\new"
dirs = os.listdir(path)

for dir in dirs:
	print dir
	for file in os.listdir(path + '/' + dir):
		print file
	    if os.path.isfile(os.path.join(path,dir)):
	        if file.find('.mp4'):
	            with open("C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\\new\huoyingthename.txt", 'a+') as s:
					s.write(file + "    " + dir + '\n')
	            	print file,'ok'
# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\\new"
dirs = os.listdir(path)

for dir in dirs:
	print dir
	for file in os.listdir(path + '\\' + dir):
	    if file.endswith('.mp4'):
	    	print file
	        with open("C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\huoyingthename.txt", 'a+') as s:
				s.write(file + "    " + dir + '\n')
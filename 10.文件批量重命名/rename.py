# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\\new"
dirs = os.listdir(path)

for dir in dirs:
	for file in os.listdir(path + '\\' + dir):
	    if os.path.isfile(os.path.join(path,dir)):
	        if file.find('.')<0:
	            newname=file+'rsfdjndk.jpg'
	            os.rename(os.path.join(path,file),os.path.join(path,newname))
	            print file,'ok'
	#        print file.split('.')[-1] 



	with open("huoyingthename.txt", 'a+') as s:
			s.write(name + '\n')
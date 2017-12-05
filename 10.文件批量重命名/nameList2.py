# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\\testSet"
files = os.listdir(path)

for file in files:
	
	with open("C:\Users\Administrator\Desktop\\nameList.txt", 'a+') as s:
		s.write(file + '\t' + '\n')
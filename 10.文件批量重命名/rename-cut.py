# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\data\\20171027\\20171027\label_results"


for file in os.listdir(path):

	#newname = dir + '_Preprocessing_%08d_00.jpg' % n
	newname = file[0:94] + '.xml'
	print newname
	os.rename(path + '\\' + file, path + '\\' + newname)

	print newname, 'Done'
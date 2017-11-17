# -*- coding: utf-8 -*-
import os

ath = "C:\Users\Administrator\Desktop\data\\20171027\\20171027\label_results"
dirs = os.listdir(path)

for file in os.listdir(path):

	#newname = dir + '_Preprocessing_%08d_00.jpg' % n
	newname = [0:95]
	os.rename(path + '\\' + file, path + '\\' + newname)

	print newname, 'Done'
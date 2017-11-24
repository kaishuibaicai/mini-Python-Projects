# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\errors\cosplay_error_0"


for file in os.listdir(path):
	if file.endswith('.xml'):
	#newname = dir + '_Preprocessing_%08d_00.jpg' % n
		newname = file[0:87] + '.xml'
		print newname
		os.rename(path + '\\' + file, path + '\\' + newname)

		print newname, 'Done'
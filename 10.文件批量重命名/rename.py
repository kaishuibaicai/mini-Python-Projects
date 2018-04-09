# -*- coding: utf-8 -*-
import os

path = "C:\\Users\Administrator\Desktop\missions\哆啦A梦Preprocessing\新建文件夹"
dirs = os.listdir(path)

for dir in dirs:
	#print dir
	n = 1
	for file in os.listdir(path + '\\' + dir):
	    	#newname = dir + '_Preprocessing_%08d_00.jpg' % n
	    newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_%08d_00_Preprocessing_20171116_00.jpg' % n
	    os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + 'cartoon_characterdetectionai' + file[25:])
	    n = n + 1
	    print (file, 'Done')
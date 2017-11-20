# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\cosplay\yueqianlongma\\new"

n = 124

	
for file in os.listdir(path):
	    
	    
	newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % n + '_00_Preprocessing_20171116_00.jpg'
	os.rename(path + '\\' + file, path  + '\\' + newname)
	    
	print newname, 'Done'

	n = n + 1
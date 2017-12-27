# -*- coding: utf-8 -*-
import os

path = "C:\\Users\Administrator\Desktop\missions\\toy\\toy\SuoLong\新建文件夹"

n = 723

	
for file in os.listdir(path):
	    
	if file.endswith('.xml'):    
		#newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % n + '_00_Preprocessing_20171116_00.jpg'
		newname = 'cartoon_toyCharacterAI_Origin_Image_20171225_%08d_00_Preprocessing_20171225_00.jpg' % n
		os.rename(path + '\\' + file, path  + '\\' + newname)
		    
		print (newname, 'Done')

		n = n + 1
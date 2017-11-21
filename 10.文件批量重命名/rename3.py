# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\cosplay\moshukuaidou"

n = 132

	
for file in os.listdir(path):
	    
	if file.endswith('.xml'):    
		newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % n + '_00_Preprocessing_20171116_00.xml'
		os.rename(path + '\\' + file, path  + '\\' + newname)
		    
		print newname, 'Done'

		n = n + 1
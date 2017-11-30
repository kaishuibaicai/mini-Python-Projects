# -*- coding: utf-8 -*-
import os

path = "E:\juren-buchong\cartoon_characterDetectionAI_Origin_Video_20171122_00000017_00"

n = 1

	
for file in os.listdir(path):
	    
	if file.endswith('.jpg'):    
		#newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % n + '_00_Preprocessing_20171116_00.jpg'
		newname = file[0:83] + '22' + file[85:]
		os.rename(path + '\\' + file, path  + '\\' + newname)
		    
		print newname, 'Done'

		n = n + 1
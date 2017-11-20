# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\cosplayData\cosplay\moshukuaidou"

index = 123

for file in os.listdir(path):
	if file.endswith('.xml'):
	#newname = dir + '_Preprocessing_%08d_00.jpg' % n
		newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % index + '_00_Preprocessing_20171116_00.jpg' 
		#newname = file[0:94] + '_label_20171024_00_00' + '.xml'
		print newname
		os.rename(path + '\\' + file, path + '\\' + newname)
		index += 1
		print newname, 'Done'
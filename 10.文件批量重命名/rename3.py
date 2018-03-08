# -*- coding: utf-8 -*-
import os

path = "C:\\Users\\Administrator\\Desktop\\label\\new\\fzynt-海澄天\海澄天"

n = 1

	
for file in os.listdir(path):
	    
	#if file.endswith('.xml'):    
		#newname = 'mgdm_relevantCharacterAI_Origin_Image_20171116_' + '%08d' % n + '_00_Preprocessing_20171116_00.jpg'
	newname = 'haichengtian_%d.png' % n
	os.rename(path + '\\' + file, path  + '\\' + newname)

	print (newname, 'Done')

	n = n + 1
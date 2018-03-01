# -*- coding: utf-8 -*-
import os
import shutil

path = 'H:\死神\\task\\'
#pathR = "C:\\Users\Administrator\Desktop\missions\哆啦A梦Preprocessing\新建文件夹\mgdm_characterDetectionAI_Origin_Video_20171108_00000013_00"
#pathL = "C:\\Users\Administrator\Desktop\missions\哆啦A梦Preprocessing\新建文件夹\mgdm_characterDetectionAI_Origin_Video_20171108_00000013_00"
for dir in os.listdir(path):
	L = []
	
	for file in os.listdir(path + dir):
		if file.endswith('xml'):
			L.append(file[:-3])

	
	for file in os.listdir(path + dir):
		if file.endswith('jpg') and file[:-3] not in L:
			print ("hey:")
			#shutil.copyfile(pathR + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\notL\\" + file)	
			os.remove(path + dir + '\\' + file)
			print (file, '	deleted')
#print L
# for dir in dirs:
# 	#with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
# 	#			s.write(str(n) + "    " + dir + '\n')
# 	for file in os.listdir(path + '\\' + dir):
	    
# 	    if file.endswith('.jpg'):
# 		    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
# 		shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\rich_text\\" + file)
# 		print file, 'Done'
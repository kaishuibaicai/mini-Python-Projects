# -*- coding: utf-8 -*-
import os
import shutil
L = []

pathR = "C:\Users\Administrator\Desktop\missions\jinjidejuren\cartoon_characterDetectionAI_Origin_Video_20171122_00000009_00"
pathL = "C:\Users\Administrator\Desktop\missions\jinjidejuren\cartoon_characterDetectionAI_Origin_Video_20171122_00000009_00"

filesL = os.listdir(pathL)
for file in filesL:
	if file.endswith('xml'):
		L.append(file[0:97])

filesR = os.listdir(pathR)
for file in filesR:
	if file.endswith('jpg') and file[0:97] not in L:
		print "hey:"
		#shutil.copyfile(pathR + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\notL\\" + file)	
		os.remove(pathR + '\\' + file)
		print file, '	deleted'
#print L
# for dir in dirs:
# 	#with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
# 	#			s.write(str(n) + "    " + dir + '\n')
# 	for file in os.listdir(path + '\\' + dir):
	    
# 	    if file.endswith('.jpg'):
# 		    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
# 		shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\rich_text\\" + file)
# 		print file, 'Done'
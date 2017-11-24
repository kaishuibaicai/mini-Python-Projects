# -*- coding: utf-8 -*-
import os
import shutil
L = []
R = []
pathR = "C:\Users\Administrator\Desktop\cosplay1112\luotianyi"
pathL = "C:\Users\Administrator\Desktop\cosplay1112\luotianyi"

filesL = os.listdir(pathL)
for file in filesL:
	L.append(file[0:87])  
print L
filesR = os.listdir(pathR)
for file in filesR:
	R.append(file[0:87])


print len(L)
print len(R)
	# if file[0:87] not in L:
	# 	print "hey:"
	# 	#shutil.copyfile(pathR + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\notL\\" + file)	
	# 	os.remove(pathR + '\\' + file)
	# 	print file
#print L
# for dir in dirs:
# 	#with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
# 	#			s.write(str(n) + "    " + dir + '\n')
# 	for file in os.listdir(path + '\\' + dir):
	    
# 	    if file.endswith('.jpg'):
# 		    #newname = dir + '_Preprocessing_%08d_00.jpg' % n
# 		shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\cosData\\rich_text\\" + file)
# 		print file, 'Done'
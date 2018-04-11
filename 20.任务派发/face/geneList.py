import os


path = 'H:\\标注管理\images\\0324\\pictures'
fileList = open('H:\标注管理\\images\\0324\\all.txt', 'a+')
for i in os.listdir(path):
	fileList.write(i + '\n')
	#for f in os.listdir(os.path.join(path, i)):
		#fileList.write(f + '\n')

fileList.close()

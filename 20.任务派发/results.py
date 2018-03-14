import os, shutil


pathp = 'H:\标注管理\\images\\0312\\pictures'
pathl = 'H:\标注管理\\images\\0312\\xml'
pathr = 'H:\标注管理\\images\\0312\\results'

p = []
l = []

for i in os.listdir(pathp):
	p.append(i[0:23])

for i in os.listdir(pathl):
	if i[0:23] in p:
		shutil.copyfile(pathl + '\\' + i, pathr + '\\' + i) 
		shutil.copyfile(pathp + '\\' + i[0:23] + '.jpg', pathr + '\\' + i[0:23] + '.jpg')
		print (i, 'done')



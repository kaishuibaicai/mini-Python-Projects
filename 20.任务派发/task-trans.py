import os, shutil


pathp = 'H:\标注管理\\images\\0321\\pictures'
pathl = 'H:\标注管理\\images\\0321\\points'
pathr = 'H:\标注管理\\images\\0321\\results'
pathb = 'H:\标注管理\\images\\0321\\boxes'


task_done = open('H:\标注管理\\images\\0321\\task_done.txt','r', encoding='UTF-8')

'''
for i in task_done.readline():
	if i:
		shutil.copyfile(pathl + '\\' + i + '_keypoint.xml', pathr + '\\' + i + '_keypoint.xml') 
		shutil.copyfile(pathp + '\\' + i + '.jpg', pathr + '\\' + i + '.jpg')
		shutil.copyfile(pathb + '\\' + i + '_bndbox.xml', pathr + '\\' + i + '_bndbox.xml')
'''

while 1:
	i = task_done.readline()[21:44]
	if not i:
		break
	if os.path.exists(pathl + '\\' + i + '_keypoint.xml'):
		shutil.copyfile(pathl + '\\' + i + '_keypoint.xml', pathr + '\\' + i + '_keypoint.xml') 
		shutil.copyfile(pathp + '\\' + i + '.jpg', pathr + '\\' + i + '.jpg')
		shutil.copyfile(pathb + '\\' + i + '_bndbox.xml', pathr + '\\' + i + '_bndbox.xml')
		print (i, 'done')
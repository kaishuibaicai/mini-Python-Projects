import os, shutil


pathp = 'H:\标注管理\\images\\0315\\pictures'
pathl = 'H:\标注管理\\images\\0315\\points2'
pathr = 'H:\标注管理\\images\\0315\\results2'
pathb = 'H:\标注管理\\images\\0315\\boxes2'


task_done = open('H:\标注管理\\images\\0315\\task-done.txt','r', encoding='UTF-8')

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
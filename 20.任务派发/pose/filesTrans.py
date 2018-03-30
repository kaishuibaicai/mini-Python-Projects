import os, shutil

basePath = 'H:\标注管理\\images\\0327舞蹈动作\图片收集'
picPath = 'H:\标注管理\\images\\0327舞蹈动作\pictures'

c = 1
for people in os.listdir(basePath):
	peopleList = os.listdir(os.path.join(basePath, people))
	for dirs in peopleList:
		if dirs:
			picList = os.listdir(os.path.join(basePath, people, dirs))
			for file in picList:
				newname = 'pose_20180330_' + people[0:2] + '%06d.jpg' % c
				shutil.copyfile(os.path.join(basePath, people, dirs, file), os.path.join(picPath, newname))
				print (newname, 'Done')
				c += 1

import os

basePath = 'H:\标注管理\\images\\0327舞蹈动作\图片收集'
picPath = 'H:\标注管理\\images\\0327舞蹈动作\pictures'


for people in os.listdir(basePath):
	peopleList = os.listdir(os.path.join(basePath, people))
	for dirs in peopleList:
		if dirs:
			picList = os.listdir(os.path.join(peopleList, dirs))
			for file in picList:
				print (file)

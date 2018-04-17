import os, shutil
baseP = 'H:\标注管理\\images\\0411舞蹈动作'
basePath = os.path.join(baseP, '图片收集2')
picPath = os.path.join(baseP, 'pictures2')
taskLPath = os.path.join(baseP, 'taskList2\\')

c = 614
for people in os.listdir(basePath):
	peopleList = os.listdir(os.path.join(basePath, people))

	taskFile = taskLPath + people[0:2] + '.txt'
	if os.path.exists(taskFile):
		os.remove(taskFile)
	tf = open(taskFile, 'a+')
	tf.write('task_20180411_' + people[0:2] + '\n')
	tf.write('[')
	for dirs in peopleList:

		
		picList = os.listdir(os.path.join(basePath, people, dirs))
		for file in picList:
			newname = 'pose_20180411_' + people[0:2] + '%06d.jpg' % c
			shutil.copyfile(os.path.join(basePath, people, dirs, file), os.path.join(picPath, newname))
			tf.write('"static/img/20180411/%s",\n' % newname)
			print (newname, 'Done')
			c += 1
	
					
	tf.close()

	with open(taskFile) as tf:
		rl = tf.readlines()
		lastline = rl[len(rl)-1].replace(',\n', ']')
		
		rl = rl[:-1]#.append(lastline)
		rl.append(lastline)
	
	with open(taskFile, 'w') as tf:
		tf.writelines(rl)
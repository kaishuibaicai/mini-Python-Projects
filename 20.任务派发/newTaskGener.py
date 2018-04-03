import os, random, shutil

picPath = 'H:\标注管理\\images\\0403\\images'
tpicPath = 'H:\标注管理\\images\\0403\\img'
taskPath = 'H:\标注管理\\images\\0403\\tasklist'


def rename(path, tpath):
	files = os.listdir(path)
	random.shuffle(files)
	n = 1
	for i in files:
		oldp = os.path.join(path, i)
		newname= 'comic_20180403_%08d.jpg' % n 
		newp = os.path.join(tpath, newname)
		shutil.copyfile(oldp, newp)
		print(newname, '[name changed]')
		n += 1


def geneTList(per_count, prelatters, taskname, tPath, tlPath):
	files = os.listdir(tPath)
	n = 1
	for i in range(len(files)):
		if (i+1) % per_count == 1:
			taskFile = taskname + '%02d' % n + '.txt'
			taskFileP = os.path.join(tlPath, taskFile)
			if os.path.exists(taskFileP):
				os.remove(taskFileP)
			tf = open(taskFileP, 'a+')
			tf.write(taskFile[0:16] + '[' + prelatters + files[i]+ '",\n')
		elif (i+1) % per_count == 0:
			tf.write(prelatters + files[i]+ '"]')
			tf.close()
			n += 1
		else:
			tf.write(prelatters + files[i]+ '",\n')

if __name__ == '__main__':
	#rename(picPath, tpicPath)
	geneTList(187, '"static/img/20180403/', 'task_20180403_', tpicPath, taskPath)
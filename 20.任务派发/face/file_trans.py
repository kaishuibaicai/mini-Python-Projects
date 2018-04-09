import os, shutil, random


picPath = 'H:\\face\\draw\\1'
taskPath = 'H:\\face\\draw\\task_files'


files =  os.listdir(picPath)
random.shuffle(files)

n = 0
for i in range(len(files) + 1):
	if (i + 1) % 500 == 1:
		n += 1
		N = '%02d' % n
		taskDir = os.path.join(taskPath, N)
		if os.path.exists(taskDir):
			os.remove(taskDir)
		os.mkdir(taskDir)
		print ('\n\n\n【{0}文件夹创建完成】\n\n'.format(taskDir))
	shutil.copyfile(os.path.join(picPath, files[i]), os.path.join(taskDir, files[i]))
	print ('{0} 文件已复制'.format(files[i]), i)
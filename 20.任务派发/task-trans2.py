import os, shutil, re

resName = '4-results'
pathpic = '/home/taguser/opt/dongman/static/images/20180307'
pathpio = '/home/taguser/opt/dongman/static/images/xml/points'
pathbox = '/home/taguser/opt/dongman/static/images/xml/bndbox'
pathres = '/home/taguser/opt/dongman/static/images/标注数据/' + resName
taskLP = '/home/taguser/opt/dongman/static/images/dataTrans/4-tasklist'

task_done = ['all.txt']

def task_trans(taskfile):
	task_done = open(os.path.join(taskLP, taskfile),'r', encoding='UTF-8')
	print ('【{0}任务列表打开完成】'.format(taskfile))

	while 1:
		i = task_done.readline()
		if not i:
			break
		rg = re.compile('(comic_\\d+_\\d+)',re.IGNORECASE|re.DOTALL)
		m = rg.search(i)
		if m:
			file = m.group()
			if os.path.exists(pathpio + '/' + file + '_keypoint.xml'):
				shutil.copyfile(pathpio + '/' + file + '_keypoint.xml', pathres + '/' + file + '_keypoint.xml') 
				shutil.copyfile(pathpic + '/' + file + '.jpg', pathres + '/' + file + '.jpg')
				shutil.copyfile(pathbox + '/' + file + '_bndbox.xml', pathres + '/' + file + '_bndbox.xml')
				print (file, 'done')
	task_done.close()

if __name__ == '__main__':
	if os.path.exists(pathres):
		shutil.rmtree(pathres)
		os.mkdir(pathres)
	else:
		os.mkdir(pathres)
	for i in task_done:
		task_trans(i)
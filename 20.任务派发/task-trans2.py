import os, shutil, re

resName = '1-pose_results'
pathpic = '/home/taguser/opt/dongman/static/images/20180330'
pathpio = '/home/taguser/opt/dongman/static/images/xml/points'
pathbox = '/home/taguser/opt/dongman/static/images/xml/bndbox'
pathres = '/home/taguser/opt/dongman/static/images/标注数据/' + resName
taskLP = '/home/taguser/opt/dongman/static/images/dataTrans/1_post_task_list'

task_done = ['01.txt',
			 '02.txt',
			 '03.txt',
			 '04.txt',
			 '06.txt',
			 '07.txt',
			 '09.txt',
			 '10.txt',
			 '12.txt',
			 '13.txt',
			 '14.txt',
			 '15.txt',
			 '16.txt',
			 '17.txt',
			 '18.txt',
			 '19.txt',
			 '23.txt']

def task_trans(taskfile):
	task_done = open(os.path.join(taskLP, taskfile),'r', encoding='UTF-8')


	while 1:
		i = task_done.readline()
		if not i:
			break
		rg = re.compile('(pose_\\d+_\\d+)',re.IGNORECASE|re.DOTALL)
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
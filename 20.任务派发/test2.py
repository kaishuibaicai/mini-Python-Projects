import os
n = 1
path = 'H:\标注管理\images\\0312'
files = os.listdir(path)
for i in range(len(files)):
	if (i+1) % 20 == 1:
		print ('task_20180312_%02d' % n )
		n += 1
	

#with open("H:\标注管理\\files.txt", 'a+') as s:
#	s.write(files)
import os
c = 1



path = 'H:\新建文件夹\\duitang\\duitang'
for i in os.listdir(path):
	if not i.endswith('.jpg'):
		n = '%d.jpg' % c
		old = os.path.join(path, i)
		new = os.path.join(path, n)
		os.rename(old, new)
		print (i)
		c += 1
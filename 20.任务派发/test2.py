import os
n = 1
path = 'H:\标注管理\images\\0321\\pictures'
files = os.listdir(path)
for i in range(len(files)):
	if (i+1) % 20 == 1:
		print ('task_20180324_%02d' % n )
		n += 1
	
email = ['2923204011@qq.com',
	'1019128103@qq.com',
	'13015887627@163.com',
	'919945711@qq.com',
	'764115114@qq.com',
	'1228443483@qq.com',
	'1345416620@qq.com',
	'823217134@qq.com',
	'1246118853@qq.com',
	'1714961499@qq.com',
	'510308730@qq.com',
	'sqalaska@163.com',
	'245121965@qq.com',
	'diyidaqiao@163.com',
	'1273202335@qq.com',
	'962379394@qq.com',
	'601854062@qq.com',
	'1738846461@qq.com',
	'137456786@qq.com',
	'1533520601@qq.com',
	'1287747557@qq.com',
	'1071787994@qq.com',
	'1729011181@qq.com']
ee = ''
for e in email:
	ee += e + ';'
print (ee)

#with open("H:\标注管理\\files.txt", 'a+') as s:
#	s.write(files)
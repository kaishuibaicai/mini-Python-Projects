import os
n = 1
path = 'H:\标注管理\images\\0312'
files = os.listdir(path)
for i in range(len(files)):
	if (i+1) % 20 == 1:
		print ('\n\ntask_20180312_%02d\n\n["static/img/20180312/' % n + files[i]+ '",')
		n += 1
	elif (i+1) % 20 == 0:
		print ('"static/img/20180312/' + files[i]+ '"]\n\nhttp://112.5.162.246:180')
	else:
		print ('"static/img/20180312/' + files[i]+ '",')

#with open("H:\标注管理\\files.txt", 'a+') as s:
#	s.write(files)
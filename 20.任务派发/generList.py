import os
n = 5
path = 'H:\标注管理\images\\0315\\qs'
files = os.listdir(path)
for i in range(len(files)):
	if (i+1) % 100 == 1:
		print ('\n\ntask_20180315_%02d\n\n["static/img/20180312/' % n + files[i]+ '",')
		n += 1
	elif (i+1) % 100 == 0:
		print ('"static/img/20180312/' + files[i]+ '"]')
	else:
		print ('"static/img/20180312/' + files[i]+ '",')

#with open("H:\标注管理\\files.txt", 'a+') as s:
#	s.write(files)
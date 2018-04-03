import os, random
n = 1
path = 'H:\标注管理\\images\\0324\pictures'
files = os.listdir(path)
#random.shuffle(files) 
for i in range(len(files)):
	if (i+1) % 60 == 1:
		print ('\n\ntask_20180324_%02d\n\n["static/img/20180307/' % n + files[i]+ '",')
		n += 1
	elif (i+1) % 60 == 0:
		print ('"static/img/20180307/' + files[i]+ '"]')
	else:
		print ('"static/img/20180307/' + files[i]+ '",')

#with open("H:\标注管理\\files.txt", 'a+') as s:
#	s.write(files)
import os
path = 'C:\Users\Administrator\Desktop\火影全部的标注结果-zl'
files = os.listdir(path)
s = []

for file in files:
	print (file)
	#if not os.path.isdir(file):
	#	f = open(path + '/' + file)
		
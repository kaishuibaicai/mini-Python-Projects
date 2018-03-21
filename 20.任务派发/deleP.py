import os, random, shutil
from PIL import Image

n = 1
path = 'H:\标注管理\images\\0321\\pictures\\'
dpath = 'H:\标注管理\images\\0321\p\\'
files = os.listdir(path)

for i in files:
	img = Image.open(path + i)
	width, height = img.size
	if width * height > 160000:
		print (width, height, n, i)
		shutil.copy(path + i, dpath + i )
		n += 1
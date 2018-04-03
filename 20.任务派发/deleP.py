import os, random, shutil
from PIL import Image

n = 1
path = 'H:\新建文件夹\\duitang\\duitang\\'
dpath = 'H:\新建文件夹\\duitang\\duitangImages\\'
files = os.listdir(path)

for i in files:
	img = Image.open(path + i)
	width, height = img.size
	if width * height > 90000:
		print (width, height, n, i)
		shutil.copy(path + i, dpath + i )
		#os.remove(path + i)
		n += 1
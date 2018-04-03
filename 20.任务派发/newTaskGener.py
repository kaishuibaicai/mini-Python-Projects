import os, random, shutil

picPath = 'H:\标注管理\\images\\0403\\images'
tpicPath = 'H:\标注管理\\images\\0403\\img'
taskPath = ''


def rename(path, tpath):
	files = os.listdir(path)
	random.shuffle(files)
	n = 1
	for i in files:
		oldp = os.path.join(path, i)
		newname= 'comic_20180403_%08d.jpg' % n 
		newp = os.path.join(tpath, newname)
		shutil.copyfile(oldp, newp)
		print(newname, '[name changed]')
		n += 1


if __name__ == '__main__':
	rename(picPath, tpicPath)
import os, hashlib
c = 1


with open('C:\\Users\\Administrator\\Desktop\\mini-Python-Projects\\16.图片去重\\new\\output_file.txt') as of:
		doneList = of.readlines()
		

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

path = 'H:\新建文件夹\\duitang\\duitang'
for i in os.listdir(path):
	#print (i)
	file = os.path.join(path, i)
	md = GetFileMd5(file) + '\n'
	if md in doneList:
		os.remove(file)
		print (md)
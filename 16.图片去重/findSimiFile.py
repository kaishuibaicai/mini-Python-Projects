#-*-coding:utf-8-*-
from PIL import Image
import imagehash
import difflib
import os,shutil

pathF = 'E:\The Second\\new\cartoon_characterdetectionai_Origin_Video_20171129_00000628_00\\'
path = 'E:\叛逆的鲁鲁修\米蕾\cartoon_characterdetectionai_Origin_Video_20171129_00000628_00\\'
simiCtrl = 0.65  # 相似度阈值控制
simS = []
def ImageHash(path):
	image = Image.open(path)
	h = str(imagehash.dhash(image))
	return h

for file in os.listdir(pathF):
	if file.endswith('.jpg'):
		simS.append(ImageHash(pathF + file))

for file in os.listdir(path):
	h2 = ImageHash(path + file)
	for sims in simS:
		simiValue = difflib.SequenceMatcher(None, sims, h2).ratio()
		if simiValue >= simiCtrl:
			shutil.move(path + file, pathF + file)
			print ('{}  [Moved]'.format(file))
			break
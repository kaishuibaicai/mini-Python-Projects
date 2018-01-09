#-*-coding:utf-8-*-
from PIL import Image
import imagehash
import difflib
import os

path = 'C:\\Users\Administrator\Desktop\missions\哆啦A梦Preprocessing\新建文件夹2\\'
simiCtrl = 0.65  # 相似度阈值控制

def ImageHash(path):
	image = Image.open(path)
	h = str(imagehash.dhash(image)) 
	return h


for dir in os.listdir(path):
	h = ''
	for image in os.listdir(path + dir):
		h2 = ImageHash(path + dir + '\\' + image)
		simiValue = difflib.SequenceMatcher(None, h, h2).ratio()
		if simiValue >= simiCtrl:
			os.remove(path + dir + '\\' + image)
			print ('{}  [deleted]'.format(image))	
		h = h2

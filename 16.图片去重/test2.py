from PIL import Image
import imagehash
import difflib
import os, shutil

path = 'C:\Users\Administrator\Desktop\\testImageSet\\teest\\'


def ImageHash(path):
	image = Image.open(path)
	h = str(imagehash.dhash(image))
	return h


# seq = difflib.SequenceMatcher(None, h, h2)
# print seq.ratio()

images = os.listdir(path)
h = ''
for image in images:
	h2 = ImageHash(path + image)
	print h2
	simiValue = difflib.SequenceMatcher(None, h, h2).ratio()
	print simiValue
		
	h = h2

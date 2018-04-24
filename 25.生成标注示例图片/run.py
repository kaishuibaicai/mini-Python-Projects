
from xml.etree.ElementTree import parse
from PIL import Image, ImageDraw, ImageFont
import os

font = ImageFont.truetype('simsun.ttc',24)
filepath = 'H:\标注管理\\images\标注方法介绍\\5\\panni'
savepPath = 'H:\标注管理\\images\标注方法介绍\\5\\示例图片'

for i in os.listdir(filepath):
	if i.endswith('xml'):
		im = Image.open(os.path.join(filepath, i[:-3] + 'jpg'))
		draw = ImageDraw.Draw(im)
		xml_tree = parse(os.path.join(filepath, i))
		root = xml_tree.getroot()
		for label in root.findall('object'):
			label_name = label.find('name').text
			print (label_name)
			p = []
			for n in label.find('bndbox'):
				p.append(int(n.text))

			xmin, ymin, xmax, ymax = p
			print (xmin, ymin, xmax, ymax)

			draw.rectangle((xmin, ymin, xmax, ymax), outline='red')
			#draw.text([xmax, ymax], label_name.encode('utf-8'), font=font)
		im.save(os.path.join(savepPath, i[:-3] + 'jpg'))
			 
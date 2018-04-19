from xml.etree.ElementTree import parse

filepath = 'test.xml'


xml_tree = parse(filepath)
root = xml_tree.getroot()
for label in root.findall('object'):
	label_name = label.find('name').text
	print (label_name)
	for n in label.find('bndbox'):
		print (int(n.text))



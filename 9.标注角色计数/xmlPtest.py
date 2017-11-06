# coding:utf-8
import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='C:/Users/Administrator/Desktop/huoying-zl/mgdm_characterDetectionAI_Origin_Video_20171019_00000053/mgdm_characterDetectionAI_Origin_Video_20171019_00000053_Preprocessing_00000917_00.xml')
# root = tree.getroot()
# print root.tag
# print root.attrib
for elem in tree.iter(tag='name'):
	print elem.tag, elem.attrib
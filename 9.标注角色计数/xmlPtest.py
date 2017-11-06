#-- coding:utf-8 --
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib

nameSets = []
response = urllib.urlopen('file:///C:/Users/Administrator/Desktop/huoying-zl/mgdm_characterDetectionAI_Origin_Video_20171019_00000053/mgdm_characterDetectionAI_Origin_Video_20171019_00000053_Preprocessing_00000917_00.xml')
html = response.read()
soup = BeautifulSoup(html, "xml")
names = soup.select("name")

name_counts = {}

for name in names:
	nameSets.append(name.get_text())
print nameSets

for n in nameSets:
    if name_counts.has_key(n):
        name_counts[n] = name_counts[n] + 1
    else:
        name_counts[n] = 1
for item in name_counts:
	print item, name_counts[item]
# tree = ET.ElementTree(file='C:/Users/Administrator/Desktop/huoying-zl/mgdm_characterDetectionAI_Origin_Video_20171019_00000053/mgdm_characterDetectionAI_Origin_Video_20171019_00000053_Preprocessing_00000917_00.xml')
# # root = tree.getroot()
# # print root.tag
# # print root.attrib
# for elem in tree.iter(tag='name'):
# 	print elem.tag, elem.attrib
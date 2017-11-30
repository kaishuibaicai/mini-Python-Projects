# coding:utf-8
import os
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib

path = "C:\Users\Administrator\Desktop\missions\jinjidejuren"
dirs = os.listdir(path)
nameSets = []
name_counts = {}

for Dir in dirs:
	if not os.path.isdir(Dir):
		files = os.listdir(path + '/' + Dir)
		for file in files:
			if file.endswith(".xml"):
				Path = 'file:///' + path + '/' + Dir + '/' + file
				print Path
				response = urllib.urlopen(Path)
				html = response.read()
				soup = BeautifulSoup(html, "xml")
				names = soup.select("name")

				for name in names:
					if name.get_text().endswith('-head'):
						nameSets.append(name.get_text())
						print 'Done'

for n in nameSets:
    if name_counts.has_key(n):
        name_counts[n] = name_counts[n] + 1
    else:
        name_counts[n] = 1
for item in name_counts:
	print item[:-5], name_counts[item]
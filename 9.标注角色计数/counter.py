# coding:utf-8
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib

path = "C:\Users\Administrator\Desktop\huoying-zl"
dirs = os.listdir(path)
name_counts = {}

for Dir in dirs:
	if not os.path.isdir(Dir):
		files = os.listdir(path + '/' + Dir)
		for file in files:
			Path = 'file://' + path + '/' + Dir + '/' + file
			response = urllib.urlopen('file:///C:/Users/Administrator/Desktop/huoying-zl/mgdm_characterDetectionAI_Origin_Video_20171019_00000053/mgdm_characterDetectionAI_Origin_Video_20171019_00000053_Preprocessing_00000917_00.xml')
html = response.read()
soup = BeautifulSoup(html, "xml")
names = soup.select("name")
# coding:utf-8
import os
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib

path = "C:\Users\Administrator\Desktop\missions\jinjidejuren"
dirs = os.listdir(path)
nameSets = []
name_counts = {}
errorFile = []

for Dir in dirs:
    if not os.path.isdir(Dir):
        files = os.listdir(path + '/' + Dir)
        for file in files:
            if file.endswith(".xml"):
                Path = 'file:///' + path + '/' + Dir + '/' + file
                #print Path
                response = urllib.urlopen(Path)
                html = response.read()
                soup = BeautifulSoup(html, "xml")
                names = soup.select("name")

                for name in names:
                    if name.get_text().startswith('让'):
                        print "Hey!"
                    elif name.get_text().startswith('艾伦'):
                        print "Hey!"
                    elif name.get_text().startswith('利威尔'):
                        print "Hey!"
                    elif name.get_text().startswith('三笠'):
                        print "Hey!"
                    elif name.get_text().startswith('阿明'):
                        print "Hey!"

                    else:
                        errorFile.append(file)

print errorFile
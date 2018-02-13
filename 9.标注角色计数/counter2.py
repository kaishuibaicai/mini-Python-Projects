# -*- coding:utf-8 -*-
'''
标注文件校验
'''
import xml.etree.ElementTree as ET
import fnmatch
import string
from PIL import Image
import os
import sys
import shutil

# 获取标注的角色名称list
def extract_character_name_list(xml_file):
    xml_tree = ET.parse(xml_file)
    root = xml_tree.getroot()
    name_list = list()
    for label in root.findall('object'):
        label_name = label.find('name').text
        name_list.append(label_name)
    return name_list


if __name__ == "__main__": 
    path = 'H:\家庭教师\\task'

    name_dict = dict()
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        for file in os.listdir(folder_path):
            if not 'xml' in file:
                continue
            file_path = os.path.join(folder_path, file)
            name_list = extract_character_name_list(file_path)
            for name in name_list:
                if not name in name_dict:
                    name_dict[name] = 0
                name_dict[name] += 1
    for name, count in name_dict.items():
        #if name.endswith('-head'):
        print('%s\t%d' % (name, count))

    print ('2018,相信未来！')
# -*- coding: utf-8 -*-
import os

path = "E:\juren-buchong"
dirs = os.listdir(path)

for dir in dirs:
    n = 1
    #with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
    #			s.write(str(n) + "    " + dir + '\n')
    for file in os.listdir(path + '\\' + dir):

        if file.endswith('.jpg'):
            newname = dir + '_Preprocessing_20171122_%08d_00.jpg' % n
            #newname = file[0:87]  + '_label_20171117_00_00' + '.xml'
            #newname = '%02d_' % n +  file

            os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + newname)


        n = n + 1
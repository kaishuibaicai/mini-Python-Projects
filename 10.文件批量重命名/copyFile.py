# -*- coding: utf-8 -*-
import os
import shutil

path = "C:\Users\Administrator\Desktop\linxi"
dirs = os.listdir(path)

for dir in dirs:
    #with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
    #			s.write(str(n) + "    " + dir + '\n')
    for file in os.listdir(path + '\\' + dir):

        if file.endswith('.jpg'):
            #newname = dir + '_Preprocessing_%08d_00.jpg' % n
            shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\\linxiData\\rich_text\\" + file)
            print file, 'Done'
        elif file.endswith('.xml'):
            newname = file[0:97] + '_label_20171127_00_00' + '.xml'
            #os.rename(path + '\\' + dir + '\\' + file, path + '\\' + dir + '\\' + newname)
            shutil.copyfile(path + '\\' + dir + '\\' + file,"C:\Users\Administrator\Desktop\\linxiData\\label_results\\" + newname)
            print file, 'Done'
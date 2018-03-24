# -*- coding: utf-8 -*-
import os, shutil

path = "H:\新建文件夹\\acg"
tpath = "H:\新建文件夹\\ACGimages"
dirs = os.listdir(path)

c = 730
for dir in dirs:
    
    
    #with open("C:\Users\Administrator\Desktop\DirList.txt", 'a+') as s:
    #			s.write(str(n) + "    " + dir + '\n')

    folder_path = os.path.join(path, dir)
    if os.path.isdir(path + '\\' + dir) and os.listdir(path + '\\' + dir):
        
        for file in os.listdir(path + '\\' + dir):

            #if file.endswith('.jpg'):
            newname = 'comic_20180307_%08d.jpg' % c
            #newname = file[0:87]  + '_label_20171117_00_00' + '.xml'
            #newname = '%02d_' % n +  file

            old_name_path = os.path.join(folder_path, file)
            new_name_path = os.path.join(tpath, newname)
            #os.rename(old_name_path, new_name_path)
            shutil.copyfile(old_name_path, new_name_path)

            print (dir, file, newname + '  Done')
            with open(path + "\\nameList.txt", 'a+') as s:
                s.write(newname + '\t' + dir + '\n')
            c += 1

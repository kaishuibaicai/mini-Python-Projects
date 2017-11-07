# -*- coding: utf-8 -*-
import os

path = "C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\\new"
dirs = os.listdir(path)

path = 'D:\\图片\\'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
            newname=file+'rsfdjndk.jpg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
#        print file.split('.')[-1] 
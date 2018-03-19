'''
"static/img/20180312/comic_20180312_00000623.jpg",

comic_20180308_00000003_bndbox.xml

comic_20180308_00000004.jpg

comic_20180308_00000015_keypoint.xml
'''

print (len('"static/img/20180312/comic_20180312_00000623'))
print ('"static/img/20180312/comic_20180312_00000623.jpg",'[21:44])

task_done = open('H:\标注管理\\images\\0315\\task-done.txt','r', encoding='UTF-8')

while 1:
    i = task_done.readline()[21:44]
    if not i:
        break
    print (i)
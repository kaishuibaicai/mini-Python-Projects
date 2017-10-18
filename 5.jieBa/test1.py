#encoding=utf-8
import jieba
import time
seg_list = jieba.cut('他来到了厦门软件园', cut_all=True)
time.sleep(5)
print ('Full Mode:' + '/ '.join(seg_list))
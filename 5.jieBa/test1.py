#encoding=utf-8
import jieba

seg_list = jieba.cut('他来到了厦门软件园', cut_all=True)

print ('Full Mode:' + '/ '.join(seg_list))
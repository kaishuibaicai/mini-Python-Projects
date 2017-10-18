#encoding=utf-8
import jieba
import jieba.posseg as pseg

seg_list = jieba.cut('他来到了厦门软件园', cut_all=True)
words = pseg.cut('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print ('Full Mode:' + '/ '.join(seg_list))
for word, flag in words:
	print ('%s %s' % (word, flag))
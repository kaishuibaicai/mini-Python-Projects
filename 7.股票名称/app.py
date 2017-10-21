#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import pymysql
import time

# for num in open('numList.txt', 'r'):
# 	print num
f = open("numList.txt")             # 返回一个文件对象
num = f.readline().strip('\n')             # 调用文件的 readline()方法
while num:
	s = open("nameList.txt", 'w')
	s.write(num)
    #print type(num)              # 后面跟 ',' 将忽略换行符
    # print(num, end = '')　　　# 在 Python 3中使用
    num = f.readline().strip('\n')

f.close()
s.close()
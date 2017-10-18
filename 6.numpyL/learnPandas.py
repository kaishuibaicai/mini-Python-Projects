#encoding:utf-8
import pandas as pd
reviews = pd.read_csv('ign.csv')

# print reviews.head()   # 查看前多少行数据，默认5行
# print reviews.tail()   # 查看末尾多少行数据，默认5行
# print reviews.shape    # 查看数据有多少行列

reviews = reviews.iloc[:,1:]   # 去掉无用的第一列

print reviews.head()
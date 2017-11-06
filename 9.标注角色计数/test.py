# coding:utf-8
import os
path = "C:\Users\Administrator\Desktop\huoying-zl"
files = os.listdir(path)
s = []

for file in files:
	print file
	#if not os.path.isdir(file):
	#	f = open(path + '/' + file)
#-- coding:utf-8 --
import urllib
from bs4 import BeautifulSoup
import pymysql
import time

with open('numList.txt', 'r') as f:
	for f in f.readline():
		print f

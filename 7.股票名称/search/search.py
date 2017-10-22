#-- coding:utf-8 --

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# name = "\"天宝食品\""
# keyword = name + "\"环境报告书\""
# driver.find_element_by_id("kw").send_keys(keyword.decode('utf-8'))
# driver.find_element_by_id("su").click()

import urllib
from bs4 import BeautifulSoup


f = open("nameList.txt.txt")        
names = f.readlines()      
 
for name in names:
	name = name.strip()
	print name
		
	url = https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%22%E5%A4%A9%E5%AE%9D%E9%A3%9F%E5%93%81%22%22%E7%8E%AF%E5%A2%83%E6%8A%A5%E5%91%8A%E4%B9%A6%22&rsv_pq=8b571d160000138b&rsv_t=05685piESqzn2F8YfpupAfHH%2Fjhsv4%2BV61GM%2Fit7CV3Waq%2FBfnd00QohnZM&rqlang=cn&rsv_enter=0&rsv_sug3=13&inputT=329&rsv_sug4=330
	response = urllib.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")
		

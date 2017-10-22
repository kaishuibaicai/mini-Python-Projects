#-- coding:utf-8 --

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
name = "\"天宝食品\""
keyword = name + "\"环境报告书\""
driver.find_element_by_id("kw").send_keys(keyword.decode('utf-8'))
driver.find_element_by_id("su").click()
#-- coding:utf-8 --

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# name = "\"天宝食品\""
# keyword = name + "\"环境报告书\""
# driver.find_element_by_id("kw").send_keys(keyword.decode('utf-8'))
# driver.find_element_by_id("su").click()
import re
import urllib
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as Pq

class BaiduSearchSpider(object):
    
    def __init__(self, searchText):
        self.url = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg" % searchText
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"}
        self._page = None
    
    @property 
    def page(self):
        if not self._page:
            r = requests.get(self.url, headers=self.headers)
            r.encoding = 'utf-8'
            self._page = Pq(r.text)
        return self._page
    
    @property
    def baiduURLs(self):
        return [(site.attr('href'), site.text().encode('utf-8')) for site in self.page('div.result.c-container  h3.t  a').items()]
    
    @property    
    def originalURLs(self):
        tmpURLs = self.baiduURLs
        print tmpURLs
        originalURLs = []
        for tmpurl in tmpURLs:
            tmpPage = requests.get(tmpurl[0])
            #tmpPage.encoding = 'utf-8' #这样不好使，print的时候python报错
            tmptext = tmpPage.text.encode('utf-8')
            urlMatch = re.search(r'URL=\'(.*?)\'', tmptext, re.S)
            if not urlMatch == None:
                print urlMatch.group(1), "   ", tmpurl[1]
                originalURLs.append(tmpurl)
            else:
                print "---------------"
                print "No Original URL found!!"
                print tmpurl[0]
                print tmpurl[1]
 
        return originalURLs


try:
	f = open("searchList.txt")        
	names = f.readlines()      
	 
	for name in names:
		name = "\"{}\"".format(name.strip())
		print name
		keyword = name + "\"环境报告书\""
		# url = 'http://www.baidu.com'
		# #url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=" + keyword + "&rsv_pq=8b571d160000138b&rsv_t=05685piESqzn2F8YfpupAfHH%2Fjhsv4%2BV61GM%2Fit7CV3Waq%2FBfnd00QohnZM&rqlang=cn&rsv_enter=0&rsv_sug3=13&inputT=329&rsv_sug4=330"
		# print url
		# response = urllib.urlopen(url)
		# html = response.read()
		# soup = BeautifulSoup(html, 'html.parser')
		# print soup
		bdsearch = BaiduSearchSpider(keyword) 
		originalurls = bdsearch.originalURLs
		print '=======Original URLs========'
		print originalurls
		print '============================'
		
finally:
	if f:
		f.close()	

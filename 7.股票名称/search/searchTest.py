#!/usr/bin/python
#coding=utf-8

import re
import requests
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

# searchText = raw_input("搜索内容是：") 
# print searchText

bdsearch = BaiduSearchSpider("\"科伦药业\"\"环境报告书\"") 
originalurls = bdsearch.originalURLs
print '=======Original URLs========'
print originalurls
print '============================'
import urllib2
import socket
def send_req(url):
    host='weixinmp.fjedu.gov.cn'
#   header={'Host':host}
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; MI PAD Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/en',
        'Referer': 'http://weixinmp.fjedu.gov.cn/vote/31/408/item?from=timeline&code=013rxTOz1EN0Rd06W7Rz1bwXOz1rxTOq',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'Cookie': 'request_method=GET; _weixin_front_sessionn=TG5TRXV2UFNPUVZERXUzQXk0U0prYWg5cnpieXpSdlMrR21vbDE0YmJZeGkxQ3g5OXBIcEo1OFFRbkEwZ0RzVlVlbmlCa0R6aGxVTmE1NVMzcnBROCtWVC9XYWk0MFZTQzdjbm81enZOT2dxN2dFRmUyb0xSUmVFNC91UGVLak5sS1pKa3dRZHkrNmxTOVQxM3g4L2hIQnVYaXBzem1BaGp6dy9mU251bUwzZzBlV1NvRC9QaitMTE9lMzg3V0VRUU83UFNPbTUzcElKR3hGbHdIKy9QaUpoSTliWmh1MUlVZDZoSE54YzN1MWNaZ0tsb0cxK2Y3VUFVekxOSnpkeC0tcTlRWk5mVTdQdGxYMlBJV2dhUE1zdz09--b16973d9467ec3b6b23b70a82bf9c43691fbd21f',
        'If-None-Match': "6502b2ce7fcc3afd5b311a94d49d1119"

}
    req=urllib2.Request(url,headers=headers)
    req.get_method=lambda: 'HEAD'
    res=urllib2.urlopen(req)
    #msg=res.msg
#   print msg
    head=res.headers
    content=dict(head)
    print 'content-length:%s'%content['content-length']
    #data=res.read()
    #print data
    #print type(data)
    #print data
url='http://www.baidu.com/search/error.html'
if __name__=="__main__":
    socket.setdefaulttimeout(2)
    send_req(url)

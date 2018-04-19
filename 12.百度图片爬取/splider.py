import requests
import os
import logging


def get_pages(keyword, pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '3',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for param in params:
        try:
            text = requests.get(url, params=param)
            urls.append(text.json().get('data'))
        except Exception:
            logging.info("{}角色图片下载失败,地址:{}".format(keyword, url))
            continue

    return urls


def get_images(data_list, local_path, char_name):

    if not os.path.exists(local_path):  # 新建文件夹
        os.mkdir(local_path)

    count = 0
    for url_list in data_list:
        for image_url in url_list:
            if image_url.get('thumbURL') != None:
                #print('正在下载：%s' % image_url.get('thumbURL'))
                ir = requests.get(image_url.get('thumbURL'))
                open(local_path + '%s_%d.jpg' % (char_name, count), 'wb').write(ir.content)
                count += 1
        print("当前已下载%d张" % count)
    logging.info("共下载{}角色动漫图片{}张".format(char_name, count))
    print("共下载{}角色动漫图片{}张".format(char_name, count))

def logging_init():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s)',
                        datefmt='%Y-%b-%d %H:%M:%S', filename='baidu_image.log', filemode='w')


if __name__ == '__main__':
    logging_init()
    i = 1
    basepath = 'H:\标注管理\images\动漫角色爬取\第一周角色标注任务'
    for m in os.listdir(basepath):
      for a in os.listdir(os.path.join(basepath, m)):
        curpath = os.path.join(basepath, m, a)
        file = os.path.join(curpath, 'keywords.txt')
        print(file)
        keywords = []
        with open(file, 'r', encoding='utf-8') as f:
          keywords = f.readlines()
        print (i, keywords)
        i += 1


    '''for word in key_words7:
        data_list = get_pages(word, 20)
        get_images(data_list, file_path, word)'''


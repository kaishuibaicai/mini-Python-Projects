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
    key_words = ['六道骸','沢田纲吉','狱寺隼人','山本武','云雀恭弥','里包恩',
                 '三浦春','笹川京子','武藤游戏','海马濑人','城之内克也',
                 '真崎杏子','游戏王本田','貘良了','游戏王舞','黑崎一护',
                 '朽木露琪亚','井上织姬','阿散井恋次','石田雨龙']
    key_words2 = ['小丸子','樱桃小丸子姐姐','樱桃小丸子妈妈','樱桃小丸子爸爸',
                 '樱桃小丸子爷爷','樱桃小丸子奶奶','钢之炼金术师爱德华',
                 '钢之炼金术师温莉','霍恩海姆 艾尔利克','伊兹米 卡迪斯','斯卡',
                 'Saber','卫宫士郎','吉尔伽美什','Lancer','伊斯坎达尔']
    key_words3 = ['自拍大头照']
    key_words4 = ['动漫男生头像','动漫女生头像']
    key_words5 = ['动漫主角', '日本动漫人物', '日本动漫']
    key_words6 = ['证件照 女']
    key_words7 = ['蜘蛛侠']
    file_path = '/home/codeadmin/python-workspace/baidu_image_splider/images_face/face_0413/'
    for word in key_words7:
        data_list = get_pages(word, 20)
        get_images(data_list, file_path, word)

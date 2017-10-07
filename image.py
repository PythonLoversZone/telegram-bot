'''
抓取 weheart.com图站
指定关键字的图片
'''

import requests
from bs4 import BeautifulSoup
import random

query_url = 'http://weheartit.com/search/entries?utf8=%E2%9C%93&ac=0&query={}'


def get_html_text(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def parse_img(keyword):
    'weheart 网站'
    html = get_html_text(query_url.format(keyword))
    if html != 'error':
        soup = BeautifulSoup(html, 'lxml')
        imgs = soup.find_all('img', class_='entry-thumbnail')
        return random.choice(imgs)['src']
    else:
        return 'error'


# print(parse_img('日'))

def get_html_with_header(url):
    '''获取网页的原始text'''
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    try:
        r = requests.get(url, timeout=9, headers=headers)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


SEARCHRUL = 'https://www.google.com/search?&safe=off&q={}&tbm=isch&tbs=itp:photo,isz:l'


def parse_img_url(q):
    '''
    Google图片
    '''

    url = SEARCHRUL.format(q)
    html = get_html_with_header(url)
    if html != 'error':
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.find_all('div', class_='rg_meta')
        content = random.choice(contents)
        rec = eval(content.text)
        return rec['ou']
    else:
        return 'error'


# print(parse_img_url('猫咪'))

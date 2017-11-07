'''
time:   2017-11-07
author: Ehco1996

bot 用的一些小爬虫
'''

import requests
from bs4 import BeautifulSoup
import random


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
}


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30, headers=HEADERS)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return -1


def get_joke():
    '''
    抓取一个糗事段子
    '''
    html = get_html_text(
        'https://www.qiushibaike.com/8hr/page/{}/'.format(random.randint(1, 9)))
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all(
        'div', class_='article block untagged mb15 typs_hot')
    article = random.choice(articles)

    body = article.find('span').text
    author = article.find('img')['alt']
    try:
        comment = article.find(
            'div', class_='main-text').contents[0].replace('\n', '')
    except:
        comment = '暂时没有热评'
    joke = '作者：{}{}热评: {}'.format(author, body, comment)
    return joke


def get_joke_images():
    '''糗事百科搞笑图片'''

    html = get_html_text(
        'https://www.qiushibaike.com/imgrank/page/{}'.format(random.randint(1, 10)))
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all(
        'div', class_='article block untagged mb15 typs_hot')
    article = random.choice(articles)
    img = 'http:' + article.find('div', class_='thumb').a.img['src']

    return img


def get_meizi_images():
    '''煎蛋网妹子图'''
    url = 'http://jandan.net/ooxx/page-{}'.format(random.randint(1, 268))
    html = get_html_text(url)
    if html != -1:
        soup = BeautifulSoup(html, 'lxml')
        imgs = soup.find_all('a', class_='view_img_link')
        # 随机取出一个div
        img = imgs[random.randint(0, len(imgs))]
        return 'http:' + img['href']
    else:
        return -1

def get_boring_images():
    '''煎蛋网无聊图'''
    url = 'http://jandan.net/pic/page-{}'.format(random.randint(1, 377))
    html = get_html_text(url)
    if html != -1:
        soup = BeautifulSoup(html, 'lxml')
        imgs = soup.find_all('a', class_='view_img_link')
        # 随机取出一个div
        img = imgs[random.randint(0, len(imgs))]
        return 'http:' + img['href']
    else:
        return -1



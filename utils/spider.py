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
    '''
    获取
    https://www.eatliver.com/
    搞笑图
    '''

    html = get_html_text(
        'https://www.eatliver.com/page/{}/'.format(random.randint(1, 175)))
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all(
        'div', class_='post-content clearfix')
    article = random.choice(articles)
    img = article.find('img')['src']

    return img

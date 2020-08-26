import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin
import django


# 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest.settings")

# 장고를 가져와 장고 프로젝트를 사용할 수 있는 환경을 만들기
django.setup()

from newscrawl.models import NewsData


def parse_news():

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    base = 'https://news.naver.com/'

    req= requests.get(base)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_title = soup.select('div.hdline_news ul.hdline_article_list div.hdline_article_tit a')


    data = {}

    for i in my_title:
        data[i.text.strip()] = urljoin(base, i['href'])
        # print(i.text.strip())
        # print(urljoin(base, i['href']))
    # with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    #     json.dump(data, json_file)
    return data


if __name__ == '__main__':
    news_data_dict = parse_news()
    for t, l in news_data_dict.items():
        NewsData(title=t, link=l).save()
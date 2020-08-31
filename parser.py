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


def parse_news(keyword):
    data = {}
    search_keyword = keyword

    # for idx in [0,11]: # 여러 페이지를 가지고 올때 사용합니다.
    base = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}&start={0}'

    req= requests.get(base)
    soup = BeautifulSoup(req.text, 'html.parser')
    my_title = soup.select('a._sp_each_title') # 제목, 링크
    my_contents = soup.select('ul.type01 dl > dd:nth-child(3)') # 내용

    for idx, i in enumerate(my_title): #10개씩
        title = i['title']
        link = urljoin(base, i['href'])
        contents = my_contents[idx].text
        
        data[title] = (link, contents)
        
    return data


def del_save_data(keyword):
    ban_list = ['코로나', '마스크', '교회', '방역', '확진', '공모전', '인공지능']

    news_data_dict = parse_news(keyword) # 현재시간 뉴스 받아옴
    
    # print(news_data_dict)
    print(len(news_data_dict))

    cnt = 0
    for t, l in news_data_dict.items():
        if not any([ban in t or ban in l[1] for ban in ban_list]):
            print(t)
            NewsData(title=t, link=l[0], contents=l[1]).save() # 저장
            cnt += 1
        if cnt == 2: # 검색어 하나당 기사 두개
            break

def main():
    NewsData.objects.all().delete() # 객체 전체 삭제
    del_save_data('서울집값')
    del_save_data('서울시안전')
    del_save_data('서울살인')
    del_save_data('서울시홍수피해지역')
    
if __name__ == '__main__':
    main()
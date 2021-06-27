# web_cr09.py
# 네이버 웹툰 크롤링 (전체)

import requests
from bs4 import BeautifulSoup
import webbrowser

# 변수 초기화
page_num = 0
wt_titles = []

# 1. 웹 페이지 주소 찾기
base = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=sun&page='

# 파일 생성
wt_f = open('wtoons.html','w')

# 페이지 별 크롤링
while True:
    page_num = page_num + 1
    url = f'{base}{page_num}'

    # 2. 페이지 요청
    resp = requests.get(url)
    resp.raise_for_status()
    
    # 3. 구문 정리하기
    text = resp.text
    soup = BeautifulSoup(text, 'html.parser')

    # 4. 회별 제목 추출하기
    titles = soup.find_all('td', class_='title')

    # 마지막 페이지 확인
    chk_title = titles[0].text.strip()
    if chk_title in wt_titles:
        break

    # 5. 출력하기
    for idx, one in enumerate(titles):
        num = idx + 1
        title = one.text.strip()
        link = 'https://comic.naver.com' + one.a['href']
        tag = '<a href="{}">{}</a>'.format(link, title)
        wt_titles.append(title)
        wt_f.write(tag + '<br>')

wt_f.close()
webbrowser.open('wtoons.html')





    

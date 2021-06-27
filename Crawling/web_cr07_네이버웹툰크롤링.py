# web_cr07.py
# 네이버 웹툰 크롤링 

import requests
from bs4 import BeautifulSoup
import webbrowser


# 1. 웹페이지 주소 찾기
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=sun'

# 2.페이지 요청하기 
resp = requests.get(url)
resp.raise_for_status()

# 3. 요청 페이지 구문 분석 
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 정보 추출
titles = soup.find_all('td', class_='title')

# 5. 정보 출력
w_f = open('wtoons.html','w')

for idx, one in enumerate(titles):
    num = idx + 1
    title = one.text.strip()
    link = 'https://comic.naver.com' + one.a['href']
    tag = '<a href="{}">{}</a>'.format(link, title)
    print(num, title)
    w_f.write(tag + '<br>')

w_f.close()

webbrowser.open('wtoons.html')

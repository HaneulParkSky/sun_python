# web_cr05.py
# 네이버 영화 랭킹 추출 (입력)


import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 주소 찾기 
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date='
date = input('조회할 날짜 입력(yyyymmdd): ')
url = url + date

# 2. 해당 페이지 정보 요청
resp = requests.get(url)
resp.raise_for_status()

# 3. 요청 문서 구문 정리
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 정보 추출
titles = soup.find_all('div', class_='tit3')

# 5. 정보 출력
for idx, one in enumerate(titles):
    num = idx + 1
    title = one.text.strip()
    link = 'http://movie.naver.com/' + one.a['href']
    tag = '<a href="{}">{}</a>'.format(link, title)
    print(tag)
    #print(f'{num}. {title} {link}') # .strip() 양쪽 옆에 공백 삭제
    
# 6. 파일로 출력
m_f = open('nmrank.html','w')
for idx, one in enumerate(titles):
    title = one.text.strip()
    link = 'https://movie.naver.com/' + one.a['href']
    tag = '<a href="{}">{}</a><br>'.format(link,title)
    m_f.write(tag)
m_f.close()

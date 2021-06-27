# web_cr04.py
# 네이버 영화 랭킹 추출

# 영화 제목 titles : div(tit3)

import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 주소 찾기 
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

# 2. 해딩 페이지에 정보 요청
resp = requests.get(url)
resp.raise_for_status()

# 3. 요청 문서 구문 정리
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 정보 추출
titles = soup.find_all('div', class_='tit3')

# 5. 정보 출력
for idx, one in enumerate(titles):
    print(f'{idx + 1}. {one.text[1:-1]}')

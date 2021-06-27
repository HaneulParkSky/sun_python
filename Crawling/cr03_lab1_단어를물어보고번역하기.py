# cr03_lab1.py
# 단어를 물어보고 번역하기

import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 주소 찾기
base = 'https://dic.daum.net/search.do?q='
user = input('번역할 단어는? ')
url = base + user

# 2. 해당 페이지 정보 요청
resp = requests.get(url)
resp.raise_for_status()

# 3. 요청한 문서를 구문 정리
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 찾는 정보 추출
dic = soup.find('div', class_='cleanword_type kuek_type')
word = dic.find_all('span', class_='txt_search')

# 5. 추출 정보 출력
for idx, one in enumerate(word):
    print(f'{idx + 1}. {one.text}')

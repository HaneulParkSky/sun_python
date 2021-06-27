# web_cr03.py
# 다음 사전

# 대표 블록 : div(cleanword_type kuek_type) -> find
# 번역 단어 : span(txt_search) -> find_all (여러개를 찾아야 하므로)

import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 주소 찾기
url = 'https://dic.daum.net/search.do?q=python'

# 2. 해당 페이지 정보 요청
resp = requests.get(url)
resp.raise_for_status()

# 3. 요청한 문서 구문 정리
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 찾고자 하는 정보 추출
dic = soup.find('div', class_='cleanword_type kuek_type')
word = dic.find_all('span', class_='txt_search')
#print(word)

# 5. 해당 정보 출력

for idx, one in enumerate(word):
    print(f'{idx + 1}. {one.text}')

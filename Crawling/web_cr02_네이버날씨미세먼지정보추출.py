# web_cr02.py
# 네이버 날씨 미세먼지 정보 추출

import requests
from bs4 import BeautifulSoup

# 1. url 
url = 'https://weather.naver.com/today/02173104'

# 2. 자료 요청하기
resp = requests.get(url)

# 3. 구문 분석하기
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 미세먼지 정보 태그 추출 (클래스 이름은 크롬 검사에서 추출)
today = soup.find('ul', class_='today_chart_list')

title = today.find_all('strong')
value = today.find_all('em')

# print(title, value)
for one in title:
    print(one.text)

print('-'*30)

# 타이틀과 값 모두 출력하기
for idx, one in enumerate(title):
    print('{}: {}'.format(one.text,value[idx].text))

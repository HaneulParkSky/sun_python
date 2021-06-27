# cr03_lab1.py
# 네이버 날씨 주간예보 추출하기 

# 주간예보(변수 week): div(scroll_control end_left)
# 날짜(변수 date): span(date)
# 최저기온(변수 tmp_l): span(lowest)
# 최고기온(변수 tmp_h): span(highest)
# 지역명 (변수 location) : strong(location_name)

import requests
from bs4 import BeautifulSoup


# 1. 웹페이지 주소 찾기
url = 'https://weather.naver.com/today/02173104'

# 2. 해당 페이지에 정보 요청하기
resp = requests.get(url)
resp.raise_for_status() # 잘못된 정보를 찾아 알려줌 

# 3. 요청한 문서를 구문 정리하기
text = resp.text
soup = BeautifulSoup(text, 'html.parser')

# 4. 찾고자 하는 정보 추출
location = soup.find('strong', class_='location_name')
week = soup.find('div', class_='card card_week')
#print(week)
date = week.find_all('span', class_='date')
#print(date)
tmp_l = week.find_all('span', class_='lowest')
#print(tmp_l)
tmp_h = week.find_all('span', class_='highest')
#print(tmp_h)

# 5. 해당 정보 출력
# ㄴ find_all 로 찾은건 for 로 출력해야함
# ㄴ find 로 바로 찾은건 그냥 출력하면 됨 
print(location.text)
for idx,one in enumerate(date):
    print(one.text, tmp_l[idx].text, tmp_h[idx].text)


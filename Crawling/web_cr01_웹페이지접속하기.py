# web_cr01.py
# 웹페이지 접속하기

import requests

# 다음 뉴스 사이트
url = 'https://news.daum.net/'

# 사이트에 연결하기
resp = requests.get(url)

# 연결 응답 확인하기
print(resp)

# 응답 상태확인
print('is_ok:', resp.ok)
print('status:', resp.status_code)

# 인코딩 확인
print('encoding:', resp.encoding)

# 헤더 확인
print('header:', resp.headers)

# 응답 헤더의 특정 내용 보기
print(resp.headers['Content-Language'])

# 페이지 코드 보기
print('html:', resp.text)

# 특정 url 요청하기
# raise_for_status() -> 응답 결과에 오류가 있는 경우 프로그램 중단



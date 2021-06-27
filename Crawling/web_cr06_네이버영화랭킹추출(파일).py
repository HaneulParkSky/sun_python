# web_cr06.py
# 네이버 영화 랭킹 파일로 출력하기 


import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

resp = requests.get(url)

text = resp.text
soup = BeautifulSoup(text, 'html.parser')

titles = soup.find_all('div', class_='tit3')

n_f = open('mov_rank.html','w')
for idx, one in enumerate(titles):
    num = idx + 1
    title = one.text.strip()
    link = 'https://movie.naver.com/' + one.a['href']
    tag = '<a href="{}">{}</a>'.format(link, title)
    n_f.write(tag + '<br>')
n_f.close()

print('파일 기록 완료')
webbrowser.open('mov_rank.html')

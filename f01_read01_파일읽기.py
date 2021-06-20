# f01_read01.py
# 파일 읽기

m_f = open('mypitca2.txt','r') # 읽기는 r (생략 가능)

# 1. 한 줄 읽기
msg = m_f.readline()  # readline 은 파일에서 한 줄을 읽어줌
print(msg, end='')    # end='' 는 마지막 엔터를 지워줌 
msg = m_f.readline()
print(msg, end='')

m_f.close()

# 2. 모든 줄 불러오기 (자료분석에서 이걸 많이 씀)

m_f = open('mypitca2.txt','r')
msg = m_f.readlines() # readlines : 전체 라인을 리스트 형식으로 가져옴
print(msg[0], end='')
print(msg[1], end='')
m_f.close()

print('-' * 30)
for one in msg:
    print(one, end='')

print('-' * 30)

# 3. 모든 줄 불러오기 2 
m_f = open('mypitca2.txt','r')
for one in m_f:
    print(one, end='')
m_f.close()

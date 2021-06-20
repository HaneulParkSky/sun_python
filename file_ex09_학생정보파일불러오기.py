# file_ex09.py
# 학생정보 파일 불러오기

m_f = open('file_ex03.txt')

for one in m_f:
    # print(one, end='')
    data = one.split() # split은 공백을 기준으로 데이터 분리 : 홍길동 87 -> ['홍길동','87']
    name = data[0] # 항목을 구분해놓으면 좋음 
    score = data[1]
    print(f'학생이름:{name}, 성적:{score}')
    
m_f.close()

# file_ex04.py
# 반복 문장 기록하기


m_f = open('file_ex04.txt','w')

for x in range(100):
    msg = f'{x + 1}번째 줄 입니다.'
    print(msg)
    m_f.write(msg + '\n')
    
m_f.close()

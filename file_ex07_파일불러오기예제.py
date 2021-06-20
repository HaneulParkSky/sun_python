# file_ex07.py
# 파일불러오기

m_f = open('file_ex04.txt')

for one in m_f:
    print(one, end='')

m_f.close()

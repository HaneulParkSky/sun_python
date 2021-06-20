# f02_filecopy.py
# file_ex04.txt 파일 file_copy04.txt 로 복사하기

s_f = open('file_ex04.txt')
c_f = open('file_copy04.txt','w')

for one in s_f:
    print(one, end = '...복사완료')
    c_f.write(one)

print('파일 전체 복사 완료')

c_f.close()
s_f.close()

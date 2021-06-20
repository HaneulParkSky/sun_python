# file_ex03.py
# 학생정보 파일에 기록

f = open('file_ex03.txt','w')

while True:
    name = input('학생이름: ')
    if name == '종료':
        break
    score = input('성적: ')
    msg = f'{name} {score} \n'
    #msg2 = f'학생이름: {name}\n성적: {score}\n'
    f.write(msg2)

f.close()

print('file_ex03.txt 파일을 기록했습니다')

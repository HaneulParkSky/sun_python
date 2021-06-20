# f01_write011.py

f = open('mypitca01.txt','w')
msg = '파이썬 파일 기록은 쉽다.\n' # 엔터 위에 역슬래시 (\)
f.write(msg)
msg = '파일을 기록할때는 w 속성을 준다.\n'
f.write(msg)
msg = 'life is short\nyouneed python\n'
f.write(msg)
f.close()

print('파일 생성 완료')

# f01_write02.py
# 여러 문장 입력받아 mypitca2.txt 로 저장

m_f = open('mypitca2.txt','w')

while True:
    msg = input('기록할 문장을 입력하세요:')
    if msg == '':
        break
    m_f.write(msg + '\n')

m_f.close() # close 해야 파일 저장
print('파일 기록 완료')

    

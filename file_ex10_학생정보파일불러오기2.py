# file_ex10.py
# 학생정보 파일 불러오기 문제

m_f = open('file_ex03.txt')

f_sum = 0 # 합계는 항상 초기값이 있어야함 
f_all = m_f.readlines() # ['홍길동','87\n','김철수...]

for one in f_all:
    data = one.split()
    name = data[0]
    score = int(data[1])
    f_sum = f_sum + score
    #print(f'학생이름:{name}\n성적:{score}')
    print('학생이름:', name)
    print('성적:', score)

m_f.close()

print()
print(f'학급 총점: {f_sum}점')

f_avg = round(f_sum / len(f_all), 1) # round 함수는 소수 첫째자리까지 표기
print(f'학급 평균 : {f_avg}')

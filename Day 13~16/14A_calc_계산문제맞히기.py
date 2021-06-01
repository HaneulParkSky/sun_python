# 14A_calc.py
# 교재 p.126
# 계산 문제 맞히기

import random

def make_question():
    n1 = random.randint(1, 40)
    n2 = random.randint(1, 20)
    op = random.randint(1, 3)

    # 문자열 변수 q 에 문제 생성
    q = str(n1)

    # 연산자 추가
    if op == 1:
        q = q + '+'
    elif op == 2:
        q = q + '-'
    else:
        q = q + '*'

    # 두번째 숫자 추가
    q = q + str(n2)

    return q

# 정답 수, 오답수 체크 변수 sc1, sc2
sc1 = 0 # 정답 수 
sc2 = 0 # 오답 수 

# 문제 확인
for x in range(5):
    q = make_question()
    r = int(input(q + '='))

    if r == eval(q):
        print('정답')
        sc1 = sc1 + 1
    else:
        print('오답')
        sc2 = sc2 + 1

# 정답, 오답수 출력
print(f'정답 : {sc1}, 오답 : {sc2}개')

# 오답이 0인 경우 '천재' 출력
if sc2 == 0:
    print('당신은 천재입니다!')
    


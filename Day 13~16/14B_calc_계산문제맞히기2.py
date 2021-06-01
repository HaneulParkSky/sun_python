# 14B_calc.py
# 계산 문제 맞히기 2

import random

# 문제 출제 함수 make_quiz
def make_quiz():
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    # n1 이 n2 보다 작으면 값 변경
    if n1 < n2:
        n1, n2 = n2, n1 # n1, n2 값 변경
    ops = ['+', '-', '*']
    op = random.choice(ops)
    quiz = f'{n1} {op} {n2}'
    return quiz

sc1 = 0
sc2 = 0

# 문제 출제
for x in range(5):
    quiz = make_quiz()
    ans = eval(quiz)

    usr = int(input(f'{quiz} = '))
    if usr == ans:
        print('정답')
        sc1 = sc1 + 1
    else:
        print('오답')
        sc2 = sc2 + 1
        
print(f'정답 : {sc1}, 오답 : {sc2}')
if sc1 == 5:
    print('천재')
    

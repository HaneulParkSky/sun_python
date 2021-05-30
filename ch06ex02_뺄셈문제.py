# ch06ex02.py
# 계산문제 2 (뺄셈 문제 만드는 함수 makeQuiz() 만들기)

import random

def make_quiz():
    num1 = random.randint(10, 20)
    num2 = random.randint(1, 10)
    quiz = f'{num1} - {num2}'
    return quiz


for x in range(5):
    quiz = make_quiz()
    ans = eval(quiz)
    print(f'{quiz} = {ans}')
    

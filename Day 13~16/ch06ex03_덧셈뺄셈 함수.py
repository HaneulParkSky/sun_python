# ch06ex03.py
# 덧셈, 뺄셈 문제 만드는 함수 makeQuiz() 만들기

import random

def make_quiz():
    num1 = random.randint(10, 20)
    num2 = random.randint(1, 9)
    op = random.randint(1, 2)

    if op == 1:
        ops = '+'
    else:
        ops = '-'

    quiz = f'{num1} {ops} {num2}'

    return quiz

    #quiz = str(num1)    # 초기값은 반드시 필요
    #if op == 1:
    #    quiz = quiz + ' + '
    #else:
    #    quiz = quiz + ' - '
    #quiz = quiz + str(num2)

    #return quiz


    #if op == 1:
    #    quiz = f'{num1} + {num2}'
    #else:
    #    quiz = f'{num1} - {num2}'

    #return quiz

for x in range(5):
    quiz = make_quiz()
    ans = eval(quiz)
    print(f'{quiz} = {ans}')

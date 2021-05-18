# 09C_calc.py
# 무작위 덧셈 문제 만들기

import random

# 두 난수 생성
n1 = random.randint(1,30)
n2 = random.randint(1,30)

# 문제 만들기 
quiz = "{} + {} = ".format(n1, n2)

# 문제 출제
usr = int(input(quiz))

# 판정

if usr == n1 + n2:
    print("정답")
else:
    print("오답")

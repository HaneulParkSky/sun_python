# 09D_calc.py

# 무작위로 5문제 풀기

# 문제 1. 정답과 오답수 출력하기 (변수 : cnt)
# 문제 2. 총 문제 푼 시간 출력 

import random
import time

# 정답 변수 초기화

cnt = 0

# 시간 측정 시작
st = time.time()

# 문제 수 변수
q_cnt = 3

for x in range(q_cnt):      #반복해야 하는 항목 위에 기입
    
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    quiz = "{} + {} = ".format(n1, n2)

    usr = int(input(quiz))
    ans = n1 + n2

    if usr == ans:
        print("정답")
        # 정답 수를 증가
        cnt = cnt + 1
    else:
        print("오답")

# 시간 측정 종료
et = time.time()

# 정답과 오답수를 출력

print("총 {}문제 중 {}문제 정답!".format(q_cnt,cnt))
print("총 {}문제 중 {}문제 오답!".format(q_cnt,q_cnt-cnt))

# 문제 풀이 시간 출력

print("총 풀이 시간: {}초".format(int(et-st)))


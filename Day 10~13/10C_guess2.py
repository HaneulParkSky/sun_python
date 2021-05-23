# 10C_guess2.py
# 1~100 숫자 맞히기

import random

# 1에서 100사이의 난수 발생

r = random.randint(1,100)
#print('정답:',r)  # 정답을 출력해 놓고 잘 작동되는지 확인 (주석 처리)

# 변수 초기화
n = 0
cnt = 0

while n != r:   # n 이 r 이랑 다르면,
    n = int(input('1~100 숫자: '))
    cnt = cnt + 1

    if n == r:
        msg = "정답"
    elif n > r:
        msg = "커요"
    else:
        msg = "작아요"

    if abs(n - r) >= 20:
        msg = "너무" + msg

    print (msg)

print("시도횟수:,", cnt)
    
    

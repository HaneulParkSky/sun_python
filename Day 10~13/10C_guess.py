
# 10C_guess.py
# 2021.05.23
# 숫자를 추측해서 맞히는 프로그램 

import random

# 1~30사이의 난수 생성 
n = random.randint(1,30)

# 무한 반복문 구현 
while True:
    # 입력 구현 
    x = input("맞춰 보세요 : ")
    g = int(x)
    if g == n:
        print("정답")
        break           # 반복문 탈출 
    if g < n:
        print("너무 작아요")
    if g > n:
        print("너무 커요")
        

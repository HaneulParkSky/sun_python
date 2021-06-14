# trun_timer02.py
# 거북이 달리기

import turtle as t
import random

# 화면 설정
t.setup(500,300)
t.bgcolor('orange')

# 거북이 생성
tg = t.Turtle()
tg.color('green')
tg.shape('turtle')
tg.up()
tg.goto(-200,100)

# 기본 거북이 설정 
t.shape('turtle')
t.color('white')
t.up()
t.goto(-200,-100)

# 거북이 속도 초기화
t_speed = random.randint(5,15)
tg_speed = random.randint(5,15)
print(f'흰색 거북이 속도 {t_speed}, 초록 거북이 속도{tg_speed}')

# 이동 함수 구현
def play():
    t.forward(t_speed)
    tg.forward(tg_speed)
    b_t = t.xcor() < 200
    b_tg = tg.xcor() < 200
    print(f'흰색 좌표: {t.xcor()}, 녹색 좌표: {tg.xcor()}, t.x<200:{b_t}, tg.x<200:{b_tg}, and: {b_t and b_tg}')
    if t.xcor() < 200 and tg.xcor() < 200:
        t.ontimer(play, 100)
    
# 함수 호출
play()

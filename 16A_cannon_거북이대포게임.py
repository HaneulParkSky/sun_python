# 16A_cannon.py
# 거북이 대포 게임 만들기

import turtle as t
import random

# 대포 각도 조절, 발사 함수 

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
        # print(t.pos())
        # print(t.ycor())

    # 대포와 타겟의 거리 구하기
    d = t.distance(target, 0)

    t.sety(random.randint(10, 100)) # 메세지 겹치지 않기 위함
    if d < 25:
        t.color('blue')
        t.write('성공')
    else:
        t.color('red')
        t.write('실패')
        t.color('black')
        t.goto(-200, 10)
        t.setheading(ang)
    

# 바닥 그리기
t.forward(300)
t.forward(-600)

# 타겟 그리기 
target = random.randint(50, 150)

t.pensize(3)
t.color('green')
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 대포 초기화
t.up()
t.color('black')
t.goto(-200, 30)
t.setheading(20)

# 키 입력 처리
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()



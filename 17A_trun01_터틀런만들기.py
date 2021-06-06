# 17A_trun01.py
# 터틀런 만들기

import turtle as t
import random

# 화면 설정 
t.setup(500,500)
t.title('turtle RUN')
t.bgcolor('orange')

# 초기 화면 설정
# 적 거북이 
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)

# 먹이 만들기 
ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0,-200)

# 플레이어 거북이 만들기 
t.shape('turtle')
t.color('white')
t.speed(0)
t.up()

# 키 입력 함수 구현 
def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

cnt = 0

# 진행 함수 구현

def play():
    global cnt
    t.forward(10)

    # 먹이 층돌 처리
    if t.distance(ts) < 12:
        cnt = cnt + 1
        t.write(cnt)
        
        # 충돌 시 먹이 이동
        sx = random.randint(-230,230)
        sy = random.randint(-230,230)
        ts.goto(sx,sy)

    # 적 이동 구현
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(8)

    # 충돌 확인
    if t.distance(te) > 12:
        t.ontimer(play, 100)

   
# 키 입력 처리
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")

t.listen() # t.listen() 을 해줘야 무조건 실행됨

# 함수 호출
play()

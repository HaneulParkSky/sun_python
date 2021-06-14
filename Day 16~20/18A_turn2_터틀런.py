# 18A_trun2_setup.py

import turtle as t
import random

# 화면 설정 
t.setup(500,500)
t.bgcolor('orange')
t.title('Turtle RUN')

# 거북이 설정 함수 
def set_turtle(tname, tshape, tcol, tx, ty):
    tname.shape(tshape)
    tname.color(tcol)
    tname.up()
    tname.goto(tx,ty)
    tname.speed(0)

# 플레이어 설정
set_turtle(t, 'turtle', 'white', 0, 0)

# 적 거북이
te = t.Turtle()
set_turtle(te, 'turtle', 'red', 0, 200)

# 먹이 설정 
ts = t.Turtle()
set_turtle(ts, 'circle', 'green', 0, -200)

# 변수 초기화
score = 0
playing = False

# 거북이 이동 함수 play() : 0.1초마다 앞으로 10px 이동
def play():
    global score
    global playing
    
    t.forward(10)
    
    if t.xcor() > 230:
        t.setheading(180)
    if t.xcor() < -230:
        t.setheading(0)
    if t.ycor() > 230:
        t.setheading(270)
    if t.ycor() < -230:
        t.setheading(90)
            
    # 먹이 충돌 구현
    if t.distance(ts.pos()) < 12:
        score = score + 1
        t.write(score)
        sx = random.randint(-230,230)
        sy = random.randint(-230,230)
        ts.goto(sx, sy)

    # 적 이동
    opp = random.randint(1,5)
    if opp == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 10
    te.forward(speed)

    # 적 충돌 확인
    if t.distance(te) < 12:
        playing = False
        message('GAME OVER', f'score: {score}')

    # if playing == True:
    if playing: # True 일 때만 실행함 
        t.ontimer(play, 100)


# 방향 전환 함수 
def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        te.goto(0,200)
        ts.goto(0,-200)
        play()
    
# 메세지 출력 함수
def message(m1, m2):
    t.goto(0,100)
    t.write(m1, 'False', 'center', ('Arial Black',20))
    t.goto(0,-100)
    t.write(m2, 'False', 'center', ('Arial Black',15))
    t.home()

# 키 입력 처리
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(start, "space")
t.listen()

# 이동함수 호출 
message('Turtle Run', '[space bar to start]')




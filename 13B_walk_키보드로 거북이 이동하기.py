# 13B_walk.py
# 키보드로 거북이 이동하기

import turtle as t

# 이동 함수 구현

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

# 펜사이즈 조정

def set_pensize1():
    t.pensize(1)

def set_pensize5():
    t.pensize(5)

# 거북이 펜 이동

def pen_up():
    t.up()

def pen_down():
    t.down()

# 화면 지우기

def black():
    t.reset()


# 거북이 설정
t.shape('turtle')
t.speed(0)

# 키 입력 처리
t.onkeypress(turn_right, 'Right')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(set_pensize1, '1')
t.onkeypress(set_pensize5, '5')
t.onkeypress(pen_up, 'u')
t.onkeypress(pen_down, 'd')
t.onkeypress(black, 'Escape')

t.listen()

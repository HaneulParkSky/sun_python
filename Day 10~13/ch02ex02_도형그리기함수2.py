# ch02ex02_py
# 도형그리기 함수 step2

import turtle as t
t.speed(0)

def draw_rect(n):
    for x in range(4):
        t.forward(n)
        t.left(90)

def draw_tri(n):
    for x in range(3):
        t.forward(n)
        t.left(120)



draw_rect(200)
draw_tri(200)

t.up()
t.forward(300)
t.down()

draw_rect(90)
draw_tri(90)


# ch02ex03.py
# 도형그리기 함수 step3

import turtle as t
t.speed(0)

def draw_rect(x, y, n):
    t.up()
    t.goto(x, y)
    t.down()
    for x in range(4):
        t.forward(n)
        t.left(360 / 4)

def draw_rect(x, y, n):
    t.up()
    t.goto(x, y)
    t.down()
    for x in range(4):
        t.forward(n)
        t.left(360 / 4)

def draw_tri(x, y, n):
    t.up()
    t.goto(x, y)
    t.down()
    for x in range(3):
        t.forward(n)
        t.left(360 / 3)

def draw_tri(x, y, n):
    t.up()
    t.goto(x, y)
    t.down()
    for x in range(3):
        t.forward(n)
        t.left(360 / 3)

# 도형 그리기 

draw_rect(200, 200, 100)
draw_rect(-200, -200, 100)
draw_tri(-200, 200, 100)
draw_tri(200, -200, 100)

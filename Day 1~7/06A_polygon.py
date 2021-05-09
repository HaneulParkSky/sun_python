# 06A_polygon.py

# 정오각형을 그리는 프로그램

import turtle as t

n = 180
t.color('purple')
t.speed(0)

t.begin_fill()
for x in range(n):
    t.forward(2)
    t.left(360/n)
t.end_fill()

t.hideturtle()

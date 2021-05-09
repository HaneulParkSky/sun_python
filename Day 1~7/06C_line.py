# 06C_line.py

# 선을 반복해서 그리는 프로그램

import turtle as t

ang = 89
t.bgcolor('black')
t.color('yellow')
t.speed(0)
t.fillcolor('red')

t.begin_fill()
for x in range(200):
    t.forward(x)
    t.left(ang)
t.end_fill()

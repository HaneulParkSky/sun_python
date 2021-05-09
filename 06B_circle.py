# 06B_circle.py

# 원을 반복해서 그리기

import turtle as t

t.bgcolor('black')
t.color('green')
t.speed(0)

# 반복횟수 변수 n

n = 50
for x in range(n):
    t.circle(180)
    t.left(360 / n)
    
t.color('orange')
for x in range(n):
    t.circle(80)
    t.left(360 / n)

t.up()
t.goto(200,200)
t.down()

t.color('red')
for x in range(n):
    t.circle(80)
    t.left(360 / n)

t.up()
t.goto(-200,-200)
t.down()

t.color('blue')
for x in range(n):
    t.circle(80)
    t.left(360 / n)

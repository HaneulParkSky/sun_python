# ch03ex01.py
# 태극모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(500):
    if x % 4 == 0:
        t.color('red')
    elif x % 4 == 1:
        t.color('green')
    elif x % 4 == 2:
        t.color('blue')
    else:
        t.color('yellow')

    t.forward(x * 2)
    t.left(89)
    

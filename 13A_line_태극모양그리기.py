# 13A_line.py
# 태극 모양 그리기


import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(200):
    if x % 3 == 0:
        t.color('red')
    elif x % 3 == 1:
        t.color('yellow')
    else:
        t.color('blue')

    t.forward(x * 5)
    t.left(119)
    

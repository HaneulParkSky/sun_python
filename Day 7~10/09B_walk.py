# 09B_walk.py
# 2021.05.16 박하늘
# 마음대로 걷는 거북이

import turtle as t
import random as r

t.shape('turtle')
t.speed(0)

for x in range(500):
    ang = r.randint(1, 360)
    dis = r.randint(5, 15)
    t.setheading(ang)
    t.forward(dis)
    

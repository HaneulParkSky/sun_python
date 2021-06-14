# trun01.py
# 터틀 객체 생성하기 

import turtle as t

# 파란 거북이 (t)
t.shape('turtle')
t.color('blue')
t.forward(150)

# 빨강 거북이 (te)
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.goto(100,100)
te.forward(100)
te.forward(50)

# 초록 거북이 (ts)
ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.goto(-100,-100)
ts.forward(70)

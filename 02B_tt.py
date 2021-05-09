# 02B_tt.py
# 2021-05-09 박하늘
# 거북이로 도형 그리기

import turtle as t

t.shape('turtle')

t.color('red')
# 삼각형 그리기

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.color('blue')
t.pensize(5)
# 사각형 그리기
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.color('green')
t.pensize(20)
# 원 그리기

t.circle(50)    #반지름이 50인 원 그리기


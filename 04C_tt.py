# 04C_tt.py

# 반복 기능으로 도형을 그리는 프로그램

import turtle as t

t.shape('turtle')

# 삼각형 그리기



d = 100
for x in range(3):
    t.forward(d)
    t.left(120)

# 사각형 그리기

for x in range(4):
    t.forward(d)
    t.left(90)

# 원 그리기
t.circle(50)

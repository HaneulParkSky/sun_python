# 12C_poly.py
# 다각형 그리기

import turtle as t
t.shape('turtle')
t.speed(0)

# 다각형 그리기 함수 poly(n)

def poly(n):
    for x in range(n):
        t.forward(100)
        t.left(360 / n)


# 다각형 그리기 함수 poly2(n, d)

def poly2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360 / n)
        

# 한변의 길이가 100px 인 다각형 그리기
poly(3)
poly(5)
poly(8)

# 위치 이동하기
t.up()
t.forward(300)
t.down()

# 거리를 지정한 다각형 그리기
poly2(3, 50)
poly2(5, 50)
poly2(8, 50)


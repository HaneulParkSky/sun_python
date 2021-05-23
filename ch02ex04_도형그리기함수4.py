# ch02ex04.py
# 도형그리기 함수 step4 (이동함수)

import turtle as t
import random

t.speed(0)

def move_t(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def draw_poly(n, d, x, y):
    move_t(x, y)    # 함수 안에 다른 함수 쓸 수 있음
    for x in range(n):
        t.forward(d)
        t.left(360 / n)


# 무작위로 도형 그리기

for i in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    n = random.randint(3, 8)
    d = random.randint(50, 100)
    draw_poly(n, d, x, y)
    

# 도형 그리기
#draw_poly(5, 50, 150, 150)
#draw_poly(6, 70, 150, -150)
#draw_poly(7, 90, -150, -150)
#draw_poly(8, 110, -150, 150)

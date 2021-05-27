# ch02ex01.py
# 도형그리기 함수 step1 (draw_Rect)

import turtle as t
t.speed(0)

def draw_rect():
    # 사각형 그리기
    for x in range(4):
        t.forward(50)
        t.left(90)


def draw_tri():
    # 3각형 그리기
    for x in range(3):
        t.forward(50)
        t.left(120)


draw_rect()
draw_tri()
t.forward(100)
draw_rect()
draw_tri()
t.forward(100)
draw_rect()
draw_tri()


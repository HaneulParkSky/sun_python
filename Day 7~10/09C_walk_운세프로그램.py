# 09C_walk.py
# 2021.05.16
# 마음대로 걷는 거북이 2

import turtle as t
import random

# 거북이 설정
t.shape('turtle')
t.speed(0)

# 화면 분할 선 그리기

t.forward(400)
t.forward(-800)
t.forward(400)
t.left(90)
t.forward(400)
t.forward(-800)
t.forward(400)

# 운세 적기

t.up()
t.goto(350,350)
t.down()
t.write('무엇이든 가능해!')
t.up()
t.goto(-350,350)
t.down()
t.write('행운 가득한 날')
t.up()
t.goto(-350,-350)
t.down()
t.write('오늘은 집에만 있어!')
t.up()
t.goto(350,-350)
t.down()
t.write('평범한 하루')
t.up()
t.goto(0,0)
t.down()

# 거북이 이동하기
t.color('orange')

for x in range(500):
    ang = random.randint(1,360)
    dis = random.randint(1,15)
    t.setheading(ang)
    t.forward(dis)

# 거북이 표시
t.color('red')

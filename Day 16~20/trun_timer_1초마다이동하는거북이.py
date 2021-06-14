# trun_timer.py
# 1초마다 이동하는 거북이

import turtle as t

# 화면 설정
t.setup(500,500)
t.bgcolor('orange')

# 거북이 초기화
t.shape('turtle')
t.color('white')
t.up()

# 이동 함수 구현
def t_run():
    t.forward(10)
    print('x pos:',t.xcor())
    if t.xcor() < 230: # x좌표가 230보다 작을때, 거북이 움직임
        t.ontimer(t_run, 100) # 1초마다 함수 다시 호출 (반복이 아니라 반복해줘야함)

t_run()


import turtle as t

# 배경 세팅 
t.setup(500,500)
t.bgcolor('orange')
t.title('turtle RUN')

# 악당 거북이 (te)
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)

# 터틀 모양 설정 (t)
t.shape('turtle')
t.color('white')
t.speed(0)
t.up()
t.goto(0,0)

# 먹이 (ts)
ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0,-200)


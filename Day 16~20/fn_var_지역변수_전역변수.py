# fn_var.py
# 지역변수, 전역변수

a = 3
def f():
    a = 5
    print('지역변수 a:', a)

f()
print('전역변수 a:', a)

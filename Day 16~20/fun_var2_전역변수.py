# fn_var2.py
# 전역변수

a = 5
def f():
    global a 
    a = a + 1
    print('함수 전역 변수:',a)

f()
print('전역변수:',a)

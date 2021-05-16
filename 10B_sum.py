# 10B_sum.py
# 1부터 10까지의 숫자 합계

s = 0
x = 1

while x <= 10:
    s = s + x
    print("x : {}, s: {}".format(x, s))
    x = x + 1
    
print("종료 후에 x:",x)


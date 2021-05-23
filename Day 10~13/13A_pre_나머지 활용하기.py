# 13A_pre.py
# 나머지 활용하기

for x in range(10):
    if x % 3 == 0:
        color = 'red'
    elif x % 3 == 1:
        color = 'yellow'
    else:
        color = 'blue'
        
    print('x: {}, x % 3: {}, color: {}'.format(x, x%3, color))
    


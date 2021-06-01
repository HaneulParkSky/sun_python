# 15A_typing.py
# 타자 게임 만들기 

import random
import time

# 단어 리스트

w = ['cat', 'dog', 'fox', 'monkey', 'mouse',
     'panda', 'frog', 'snake', 'wolf']

# 문제 번호

n = 1

# 안내 메세지 출력
print('[타자 게임] 준비 되면 엔터!')
input()

# 시간 측정
st = time.time()

# 문제 출제
q = random.choice(w)

while n <= 5:
    print('문제', n)
    print(q)
    x = input()
    if q == x:
        print('통과')
        n = n + 1
        q = random.choice(w)
    else:
        print('오타! 다시 도전')

# 시간 측정 
et = time.time()
t = et - st
t = format(t, '.2f')
print(f'타자시간:{t}초')


import random
import time

word = ['abc','dc','asdf','asdfc','qwer','aaa','bbb','ccc']
random.shuffle(word)

st = time.time()

cnt = 0

while cnt < 6:
    for one in word:
        usr = input(f'{one}:')
    
        if usr == one:
            print('정답')
            cnt = cnt + 1
        else:
            print('오답')
         
et = time.time()

est = et - st
print(est)

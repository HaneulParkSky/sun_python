# ch08lab4.py
# 복권 번호 생성기 

import random

nums = []
cnt = 0

while cnt < 6:
    r = random.randint(1,45)
    if r not in nums:
        nums.append(r)
        cnt = cnt + 1

nums.sort()
print(nums)

# random.shuffle 생성 (중복 아님) 
nums = list(range(1,46))
random.shuffle(nums) # a = random.shuffle 은 안됨
print(nums[:6])

# random.sample 생성 (중복 아님)
n2 = list(range(1,46))
sam = random.sample(n2,6) # 6개 
print(sam)


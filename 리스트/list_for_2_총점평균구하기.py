# list_for_2.py
# 총점 평균 구하기

sc = [80,70,90,60,100]

# 총점 : sum_s, 평균 : avg_s
sum_s = 0

for one in sc:
    sum_s = sum_s + one

avg_s = sum_s / len(sc)

print('학급 총점:', sum_s)
print('학급 평균:', avg_s)


# list_for_04.py
# 점수 수정하기

sc = [60,70,80,90,85]

# 모두 5점씩 추가 점수 주기
for one in sc:
    print(one + 5)
    
print(sc)
print('-' * 30)

# 각 점수를 업데이트 하기
for idx, one in enumerate(sc):
    sc[idx] = one + 5
    print(idx+1, sc[idx])

print(sc)

# list_for_01.py
# 리스트 원소 접근

sc = [80,90,70,100,50]

# 모든 원소 출력하기
for one in sc:
    print(one)

print('-' * 30)


# 인덱스 사용해 모든 원소 출력하기
cnt = len(sc)
for idx in range(cnt):
    print(f'{idx + 1}번 성적 : {sc[idx]}')


print('-' * 30)

# 인덱스와 값을 한번에 가져오기 (enumerate)
for idx, one in enumerate(sc):
    print(idx, ':', one)
    

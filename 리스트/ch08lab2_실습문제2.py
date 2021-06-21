# ch08lab2.py
# 실습문제 2

fruits = ['사과', '바나나', '딸기', '키위', '귤', '수박', '사과']

print(f'과일은 총 {len(fruits)}개 입니다.')
print('사과의 개수:', fruits.count('사과'))

del fruits[-1]
fruits.insert(2,'복숭아')

print('과일 바구니:', fruits)

print()

if '사과' in fruits:
    print('사과가 과일 바구니에 있습니다.')

print()
print('2번째 ~ 4번째 과일은', fruits[1:4])




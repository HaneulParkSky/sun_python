# ch08lab5.py
# for 문을 이용한 세트메뉴 출력

bread = ['베이글','머핀','초코케이크']
coffee = ['아메리카노','카페라떼']

print('<세트 메뉴 5000원>')
for one1 in bread:
    for one2 in coffee:
        print(one1, '+', one2)


print('-'*30)

# 구구단 출력하기 (단 마다 ----- 구분선 출력)
for x in range(2,10):
    for y in range(1,10):
        print(f'{x} * {y} = {x * y}')
    print('-' * 30)
        
        

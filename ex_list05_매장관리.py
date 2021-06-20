# ex_list05.py
# 매장관리

data = [ ['아메리카노', 47, 4],
         ['카페라떼', 38, 4],
         ['카페모카', 35, 3] ]

for one in data:
    print(f'{one[0]}, 판매실적: {one[1]}, 고객평가: {one[2]}')

    
usr = input('메뉴명: ')
for one in data:
    if usr == one[0]:
        print('커피 메뉴:', usr)
        print(f'판매 실적: {one[1]}, 고객 평가: {one[2]}')




# dict_02.py
# 재고 확인 코드

product = {'커피':7, '펜':3, '지우개':5}

k = product.keys()
usr = input('재고 확인 물품명: ')
if usr in k:
    print(product[usr])
else:
    print('물품이 없습니다')




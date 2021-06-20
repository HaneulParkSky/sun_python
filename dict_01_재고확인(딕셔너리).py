# dict_01.py
# 재고확인



# dictionary
# key 와 value 값으로 구성된다.
# 자료에 순서가 없다.
# tmp = {key1:value1, key2:value2, ...}

product = {'커피':7, '펜':3, '지우개':5}

k = product.keys()
v = product.values()
i = product.items()

print('키 값:',k)
print('값:',v)
print('키와 값:',i)

print('-' * 30)
# 키 값 출력하기
for one in k:
    print('키:',one)
    print('값:',product[one])

print('-' * 30)
# 값 출력하기
for one in v:
    print('값:',one)

print('-' * 30)
# 키, 값 한 번에 출력
for k,v in i:
    print(f'{k}:{v}')
    

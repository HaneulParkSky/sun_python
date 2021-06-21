# list_02.py
# list 처리 명령

cart = ['과자', '멜론', '아이스크림']
print(cart)

# 과자를 사과로 바꾸기
cart[0] = '사과'
print(cart)

# 카트에 'TV' 추가하기
cart.append('TV')
print(cart)

# 카트에 마지막 항목 지우기
del cart[-1]
print(cart)

# 카드 2번째 자리에 '수박' 추가하기
cart.insert(1, '수박')
print(cart)

# 카트 3번째 자리에 '딸기' 추가하기
cart.insert(2, '딸기')
print(cart)

# 카트에서 '딸기' 지우기
cart.remove('딸기')
print(cart)

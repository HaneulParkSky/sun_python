# ch08ex01.py
# 카트 리스트

# 카트 리스트 만들기 
cart = []
cart.append('사과')
cart.append('수박')
print(cart,'리스트에 원소 추가하기')

# 팩 리스트 만들기 
pack = []
pack.append('홈런볼')
pack.append('우유')
print(pack)

# 카트 + 팩 리스트 결합 
cart += pack
print(cart, '리스트 결합하기')

# cart 리스트에서 '수박' 을 '멜론'으로 변경
cart[1] ='멜론'
print(cart)

# cart 리스트에서 3번째 구매 물품을 제거
del cart[2]
print(cart)

# cart 리스트에서 3번째 항목에 '요거트' 추가
cart.insert(2,'요거트')
print(cart)

# cart 리스트에서 '요거트' 제거
cart.remove('요거트')
print(cart, '리스트 원소 추가 후 제거')


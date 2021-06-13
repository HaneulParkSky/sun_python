# ch08ex02.py
# 리스트 원소 개수, 포함 여부 확인

# len(num) -> len 함수는 리스트가 몇개 데이터인지 확인 가능

cart = ['사과', '멜론', '수박']

num = len(cart)
print('리스트 원소 개수 : {}개'.format(num))

while True:
    pd = input('확인할 물품: ')
    if pd == '종료':
        break
    if pd in cart:
        print('구매 했습니다.')
    else:
        print('구매 전 입니다.')



# ch08ex04.py
# 책장 리스트

# 책장 리스트 만들기 
bs = ['파이썬','c','캐드','포토샵','java','엑셀']
print(bs)

# 파워포인트 책 추가 
bs.append('파워포인트')
print(bs)

# 'java' 리스트에서 제거 
bs.remove('java')
print(bs)

# '일러스트' 도서를 '포토샵' 도서 오른쪽에 추가 
bs.insert(4, '일러스트')
print(bs)

# 총 도서의 개수 
print(f'총 도서의 개수 : {len(bs)}')

# 책을 대여 시 책장에 책이 있는지 판단해서 알려주기 
book = input('도서 이름: ')
if book in bs:
    print('대여 가능')
else:
    print('대여 불가')
    
# slice(slicing)
# -> 연속적인 객체들 (리스트, 튜플, 문자열) 의 특정 범위를 가져오는 방법

# slicing 
cg = bs[2:5]
code = bs[:2]
office = bs[-2:]
print(cg)
print(code)
print(office)

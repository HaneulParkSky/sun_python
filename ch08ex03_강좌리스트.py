# ch08ex03.py
# 강좌 리스트

lec =[]
print(lec)

# lec 리스트 만들기 
lec = ['python', 'c']
print(lec)

# office, cad, game 추가 
lec.append('office')
lec.append('cad')
lec.append('game')
print(lec)

# game 제거 
lec.remove('game')
print(lec)

# 원소 수 
print(f'원소수 : {len(lec)}')

# 포함 여부 판단 
if 'python' in lec:
    print('파이썬 포함')
else:
    print('파이썬 미포함')

# ex_dict03.py
# 매장관리(딕셔너리)

data = { '아메리카노': [47, 4],
         '카페라떼': [38, 4],
         '카페모카': [35, 3] }

for k,v in data.items():
    print(f'{k}, 실적:{v[0]}, 평가:{v[1]}')
    

usr = input('커피 메뉴: ')
value = data[usr]
print(f'{usr} 실적: {value[0]}, 평가: {value[1]}')

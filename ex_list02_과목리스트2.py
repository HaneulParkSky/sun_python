# ex_list02.py
# 과목리스트 2 

sub = ['python','c','html']
num = [37, 32, 29]
sco = [4.5, 4.7, 4.4]

one = input('조회할 수강과목: ')
idx = sub.index(one)
print(one, num[idx], sco[idx])

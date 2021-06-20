# ex_list01.py
# 과목리스트 (컬럼별)

sub = ['python','c','html']
num = [37, 32, 29]
sco = [4.5, 4.7, 4.4]

cnt = len(sub)

for idx in range(cnt):
    print(f'수강과목:{sub[idx]}, 학생수:{num[idx]}, 평가:{sco[idx]}')
    

one = input('조회할 수강과목: ')
for idx, x in enumerate(sub):
    if one == x:
        print(one, '학생수:',num[idx], '평가:',sco[idx])



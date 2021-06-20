# ex_dict01.py
# 딕셔너리 내용보기 

report = {'python':[37, 4.5], 'C':[32, 4.7], 'HTML':[29, 4.4]}

for k, v in report.items():
    print(f'수강과목: {k}, 학생 수 : {v[0]}, 평가 점수: {v[1]}')

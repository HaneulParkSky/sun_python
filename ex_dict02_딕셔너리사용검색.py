# ex_dict02.py
# 딕셔너리 사용검색 2

report = {'python':[37, 4.5], 'C':[32, 4.7], 'HTML':[29, 4.4]}

usr = input('조회할 과목: ')
keys = report.keys()

if usr not in keys:
    print('해당 과목은 목록에 없습니다.')
else:
    print('과목명\t학생수\t평가점수')  # \t 는 탭 (띄어쓰기)
    print(usr, report[usr][0], report[usr][1], sep='\t') 
    

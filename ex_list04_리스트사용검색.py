# ex_list04.py
# 리스트 사용 검색


report = [ ['파이썬', 37, 4.5],
           ['C', 32, 4.7],
           ['HTML', 29, 4.4] ]

usr = input('조회할 수강 과목: ')

for one in report:
    if one[0] == usr:
        print('수강과목: ', usr)
        print(f'학생수:{one[1]}, 평가점수:{one[2]}')

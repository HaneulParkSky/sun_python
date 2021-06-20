# ex_list03.py
# 리스트 사용

report = [ ['파이썬', 37, 4.5],
           ['C', 32, 4.7],
           ['HTML', 29, 4.4] ]


# n번째 항목 보기
#print(report[0])
#print(report[1][2])
#print(report[2][1])

for row in report:
    sub = row[0]
    stu = row[1]
    sco = row[2]
    print(f'{sub}   {stu}   {sco}')

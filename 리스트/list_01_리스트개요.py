# list_01.py
# 리스트 자료 만들고 접근하기 

# 인덱스란 ?
# -> 리스트의 각 자료에 접근하기 위한 일련의 변호로 0부터 시작한다.

# 리스트 [], 딕셔너리 {K1:V1, K2:V2}, 튜플 ()

lec = ['python', 'CAD', 'C', 'C++', 'Java']

# 인덱스를 사용해 리스트 자료 출력하기 
print(lec[0])
print(lec[2])

# 인덱스로 'java' 출력하기
print(lec[4])
print(lec[-1])

# 'python' 을 대문자로 변경하기 
lec[0] = 'PYTHON'
print(lec)

# 리스트 간 연산하기 (추가 강좌를 lec에 합치기)
a_lec = ['PHOTOSHOP', 'ILLUST']
lec = lec + a_lec
print(lec)

# 리스트 초기화 하기 (num = list() , num = [])
# 추가 강좌 빈 리스트 만들기

a_lec = []

# 추가 강좌에 'Excel', 'powerpoint' 추가하기
a_lec.append('excel')
a_lec.append('powerpoint')
print(a_lec)

# 추가 강좌를 lec 에 합치기 (a = a+b -> a += b)
lec += a_lec 
print(lec)

# append 는 특정 index 에 넣는게 아닌 리스트 뒤에 자료 추가 
# Insert 함수는 index 가 들어감 -> lec.insert(2,'R')
# delete 는 인덱스 번호로 삭제 
# Remove 함수는 특정 인덱스를 삭제할 때 -> lec.remove('excel')
# sort 함수는 정렬 

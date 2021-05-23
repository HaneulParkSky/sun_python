# ch04ex01.py
# 평균 계산기

# 변수 초기화 
cnt = 0
s = 0

# 점수 입력 
while True:
    score = int(input("점수를 입력하세요: "))
    if score < 0:
        break
    cnt = cnt + 1  # 문제 수 세기 (cnt 는 문제 갯수를 구하는 변수)
    s = s + score  # 점수 합계 (s 는 합을 구하는 변수)
    
print()
print("입력한 점수의 평균은 {:.1f}점 입니다.".format(s/cnt))

# 소수점 지정할 때 -> :.숫자f

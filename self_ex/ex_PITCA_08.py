
# 8. 학점 계산기


for x in range(2):
    
    score = int(input("점수를 입력하세요: "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("당신의 학점은 '{}' 입니다.".format(grade))

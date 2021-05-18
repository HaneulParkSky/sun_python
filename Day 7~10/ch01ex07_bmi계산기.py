# ch01ex07.py
# 체질량지수 구하기

print("체질량지수 (BMI) 구하기")
print()

t = int(input("키 :"))
w = int(input("몸무게 :"))
t = t / 100
bmi = w / (t * t)

if bmi >= 40:
    msg = "고도 비만"
elif bmi >= 35:
    msg = "중등도 비만"
elif bmi >= 30:
    msg = "경도 비만 (1단계 비만)"
elif bmi >= 25:
    msg = "과체중"
elif bmi >= 18.5:
    msg = "정상"
else:
    msg = "저체중"

print("당신의 체질량지수는 {} 입니다.".format(int(bmi)))
print("당신은 {} 입니다.".format(msg))

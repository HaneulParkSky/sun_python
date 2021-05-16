# ch01ex05.py

print("체질량지수(BMI)구하기")
print()

t = int(input("키 :"))
w = int(input("몸무게 :"))

t = t/100
bmi = w / (t * t)

print("당신의 체질량지수는 {}입니다.".format(int(bmi)))


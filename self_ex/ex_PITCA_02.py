
#2. 간단 계산기

num1 = int(input("정수를 입력하세요: "))
num2 = int(input("정수를 입력하세요: "))

print()

s = num1 + num2
d = num1 / num2
t = num1 // num2

print("{}과 {}을 더하면 {}입니다.".format(num1, num2, s))
print("{}을 {}로 나누면 {}입니다.".format(num1, num2, d))
print("{}나누기 {}의 몫은 {}입니다.".format(num1, num2, t))


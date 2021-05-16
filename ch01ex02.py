# ch01ex02.py

num1 = int(input("정수를 입력하세요: "))
num2 = int(input("정수를 입력하세요: "))

print()

s = num1 + num2
s1 = num1 / num2
s2 = num1 // num2

print()
print("{}과 {}을 더하면 {}입니다.".format(num1, num2, s))
print("{}을 {}로 나누면 {}입니다.".format(num1, num2, s1))
print("{}나누기 {}의 몫은 {}입니다.".format(num1, num2, s2))

#print("{}과 {}을 더하면 {}입니다.".format(num1, num2, num1 + num2))
#print("{}을 {}로 나누면 {}입니다.".format(num1, num2, num1 / num2))
#print("{}나누기 {}의 몫은 {}입니다.".format(num1, num2, num1 // num2))



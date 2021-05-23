# 11C_func3.py
# 결과값이 있는 함수


def square(n):      # def은 import 아래 (추천) 
    r = n * n
    return r


def tri(b, h):      # 함수 선언은 위 아래 1~2줄 공백 
    a = b * h / 2
    return a


result = square(2)
print(result)
print(square(3))

print(tri(5, 10))



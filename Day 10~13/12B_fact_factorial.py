# 12B_fact.py
# 1~n까지의 곱 (factorial)


def factorial(n):
    fact = 1        # 곱셈일때는 초기값 '1'
    for x in range(1, n+1):
        fact = fact * x
    return fact


print('5! =',factorial(5))
print('10! =',factorial(10))

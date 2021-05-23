# 12A_sum.py
# 1~n까지 합 함수 : sum_func(n)


def sum_func(n):
    s = 0
    for x in range(n + 1):
        s = s + x
    return s


print("1~10까지의 합 :",sum_func(10))
print("1~100까지의 합 :",sum_func(100))

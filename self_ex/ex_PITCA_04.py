
# 4. 화폐 교환기

pay = int(input("교환할 금액을 입력하세요: "))

change = pay

print("교환금액: ",change)

print("50000원:", change // 50000)
change = change % 50000
print("10000원:", change // 10000)
change = change % 10000
print("5000원:", change // 5000)
change = change % 5000
print("1000원:", change // 1000)
change = change % 1000
print("기타:", change)

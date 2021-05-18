# ch01ex04.py
# 화폐 교환기 (자판기)

# 교환 금액 입력
pay = int(input("교환할 금액을 입력하세요: "))

# 잔돈 초기화
change = pay # 원금 보존 위해 change 변수 사용

print("교환금액:",change)

print("50000원:",change // 50000)
change = change % 50000
print("10000원:",change // 10000)
change = change % 10000
print("5000원:",change // 5000)
change = change % 5000
print("1000원:",change // 1000)
change = change % 1000
print("500원:",change // 500)
change = change % 500
print("10원:",change // 10)
change = change % 10
print("기타:",change)




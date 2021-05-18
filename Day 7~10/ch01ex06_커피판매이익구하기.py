# ch01ex06.py
# 커피 판매 이익 구하기

print("일일 판매량을 입력하세요.")

ameNum = int(input("아메리카노 판매 수: "))
cafNum = int(input("카페라떼 판매 수: "))
capNum = int(input("카푸치노 판매 수: "))

# 일일, 한 달 판매량 구하기

s = (ameNum * 2000) + (cafNum * 3000) + (capNum * 3500) # 하루 매출
m_s = s * 30   # 한 달 매출

print()

print("일일 판매 매출액은 {} 입니다.".format(s))
print("한 달 30일 기준 예상 매출액은 {} 입니다.".format(m_s))

# 지출액 입력 받기

print()
cost = int(input("예상 지출액을 입력하세요: "))

print("한달 예상 순이익은 {} 입니다.".format(m_s - cost))


# ch07ex03.py
# 놀이기구 탑승 검사기


age = int(input("나이를 입력하세요: "))
height = int(input("키를 입력하세요 (단위: cm) :"))

print()

if age >= 10 and height >= 165:
    print("축하합니다.")
    print("놀이기구를 탈 수 있습니다.")
else:
    print("죄송합니다.")
    print("10살 이상이고 키 165cm이상만 이용할 수 있습니다.")


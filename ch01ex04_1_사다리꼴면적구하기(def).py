# ch01ex04_1.py
# 사다리꼴 면적 구하기


def tra(base, upper, height):
    area = ((base + upper) * height) / 2
    return area


print("사다리꼴 면적 구하는 프로그램")
print()

upper = int(input("윗변의 길이를 입력하세요: "))
base = int(input("밑변의 길이를 입력하세요: "))
height = int(input("높이를 입력하세요: "))

area = tra(base, upper, height)  # 공식을 구해야함 

print()
print("면적은 {}입니다.".format(area))


# 7. 정수 판별 프로그램


for x in range(3):
    
    num = int(input("정수를 입력하세요: "))

    if num > 0:
        msg = "양수"
    elif num == 0:
        msg = "0"
    else:
        msg = "음수"

    print("{} 입니다.".format(msg))



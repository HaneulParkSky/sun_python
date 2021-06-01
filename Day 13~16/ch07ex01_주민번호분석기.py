# ch07ex01.py
# 주민번호 분석기

pinNum = input("주민등록번호 앞 7자리를 입력하세요: ")
print('=' * 50)

year = int(pinNum[:2])
month = pinNum[2:4]
day = pinNum[4:6]
gender = int(pinNum[-1])

print(f"당신의 생일은 {year}년 {month}월 {day}일 입니다.")

if gender % 2 == 0:
    g_str = "여"
else:
    g_str = "남"
    

if gender > 2:
    year = year + 2000
else:
    year = year + 1900

age = 2021 - year + 1


print(f'당신의 나이는 {age}살이고, 성별은 {g_str}입니다.')

    



# f01_write01.py
# 파일 입출력 절차

# 변수명 = open(파일명, 모드)

# 파일 열기 모드
# -> r : 읽기 모드
# -> W : 쓰기 모드
# -> A : 추가 모드


my_file = open("mypitca.txt","w")
msg = input("기록할 문장을 입력하세요: ")
my_file.write(msg)
my_file.close() # 이 명령어가 없으면 파일 생성 안됨


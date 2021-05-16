# 07C_timer.py
# 속으로 20초를 세어 맞히기

import time     #시간 체크 모듈

input("엔터를 누르고 20초를 셉니다.")
start = time.time()     # time.time 은 현재 시간을 가져옴

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

st = end - start
print("실제 시간 : {}초".format(st))
print("차이 : {}초".format(abs(20-st)))



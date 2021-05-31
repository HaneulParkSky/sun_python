

##     사용자로부터 정수를 입력을 받아서 그 총합과 평균을 출력하는 프로그램        
##     사용자가 0을 입력하면 프로그램이 종료되는 것으로 한다                     
##     과제: 프로그램 실행 직후 그 반복 회수를 사용자가 입력한다.   


def list_gen():
    input_list = list()
    while True:
        a = int(input('정수를 입력하세요 (0 입력시 무시하고 총합과 평균 출력): '))
        if a == 0:
            break
        input_list.append(a)
    return input_list


def list_sum(list_gen):
    sum = 0
    for x in list_gen:
        sum = sum + x
    return sum

def main():
    x = list_gen()
    y = list_sum(x)

    print('총합: ',y)
    print('평균: ',y/len(x))  # x의 개수 만큼 나누기 (평균)

main()

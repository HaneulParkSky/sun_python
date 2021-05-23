
# https://wikidocs.net/23906

## 201 ~ 210

# def print_coin():
#    print("비트코인")


# for x in range(100):
#    print_coin()


# def print_coins():
#     for x in range(100):
#        print("비트코인")


## 215, 216

# def print_with_smile(string):
#    print(string + ":D")
    
# print_with_smile("안녕하세요")

## 217

#def print_upper_price(price):
#    price(price * 1.3)


## 218

# def print_sum(a,b):
#    print(a + b)

## 219

#def print_arithmetic_operation(a,b):
#    print(a,"+",b,"=",a + b)
#    print(a,"-",b,"=",a - b)
#    print(a,"*",b,"=",a * b)
#    print(a,"/",b,"=",a / b)
    
#print_arithmetic_operation(3,5)



## 220

#def print_max(a,b,c):
#    max_val = 0
#    if a > max_val:
#        max_val = a
#    if b > max_val:
#        max_val = b
#    if c > max_val:
#        max_val = c
#    print(max_val)

## 223

#my_list = [1,3,2,10,12,11,15]

#def print_even(my_list):
#    for x in my_list:
#        if x % 2 == 0:
#            print(x)

#print_even(my_list)

## 228

#def calc_monthly_salary(annual_salary):
#    monthly_salary = int(annual_salary / 12)
#    return monthly_salary

#print(calc_monthly_salary(63000000))

## 236

# def sum_func1(num):
#    return num + 5

#a = sum_func1(5)
#b = sum_func1(a)
#c = sum_func1(b)
#print(c)

## 238

#def sum_func2(num):
#    return num + 4

#def sum_func3(num):
#    return num * 10

#a = sum_func2(10)
#c = sum_func3(a)
#print(c)

## 239

#def func1(num):
#    return num + 4

#def func2(num):
#    num = num + 2
#    return func1(num)

#c = func2(10)
#print(c)

## 240

def func_1(num):
    return num * 2 #28

def func_2(num):
    return func_1(num + 2) #28

def func_3(num):
    num = num + 10 #12
    return func_2(num) 

c = func_3(2)
print(c)







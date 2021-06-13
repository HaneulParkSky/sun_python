# ch08lab1.py
# 실습문제 1

my_list = [1,3,7,9]

my_list.append(11)
print(my_list)

my_list.insert(2, 5)
print(my_list)

new_list = my_list[1:3]
print('new_list =', new_list)

new_list[0] = 10
print('new_list =', new_list)

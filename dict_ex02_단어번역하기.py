# dict_ex02.py
# 단어 번역하기

dic = {'사과':'apple','바나나':'banana','수박':'watermelon','포도':'grape'}

k = dic.keys() # 키를 수집

while True:
    usr = input('번역할 단어는: ')

    if usr in k:
        print(dic[usr])
    else:
        print('번역할 단어가 없습니다.')
        break

